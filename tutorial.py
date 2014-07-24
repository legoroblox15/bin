lang = input("english?, español? ")
lang = lang.strip().lower()
if lang == "english":
    lang = "en"
elif lang == "español":
    lang = "sp"
if lang == "en":
    print("Hello! and welecome to my Python tutorial. ")
    y/n = input("Would you like to start? y/n. ")
    y/n = y/n.strip().lower()
    if y/n == "y":
        print("good")
        print("ok so the first thing you need to know is 'print', The syntax is")
        print('as follows: print("*message*")')
        while True:
            ans1 = input('so try writing a script that says "Hello World"')
            
    elif y/n == "n":
        print("to bad! >:)")
