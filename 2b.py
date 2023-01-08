def multiplyNumbers(numbers):
    for i in range(len(numbers)):
        numbers[i] = numbers[i]*2
    return numbers

print(multiplyNumbers([1, 2, 3, 4, 5]))


def multiplyNumbersV2(numbers):
    numbers = [number*2 for number in numbers]
    return numbers

print(multiplyNumbersV2([1, 2, 3, 4, 5]))