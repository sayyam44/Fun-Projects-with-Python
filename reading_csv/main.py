# with open("weather_data.csv") as data_file:
#     data=data_file.readlines()
#     print(data)

# import csv
# with open("weather_data.csv") as data_file:
#     data=csv.reader(data_file)
#     # print(data)
#     temp=[]
#     for row in data:
#         if row[1]!='temp':
#             temp.append(int(row[1]))
#     print(temp)

import pandas as pd
data = pd.read_csv("weather_data.csv")
print(data)

#for converting data to dictionary
data_dict=data.to_dict()
print(data)

#converting a particular column to a list
temp_list=data["temp"].to_list()
print(temp_list)

#print the row with day is monday
data[data.day=="Monday"]


#print the row with day is monday and its temperature on that day
monday=data[data.day=="Monday"]
monday_temp=(monday.temp)
print(monday_temp)

data_new=pandas.DataFrame(data_dict)
data.to_csv("data_new")