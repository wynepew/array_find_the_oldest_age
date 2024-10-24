#ask user 
    #input name
    #input age
    #if invalid 
    #print error
#ask user again if they want to input again
    #if yes
    #input again
    #if no
    #print the name and age of the oldest person

citizen = {}

#Loop 1: ask user to input
while True:
    #Loop 2: use to retry when input raised an error
    while True:
        try:
            name = input("Input a name: ")
            age = int(input("Input age: "))

            citizen[name] = {
                "name" : name,
                "age" : age
            }
            print(citizen[name]["name"])
            print(citizen[name]["age"])

            retry = input("Do you want to input again: ")
            break
        except ValueError:
            print("Invalid input")

    if retry == "n":
        break
    elif retry != "y":
        print("Invalid")

