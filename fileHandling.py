with open(r"E:\fileHand\Student.txt", "r") as file:
    content = file.readline()
    print(content)

with open(r"E:\fileHand/Student.txt", "a") as file:
    file.write("\nI am a Btech 3rd year student")

with open(r"E:\fileHand\Student.txt", "r") as file:
    content = file.readlines()
    print(len(content))

with open(r"E:\fileHand/Student.txt", "w") as file:
    file.write("\nAyush Verma, 30, 98")
    file.write("\nBalvant, 30, 90")
    file.write("\nAvanish, 20, 87")

with open(r"E:\fileHand\Student.txt", "r") as file:
    content = file.read()
    print(content)



with open(r"E:\fileHand/Student.txt", "a") as file:
    file.write("\nAnurag, 30, 98")

with open(r"E:\fileHand\Student.txt", "r") as file:
    content = file.read()
    print(content)


with open(r"E:\fileHand\Student.txt", "r+") as file:
    file.seek(0, 0)
    file.write("Divyanshu, 43, 78\n")
    # print(file.read())


    
with open(r"E:\fileHand\Student.txt", "r") as file:
    content = file.read()
    print(content)
