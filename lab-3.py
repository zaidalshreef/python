

even = list()
odd = list()

for number in range(0,101):
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)
        
        
print("even number :",even)
print("odd number :",odd)

# for number in range(0,101,2):
#     print(number)
