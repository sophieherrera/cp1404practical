for i in range(1, 21, 2):
    print(i, end=' ')
print()

#a
print("a.")
for i in range(0, 101, 10):
    print(i, end=' ')
print("\n")


#b
print("b.")
for i in range(20, 0, -1):
    print(i, end=' ')
print("\n")


#c
print("c.")
n = int(input("Number of stars: "))
for i in range(n):
    print("*", end='')
print("\n")


#d
print("d.")
for i in range(1, n + 1):
    print("*" * i)