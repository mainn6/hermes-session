function emaValues(values, period) {
  let previous = null, seed = [];
  return values.map(value => {
    if (value == null) return null;
    if (previous == null) {
      seed.push(value);
      if (seed.length < period) return null;
      previous = seed.reduce((a,b)=>a+b,0)/period;
    } else previous += 2/(period+1)*(value-previous);
    return previous;
  });
}
function points(rows, values) {return values.flatMap((value,i)=>value==null?[]:[{time:rows[i][0],value}]);}
function sma(rows, period=20) {
  return points(rows,rows.map((_,i)=>i+1<period?null:rows.slice(i+1-period,i+1).reduce((a,r)=>a+r[4],0)/period));
}
function ema(rows, period=20) {return points(rows,emaValues(rows.map(r=>r[4]),period));}
function bollinger(rows, period=20, mult=2) {
  const middle=sma(rows,period),upper=[],lower=[];
  middle.forEach((p,j)=>{
    const values=rows.slice(j,j+period).map(r=>r[4]);
    const sd=Math.sqrt(values.reduce((sum,v)=>sum+(v-p.value)**2,0)/period);
    upper.push({time:p.time,value:p.value+mult*sd});lower.push({time:p.time,value:p.value-mult*sd});
  });
  return {middle,upper,lower};
}
function rsi(rows, period=14) {
  let gains=0,losses=0;const result=[];
  for(let i=1;i<rows.length;i++) {
    const change=rows[i][4]-rows[i-1][4],gain=Math.max(change,0),loss=Math.max(-change,0);
    if(i<=period){gains+=gain;losses+=loss;if(i<period)continue;gains/=period;losses/=period;}
    else{gains=(gains*(period-1)+gain)/period;losses=(losses*(period-1)+loss)/period;}
    result.push({time:rows[i][0],value:losses===0?(gains===0?50:100):100-100/(1+gains/losses)});
  }
  return result;
}
function macd(rows, fast=12, slow=26, signalPeriod=9) {
  const f=emaValues(rows.map(r=>r[4]),fast),s=emaValues(rows.map(r=>r[4]),slow);
  const values=f.map((v,i)=>v==null||s[i]==null?null:v-s[i]);
  const signal=emaValues(values,signalPeriod);
  return {line:points(rows,values),signal:points(rows,signal),histogram:points(rows,values.map((v,i)=>v==null||signal[i]==null?null:v-signal[i]))};
}
function vwap(rows) {
  let day=null,amount=0,volume=0;const result=[];
  rows.forEach(r=>{
    const next=Math.floor(r[0]/86400);if(day!==next){day=next;amount=volume=0;}
    amount+=(r[2]+r[3]+r[4])/3*r[5];volume+=r[5];
    if(volume>0)result.push({time:r[0],value:amount/volume});
  });
  return result;
}
if(typeof module!=='undefined')module.exports={sma,ema,bollinger,rsi,macd,vwap};
