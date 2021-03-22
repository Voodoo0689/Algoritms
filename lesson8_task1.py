import hashlib

user_string = input("Введите любую строку из строчных латинских букв:\n")

def func(string):
    sum_substring = set()
    for i in range(len(string)):
        for j in range(len(string), i, -1):
            hash_str = hashlib.sha1(string[i:j].encode('utf-8')).hexdigest()
            sum_substring.add(hash_str)

    return f'{len(sum_substring) - 1} различных подстрок в строке {string}'


print(func(user_string))
