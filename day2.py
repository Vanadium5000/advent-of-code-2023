def day2(day_input: str, part_2: bool):
    sum_ids = 0
    sum_powers = 0
    lines = day_input.split("\n")
    for x in lines:
        max_red = 0
        max_green = 0
        max_blue = 0
        # To get number from format "Game {ID}: ..."
        game_id = x.split(":")[0][5:]
        x = x[7 + len(game_id) :]  # Removes "Game {ID}: "
        for y in x.split("; "):
            for z in y.split(", "):
                if "red" in z:
                    max_red = max(max_red, int(z[:-4]))
                if "green" in z:
                    max_green = max(max_green, int(z[:-6]))
                if "blue" in z:
                    max_blue = max(max_blue, int(z[:-5]))
        if max_red <= 12 and max_green <= 13 and max_blue <= 14:
            sum_ids += int(game_id)
        sum_powers += max_red * max_green * max_blue
    if not part_2:
        print(sum_ids)
    else:
        print(sum_powers)
