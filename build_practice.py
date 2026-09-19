import json
U=json.load(open('qr/qr.json'))['uris']
def s(kick,title,body,cls=''):
    return f'<section class="slide {cls}"><div class="kick">{kick}</div><h1>{title}</h1>{body}</section>'
def qr(k,label,size=260): return f'<figure class="q" style="width:{size}px"><img src="{U[k]}"><figcaption>{label}</figcaption></figure>'
S=[]
S.append('<section class="slide cover"><div class="kick">실습</div><h1>Hermes Agent<br>설치와 연결</h1><p class="sub">SESSIONS → #헤르메스 채널의 순서대로 진행합니다.</p><p class="tag">설치 → 모델 키 → 연결 → 텔레그램 → 확인</p></section>')
S.append(s('실습 1/4','오늘 하는 것','<ol class="big"><li>Hermes 설치</li><li>Dgrid 모델 키 (무료 라우터 <code>dgridai/free</code>)</li><li>Hermes에 모델 연결 → 대화 확인</li><li>텔레그램 봇 연결 → 폰에서 “안녕”</li><li>완료 체크 스크립트</li></ol><p class="note">순서와 명령은 #헤르메스 채널에. 위에서부터 하나씩.</p>'))
S.append(s('실습 2/4','필요한 것','<table class="kv"><tr><td>노트북</td><td>Mac(Apple Silicon) 또는 Windows 11. 인텔 맥은 미지원</td></tr><tr><td>텔레그램</td><td>폰과 노트북 둘 다 로그인</td></tr><tr><td>모델 키</td><td>Dgrid. 지갑으로 로그인. 지갑 없으면 세션용 키 배포</td></tr><tr><td>적어 둘 값</td><td>Dgrid 키 · 봇 토큰 · 내 텔레그램 ID. 메모장에만</td></tr></table>'))
S.append(f'<section class="slide center"><div class="kick">실습 · Dgrid</div><h1>Dgrid 가입은 이 QR로</h1>{qr("dgrid","dgrid.ai/arena?code=5GG6FQ",340)}<p class="note">가입 후 dgrid.ai/api-keys 에서 모델 키를 만듭니다. 오늘은 무료 라우터라 크레딧이 필요 없습니다.</p></section>')
S.append(s('실습 3/4','막히면','<table class="kv"><tr><td>hermes 명령 없음</td><td>터미널 새로 열기</td></tr><tr><td>답이 비어 있음</td><td><code>hermes model</code> 다시. base URL·모델명 확인</td></tr><tr><td>봇이 unauthorized</td><td>내 ID가 Allowed users에 없음</td></tr><tr><td>봇이 무반응</td><td><code>hermes gateway</code> 창 확인</td></tr><tr><td>Dgrid 429</td><td>무료 라우터 한도. 1분 뒤 재시도</td></tr></table>'))
S.append(s('실습 4/4','마무리','<ul class="big"><li>옆 사람 봇에 “안녕” → 답이 오면 완료</li><li>집에 가서: 옵시디언 연결 · 반복 작업 · 구글 연동 (채널 글 참고)</li><li>오늘 만든 키는 지워도 됩니다</li></ul><p class="note">질문과 후속 자료는 #헤르메스에서.</p>'))
CSS='''
:root{--bg:#070a0b;--ink:#eef4f6;--muted:#97a9b0;--acc:#97d3eb;--acc2:#ffd879;--line:#233036;--panel:#0f1517}
*{box-sizing:border-box;margin:0;padding:0}html,body{height:100%;background:var(--bg);color:var(--ink);font-family:"IBM Plex Sans KR",Pretendard,-apple-system,"Segoe UI",sans-serif}
body{overflow:hidden}.deck{position:relative;width:100vw;height:100vh}
.slide{position:absolute;inset:0;padding:7vh 8vw;display:none;flex-direction:column;justify-content:center;gap:2.2vh}.slide.on{display:flex}
.kick{color:var(--acc2);font-size:1.5vh;font-weight:800;letter-spacing:.16em;text-transform:uppercase}
h1{font-size:6.2vh;line-height:1.08;letter-spacing:-.03em}.cover h1{font-size:8.4vh}.center{align-items:center;text-align:center}
p,li,td{font-size:2.6vh;line-height:1.5}.sub{color:var(--muted);font-size:3vh;max-width:70vw}.tag{color:var(--acc);font-size:2vh}
.note{color:var(--muted);font-size:2.2vh}
ol.big,ul.big{padding-left:3.2vh}ol.big li,ul.big li{font-size:3.1vh;margin:.9vh 0}
.cols{display:flex;gap:6vw;margin:1.5vh 0}.num{font-size:7vh;font-weight:800;letter-spacing:-.03em;color:var(--acc)}.lab{color:var(--muted);font-size:2vh}
figure.q{text-align:center}figure.q img{width:100%;background:#fff;border-radius:1.6vh;padding:1vh}figcaption{color:var(--muted);font-size:1.8vh;margin-top:.8vh}
pre{background:var(--panel);border:1px solid var(--line);border-radius:1.4vh;padding:1.8vh 2.2vh;font:2.3vh/1.6 ui-monospace,Menlo,monospace;white-space:pre-wrap;color:#e6f0f3;margin:1vh 0}
code{background:#16232a;padding:.2vh .8vh;border-radius:.8vh}
.kv{border-collapse:collapse;width:100%}.kv td{padding:1.2vh 1.4vh;border-bottom:1px solid var(--line);vertical-align:top}.kv td:first-child{color:var(--muted);width:22%}
.grid7{display:grid;grid-template-columns:repeat(4,1fr);gap:1.6vh;margin:1vh 0}.grid7 div{border:1px solid var(--line);border-radius:1.4vh;padding:2.4vh 1.8vh;font-size:2.6vh;background:var(--panel)}
.pager{position:fixed;right:2vw;bottom:2vh;color:var(--muted);font-size:1.6vh}
@media print{@page{size:338.7mm 190.5mm;margin:0}body{overflow:visible}.deck{height:auto}.slide{display:flex!important;position:relative;height:190.5mm;width:338.7mm;page-break-after:always;padding:14mm 26mm}.pager{display:none}
h1{font-size:34pt}.cover h1{font-size:46pt}p,li,td{font-size:14pt}ol.big li,ul.big li{font-size:17pt}.sub{font-size:16pt}.kick{font-size:9pt}.note{font-size:12pt}.num{font-size:38pt}.lab{font-size:11pt}pre{font-size:13pt}figcaption{font-size:10pt}.grid7 div{font-size:14pt}.tag{font-size:11pt}figure.q{width:64mm!important}}
'''
JS='''const sl=[...document.querySelectorAll('.slide')];let i=Math.max(0,Math.min(sl.length-1,parseInt(location.hash.slice(1)||'0')));function go(n){i=(n+sl.length)%sl.length;sl.forEach((s,k)=>s.classList.toggle('on',k===i));location.hash=i;document.getElementById('pg').textContent=(i+1)+' / '+sl.length}
addEventListener('keydown',e=>{if(['ArrowRight','PageDown',' '].includes(e.key))go(i+1);if(['ArrowLeft','PageUp'].includes(e.key))go(i-1);if(e.key==='Home')go(0)});addEventListener('click',e=>{if(e.clientX>innerWidth/2)go(i+1);else go(i-1)});go(i)'''
html='<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Hermes Agent 실습</title><style>'+CSS+'</style></head><body><div class="deck">'+''.join(S)+'</div><div class="pager" id="pg"></div><script>'+JS+'</script></body></html>'
open('practice.html','w',encoding='utf-8').write(html); print('deck slides',len(S))
