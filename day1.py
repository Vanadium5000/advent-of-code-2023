def day1(day_input: str, part_2: bool):
    if not part_2:
        lines = day_input.split("\n")
    else:
        lines = day_input.split("\n")

        for i, _ in enumerate(lines):
            for i1, _ in enumerate(lines[i]):
                try:
                    if lines[i][i1 : i1 + 3] == "one":
                        lines[i] = lines[i].replace("one", "1ne", 1)
                except:
                    lines[i]
                try:
                    if lines[i][i1 : i1 + 3] == "two":
                        lines[i] = lines[i].replace("two", "2wo", 1)
                except:
                    lines[i]
                try:
                    if lines[i][i1 : i1 + 5] == "three":
                        lines[i] = lines[i].replace("three", "3hree", 1)
                except:
                    lines[i]
                try:
                    if lines[i][i1 : i1 + 4] == "four":
                        lines[i] = lines[i].replace("four", "4our", 1)
                except:
                    lines[i]
                try:
                    if lines[i][i1 : i1 + 4] == "five":
                        lines[i] = lines[i].replace("five", "5ive", 1)
                except:
                    lines[i]
                try:
                    if lines[i][i1 : i1 + 3] == "six":
                        lines[i] = lines[i].replace("six", "6ix", 1)
                except:
                    lines[i]
                try:
                    if lines[i][i1 : i1 + 5] == "seven":
                        lines[i] = lines[i].replace("seven", "7even", 1)
                except:
                    lines[i]
                try:
                    if lines[i][i1 : i1 + 5] == "eight":
                        lines[i] = lines[i].replace("eight", "8ight", 1)
                except:
                    lines[i]
                try:
                    if lines[i][i1 : i1 + 4] == "nine":
                        lines[i] = lines[i].replace("nine", "9ine", 1)
                except:
                    lines[i]
    total = 0

    numbers = []
    for line in lines:
        last_number = None
        for y in line:
            try:
                if last_number is None:
                    first_number = int(y)
                last_number = int(y)
            except:
                continue
        total += first_number * 10 + last_number
        numbers += [first_number * 10 + last_number]

    print(total)
