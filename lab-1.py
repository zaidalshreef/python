
# Question 1:

'''
Make 5 variable: integer, float, boolen and a string
Print the variables
increament the integer and print it
make a substring of the original string print it
convert the int to a string
conver the float to int

'''

number1 = 10
float1 = 10.20
boolean1 = True
string = "Name"

print("Int:", number1)
print("Float:", float1)
print("boolean:", boolean1)
print("String:", string)

number1 += 1

print("integer incremented by 1 : ", number1)

substring = string[2:]

print("substring :", substring)

number1 = str(number1)

float1 = int(float1)

################################

# Question 2:

'''
Make a list
Print the entire list
Print the first element
print the last element

'''

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("list :", list1)

print("value of first index in the list :", list1[0])
print("value of last index in the list :", list1[-1])


###############################################


# Question 3:

'''
Make a dictionary with 5 people, the dictionary should contain information such as:
name, phone_number

Print the dictionary

'''

dictionary = [{"name": "zaid", "phone_number": "0098308403"},
              {"name": "Ahmad", "phone_number": "008898989"},
              {"name": "Youssef", "phone_number": "00989789798"},
              {"name": "Faisal", "phonen_umber":  "007867867867"},
              {"name": "Khaled", "phonen_umber":  "08798789798"}]

dictionary2 = {"id1":{"name": "zaid", "phone_number": "0098308403"},
              "id2":{"name": "Ahmad", "phone_number": "008898989"},
              "id3":{"name": "Youssef", "phone_number": "00989789798"},
              "id4":{"name": "Faisal", "phonen_umber":  "007867867867"},
              "id5":{"name": "Khaled", "phonen_umber":  "08798789798"}}

print(dictionary)
print(dictionary2)
