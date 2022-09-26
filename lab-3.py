
# even = list()
# odd = list()

# for number in range(1,101):
#     if number % 2 == 0:
#         even.append(number)
#     else:
#         odd.append(number)


# print("even number :",even)
# print("odd number :",odd)

# # for number in range(0,101,2):
# #     print(number)


# for i in range(5):
#     if i == 3:
#         print("break")
#         break
#     print(i)


# n1=1
# n2=2
# def sum():
#  return  n1+n2
# print(sum())


# def evenfun():

#     startnumber = int(input("Enter start number: "))
#     endnumber = int(input("Enter end number: "))

#     even = list()
#     odd = list()

#     for number in range(startnumber, endnumber+1):
#         if number % 2 == 0:
#             even.append(number)
#         else:
#             odd.append(number)
#     print("even number :", even)
#     print("odd number :", odd)


# evenfun()

# 1
def sum(a, b):
  return a+b

# 2
def print_element_list(list):
  for item in list:
    print(item, end='\n')
    
# 3
def sum_item_list(list):
    sum=0
    for item in list:
      sum+=item
    return sum
  
# 4
def largest_element(list):
  number = 0
  for item in list:
    if item > number:
      number=item
  print(number)
  
  
# 5
def  partial_list(list,number):
  # if number < len(list) and number > 0:
  if number is int:
    return list[0:number]
  return "not a valid number"


# 7
def break_list(list):
  for item in list:
    print(item)
    if item.lower() == "c++":
      break
    
    
    
list = ["Python", "C++", "Java"]
list_of_number = [1,2,3,10,11,12,13,14,15,16,4,5,6,7,8,9]
name = "Tuwaiq_Academy"
print(sum(2,1))
print_element_list(list)
print(sum_item_list(list_of_number))
largest_element(list_of_number)
print(partial_list(list_of_number,5))
print_element_list(name)
break_list(list)