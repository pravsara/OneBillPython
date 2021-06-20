def bmi():
    name = input('What is your Name : ')
    print('Hi', name, ', What is your Weight in Kg?')
    weight = float(input())
    height = float(input('What is your Height in metres?'))
    bmivalue = round(weight / (height * height), 1)
    return 'Your BMI is ', bmivalue, 'which means you are underweight.' if bmivalue < 18.5 else \
        'which means you are healthy.' if bmivalue < 24.9 else \
        'which means you are overweight.' if bmivalue < 29.9 else \
        'which means you are obese.'
print(bmi())

