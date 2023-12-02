# For the 24 days of advent
for x in range(25):
    # "w" creates a new file if it doesn't already exist
    f = open("day" + str(x + 1) + ".py", "w")
    f.write(
        "def day"
        + str(x + 1)
        + '(day_input: str, part_2: bool):\n    print("INCOMPLETE: Hello, from day '
        + str(x + 1)
        + '!")'
    )
    f.close()
