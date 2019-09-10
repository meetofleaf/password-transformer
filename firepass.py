import random as r

print("\nFire Password")
print("_____________\n")

user_pass = input("Password: ")

def passgen(upass):
    chars = list(upass)
    for i in range(len(chars)):
        if chars[i] == 'a':
            chars[i] = '@'
        elif chars[i] == 'A':
            chars[i] = '4'
        elif chars[i] == 'E':
            chars[i] = '3'
        elif chars[i] == 'g':
            chars[i] = '9'
        elif chars[i] == 'i':
            chars[i] = 'I'
        elif chars[i] == 'I':
            chars[i] = '|'
        elif chars[i] == 'K':
            chars[i] = '|<'
        elif chars[i] == 'l':
            chars[i] = '1'
        elif chars[i] == 'L':
            chars[i] = '\_'
        elif chars[i] == 'o' or chars[i] == 'O':
            chars[i] = '0'
        elif chars[i] == 'p':
            chars[i] = 'P'
        elif chars[i] == 's':
            chars[i] = 'S'
        elif chars[i] == 'S':
            chars[i] = '5'
        elif chars[i] == 't' or chars[i] == 'T':
            chars[i] = '+'
        elif chars[i] == 'v':
            chars[i] = '\/'
        elif chars[i] == 'V':
            chars[i] = '\/'
        elif chars[i] == 'w':
            chars[i] = 'vv'
        elif chars[i] == 'W':
            chars[i] = 'VV'
        elif chars[i] == 'x' or chars[i] == 'X':
            chars[i] = '><'
        elif chars[i] == '0':
            chars[i] = ')'
        elif chars[i] == '1':
            chars[i] = '!'
        elif chars[i] == '2':
            chars[i] = '@'
        elif chars[i] == '3':
            chars[i] = '#'
        elif chars[i] == '4':
            chars[i] = '$'
        elif chars[i] == '5':
            chars[i] = '%'
        elif chars[i] == '6':
            chars[i] = '^'
        elif chars[i] == '7':
            chars[i] = '&'
        elif chars[i] == '8':
            chars[i] = '*'
        elif chars[i] == '9':
            chars[i] = '('
        else:
            continue
    
    firepass = "".join(chars) + "_" + str(r.randint(0,1000))
    return firepass

print(passgen(user_pass))
