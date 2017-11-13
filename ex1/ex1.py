import random
import string

lis = []
while(1):
    password = input("what password do you want:wake or strong")
    if password == "strong" or password == "STRONG" :
        for i in range(3):
            lis.append(str(random.randrange(1,10)))
        for i in range(5):
            lis.append(random.choice(string.ascii_letters))
        L=['@','#','$','%','^','&']
        lis.append(random.choice(L))
        random.shuffle(lis)
        st = "".join(lis)
        print(st)
        break
    elif password == "wake" or password == "WAKE":
        for i in range(9):
            lis.append(random.choice(string.ascii_uppercase))
        random.shuffle(lis)
        st = "".join(lis)
        print(st)
        break
    else:
        pass
