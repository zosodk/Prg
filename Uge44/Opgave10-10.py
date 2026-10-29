filename = "williamshakespeare.txt"
with open(filename, "r", encoding="utf-8") as fil:
    cnt = 0
    for line in fil:
        cnt += line.count("and")
    print(f"Antallet af gange ordet and fremkommer er: ", cnt)