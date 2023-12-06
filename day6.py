def day6(day_input: str, part_2: bool):
    lines = day_input.split("\n")

    times = []
    distances = []
    total_error_margin = 1
    if not part_2:
        for x in lines[0].replace("Time:", "").split(" "):
            if x.isdigit():
                times += [int(x)]
        for x in lines[1].replace("Distance:", "").split(" "):
            if x.isdigit():
                distances += [int(x)]
    else:
        times += [int(lines[0].replace("Time:", "").replace(" ", ""))]
        distances += [int(lines[1].replace("Distance:", "").replace(" ", ""))]
    for i in range(len(times)):
        posabilities = 0
        distance = distances[i]
        time = times[i]

        for x in range(0, time, 1):
            speed = x + 1
            if (time - x - 1) * speed > distance:
                posabilities += 1
        total_error_margin *= posabilities
    print(total_error_margin)
