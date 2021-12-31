def main(a):
    """
    The two-digit integer is given.
    Replace the digits of the number.
    True if the resulting number is less than or equal to the old number, otherwise return False.
    
    Args:
        a: integer
    Returns:
        boolean: True if the resulting number is less than or equal to the old number, otherwise return False.
    """
    s1=a//10
    s2=a%10
    s3=(s2*10)+s1

    if  s3<=a:
        k=True
    else:
        k=False
    return k
k=main(44)
print(k)