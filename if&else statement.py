# marks = int(input('how many marks did you get'))
# if marks >= 80 and marks <= 100:
#     print('A')
# elif marks >= 60 and marks < 80:
#     print('B')
# elif marks >= 40 and marks < 60:
#     print('c')
# elif marks >= 0 and marks < 30:
#     print('F')
# else:
#     print('please enter valid marks')
weight = int(input('What is your weight'))
unit = input('kilograms or pounds? (Kg or Ibs)').lower()

if unit == 'kg':
    weight = weight / 2.205
    unit = 'Ibs'
    print(f'you are {weight}{unit}')
elif unit == 'ibs':
    weight = weight * 2.205
    unit = 'Kg'
    print(f'you are {weight} {unit}')
