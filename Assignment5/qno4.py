from sys import argv
def bmi():
    print('Name : ', argv[1])
    print('Height : ', argv[2])
    print('Weight : ', argv[3])
    height = float(argv[2])
    weight = float(argv[3])
    bmivalue = round(weight / (height * height), 1)
    return 'Your BMI is ', bmivalue, 'which means you are underweight.' if bmivalue < 18.5 else \
        'which means you are healthy.' if bmivalue < 24.9 else \
        'which means you are overweight.' if bmivalue < 29.9 else \
        'which means you are obese.'
print(bmi())

