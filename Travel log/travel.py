travel_log=[
    {"country":"France", "visits":3, "cities": ["Paris","Lille", "Dijon"]},
    {"country":"Germany", "visits":1, "cities": ["Berlin","Hamburg", "Stuttgart"]},
]

print(travel_log)
def add_new_country():
    Country=input("Enter the name of the country visited: ")
    Visits=int(input("Enter the number of time you have visited the country: "))
    Cities=input("Enter the name of the cities visited in that country (Sepereate the cities using a comma)\n").split(",")
    travel_log.append({"country":Country, "visits":Visits, "cities":Cities})


add_new_country()
print(travel_log[2])
