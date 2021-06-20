def bmi():
    age = int(input('Hi Agro, What is your Age?'))
    weight = float(input('What is your Weight in Kg?'))
    height = float(input('What is your Height in metres?'))
    return round(weight / (height * height), 1)
print('Your BMI is : ', bmi())

