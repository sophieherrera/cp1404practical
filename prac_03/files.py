#1.
name = input("Enter your name: ")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()
