
# Question 1 :



list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list)
list.append(10)
print(list)
list.remove(5)
print(list)
list.reverse()
print(list)
list.sort()
print(list)
list.insert(0, 100)
print(list)
print(list.index(list[len(list) - 1]))


# Question 2 :

people = ["Ahmed", "Nasser", "Mohammed"]

print(','.join(people))



# Question 3 :

dic = [{"name":"zaid" , "phone_number":"05034545545"},
       {"name":"ahmad" , "phone_number":"050767677"},
       {"name":"faisal" , "phone_number":"0507777"},]

print(dic)

dic.append({"name":"faris" , "phone_number":"050332999"} )

print("add person to list ",dic)

dic[0].pop('name')

print("delete name from first item :",dic)

dic[-1]["phone_number"] = "050999999999"

print("add phone number to last item :",dic)

print("key is found in last item :","name" in dic[0].keys())

print("key is found in last item :","name" in dic[0])