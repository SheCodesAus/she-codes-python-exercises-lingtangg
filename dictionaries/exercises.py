import csv

# # 1
# groceries = {"Baby Spinach": 2.78,"Hot Chocolate": 3.70,"Crackers": 2.10,"Bacon": 9.00,"Carrots": 0.56,"Oranges": 3.08}
# # quantity = {"Baby Spinach": 1,"Hot Chocolate": 3,"Crackers": 2,"Bacon": 1,"Carrots": 4,"Oranges": 2}
# quantity = {"Baby Spinach": 2,"Hot Chocolate": 1,"Crackers": 4,"Bacon": 0,"Carrots": 8,"Oranges": 5}

# for item, price in groceries.items():
#     cost = round(groceries[item] * quantity[item], 2)
#     print(f"{quantity[item]} {item} @ {groceries[item]} = {cost}")

# 2
# colour_counts = {"blue": 0,"green": 0,"yellow": 0,"red": 0,"purple": 0,"orange": 0,}
# # colours = ["purple","red","yellow","blue","purple", "orange", "blue", "purple", "orange", "green"]
# colours = ["orange","purple","blue","yellow","green","green","purple","purple","green","blue","green","orange","purple","blue","green","orange","orange","red","yellow","yellow"]

# for colour in colours:
#     colour_counts[colour] += 1

# print(colour_counts)

# # 3
# # names = ["Maddy", "Bel", "Elnaz", "Gia", "Izzy","Joy", "Katie", "Maddie", "Tash", "Nic","Rachael", "Bec", "Bec", "Tabitha", "Teagen","Viv", "Anna", "Catherine", "Catherine", "Debby","Gab", "Megan", "Michelle", "Nic", "Roxy","Samara", "Sasha", "Sophie", "Teagen", "Viv"]
# names = ["Miranda", "Sophie", "Emily", "Taylor", "Anne","Djuarli", "Anika", "Rosie", "Miranda", "Taylor","Abby", "Sarah", "Teagen", "Abby", "Abby","Maddie", "Miranda", "Rosie"]

# unique_names = list(set(names))
# name_counter = {}
# for u_name in unique_names:
#     name_counter[u_name] = 0

# for name in names:
#     name_counter[name] += 1

# print(name_counter)

# # 4
# with open("colours_20_simple.csv") as csv_file:
#     reader = csv.reader(csv_file)
#     dict = {}
#     for line in reader:
#         dict[line[1]] = line[2]
#     print(dict)

# 5
with open("colours_20_simple.csv") as csv_file:
    reader = csv.reader(csv_file)
    dict = {}
    for line in reader:
        dict[line[1]] = [line[0], line[2]]
    print(dict)