import csv

# # 1
# with open("colours_20.csv") as csv_file:
#     reader = csv.reader(csv_file)
#     for line in reader:
#         print(line[1] + " " + line[2] + " " + line[4])

# # 2
# with open("colours_20_simple.csv") as csv_file:
#     reader = csv.reader(csv_file)
#     for line in reader: 
#         print(line[2] + ", Hex: " + line[1] + ", RGB: " + line[0])

# # 4
# with open('colours_213.csv') as csv_file:
#     reader = csv.reader(csv_file)
#     colours = [["red", 0], ["green", 0], ["blue", 0], ["yellow", 0]]
    
#     for line in reader:
#         for i in range(0, len(colours)):
#             if colours[i][0] in line[4]:
#                 colours[i][1] += 1
#     print(colours)

# 5
with open('galaxies.csv') as csv_file:
    reader = csv.reader(csv_file)
    next(reader, None) # skip the headers
    velocity = [["min", 999999999, 0], ["max", 0, 0]]
    for line in reader:
        if int(line[1]) < velocity[0][1]:
            velocity[0][1] = int(line[1])
            velocity[0][2] = int(line[0])
        elif int(line[1]) > velocity[1][1]:
            velocity[1][1] = int(line [1])
            velocity[1][2] = int(line[0])

    print(f"Galaxy {velocity[0][2]} has the min velocity of {velocity[0][1]}km/sec. \nGalaxy {velocity[1][2]} has the max velocity of {velocity[1][1]}km/sec.")