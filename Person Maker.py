import random

name = random.choice(["Bella","Lucy","Chris","Gabe","Ben","Rob","Susan","Sue"])
age = random.randint(18,40)
color = random.choice(["red","orange","yellow","green","blue","purple"])
free = random.choice(["go fishing", "ride my bike", "play minecraft", "code"])
ft = random.randint(4,6)
inc = random.randint(1,11)
food = random.choice(["pizza", "chocolate", "icecream", "steak", "donuts"])
lb = random.randint(100,200)
hair = random.choice(["bloned", "brown", "ginger", "black"])
length = random.choice(["long", "short"])
hairstyle = random.choice(["curly", "frizzy", "straight"])
area = random.choice(["suburban", "city", "country"])
sisters = random.randint(0,4)
brothers = random.randint(0,4)
money = random.choice(["lower class", "upper class", "middle class"])
grades = random.choice(["bad", "deceant", "good"])
job = random.choice(["Mc. Donnalds", "a science lab", "an airport", "a school"])

age = str(age)
ft = str(ft)
inc = str(inc)
lb = str(lb)
sisters = str(sisters)
brothers = str(brothers)

if sisters == "0":
    sisters = "no"
if brothers == "0":
    brothers == "no"

person1 = "Hi, my name is {}, I am {}, and my favorite color".format(name, age)
person2 = "is {}. In my free time, I like to {}. I am".format(color, free)
person3 = "{} '{} and weight {} lbs. My favorite food is".format(ft, inc, lb)
person4 = "{} and I have {}, {}, {}, hair".format(food, length, hair, hairstyle)
person5 = ". I grew up in a {} area and I have {} sister(".format(area, sisters)
person6 = "s) and {} brother(s). My family was in the".format(brothers)
person7 = "{} and I got {} grades in school. I work at".format(money, grades)
person8 = "{}.".format(job)

print(person1)
print(person2)
print(person3)
print(person4)
print(person5)
print(person6)
print(person7)
print(person8)

