# # 1
# foods = ["orange","apple","banana","strawberry","grape","blueberry",["carrot", "cauliflower", "pumpkin"],"passionfruit","mango","kiwifruit"]
# print(f"{foods[0]}")
# print(f"{foods[2]}")
# print(f"{foods[-1]}")
# print(f"{foods[0:3]}")
# print(f"{foods[-3:]}")
# print(f"{foods[6][-1]}")

# # 2
# mailing_list = [["Chilli", "chilli@thechihuahua.com"],["Roary", "roary@moth.catchers"],["Remus", "remus@kapers.dog"],["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"],["Ivy", "noreply@goldendreamers.xyz"],]
# updatedList = []
# for mail in mailing_list:
#     joined = ': '.join(mail)
#     updatedList.append(joined)
# print(updatedList)

# # 3
# names = []
# for name in range(0, 3):
#     names.append(input('Enter a name: '))
# print(names)

# 4 
a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]
d = []
e = [] 

d.extend((a, b, c))
print(d)
e = a + b + c
print(e)