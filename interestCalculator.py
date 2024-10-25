principle = 0
rate = 0
time = 0
# si = (P * R * T)/100
# amount = si + p
while True:
    principle = float(input('Enter the principal Amount : '))
    if principle < 0:
        print('Principle cant be less than zero')
    else:
        break

while True:
    rate = float(input('Enter the Interest rate : '))
    if rate < 0:
        print('Interest rate cant be less zero')
    else:
        break

while True:
    time = float(input('Enter time in Years : '))
    if time < 0:
        print('Time cant be less zero')
    else:
        break

# print(principle)
# print(rate)
# print(time)
SI = (principle * rate * time)/100
total = principle + SI
print(f"simple interest is {SI}")
print(f"Total Amount is {total}")
