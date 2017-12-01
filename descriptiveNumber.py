numberBase = {  "1":"one",
                "2":"two",
                "3":"three",
                "4":"four",
                "5":"five",
                "6":"six",
                "7":"seven",
                "8":"eight",
                "9":"nine",
                "0":"zero" }
tendigitBase = {  "1":"teen",
                  "2":"twenty",
                  "3":"thirty",
                  "4":"fourty",
                  "5":"fifty",
                  "6":"sixty",
                  "7":"seventy",
                  "8":"eighty",
                  "9":"ninty",
                  }
digitBase = { "2":"hundred",
                "3":"thousand",
                "6":"million",
                "9":"billsion"}

def numberConverter(number):
    numberArray = ""
    numberArray = list(str(number))

    # for single digit case
    if len(numberArray) == 1:
        for key in numberBase :
            if key == numberArray[0]:
                return numberBase[key]
    # for double digit case
    elif len(numberArray)== 2:
        resultString = []
        for key in numberBase:
            if key == numberArray[1]:
                resultString = resultString.append(numberBase[key])
        for key in numberBase:
            if key == numberArray[0]:
                resultString = resultString.append(numberBase[key])
        return resultString

input_number = int(raw_input("please enter a number less than 100\n"))
converted_number = numberConverter(input_number)

print("the converted descriptive number is {0}".format(converted_number))
