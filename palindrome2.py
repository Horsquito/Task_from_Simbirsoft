def palindrom(string):
    a = string.split()
    a.reverse()
    b = ''.join(a)
    if b == string:
        return 'Палиндром!'
    else:
        return 'Не палиндром!'

def palindrom_dva(str1, str2):
    result1 = palindrom(str1)
    result2 = palindrom(str2)
    return result1, result2
