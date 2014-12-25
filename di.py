import random
while True:
    numb = 0
    number_roll_max = 100
    number_roll_min = 1
    number_range_min = 1
    number_range_max = 1
    print_every_roll = False
    while True:
        numb = numb + 1
        roll = random.randint(number_roll_min, number_roll_max)
        if print_every_roll == True:
            print(roll)
        if roll >= number_range_min and roll <= number_range_max:
            if numb > 1:
                if number_range_min == number_range_max:
                    trys = "It took {} trys to get the number {}".format(numb, number_range_min)
                else:
                    number_range_min = number_range_min - 1
                    number_range_max = number_range_max + 1
                    trys = "It look {} trys to get a number in between {} and {}".format(numb, number_range_min, number_range_max)
            else:
                if number_range_min == number_range_max:
                    trys = "It took {} try to get the number {}".format(numb, number_range_min)
                else:
                    number_range_min = number_range_min - 1
                    number_range_max = number_range_max + 1
                    trys = "It look {} try to get a number in between {} and {}".format(numb, number_range_min, number_range_max)
            print(trys)
            break

