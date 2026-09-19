"""Google Forms API로 폼 생성 + 질문 추가 + 응답 시트 연결. 사용: python3 make_form.py <access_token>
ponytail: gog CLI는 질문 추가를 지원하지 않아 REST 직접 호출. 토큰은 인자로만 받고 어디에도 저장하지 않는다."""
import json, sys, urllib.request
tok=sys.argv[1]; spec=json.load(open('form-spec.json'))
def call(url,data=None,method=None):
    r=urllib.request.Request(url,headers={'Authorization':f'Bearer {tok}','Content-Type':'application/json'},data=json.dumps(data).encode() if data else None,method=method or ('POST' if data else 'GET'))
    return json.load(urllib.request.urlopen(r))
f=call('https://forms.googleapis.com/v1/forms',{'info':{'title':spec['title'],'documentTitle':spec['title']}})
fid=f['formId']; reqs=[{'updateFormInfo':{'info':{'description':spec['description']},'updateMask':'description'}}]
for i,q in enumerate(spec['questions']):
    if q['type']=='text':
        item={'title':q['title'],'description':q.get('help',''),'questionItem':{'question':{'required':q['required'],'textQuestion':{'paragraph':False}}}}
    else:
        item={'title':q['title'],'description':q.get('help',''),'questionItem':{'question':{'required':q['required'],'choiceQuestion':{'type':'RADIO','options':[{'value':o} for o in q['options']]}}}}
    reqs.append({'createItem':{'item':item,'location':{'index':i}}})
call(f'https://forms.googleapis.com/v1/forms/{fid}:batchUpdate',{'requests':reqs})
print('form', fid); print('edit  https://docs.google.com/forms/d/'+fid+'/edit'); print('fill  '+f['responderUri'])
json.dump({'formId':fid,'responderUri':f['responderUri']},open('form.json','w'))
