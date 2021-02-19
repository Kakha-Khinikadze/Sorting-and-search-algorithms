
numbers = [int(x) for x in input("Enter a sequence of numbers: ").split()]

for i in range(len(numbers)):
    for j in range(len(numbers)-i-1):
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]


def binary_search(array, element, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if array[middle] == element:
        return middle
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)


while True:
    try:
        element = int(input("Enter the number: "))
        if element < 0 or element > 999:
            raise Exception
        break
    except ValueError:
        print("Need to enter the number!")
    except Exception:
        print("Wrong range!")

array = [i for i in range(1, 1000)]

print(binary_search(array, element, 0, 999))
