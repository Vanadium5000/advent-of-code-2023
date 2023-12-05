"""seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

# Buggy code
def day5(day_input: str, part_2: bool):
    locations = []
    print("INCOMPLETE: Hello, from day 5!")
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
    seeds = sects.pop(0).split(" ")
    for i, x in enumerate(seeds):
        seeds[i] = int(x)
    maps = []
    for i, x in enumerate(sects):
        maps += [[]]
        for y in x.split("\n"):
            if y != "":
                z = y.split(" ")
                maps[i] += [(int(z[0]), int(z[1]), int(z[2]))]
    print(maps)
    for x in seeds:
        for y in maps[0]:
            # out start, in start, range length
            if x >= y[1] and x < y[2] + y[1]:
                soil = y[0] + x - y[1]
                break
        for y in maps[1]:
            if soil >= y[1] and soil < y[2] + y[1]:
                fert = y[0] + soil - y[1]
                break
        for y in maps[2]:
            if fert >= y[1] and fert < y[2] + y[1]:
                water = y[0] + fert - y[1]
                break
        for y in maps[3]:
            if water >= y[1] and water < y[2] + y[1]:
                light = y[0] + water - y[1]
                break
        for y in maps[4]:
            if light >= y[1] and light < y[2] + y[1]:
                temp = y[0] + light - y[1]
                break
        for y in maps[5]:
            if temp >= y[1] and temp < y[2] + y[1]:
                hum = y[0] + temp - y[1]
                break
        for y in maps[6]:
            if hum >= y[1] and hum < y[2] + y[1]:
                loc = y[0] + hum - y[1]
                break
        print(x, loc)