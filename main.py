# Not very beautiful, but it works.
def cli_fun():
    day_num = input("AoC CLI, Input Day (1-25): ")
    part_2 = input("Part 2? (y/n): ")
    try:
        if (int(day_num) < 1 or int(day_num) > 25) or (
            part_2.lower() != "y" and part_2.lower() != "n"
        ):
            print("Invalid Input!")
            cli_fun()
        else:
            if part_2 == "y":
                part_2 = True
            else:
                part_2 = False
            day_input = input("Input File Containing the Day's Input: ")
            f = open("day" + (day_num) + ".py", "r")
            f1 = open(day_input, "r")
            exec(f.read())
            eval("day" + (day_num) + "(f1.read(), part_2)")
            f.close()
            f1.close()
    except:
        print("Invalid Input (or buggy code)!")
        cli_fun()


cli_fun()
