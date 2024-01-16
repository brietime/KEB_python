while True:
    menu = input("1) fahrenheit -> celsius  2) Celsius -> fahrenheit  3) Prime number  4) Prime numbers(two input)  5) Quit Program : ")
    if menu  == '1':
        fahrenheit = float(input('Input fahrenheit: '))
        print(f'Fahrenheit: {fahrenheit}F, Celsius: {((fahrenheit-32.0)*5.0/9.0):.4f}C')
    elif menu == '2':
        celsius = float(input('Input Celcius: '))
        print(f'Celsius: {celsius}C, fahrenheit: {((celsius *9.0/5.0)+32.0):.4f}F')
    elif menu == '3':
        number = int(input("Input number: "))
        is_prime = True
        i = 2
        if number< 2:
            print(f'{number} is NOT prime number!')
        else:
            for i in range(2, number): 
                if number % i == 0:
                    is_prime = False
                    break
            if is_prime:
                print(f'{number} is prime number.')
            else: 
                print(f'{number} is NOT prime number')
            
    elif menu == '4':
        numbers = input("first number Second number: ").split()
        n1 = int(numbers[0])
        n2 = int(numbers[1])

        if n1 > n2:
            n1,n2 = n2,n1
            
        for i in range(n1,n2+1,1):
            is_prime = True
            
            if i < 2:
                print(f'{i} is NOT prime number!') 
            else: 
                for k in range(2, i):
                    if i % k ==0:
                        is_prime = False
                        break
                if is_prime:
                    print(i, end = ' ')
        print()
    
    else: 
        print('Terminate Program.')
        break
        