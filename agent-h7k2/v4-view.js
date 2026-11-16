/* V4 uses the shared dashboard; only its snapshot content differs from V3. */
const V4View = {
  validate(data, rows) {
    if (!data || Object.keys(data).sort().join() !== 'analyzed,marks,mode,session,signals,updated,version,window' || data.version !== 'v4' || data.mode !== 'snapshot' || data.analyzed?.join() !== 'BTC') throw Error('invalid V4 snapshot');
    const {start, end} = data.window;
    if (![start, end, data.updated, data.session?.started_at].every(Number.isFinite) || end-start !== 1439*60 || data.updated !== end+60 || data.session.started_at !== start) throw Error('invalid V4 window');
    for (const symbol of SYMBOLS) {
      const bars = rows[symbol];
      if (!Array.isArray(bars) || bars.length !== 1440 || bars[0][0] !== start || bars.at(-1)[0] !== end || data.marks[symbol] !== bars.at(-1)[4]) throw Error('invalid V4 market context');
      aggregateCandles(bars, 1);
    }
    const seen = new Set();
    if (!Array.isArray(data.signals?.dots) || !Array.isArray(data.signals.history) || !Array.isArray(data.signals.rows) || data.signals.flow?.length !== 0) throw Error('invalid V4 signals');
    for (const s of data.signals.dots) {
      if (Object.keys(s).sort().join() !== 'price,side,symbol,time' || s.symbol !== 'BTC' || !['long','short'].includes(s.side) || !Number.isFinite(s.time) || s.time%60 || s.time<start || s.time>end || s.price !== rows.BTC[(s.time-start)/60][4] || seen.has(s.time)) throw Error('invalid V4 signal');
      seen.add(s.time);
    }
    if (JSON.stringify(data.signals.history) !== JSON.stringify(data.signals.dots.slice().reverse().map(s=>({time:s.time,symbol:s.symbol,side:s.side,result:'학습 신호 판정'})))) throw Error('invalid V4 history');
    if (data.signals.rows.length !== 3 || !data.signals.rows.every((r,i)=>r.name===SYMBOLS[i]+' 학습 신호' && r.on===false && r.count===(i===0?seen.size:0) && r.state===(i===0?'분석 스냅샷':'미분석'))) throw Error('invalid V4 signal state');
  },
  status() {
    el('live').textContent = D ? `V4 · 분석 스냅샷 · ${dhm(D.window.end)} 기준 · UTC+9` : 'V4 자료 불러오는 중';
    el('live').parentElement.classList.remove('failed');
    el('stale').hidden = !failed;
    el('stale').textContent = 'V4 자료를 불러오지 못했습니다. 다시 열어 주세요.';
  },
  totalPnl() {
    el('total-pnl').innerHTML = `<div><div class="pos-id"><strong>${sym} 계좌 전체 PnL</strong></div><div class="pnl-row"><div class="pnl muted">—<small>USDT</small></div></div><div class="pnl-sub">V4 학습 신호 · 손익 미검증 · 주문·체결 없음</div><div class="pnl-sub">${dhm(D.window.start)} ~ ${dhm(D.window.end)} · 자동 갱신 없는 스냅샷</div></div><dl class="facts"><div><dt>실현 손익</dt><dd>—<span>USDT</span></dd></div><div><dt>미실현 손익</dt><dd>—<span>USDT</span></dd></div><div><dt>현재 평가액</dt><dd>—<span>USDT</span></dd></div></dl>`;
  },
  position() {
    const s = D.signals.dots.filter(s=>s.symbol===sym).at(-1);
    el('pos').innerHTML = s ? `<div><div class="pos-id"><span class="side ${s.side}">${s.side.toUpperCase()}</span><span class="pair">${sym}/USDT</span><span class="when">${hm(s.time)} 학습 신호 판정 · 실제 포지션 없음</span></div><div class="pnl-row"><div class="pnl">${num(s.price,dp(sym))}<small>USDT</small></div></div><div class="pnl-sub">신호 봉 종가 · 완성봉의 시작 시각에 표시 · 봉 완성 후 판정 가능</div></div><dl class="facts"><div><dt>목표 / 익절</dt><dd>—</dd></div><div><dt>손절</dt><dd>—</dd></div><div><dt>수량</dt><dd>—</dd></div><div><dt>체결</dt><dd>없음</dd></div></dl>` : `<div><div class="none">${sym} 학습 신호 미분석</div><div class="pnl-sub">같은 시각의 실제 시장 차트만 표시합니다.</div><div class="pnl-sub">이번 V4 신호 비교는 BTC에 적용한 결과입니다.</div></div>`;
  },
  lower() {
    el('sigsum').textContent = 'BTC 7건 · 분석 스냅샷';
    el('account-title').textContent = 'V4 모의 계좌';
    el('account').innerHTML = [['평가액','—'],['새 집계 손익','미검증'],['누적 실현 손익','—'],['거래','체결 기록 없음']].map(([k,v])=>`<div class="row acct"><span class="muted">${k}</span><span class="v">${v}</span></div>`).join('');
    el('tradesum').textContent = '주문·체결 없음';
    el('trades').innerHTML = '<div class="empty-state"><span aria-hidden="true">▤</span><strong>체결 기록 없음</strong><p>V4는 학습 신호를 확인하는 화면입니다.<br>손익·목표가·체결을 만들지 않았습니다.</p></div>';
  }
};
