#1.
name = input("Enter your name: ")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()

#2
in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file.close()
print(f"Hi {name}!")

#3
with open("numbers.txt", "r") as in_file:
    num1 = int(in_file.readline())
    num2 = int(in_file.readline())
    print(num1 + num2)  # Should print 59
