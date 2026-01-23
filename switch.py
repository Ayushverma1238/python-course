def switch(day):
    return {
        1:"Monday",
        2:"Tuesday",
        3:"Wednesday",
        4:"Thursday",
        5:"Friday",
        6:"Saturday"
    }.get(day, "Invalid day")

print(switch(5))

class Number:
    def __init__(self, value):
        self.value = value
    def __add__(self, other):
        return self.value + other.value
n1 = Number(5)
n2 = Number(10)
print(n1 + n2)