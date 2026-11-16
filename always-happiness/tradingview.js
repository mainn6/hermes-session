// TradingView's hosted widget provides its own indicator picker; custom Pine is not supported.
(() => {
  let loadedKey = '', observer;
  const host = el('tv-host'), status = el('tv-load-status');
  function load() {
    const theme = document.documentElement.dataset.theme, key = `${sym}:${interval}:${theme}`;
    el('tv-symbol').textContent = `${sym} / USDT`;
    el('tv-full-chart').href = `https://www.tradingview.com/chart/?symbol=BITGET%3A${sym}USDT.P&interval=${interval}`;
    el('tv-intervals').innerHTML = [1,5,10].map(n => `<button data-tv-min="${n}" class="${n===interval?'on':''}" aria-pressed="${n===interval}">${n}분봉</button>`).join('');
    el('tv-intervals').querySelectorAll('button').forEach(b => b.onclick = () => { interval=+b.dataset.tvMin;load(); });
    if (loadedKey === key) return;
    loadedKey = key;
    observer?.disconnect();
    status.hidden = false;
    status.textContent = 'TradingView 차트 연결 중';
    host.replaceChildren();
    const container = document.createElement('div');
    container.className = 'tradingview-widget-container__widget';
    host.append(container);
    observer = new MutationObserver(() => {
      const frame = host.querySelector('iframe');
      if (!frame) return;
      frame.title = `Bitget ${sym}/USDT TradingView 차트`;
      frame.addEventListener('load', () => { status.hidden = true; }, {once:true});
      observer.disconnect();
    });
    observer.observe(host, {childList:true,subtree:true});
    const script = document.createElement('script');
    script.src = 'https://s3.tradingview.com/external-embedding/embed-widget-advanced-chart.js';
    script.async = true;
    script.textContent = JSON.stringify({autosize:true,symbol:`BITGET:${sym}USDT.P`,interval:String(interval),timezone:'Asia/Seoul',theme,style:'1',locale:'kr',allow_symbol_change:false,hide_top_toolbar:false,hide_side_toolbar:false,withdateranges:true,save_image:true,calendar:false,hide_volume:false,support_host:'https://www.tradingview.com'});
    script.onerror = () => {
      if (!script.isConnected) return;
      status.hidden=false;status.textContent='TradingView 연결을 확인해주세요.';
      const retry=document.createElement('button');retry.textContent='다시 연결';retry.onclick=()=>{loadedKey='';load();};status.append(retry);
    };
    host.append(script);
  }
  window.syncTradingView = load;
  new MutationObserver(load).observe(document.documentElement,{attributes:true,attributeFilter:['data-theme']});
  load();
})();
