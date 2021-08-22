def triangleNumbers(n):
    
    tnum = 1; #size of current triangle
    total = 0; #size of previous triangle
    
    for i in range(1, n):
        if i == tnum + total:
            print(i)
            total = total + tnum
            tnum += 1

def prime(n):
    for i in range(1,n):

        isPrime = False

        for j in range(2, i-1):
            if i % j == 0:
                isPrime = True
                #print("True")
        
        if isPrime == False:
            print(i)



def currentTime():

    from datetime import datetime
    time = datetime.now()
    print(time)


