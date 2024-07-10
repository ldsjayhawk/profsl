with open("life-expectancy.csv") as life_file:
    next(life_file)
    for line in life_file:
        list = line.split(",")