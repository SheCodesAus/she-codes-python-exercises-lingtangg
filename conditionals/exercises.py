# # 1 / 2
# moths_in_house = True
# mitch_is_home = True
# if moths_in_house and mitch_is_home:
#     print('Hooman! Help me get the moths!')
# elif not moths_in_house and not mitch_is_home:
#     print('No threats detected')
# elif moths_in_house and not mitch_is_home:
#     "Meoooooow! Hisss!"
# else:
#     print('Climn on Mitch')

# # 3
# light_colour = "Red"
# car_detected = True

# if light_colour == "Red" and car_detected:
#     print("Flash!")
# else:
#     print('Do nothing') 

# # 4
# height = int(input('What is your height in cm? '))
# if height >= 120:
#     print('Hop on')
# else:
#     print('Sorry, not today :(')

# # 5
# user = input('Username: ')
# pw = input('Password: ')
# if user == 'fleur' and pw == 'password123':
#     print('Correct!')
# else:
#     print('Incorrect')

# 6
email = input('Email: ')
if '@' in email:
    if '.' in email:
        print('Valid email address')
    else:
        print('Invalid email address')
else:
    print('Invalid email address')