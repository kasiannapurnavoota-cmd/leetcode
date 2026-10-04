class Solution {
public:
    bool isPrime(int num) {
        if (num < 2) return false;
        for (int i = 2; i * i <= num; ++i) {
            if (num % i == 0) return false;
        }
        return true;
    }

    bool isPalindrome(int num) {
        long long reversed = 0, original = num;
        while (num > 0) {
            reversed = reversed * 10 + num % 10;
            num /= 10;
        }
        return original == reversed;
    }

    int primePalindrome(int n) {
        if (8 <= n && n <= 11) return 11;

        while (true) {
            if (isPalindrome(n) && isPrime(n)) {
                return n;
            }
            n++;
            // Skip even-length digit ranges
            if (1000 < n && n < 10000) n = 10001;
            else if (100000 < n && n < 1000000) n = 1000001;
            else if (10000000 < n && n < 100000000) n = 100000001;
        }
    }
};