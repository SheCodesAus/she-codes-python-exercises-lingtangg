# # for loops 1
# num = int(input('Enter a number: '))
# total = 0
# for output in range(1, num + 1):
#     print(f"{num} * {output} = {num * output}")

# # 2
# num = int(input('Enter a number: '))
# total = 0
# for value in range(1, num + 1):
#     total += value
# print(total)

# # 3
# random_numbers = [3, 5, 9, 1]
# total = 0
# for random_number in random_numbers:
#     total += random_number
# print(total)

# # while loops 1
# total = 0
# while True:
#     num = input('Enter a number: ')
#     if num == '':
#         break
#     total += int(num)
# print(total)

# 2
# firstNumber = int(input('Enter a number: '))
# for num in range(1, firstNumber + 1):
#     if num % 2 != 0:
#         print(num)

# num = 1
# while num <= firstNumber:
#     if num % 2 != 0:
#         print(num)
#     num += 1

# 3
chosenNumber = 88
num = int(input('Guess the number: '))
if num == chosenNumber:
    print('Correct!')
else:
    while True:
        if num == chosenNumber:
            print('Correct!')
            break
        elif num < chosenNumber:
            print('Too low')
        else:
            print('Too high')
        num = int(input('Guess the number: '))
    