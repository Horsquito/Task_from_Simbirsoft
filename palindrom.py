def palindrom(string):
    a = string.split()
    a.reverse()
    b = ''.join(a)
    if b == string:
        return 'Палиндром!'
