# Suprisingly difficult


def day4(day_input: str, part_2: bool):
    sum_cards = 0
    lines = day_input.split("\n")
    global lines_cache
    lines_cache = []

    def count_matches(card: int):
        global lines_cache
        if len(lines_cache) > card:
            return lines_cache[card]
        match_count = 0
        temp = lines[card].split(": ")[1]
        input = temp.split(" | ")[1].split(" ")
        answers = temp.split(" | ")[0].split(" ")
        for x in input:
            if x.isdigit() and x in answers:
                match_count += 1
        lines_cache += [match_count]
        return match_count

    for line in range(len(lines)):
        number = count_matches(line)
        if number != 0:
            sum_cards += 2 ** (number - 1)
    if not part_2:
        print(sum_cards)
    else:
        global count_cards
        count_cards = 0
        def handle_card(card: int):
            global count_cards
            count_cards += 1
            global lines_cache
            x = lines_cache[card]
            while x > 0:
                handle_card(card + x)
                x -= 1


        for i in range(len(lines)):
            handle_card(i)
        print(count_cards)