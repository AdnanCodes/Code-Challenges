/*
 * Complete the 'shortestSubstring' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts STRING s as parameter.
 */

function shortestSubstring(s) {
  //lets find unique letters in s
  let uniqueChars = "";

  for (let i = 0; i < s.length; i++) {
    //Lets check whether the unique character has been collected
    currentChar = s.charAt(i);
    //check for currentchar inside of uniqueChars
    if (uniqueChars.indexOf(currentChar) === -1) {
      //returns -1 when character is not found
      uniqueChars = uniqueChars + currentChar;
    } else {
      continue;
    }
  }
  return uniqueChars;
}

let test = "dabbabcd";
shortestSubstring(test);
