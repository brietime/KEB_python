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

print(course)
# course = course.replace(__old:'KEB', __new:'Inha')
# print(course)

setup = 'a duck! *goes into... a bar*'
setup = setup.replace('a', 'the', 1)
print(setup)
print(setup.strip('*'))

print(poem)
print(poem.startswith("All"))
print(poem.endswith("professor."))
print(poem.find('said'))
print(poem.rfind('said'))
print(poem.rindex('said'))

subjects = "python c++ database linux"
subject = input('과목을 입력해주세요: ')
if subjects.find(subject) != 1: 
    print(f"해당 과목은 금학기에 개설됩니다. 위치는{subjects.find(subject)}번 인덱스로 가시면 됩니다.")
else: 
    print('해당과목은 개설되지 않습니다.')

# preview
subjects = "python c++ database linux"
subject = input('수강신청과목 입력: ')
try:
    print(f"해당 과목은 금학기에 개설됩니다. 위치는{subjects.find(subject)}번 인덱스로 가시면 됩니다.")
escept ValueError: 
    print('해당과목은 개설되지 않습니다.')
    
setup.capitalize(poem)

print('%s' % 7.03)
print('%f' % 7.03)
print('%e' % 7.03)
print('%g' % 7.03)


print('%s' % 42)
print('%d' % 42)
print('%x' % 42)
print('%o' % 42)
print('%e' %0.7045)
print('%d%%' % 100)

thing = 'woodchuck'

thing = 98.6
print('%f' % thing)
print('%12f' % thing)
print('%.3f' % thing)

thing = 'woodchuck'
place = 'lake'
print('The {1} is in the {0}'.format(place,thing))
print('The {thing} is in the {place}'.format(place = 'bathtub',thing = 'duck'))

subjects = {'python': 'kim', 'c++':'sung', 'data structure': 'kim', 'database': 'kang'}
print("The {0[python]} and {0[data structure]} will come".format(subjects))


thing = 'woodchuck'
place = 'lake'
print('The {:<10s} is in the {:>10s}'.format(place,thing))
print('The {:!^10s} is in the {:10s}'.format(place,thing))
print('The {thing.capitalize()} is in the {:>10s}'.format(place,thing))
print('The {thing} is in the {place}'.format(place = 'bathtub',thing = 'duck'))
