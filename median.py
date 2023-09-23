"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

# Sorted values test
# Input: 1,2,3,4,5
# Expected output: 3.0
# Five value test
# Input: 8, 789, 2, 9, 391
# Expected output: 9.0

def median(numbers):

    sortedList = sorted(numbers)
    print(sortedList)

    if len(sortedList) == 1:
        return sortedList[0]
    
    if len(sortedList) % 2 == 0:
        middle = int(len(sortedList) / 2)
        #print(middle)
        total = sortedList[middle] + sortedList[middle - 1]
        mean = float(total / 2)
        return float(mean)
    else:
        middle  = int(len(sortedList) // 2)
        mean = sortedList[middle]
        return float(mean)



while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(numbers)

medianValue = median(numbers)
print(medianValue)



