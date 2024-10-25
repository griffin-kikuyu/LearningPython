# logic operators or&and&not

# temp = 25
# is_raining = False
#
# if temp < 0 or temp > 30 or is_raining:
#     print("Today's weather is not favorable ")
#     print('The event is cancelled till next weekend')
# elif temp >= 10 and temp <= 28 and is_raining:
#     print('We are on for tomorrow guys')
# else:
#     print('')
age = 25
user_role = 'user'
tem = 30
access_level = 'full aces' if user_role == 'admin' else 'limited access'
status = 'You are an adult' if age >= 18 else 'you are a child'
print(f'{access_level}')
print(f'{status}')