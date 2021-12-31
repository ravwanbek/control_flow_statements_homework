def main(a,b,c):
    """
    Find how many positive numbers there are in the given numbers.
    Args:
        a: integer
        b: integer
        c: integer
    returns:
        integer: the number of positive numbers in the given numbers
    """
    if a>0:
        x=1
    else: x=0
    if b>0:
        y=1
    else:
        y=0
    
    if c>0:
        z=1
    else: z=0
    i=x+y+z

    return i
i=main(2,-1,-1)
print(i)