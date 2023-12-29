# Task 7

sum=0
count=0

while True:
    
    number=int(input('Enter number: '))
    
    if number==-1:
        break
        
    elif number!=-1:
        sum=sum+number
        count=count+1
        average=sum/count       
    else:
        pass
    
print('Sum: ', sum)  
print('Count: ', count)  
print('Average: ', average)