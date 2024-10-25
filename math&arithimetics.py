import math
friends = 9
# friends +=5
# friends -=5
# friends %=5
# print(friends)
# print(math.pi)
# print(math.sqrt(friends))
# getting the volume of a cylinder ////////////////////
# Radius = 21
# height = 10
# volume = math.pi * Radius**2 *height
#
# print('Volume = 22/7 *r² *h')
# print(f'v={math.pi} *{Radius**2} *{height}')
# print(f'{volume}')
radius = float(input('What is the radius of the circle:?'))
height = float(input('What is the height of the cylinder:?'))
Area = round(math.pi * radius**2 *height, 2)
print(Area)