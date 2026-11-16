const Q=new URLSearchParams(location.search),SYMBOLS=['BTC','ETH','SOL'];
const el=id=>document.getElementById(id),quotes={};
let sym=SYMBOLS.includes(Q.get('sym'))?Q.get('sym'):'BTC';
let interval=[1,5,10].includes(+Q.get('tf'))?+Q.get('tf'):1;
let preference=Q.get('theme');
try{preference ||= localStorage.getItem('always-happiness-theme');}catch{}
if(!['light','dark'].includes(preference))preference='light';
document.documentElement.dataset.theme=preference;
const u=new URL(location.href);for(const name of ['version','release','chart'])u.searchParams.delete(name);history.replaceState(null,'',u);
el('symbols').innerHTML=SYMBOLS.map(s=>`<button class="sym" data-s="${s}"><span class="s"><img class="coin-icon" src="coin-${s.toLowerCase()}.${s==='ETH'?'png':'svg'}" alt="">${s}</span><span class="p" data-price="${s}">—</span></button>`).join('');
function selectSymbol(symbol){
  sym=symbol;
  for(const button of document.querySelectorAll('[data-s],[data-asset]')){
    const active=(button.dataset.s||button.dataset.asset)===sym;
    button.classList.toggle(button.dataset.s?'on':'active',active);button.setAttribute('aria-pressed',String(active));
  }
  window.syncTradingView?.();
}
for(const button of document.querySelectorAll('[data-s],[data-asset]'))button.onclick=()=>selectSymbol(button.dataset.s||button.dataset.asset);
selectSymbol(sym);
function theme(){
  document.documentElement.dataset.theme=preference;
  const dark=preference==='dark';el('theme-toggle').textContent=dark?'밝게':'어둡게';el('theme-toggle').setAttribute('aria-label',dark?'밝은 화면으로 변경':'어두운 화면으로 변경');
}
el('theme-toggle').onclick=()=>{preference=preference==='dark'?'light':'dark';try{localStorage.setItem('always-happiness-theme',preference);}catch{}theme();};theme();
function status(){
  const fresh=SYMBOLS.every(s=>quotes[s]&&Date.now()-quotes[s].ts<15000);
  el('live').textContent=fresh?'실시간 시세':'시세 연결 중';el('live').parentElement.classList.toggle('failed',!fresh);
}
BitgetMarket.feed(q=>{quotes[q.symbol]=q;document.querySelector(`[data-price="${q.symbol}"]`).textContent=q.price.toLocaleString('en-US',{minimumFractionDigits:q.symbol==='BTC'?1:2,maximumFractionDigits:q.symbol==='BTC'?1:2});status();},status);
setInterval(status,1000);
document.querySelectorAll('.side-nav a').forEach(a=>a.onclick=()=>{document.querySelectorAll('.side-nav a').forEach(n=>n.classList.remove('active'));a.classList.add('active');});
