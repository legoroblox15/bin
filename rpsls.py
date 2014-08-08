import random
import time

while True:

    print("rock, paper, scissors, lizard, or spock?")
    player = input(">>> ").lower().strip()

    if player == "rock":
        shoot()
    if player == "paper":
        shoot()
    if player == "scissors":
        shoot()
    if player == "lizard":
        shoot()
    if player == "spock":
        shoot()
    else:
        er = "I'm sorry, '{}' is not one of the choices".format(player)
        print(er)

def shoot():
    cpu = random.choice(["rock", "paper", "scissors", "lizard", "spock"])
        
    print("rock")
    time.sleep(1)
    print("paper")
    time.sleep(1)
    print("scissors")
    time.sleep(1)
    print("lizard")
    time.sleep(1)
    print("spock")
    time.sleep(1)
    vs = "{} vs {}".format(player, cpu)
    print(vs)
    time.sleep(1)
    print("it's a tie")
