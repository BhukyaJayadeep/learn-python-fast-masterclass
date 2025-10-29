menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]

# for meal in menu:
#     if "spam" in meal:
#         spams_count = meal.count("spam")
#         for i in range(spams_count):
#             del meal[spam]
#         print(meal)
#     else:
#         print(meal)

# for meals in menu:
#     for index in range(len(meals)-1,-1,-1):
#         if meals[index] =="spam":
#             del meals[index]
#
#     print(meals)

for meal in menu:
    for item in meal:
        if item != "spam":
            print(item)
    print()
