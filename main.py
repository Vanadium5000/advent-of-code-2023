from day1 import day1
from day2 import day2
from day3 import day3
from day4 import day4
from day5 import day5
from day6 import day6
from day7 import day7
from day8 import day8
from day9 import day9
from day10 import day10
from day11 import day11
from day12 import day12
from day13 import day13
from day14 import day14
from day15 import day15
from day16 import day16
from day17 import day17
from day18 import day18
from day19 import day19
from day20 import day20
from day21 import day21
from day22 import day22
from day23 import day23
from day24 import day24
from day25 import day25
# Not very beautiful, but it works.
def cli_fun():
    day_num = input("AoC CLI, Input Day (1-25): ")
    part_2 = input("Part 2? (y/n): ")
    if True:
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
            f1 = open(day_input, "r")
            eval("day" + (day_num) + "(f1.read(), part_2)")
            f1.close()
    #except:
    #    print("Invalid Input (or buggy code)!")
    #    cli_fun()


cli_fun()
