int reverse(int test, int reversed){
    if (test < 10){
        return reversed*10 + test;
    }
    else{
        reversed = reversed * 10 + test%10;
        reverse(test/10, reversed);
    }
}

bool is_palindrome(int test){
    int temp = test;
    int reversed = 0;
    int reverse(int test, int reversed);

    reversed = reverse(test, reversed);
    if (test == reversed){
        return true;
    }
    return false;
}