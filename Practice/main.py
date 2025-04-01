import random
import pandas
list = [1,2,3]
newlist = [n+1 for n in list]
newlist_a = [n for n in list if n<2] #conditional list comprehension

print(list)
print(newlist)
print(newlist_a)

name = "Rahim"
new_name = [letter for letter in name]
print(new_name)

doubled_number = [j*2 for j in range(1,5)]
print(doubled_number)


#squared Numbers Test
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [i * i for i in numbers] # or i**2
print(squared_numbers)

#convert string to in plus make even numbers test
list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(s) for s in list_of_strings]
result = [e for e in numbers if e%2==0]
print(result)


#grabs text from two files; converts to int; finds alike nums
with open("file1.txt", "r") as file1:
    list_1 = [int(line.strip()) for line in file1.readlines()]

with open("file2.txt", "r") as file2:
    list_2 = [int(line.strip()) for line in file2.readlines()]

result = [n for n in list_1 if n in list_2]

print(result)

#dictionary comprehension
names = ["Alex", "Barb", "Jan", "Jeff"]
scores_dict = {name : random.randint(1,100) for name in names}

passed_students = {name : grade for name,grade in scores_dict.items() if grade > 50 }
print(scores_dict)
print(passed_students)

#ex 1 DC
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
sentence_list = sentence.split()
result = {word:len(word) for word in sentence_list}


#ex 2
weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {day : (temp* 9/5 + 32) for (day,temp) in weather_c.items()}

print(weather_f)

#Dataframe Comprehension

weather_df_dict = {"day":[], "temp":[]}
weather_df_dict["day"].extend(key for key in weather_c)
weather_df_dict["temp"].extend(index for (key,index) in weather_c.items())
weather_df =  pandas.DataFrame(weather_df_dict)
print(weather_df_dict)

for(index,row) in weather_df.iterrows():
    print(index)
    print(row)
    print(row.day)
    print(row.temp)

