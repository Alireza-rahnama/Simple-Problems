#Use the outer loop to step through all the numbers between 5 and 10000.
for number in range(5,10001):
#Initialize the variable divisor to be half the number to start.
    divisor=number//2
#Initialize the variable divSum to accumulate the sum of all the divisors.
    divSum= 0
#Continue to loop while the divisor is more than or equal to 1.
    while divisor >= 1 :
        #Check if the number can be divided evenly by the divisor.
        if number%divisor ==0 :
            #Update the sum.
            divSum+= divisor
        #Update the divisor, modification of the lcv.
        divisor-= 1
#Check if the number is equal to the sum, print the number if it is.
    if number== divSum :
        print(number)
