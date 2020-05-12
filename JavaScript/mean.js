function mean(num) {
  //Convert num to string
  let convert = "";
  convert = num.toString();
  //Split the string into array
  convert = convert.split("");
  //Convert each string to int of the array
  convert = convert.map((element) => parseInt(element));
  //Sum of string
  let avg = 0;
  let sum = 0;
  let size = convert.length;

  sum = convert.reduce((acc, next) => {
    return acc + next;
  }, 0);
  //Divide the sum with total number of digits aka length
  avg = sum / size;
  return avg;
}
