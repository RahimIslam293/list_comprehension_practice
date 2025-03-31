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
