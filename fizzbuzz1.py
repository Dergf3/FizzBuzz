#Added comments in

for i in range(1,100):      #Loops an int starting from 1 and ending at 100
    if i % 3 == 0 and i % 5 == 0:       #Checks for fizzbuzz
        print("fizzbuzz")
        continue
    elif i % 3 == 0:                     #Checks for fizz
        print("fizz")
        continue
    elif i % 5 == 0:                     #Checks for buzz
        print("buzz")
        continue
    print(i)
