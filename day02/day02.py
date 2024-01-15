univ = "Inha university"

print(univ)
print(univ[5])

# univ[5] = 'U' //immutable
# print(univ) #변경안됨

subjects = ['python','c++', 'linux', 'data structure', 'database']
print(subjects)
print(subjects[3])

subjects[3] = 'data structure & algorithm' #mutable
print(subjects[3])

# frozenset is not mutable 

# print(0.1)
# print(1e-1)
# print(21000)

abc = 7
Abc = 8
ABC = 6 # case sensitive in lower & upper case letters

test9 = 77
# 9test = 77 #no num can start as var
_9test =71 #okay in underline

# False = 123 #no keywords 

x = 2
y = x + 5
print(y)

print(type(3.14))
print(isinstance(3.14, float))
print(isinstance("Inha", float))

artists = ['bts','뉴진스', '핑클','ses', 'hot','블랙핑크']
groups = artists
print(artists, groups)
artists[2] = '세븐틴'
print(artists, groups)

money = 5,000,000
print(money)
print(type(money)) #tuple

cash = 5_000_000
print(cash)
print(type(cash)) #int

base_number = int(input('Input base number: '))
exponent_number = int(input('Input exponent number: '))
#f-string
print(f'밑은 {base_number}, 지수는 {exponent_number}, 결과 값은 {base_number ** exponent_number}')
print(f'밑은 {base_number}, 지수는 {exponent_number}, 결과 값은 pow{{base_number,exponent_number}}')

#format function
print('밑은 {0}, 지수는 {1}, 결과 값은 {2}'.format(*args: base_number, exponent_number, pow{base_number,exponent_number}))

first_number = int(input("first number: "))
second_number = int(input("second number: "))

quotient = first_number // second_number
remainder = first_number % second_number
print(f'몫은 {quotient} 나머지는 {remainder}입니다.')
print(f'몫은 {divmod(first_number, second_number)[0]}, 나머지는 {divmod(first_number, second_number)[1]}입니다.')

dec = 65
octal = 0o101
hexadecimal = 0x41
binary = 0b01000001
print(dec, octal, hexadecimal, binary)
print(chr(dec), chr(octal), chr(hexadecimal), chr(binary))
print(bin(dec), bin(octal), bin(hexadecimal), bin(binary))
print(ord('B'), ord('Z'),ord('a'),ord('2'))


#(f - 32 ) x 5/9 = c
fahrenheit = float(input('Input Farenheit: '))
print(f'Fahrenheit : {fahrenheit}F, Celcius {((fahrenheit - 32.0)*5.0/9.0):.2f}C')

print(int('1A',16))

print(4 + 7.0) # numeric type mix

print(True + 2) # numeric type mix

menu = input("1) fahrenheit -> celcius    2) Celcius -> fahrenheit    3) Quit program")

if menu  == '1':
    fahrenheit = float(input('Input fahrenheit: '))
    print(f'Fahrenheit: {fahrenheit}F, Celcius: {((fahrenheit-32.0)*5.0/9.0):.4f}C')
elif menu == '2':
    celcius = float(input('Input Celcius: '))
    print(f'Celcius: {celcius}C, fahrenheit: {((celcius *9.0/5.0)+32.0):.4f}F')