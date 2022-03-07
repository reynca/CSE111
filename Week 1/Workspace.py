# import math
# list = []
# def circle_area(radius):
#     area = (radius**2) * math.pi
#     area = round(area, 2)
#     return area

# radius = float(input("What is the radius? "))

# def bigger_circles():
#     radius_number = 0
#     user_input_number = int(input("How many times do you want to repeat the function? "))
#     while radius_number != user_input_number:
#         area = circle_area(radius + radius_number)
#         list.append(area)
#         radius_number += 1


# bigger_circles()
# print(list)




# model = "GMC Acadia"
# length = 193
# width = 75
# height = 67

# # Open a text file named dimensions.txt in append mode.
# with open("volumes.txt", "at") as volum_file:

#     # Print a car's model and dimensions to the file.
#     print(model, file=volum_file)
#     print(f"{length}, {width}, {height}", file=volum_file)

# math = 4**2
# print(math)



m = input("sdasad: ")
ma = m.split(",")
list_length = len(ma)
element_count = list_length/2
print(element_count)
