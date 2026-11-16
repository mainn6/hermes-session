function aggregateCandles(rows, minutes) {
  if (![1, 5, 10].includes(minutes)) throw Error('Unsupported candle interval');
  const step = minutes * 60, result = [];
  rows.forEach((row, i) => {
    if (row.length !== 6 || !row.every(Number.isFinite) || row[0] % 60 ||
        (i && row[0] - rows[i - 1][0] !== 60) || row[3] > Math.min(row[1], row[4]) ||
        row[2] < Math.max(row[1], row[4]) || row[3] <= 0 || row[5] < 0) throw Error('Invalid candle');
    const bucket = Math.floor(row[0] / step) * step;
    if (bucket < rows[0][0]) return;
    const previous = result[result.length - 1];
    if (previous && previous[0] === bucket) {
      previous[2] = Math.max(previous[2], row[2]);
      previous[3] = Math.min(previous[3], row[3]);
      previous[4] = row[4]; previous[5] += row[5];
    } else result.push([bucket, ...row.slice(1)]);
  });
  return result;
}
if (typeof module !== 'undefined') module.exports = {aggregateCandles};
