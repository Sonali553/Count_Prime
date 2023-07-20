s = "madam"
def check_Palindrome(s, start, end):
    if start > end:
        return True
    if(s[start] != s[end]):
        return False
    return check_Palindrome(s, start + 1, end - 1)
print(check_Palindrome(s, 0, len(s)-1))