# Loops

print(" FOR loop")

primes = [2,3,5,7]
for prime in primes:
    print(prime)


# For loops can iterate over a sequence of numbers using the "range" and "xrange" functions.
# range: returns a new list with numbers of that specified range.
# xrange: returns an iterator, which is more efficient
# Python 3 uses the range function, which acts like xrange

print("Prints out the numbers 0,1,2,3,4")

for x in range(5):
    print(x)

print("Prints out 3,4,5")
for x in range(3,6):
    print(x)

print("Prints out 3,5,7")
for x in range(3,8,2): # esto indica(inicio,fin,step)
    print(x)


print("WHILE:")
count = 0
while count < 5:
    print(count)
    count += 1


print(" break and continue:")

# break is used to exit a for loop or while loop, whereas continue is used to skip the current block,
# and return to the for or while

count2 = 0
while True:
    print(count2)
    count2 += 1
    if count2 >= 5:
        break

print("Prints out only odd numbers 1,3,5,7,9")
for x in range(10):
    #Check if x is even
    if x % 2 == 0:
        continue
    print(x)


print("else in a loops?")

# when the loop condition of "for" or "while" statement fails then code part in
# 'else' is executed. If break statement is executed inside for loop then the 'else'
# part is skipped.

print("Prints out 0,1,2,3,4 and then it prints 'count value reached 5")

count3 = 0
while(count<5):
    print(count3)
    count+=1
else:
    print("count value reached %d"%(count3))

print("Prints out 1,2,3,4")
for i in range(1,10):
    if(i%5==0):
        break
    print(i)
else:
    print("This is not printed because for loop is terminated because of break but not due to fail in condition")




