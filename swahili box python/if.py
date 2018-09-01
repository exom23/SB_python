temp = eval(input('Enter a temperature in Celsius: '))
f_temp = 9/5*temp+32
print('In Fahrenheit, that is', f_temp)
if f_temp > 200:
    print('That temperature is above the boiling point.')
if f_temp < 36:
      print('That temperature is below the freezing point.')
