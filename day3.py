def day3(day_input: str, part_2: bool):
    # this hurt so much
    lines = day_input.split("\n")
    digits = []
    digits_start = None
    is_part = False
    sum_parts = 0
    gears = {}

    for i, x in enumerate(lines):
        x += "."
        for i2, y in enumerate(x):
            if y.isdigit():
                if digits_start is None:
                    digits_start = i2
                digits += [y]
            elif digits_start is not None:
                if y != ".":  # and not y.isdigit():
                    is_part = True
                    if y == "*":
                        if (i, i2) in gears:
                            gears[(i, i2)] += [int("".join(digits))]
                        else:
                            gears[(i, i2)] = [int("".join(digits))]
                elif (
                    digits_start - 1 >= 0 and x[digits_start - 1] != "."
                ):  # and not x[digits_start - 1].isdigit():
                    is_part = True
                    if x[digits_start - 1] == "*":
                        if (i, digits_start - 1) in gears:
                            gears[(i, digits_start - 1)] += [int("".join(digits))]
                        else:
                            gears[(i, digits_start - 1)] = [int("".join(digits))]
                else:
                    for z in range(digits_start - 1, i2 + 1):
                        if z >= 0:
                            if (
                                len(lines) > i + 1
                                and len(lines[i + 1]) > z
                                and lines[i + 1][z] != "."
                                # and not lines[i + 1][z].isdigit()
                            ):
                                is_part = True
                                if lines[i + 1][z] == "*":
                                    if (i + 1, z) in gears:
                                        gears[(i + 1, z)] += [int("".join(digits))]
                                    else:
                                        gears[(i + 1, z)] = [int("".join(digits))]
                            if (
                                i > 0
                                and len(lines[i - 1]) > z
                                and lines[i - 1][z] != "."
                                # and not lines[i - 1][z].isdigit()
                            ):
                                is_part = True
                                if lines[i - 1][z] == "*":
                                    if (i - 1, z) in gears:
                                        gears[(i - 1, z)] += [int("".join(digits))]
                                    else:
                                        gears[(i - 1, z)] = [int("".join(digits))]
                if is_part:
                    sum_parts += int("".join(digits))
                digits = []
                digits_start = None
                is_part = False
    if not part_2:
        print(sum_parts)
    else:
        sum_gears = 0
        for x in gears.keys():
            if len(gears[x]) == 2:
                sum_gears += gears[x][0] * gears[x][1]
            elif len(gears[x]) >= 3:
                print("more than 2 gears, **** **** ******* ****** ******, ahh...")
        print(sum_gears)
