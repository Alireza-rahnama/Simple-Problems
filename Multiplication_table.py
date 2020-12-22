print("Multiplication Table")
print()
print('   ',end='')
for j in range(1,10):
    print(" ",j,end="")
print() # move to new line
print("-"*35)
for i in range(1,10):
    print(i,"|",end="")# end="" doesn't let the print end and it continues as long as the loop condition stands
    for j in range(1,10):# a nested for loop is used here to iterate j values for each i
        print("%3d" % (i*j),end="")
    print()# this print command move to new line and used for each for loop especially in table settings
print()        
