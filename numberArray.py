# define the getLargestNumber function
def getLargestNumber(numbers):
    largestNumber = 1
    for number in numbers:
        if number > largestNumber:
            largestNumber = number
    return largestNumber


def getSmallestNumber(numbers):
    smallestNumber = float("inf")
    for number in numbers:
        if number < smallestNumber:
            smallestNumber = number
    return smallestNumber


while True: # infiite loop to continously run the program

    # get the numbers from input, the input format will be a string
    # the string is then split to an array of strings
    numbers = ""
    numberString = raw_input("please enter some numbers separated by space\n")
    numbers = numberString.split()

    # transform the array of strings to an array of integers
    for i in range (0,len(numbers)):
        numbers[i]= int(numbers[i])

    #use the function defined above to find the largets/smallest number
    largest = getLargestNumber(numbers)
    print("\nthe largest number in this array is {0} !".format(largest))
    smallest = getSmallestNumber(numbers)
    print("\nthe smallest number in this array is {0} !".format(smallest))

    # conditions to quit the while loop
    choice = raw_input("\nplease enter q to quit otherwise press enter\n")
    if choice == "q":
        break
