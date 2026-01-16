# student = {
#     "name":{"Ayush", "Balvant"},
#     "age" : {20,21},
#     "Interested":{"Coding", "Coding"}
# }

# student["color"] = "red"

# print(student["name"])

# print(student.get("email"))
# # print(student["email"])  Error

# for key in student:
#     print(key, " : ", student[key])

# x = [
#     {"name":"Ayush", "Age": 20},
#     {"name":"Balvant", "Age": 21},
#     {"name":"Adsd", "Age": 32},
# ]

# print(x)

country = {
    "India":"Delhi",
    "Australia":"Canbra",
    "Bangladesh":"Dhaka",
    "Nalla":"Islamabad",
    "France":"Barlin",
    "Sri Lanka":"Shri jaiverdhanam puram kotte",
    "USA":"Washington"

}
print(country)

print(country["India"])

country["Japan"] = "Tokyo"

country["USA"] = "NewYork"
print(country)

country.pop("France")
print(country)

student = {
    "Ayush":96,
    "Balvant":95
}
print(student)
print(student.keys())
print(student.values())
print(student.items())
if(student.get("Rahul") == None):
    print("Rahul not found in dictionary")
else:
    print("Rahul mark is: ", student["Rahul"])


student.update({"Rahul":46,"Avanish":54, "Anurag":43})

print(student)

country.pop("Nalla")
# country.pop("Germany")
print(country)

country.clear()
print(country)