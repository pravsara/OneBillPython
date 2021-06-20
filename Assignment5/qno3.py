numbers = [1,2,3,4,5]
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
num =['222', '100', '85', '500', '300']
for i in numbers:
    print(i)
print()
i = 0
while i < len(numbers):
    print(numbers[i])
    i = i + 1
print()
for i in weekdays:
    print(i)
print()
i = 0
while i < len(weekdays):
    print(weekdays[i])
    i = i + 1
print()
sum = 0
for i in num:
    sum = sum + int(i)
print('The sum from for loop:', sum)
print()
i = 0
sum = 0
while i < len(num):
    sum = sum + int(num[i])
    i = i + 1
print('The sum from for while:', sum)