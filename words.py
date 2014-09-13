fin = open("C:\Users\Christopher\Desktop\words.txt")
for line in fin:
    words = line.strip()
randomword = random.choice(words)
print(randomword)


