def main(a,b,c):
    """
    Find how many positive and how many negative numbers there are in the given numbers.
    check the following conditions:
    "there are a lot of positive numbers",
    "there are a lot of negative numbers"

    Args:
        a: first number
        b: second number
        c: third number

    Returns:
        string: string with the result
    """
    if a==0:
        x=0
        k=0
    if b==0:
        y=0
        l=0
    if c==0:
        z=0
        m=0
        
    if a>0:
        x=1
        k=0
    if a<0:
        x=0
        k=1    
    if b>0:
        y=1
        l=0
    if b<0:
        y=0
        l=1    
    if c>0:
        z=1
        m=0
    if c<0:
        z=0
        m=1
    # sum of positive numbers
    i=x+y+z

     # sum of negative numbers   
    j=k+l+m
    

    if i>j:
        print('there are a lot of positive numbers')
    if i<j:
        print('there are a lot of negative numbers') 
    

    return i and j

main(2,9,-2)
