abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
name = ''


for item in abc:
    if item in ('a','b','i','e','l'):
        name = name + item
        print(name)

