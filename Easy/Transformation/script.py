with open("flag", "r") as file:
    flag = file.readline()
    print(flag)
    for i in range(0, len(flag)):
        first = chr(ord(flag[i]) >> 8)
        second = chr(flag[i].encode("utf-16be")[-1])
        print(f"{flag[i]}: {first}")
        print(f"{flag[i + 1]}: {second}")
        print()
