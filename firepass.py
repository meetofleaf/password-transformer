import random as r

print("\nFire Password")
print("_____________\n")

user_pass = input("Password: ")

MAP = {'a':'@', 'A':'4', 'E':'3', 'g':'9', 'i':'I', 'I':'|', 'K':'|<', 'l':'1', 'L':'\_', 'o':'0', 'O':'0', 'p':'P', 's':'S', 'S':'5', 't':'+', 'T':'+', 'v':'\/', 'V':'\/', 'w':'vv', 'W':'VV', 'x':'><', 'X':'><', '0':')', '1':'!', '2':'@', '3':'#', '4':'$', '5':'%', '6':'^', '7':'&', '8':'*', '9':'('}

def passgen(upass):
    chars = list(upass)
    for i in range(len(chars)):
        if chars[i] in MAP:
            chars[i] = MAP[chars[i]]
    
    firepass = "".join(chars) + "_" + str(r.randint(0,1000))
    return firepass

print(passgen(user_pass))
