# PAIN; uncomputable
def day5(day_input: str, part_2: bool):
    locations = []
    sects = (
        day_input.replace("seeds: ", "")
        .replace("seed-to-soil map:", "s")
        .replace("soil-to-fertilizer map:", "s")
        .replace("fertilizer-to-water map:", "s")
        .replace("water-to-light map:", "s")
        .replace("light-to-temperature map:", "s")
        .replace("temperature-to-humidity map:", "s")
        .replace("humidity-to-location map:", "s")
    ).split("s")
    pre_seeds = sects.pop(0).split(" ")
    seeds = []
    if part_2:
        for i in range(0, len(pre_seeds), 2):
            for x in range(int(pre_seeds[i]), int(pre_seeds[i]) + int(pre_seeds[i + 1]), 1):
                seeds += [x]
    else:
        for x in pre_seeds:
            seeds += [int(x)]
    print(seeds)
    maps = []
    for i, x in enumerate(sects):
        maps += [[]]
        for y in x.split("\n"):
            if y != "":
                z = y.split(" ")
                maps[i] += [(int(z[0]), int(z[1]), int(z[2]))]
    # print(maps)
    for x in seeds:
        soil = None
        for y in maps[0]:
            # out start, in start, range length
            if x >= y[1] and x < y[2] + y[1]:
                soil = y[0] + x - y[1]
                break
        if soil == None:
            soil = x
        fert = None
        for y in maps[1]:
            if soil >= y[1] and soil < y[2] + y[1]:
                fert = y[0] + soil - y[1]
                break
        if fert == None:
            fert = soil
        water = None
        for y in maps[2]:
            if fert >= y[1] and fert < y[2] + y[1]:
                water = y[0] + fert - y[1]
                break
        if water == None:
            water = fert
        light = None
        for y in maps[3]:
            if water >= y[1] and water < y[2] + y[1]:
                light = y[0] + water - y[1]
                break
        if light == None:
            light = water
        temp = None
        for y in maps[4]:
            if light >= y[1] and light < y[2] + y[1]:
                temp = y[0] + light - y[1]
                break
        if temp == None:
            temp = light
        hum = None
        for y in maps[5]:
            if temp >= y[1] and temp < y[2] + y[1]:
                hum = y[0] + temp - y[1]
                break
        if hum == None:
            hum = temp
        loc = None
        for y in maps[6]:
            if hum >= y[1] and hum < y[2] + y[1]:
                loc = y[0] + hum - y[1]
                break
        if loc == None:
            loc = hum
        locations += [loc]
    print(min(locations))
