function hourglassSum(arr) {
  let allMatrix = [];

  let i = 0;
  let j = 0;
  while (allMatrix.length < 16) {
    let top = arr[i][j] + arr[i][j + 1] + arr[i][j + 2]; // [0,1,0]
    let mid = arr[i + 1][j + 1]; //   [1]
    let bottom = arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]; //[1,1,1]
    let matrix = top + mid + bottom;
    allMatrix.push(matrix);
    if (j < 3) {
      j++;
    } else {
      if (i < 3) {
        j = 0;
        i++;
      }
    }
  }
  return Math.max(...allMatrix);
}
