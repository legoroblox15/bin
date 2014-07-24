while True:
    print("need something decrypted? say it here or say 'how do I incrypt somethin")
    decode = input("g?' ")
    if decode == "how do I incrypt something?":
        print("you type your message that you want to send, then type 4 random cha")
        print("racters in between each letter of your message.")
        print("ex: 'hghjkifgtw yunwtligehimsoekwnkrlopqe' would be 'hi there'")
    else:
        decode = decode[::5]
        print(decode)
