

with open("string.txt", 'r') as file:
    string = file.readline()
    list_string = string.split(',')
    
    for i in range(len(list_string)):
        with open(f"part{i+1}.txt", 'w') as file:
            file.write(list_string[i])
            
