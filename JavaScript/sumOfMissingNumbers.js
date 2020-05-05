function sumMissingNumbers(arr) {
  const max = Math.max(...arr);
  const min = Math.min(...arr);
  return ((min + max) * (max - min + 1)) / 2 - arr.reduce((s, c) => s + c);
}
