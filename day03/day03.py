poem = "'It's preety cold!' said the professor."
print(poem)

# print(not like thee, Doctor Fell:\n
#       I know, and know full well:\n) 줄바꿈 \n


print('Give', "us", '''some''', """space""") # Give us some space

print(chr(65)) # A
print(ord('A')) # 65

print(str(True)) # 'True'
print(str(1.0e4)) # '10000.0'


print('ab\tc') # ab      c

info = r'Type a \n key words' #raw string
print(info)
university = "Inha\nuniversity"
print(university)
universityr = r"Inha\nuniversity"
print(universityr)

number1 = input("First number: ")
number2 = input("Second number: ")
print(number1 + number2) # concatation

a = 'duck.'
b = a
c = 'gery duck!'
print(a+b+c)

letters = 'abcdefghijklmnopqrstuvwxyz'
letters[0]
letters[1]
letters[-1]
letters[-2]
letters[100]

name = 'Henny'
name[0] = 'P' # error
name.replace('H','P') # replace
'K' + name[1:] # slicing

print(university)
print(university[:4]) # Inha
print(university[:-11]) # Inha (reverse slice)
print(university[0:len(university)]) #inha university
print(university[::2]) # step

print(letters[20:])
print(letters[18:-3])
print(letters[-3:])
print(letters[4:20:3])
print(letters[-51:-50]) #' '

# split: 문자열을 분류하여 리스트로 담아줌
course = "2024 KEB bootcamp"
print(course)
list_course = course.split()
print(list_course)
list_courseB = course.split('B')
print(list_courseB)

numbers = input("First number Second number : ").split()
print(numbers[0] + numbers[1]) #concatnation
print(int(numbers[0]) + int(numbers[1])) # arthmatic operation

tasks = 'get gloves, get mask, give cat vitimins, call embulance'
tasks.split(',')

subjects = ["python", "c++", "database"]
subjects_string = "/".join(subjects)
print(subjects_string)

