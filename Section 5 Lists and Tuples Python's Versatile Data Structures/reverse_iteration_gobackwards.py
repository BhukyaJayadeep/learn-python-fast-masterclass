data = [104,101,4,105,308,103,5,
        107,100,306,106,102,108]
data_2= [104,101,4,105,308,103,5,
        107,100,306,106,102,108]
min_valid = 100
max_valid = 200

for index in range(len(data)-1,-1,-1):
    if data[index]<min_valid or data[index]>max_valid:
        print(index,data)
        del data[index]

print(data)

# for index in range(0,len(data_2)-1,1):
#     if data_2[index]<min_valid or data_2[index]>max_valid:
#         print(index,data_2)
#         del data_2[index]
# print(data_2)