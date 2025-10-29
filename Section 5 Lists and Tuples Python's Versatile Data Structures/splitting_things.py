# panagram = """The quick brown
#  fox jumps\tover
#   the lazy dog"""
#
# word = panagram.split()
# print(word)
# numbers = "9,223,372,036,854,775,807"
# print(numbers.split(","))

generated_list = [
    '9'," ",
    '2', '2', '3', " ",
    '3', '7', '2', " ",
    '0', '3', '6', " ",
    '8', '5', '4', " ",
    '7', '7', '5', " ",
    '8', '0', '7']

values = "".join(generated_list)
print(values)

values_list = values.split()
print(values_list)

int_value = []
for value in values_list:
    if int(value) != value:
        int_value.append(int(value))
print(int_value)