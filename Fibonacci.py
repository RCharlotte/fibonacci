from ast import Break


number = input("Enter a number: " )






def fibonacciFunction(n):
        a =0
        b=1
        counter =0

        if int(number) ==0 :
                print(a)
                print(f'{number} is in fibonacci sequence')
                Break
                
        else:
                
                if int(number) >=1:
                        for i in range (1,1+ int(number)):
                                c= a+b
                                a=b
                                b=c
                                
                                if c==int(number):
                                        print(f'{number} is in fibonacci sequence')
                                else:
                                        Break
                                        
        
fibonacciFunction(number)

        



    

