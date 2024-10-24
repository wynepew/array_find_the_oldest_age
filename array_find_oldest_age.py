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

    if retry == "no":
        break
    elif retry != "yes":
        print("Invalid")
#Find oldest person and print
if citizen:
   oldest_person = None
   oldest_age = -1

   for person in citizen.values():
    if person["age"] > oldest_age:
        oldest_person = person
        oldest_age = person["age"]

if oldest_person is not None:
    print(f"The oldest person is {oldest_person['name']} with an age of {oldest_person['age']}.")
else:
    print("No entries.")