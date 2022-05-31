#!/usr/bin/python3
for i in range(0, 10):
    for k in range(i + 1, 10):
        if (i != 0) or (k != 1):
            print(", {:02d}".format(i * 10 + k), end="")
        else:
            print("{:02d}".format(i * 10 + k), end="")

print()
