"""
CP1404/CP5632 - Practical
Loops for various ranges
"""

for i in range(1, 21, 2):
    print(i, end=' ')
print()
for i in range(0, 101, 10):
    print(i, end=' ')
print()
for i in range(20, 0, -1):
    print(i, end=' ')
print()
i = int(input("How many stars? "))
for i in range(i):
    print("*", end=' ')
print()
n = int(input("How many lines? "))
for i in range(0, n):
    print("*"* i, end=' ')
    print(sep=" ")
print()
