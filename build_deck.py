import json
U=json.load(open('qr/qr.json'))['uris']
def s(kick,title,body,cls=''):
    return f'<section class="slide {cls}"><div class="kick">{kick}</div><h1>{title}</h1>{body}</section>'
def qr(k,label,size=260): return f'<figure class="q" style="width:{size}px"><img src="{U[k]}"><figcaption>{label}</figcaption></figure>'
S=[]
# ---- Part 1. 설명 ----
S.append('<section class="slide cover"><div class="kick">AI Agent Operator</div><h1>Hermes Agent<br>알아보고, 실행하고, 활용하기</h1><p class="sub">코드를 짜지 않는 사람이 AI 에이전트를 운영하는 방법. 설명 → 활용 사례 → 실습.</p><p class="tag">JEFF · 비개발자 · Web3 마케터</p></section>')
S.append(s('01 소개','저는 개발자가 아닙니다','<ul class="big"><li>Web3 마케터. 코드는 직접 못 짭니다</li><li>AI 에이전트 트레이딩 대회 1위. 프롬프트가 아니라 <b>운영</b>으로</li></ul><div class="cols"><div><div class="num">$10.3M</div><div class="lab">거래 볼륨</div></div><div><div class="num">22,936</div><div class="lab">트레이드</div></div><div><div class="num">$100</div><div class="lab">시작 자본</div></div></div><p class="note">ClawHacks Mantle, 2026년 4월. 규칙을 정하고, 기록하고, 손절선을 지킨 결과입니다.</p>'))
S.append(s('02 Hermes Agent','폰에서 시키는 내 AI 비서','<ul class="big"><li>내 컴퓨터에서 돌아가는 오픈소스 에이전트(NousResearch)</li><li>텔레그램에 한 줄 보내면 파일·웹·메일·일정을 읽고 처리해서 답합니다</li><li>자주 하는 일은 한 번 정해두면 정해진 시간에 알아서 돌아갑니다</li><li>컴퓨터 앞에 없어도 됩니다</li></ul>'))
S.append(s('03 비교','OpenClaw와 Hermes','<table class="kv"><tr><td>OpenClaw</td><td>웹사이트를 직접 누르고 입력하는 <b>손</b>. 클릭·입력을 대신한다</td></tr><tr><td>Hermes</td><td>일을 나누고 시키는 <b>비서</b>. “이거 해줘” 하면 처리하고 정리한다</td></tr></table><p class="note">경쟁이 아니라 역할이 다릅니다. 저는 둘을 같이 씁니다.</p>'))
S.append(s('04 활용','실제로 시키는 일','<table class="kv"><tr><td>메일·일정</td><td>받은 메일 요약, 답장 초안, 오늘 일정과 충돌 확인. 발송은 내가 확인하고</td></tr><tr><td>업무 기록</td><td>회의 메모·업무 보고를 정리해 문서와 시트에 저장</td></tr><tr><td>자료 수집</td><td>X·레딧·깃허브에서 AI/Web3 소재를 모아 정리</td></tr><tr><td>트레이딩 감시</td><td>시장·포지션 상태를 읽고 규칙대로 보고. 실거래는 사람이</td></tr><tr><td>이미지·영상</td><td>포스터와 짧은 영상 제작(Higgsfield 스킬: GPT Image 2.5, Seedance 2.5)</td></tr><tr><td>반복 작업</td><td>아침 시장 요약처럼 정해진 시간에 돌아가는 일</td></tr></table>'))
S.append(s('05 구글 연동','Gmail · 캘린더 · 시트','<ul class="big"><li>메일만 필요하면 Gmail 앱 비밀번호로 2분(himalaya 스킬)</li><li>캘린더·시트·문서까지면 Google Cloud OAuth 한 번(google-workspace 스킬, 5분)</li><li>읽기·요약·초안은 에이전트가, <b>발송과 수정은 확인 후</b></li></ul><pre>“오늘 안 읽은 메일 요약해줘”\n“이 메일에 답장 초안 써줘. 보내기 전에 보여줘”\n“이번 주 일정 겹치는 거 있어?”</pre>'))
S.append(s('06 기억','Obsidian 볼트 = 에이전트의 기억','<ul class="big"><li>에이전트 자체 메모리는 2,200자. 긴 기록은 볼트(markdown 폴더)에</li><li>에이전트가 파일로 읽고 쓰고, 나도 같은 파일을 봅니다</li><li>“프로젝트 질문은 답하기 전에 볼트를 먼저 검색” 한 줄이 정체성 파일에 들어갑니다</li></ul><p class="note">연결은 세 단계. 볼트 폴더, 기본 obsidian 스킬 확인, SOUL.md에 경로와 규칙.</p>'))
S.append(s('07 원칙','회사에서 써도 되는 조건','<ol class="big"><li>위험한 일은 실행 전에 <b>묻는다</b>. 메일 발송 · 결제 · 실거래 · 삭제</li><li>진실은 채팅이 아니라 <b>볼트</b>에 있다</li><li>키는 <b>파일에만</b>. 채팅 · 스크린샷 · 문서에 안 남긴다</li></ol>'))
# ---- Part 2. 디스코드 ----
S.append(f'<section class="slide center"><div class="kick">자료</div><h1>설치 가이드와 자료는 디스코드에</h1>{qr("discord","discord.gg/TBuVE4mnhr",340)}<p class="note">입장하면 참가자 페이지 링크, 설치 가이드 PDF, 질문 채널이 있습니다.</p></section>')
# ---- Part 3. 실습 ----
S.append(s('실습','오늘 하는 것','<ol class="big"><li>Hermes 설치</li><li>Dgrid 모델 키 (무료 라우터 <code>dgridai/free</code>)</li><li>Hermes에 모델 연결 → 대화 확인</li><li>텔레그램 봇 연결 → 폰에서 “안녕”</li><li>거래소 읽기 → 규칙 카드 → 모의 주문 1건 → 취소 → 노트 기록</li></ol><p class="note">순서와 명령은 디스코드의 참가자 페이지에 있습니다. 위에서부터 하나씩.</p>'))
S.append(s('실습 준비','필요한 것','<table class="kv"><tr><td>노트북</td><td>Mac(Apple Silicon) 또는 Windows 11. 인텔 맥은 미지원</td></tr><tr><td>텔레그램</td><td>폰과 노트북 둘 다 로그인</td></tr><tr><td>모델 키</td><td>Dgrid. 지갑으로 로그인. 지갑 없으면 세션용 키 배포</td></tr><tr><td>적어 둘 값</td><td>Dgrid 키 · 봇 토큰 · 내 텔레그램 ID. 메모장에만</td></tr></table>'))
S.append(s('실습','규칙 카드','<div class="grid7"><div>종목 1개</div><div>진입 조건 1개</div><div>손절 %</div><div>익절 %</div><div>1회 주문 한도 (숫자)</div><div>거래 금지 시간·조건</div><div>하루 최대 손실</div></div><p class="note">종이에 쓴 카드가 에이전트의 역할 카드가 됩니다. “한도를 넘는 주문은 거절하고 사람에게 묻는다”는 문장은 고정.</p>'))
S.append(s('실습','안전 규칙','<ul class="big"><li>API 키는 읽기 + 거래만. <b>출금 권한 OFF</b>. IP 화이트리스트</li><li>모의 계정 또는 잔고 0 계정만</li><li>모의 주문은 현재가 대비 30% 아래 지정가 0.0001 BTC. 체결되지 않습니다</li><li>10초 뒤 취소. 조건이 안 맞으면 주문하지 않는 것이 정답</li><li>키·토큰은 화면에 비치지 않게</li></ul>'))
S.append(s('마무리','확인','<ul class="big"><li>옆 사람 봇에 “잔고 알려줘” → 답이 오면 완료</li><li>오늘 기록을 Obsidian 노트 한 장으로</li><li>집에 가서 실돈 계정에 연결하지 않습니다. 오늘 만든 키는 지워도 됩니다</li></ul><p class="note">질문과 후속 자료는 디스코드에서.</p>'))
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
html='<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Hermes Agent 세션</title><style>'+CSS+'</style></head><body><div class="deck">'+''.join(S)+'</div><div class="pager" id="pg"></div><script>'+JS+'</script></body></html>'
open('deck.html','w',encoding='utf-8').write(html); print('deck slides',len(S))
