def convertToCelsius(temp_in_f):
    return (temp_in_f - 32) * 5 / 9

print(convertToCelsius(350))

def oddEven(num):
    if num % 2 == 0:
        return "True"
    else:
        return "False"

print(oddEven(2))

def findMean(numbersList):
    return sum(numbersList) / len(numbersList)

print(findMean([10, 5, 6]))

def cost(price_per_unit, num_units):
    return price_per_unit * num_units

print(cost(1.49, 7))