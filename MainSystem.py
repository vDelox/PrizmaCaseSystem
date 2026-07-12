import random

tier5 = ["Navaja Knife Doppler", "Navaja Knife Marble Fade", "Navaja Knife Tiger Tooth", "Navaja Knife Ultraviolet", "Navaja Knife Damascus Steel", "Navaja Knife Rust Coat", "Stiletto Knife Doppler", "Stiletto Knife Marble Fade", "Stiletto Knife Tiger Tooth", "Stiletto Knife Ultraviolet", "Stiletto Knife Damascus Steel", "Stiletto Knife Rust Coat", "Talon Knife Marble Fade", "Talon Knife Tiger Tooth", "Talon Knife Damascus Steel", "Talon Knife Ultraviolet", "Talon Knife Rust Coat", "Talon Knife Doppler", "Ursus Knife Doppler", "Ursus Knife Marble Fade", "Ursus Knife Tiger Tooth", "Ursus Knife Damascus Steel", "Ursus Knife Ultraviolet", "Ursus Knife Rust Coat"]
tier4 = ["M4A4 The Emperor", "Five-SeveN Angry Mob"]
tier3 = ["XM1014 Incinegator", "AUG Momentum", "R8 Revolver Skull Crusher"]
tier2 = ["AWP Atheris", "Desert Eagle Light Rail", "Tec-9 Bamboozle", "MP5-SD Gauss", "UMP-45 Moonrise"]
tier1 = ["AK-47 Uncharted", "MP7 Mischief", "Galil AR Akoben", "FAMAS Crypsis", "MAC-10 Whitefish", "P90 Off World", "P250 Verdigris"]

while True:
    command = input("Type open to Open prizma case and exit to close the market : ")
    if command == "exit":
        print("Goodbye")
        break
    elif command == "open":
        Luck = random.randint(1, 1000)
        FloatGun = random.uniform(0.0, 1.0)
        SkinPalet = random.randint(1,1000)

        if Luck < 799:
            DropCase = random.choice(tier1)
            print("You have got " + str(DropCase) + " / float of : " + str(float(FloatGun)) + " / Seed : " + str(SkinPalet))

        elif 800 <= Luck < 959:
            DropCase = random.choice(tier2)
            print("You have got " + str(DropCase) + " / float of : " + str(float(FloatGun)) + " / Seed : " + str(SkinPalet))

        elif 959 <= Luck < 991:
            DropCase = random.choice(tier3)
            print("You have got " + str(DropCase) + " / float of : " + str(float(FloatGun)) + " / Seed : " + str(SkinPalet))

        elif 991 <= Luck < 997:
            DropCase = random.choice(tier4)
            print("You have got " + str(DropCase) + " / float of : " + str(float(FloatGun)) + " / Seed : " + str(SkinPalet))

        elif 997 <= Luck <= 1000:
            DropCase = random.choice(tier5)
            print("You have got " + str(DropCase) + " / float of : " + str(float(FloatGun)) + " / Seed : " + str(SkinPalet))
