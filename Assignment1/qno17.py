n = int(input('Enter no of Students:'))
dic = {}
for i in range(0, n):
    key, value = input('Enter Student Name and Marks: ').split()
    dic[key] = int(value);
check_name = input("Enter name to get marks : ")
print("--------Student Marks---------")
print(dic[check_name])