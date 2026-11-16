(function(root) {
  const symbols=['BTC','ETH','SOL'];
  const finite=v=>typeof v==='number'&&Number.isFinite(v);
  function parse(message,now=Date.now()) {
    try {
      const m=typeof message==='string'?JSON.parse(message):message;
      if(m.arg?.instType!=='USDT-FUTURES'||m.arg.channel!=='ticker'||!Array.isArray(m.data)||m.data.length!==1)return null;
      const symbol=m.arg.instId?.replace(/USDT$/,'');if(!symbols.includes(symbol)||m.arg.instId!==symbol+'USDT')return null;
      const row=m.data[0],price=Number(row.markPrice),ts=Number(row.ts);
      if(row.instId!==m.arg.instId||!finite(price)||price<=0||!finite(ts)||ts<=0||now-ts>10000||ts-now>5000)return null;
      return {symbol,price,ts,received:now};
    } catch { return null; }
  }
  function quoteFor(symbol,quotes,now,since=0) {
    const q=quotes[symbol];
    if(!q||!finite(q.price)||q.price<=0||!finite(q.ts)||q.ts/1000<since||q.ts-now>5000)return null;
    return {...q,live:now-q.ts<=10000&&now-q.received<=10000};
  }
  function paper(data,quotes,now=Date.now()) {
    const a=data.accounts.paper;
    const positions=a.positions.map(p=>{
      const since=Math.max(p.opened_at,...p.fills.map(f=>f.time));
      const q=quoteFor(p.symbol,quotes,now,since);
      const pnl=p.pnl+(q?(q.price-p.mark)*p.size*((p.side==='long'?1:-1)-(p.exit_fee_rate??0)):0);
      return {...p,mark:q?q.price:p.mark,pnl,pnl_pct:100*pnl/p.notional,quote_live:!!q?.live&&now/1000-data.updated<=900,quote_at:q?.ts};
    });
    const unrealized=positions.reduce((sum,p)=>sum+p.pnl,0),total=a.realized+unrealized,base=data.session.baseline_equity;
    const equity=base+total;positions.forEach(p=>{p.leverage=equity?p.notional/equity:0;});
    return {...a,positions,unrealized,total_pnl:total,total_pct:100*total/base,equity,day_pnl:total,
      quote_live:now/1000-data.updated<=900&&positions.every(p=>p.quote_live)};
  }
  function feed(onQuote,onState) {
    let socket,ping,retry,stopped=false,backoff=1000,lastMessage=Date.now();const seen={};
    function reconnect() {
      if(stopped)return;
      onState(false);clearInterval(ping);retry=setTimeout(open,backoff);backoff=Math.min(30000,backoff*2);
    }
    function open() {
      if(stopped)return;
      let s;
      try {s=new WebSocket('wss://ws.bitget.com/v2/ws/public');socket=s;} catch {reconnect();return;}
      s.onopen=()=>{
        if(stopped||s!==socket)return;
        lastMessage=Date.now();onState(true);
        s.send(JSON.stringify({op:'subscribe',args:symbols.map(symbol=>({instType:'USDT-FUTURES',channel:'ticker',instId:symbol+'USDT'}))}));
        ping=setInterval(()=>{if(s!==socket)return;if(Date.now()-lastMessage>45000)s.close();else if(s.readyState===1)s.send('ping');},30000);
      };
      s.onmessage=e=>{
        if(stopped||s!==socket)return;
        lastMessage=Date.now();if(e.data==='pong')return;
        const q=parse(e.data);if(!q||q.ts<=(seen[q.symbol]??0))return;
        seen[q.symbol]=q.ts;backoff=1000;onQuote(q);
      };
      s.onerror=()=>s.close();s.onclose=()=>{if(s===socket)reconnect();};
    }
    open();
    return ()=>{stopped=true;clearInterval(ping);clearTimeout(retry);if(socket)socket.close();onState(false);};
  }
  const api={parse,quoteFor,paper,feed};root.LivePnl=api;
  if(typeof module!=='undefined')module.exports=api;
})(globalThis);
