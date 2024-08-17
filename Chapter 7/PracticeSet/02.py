#sum of n natural number
def sum_natural_number(n):
    if (n == 0):
        return 0
    return n+sum_natural_number(n-1)  
      
        
n = int(input("Enter your number: ")) 
sum=sum_natural_number(n)       
print(sum)