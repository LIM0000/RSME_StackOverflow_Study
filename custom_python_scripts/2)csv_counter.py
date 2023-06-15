# Check if the total javascript posts are about the same as the number from stackoverflow

with open("D:\\Download (From Chrome)\\result_1.csv") as f:
    print(sum(1 for line in f))