function checkPalindrome(input) {

    const str_len = input.length;
    
    let i = 0;

    while(i < str_len / 2){
        if (input[i] != input[str_len - 1 - i]) {
            return 'It is not a palindrome';
        }
        i++;
    }

    return 'It is a palindrome';
}

const string = "racecar";

const value = checkPalindrome(string);

console.log(value);

console.log(checkPalindrome("abcdef"));
