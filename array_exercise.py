

def removeName(nameArray, nameToRemove):
    for index in range (0, len(nameArray)-1):
        if nameArray[index].lower() == nameToRemove.lower():
            del nameArray[index]
    return nameArray


names = ["steph", "mike", "james", "wilson", "hilary", "trump", "obama"]
print("the name array is {0}".format(names))
nameToRemove = raw_input("please select a name to remove from the above list \n")
newArray = removeName(names, nameToRemove)
print("the name array after removing {0} is {1} !".format(nameToRemove,names))
