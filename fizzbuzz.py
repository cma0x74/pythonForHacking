# if a number is divisible by 3 print fizz
# if a number is divisible by 5 print buzz
# if a number is divisible by 3 and 5 print fizz buzz

for i in range (0, 100):
    if i % 3 == 0 and i % 5 == 0: print(f'{i} - fizzbuzz')
    
    elif i % 3 == 0: print(f'{i} - fizz')
    
    elif i % 5 == 0: print(f'{i} - buzz')

    else: print(i)