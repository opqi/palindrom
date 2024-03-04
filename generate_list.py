import random
import string

def generate_palindrome(length):
    mid = length // 2
    left = ''.join(random.choices(string.ascii_lowercase, k=mid))
    right = left[::-1]
    if length % 2 == 0:
        return left + right
    else:
        return left + random.choice(string.ascii_lowercase) + right

def generate_non_palindrome(length):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

palindromes = [generate_palindrome(random.randint(3, 10)) for _ in range(50000)]
non_palindromes = [generate_non_palindrome(random.randint(3, 10)) for _ in range(50000)]

with open('test_data.txt', 'w+') as file:
    file.write(' '.join(palindromes+non_palindromes))
