function checkPalindrome(str) {

    const len = string.length;
    
    let i = 0;

    while(i < len / 2){
        if (string[i] != string[len - 1 - i]) {
            return 'It is not a palindrome';
        }
        i++;
    }

    return 'It is a palindrome';
}

const string = "abcabc";

const value = checkPalindrome(string);

console.log(value);
