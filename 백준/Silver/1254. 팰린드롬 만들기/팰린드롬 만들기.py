def is_palindrome(s):
    return s == s[::-1]

def shortest_palindrome_length(s):
    n = len(s)
    for i in range(n):
        if is_palindrome(s[i:]):  
            return n + i 
    return 2 * n - 1 

# 입력 받기
s = input().strip()
print(shortest_palindrome_length(s))
