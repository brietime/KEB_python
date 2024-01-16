while True:
    menu = input("1) fahrenheit -> celsius  2) Celsius -> fahrenheit  3) Quit program: ")
    if menu  == '1':
        fahrenheit = float(input('Input fahrenheit: '))
        print(f'Fahrenheit: {fahrenheit}F, Celsius: {((fahrenheit-32.0)*5.0/9.0):.4f}C')
    elif menu == '2':
        celsius = float(input('Input Celcius: '))
        print(f'Celsius: {celsius}C, fahrenheit: {((celsius *9.0/5.0)+32.0):.4f}F')
    else: 
        print('Terminate Program.')
        break
        