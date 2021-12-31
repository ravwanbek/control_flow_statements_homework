def main(a):
    """
    If the number is positive, increase it to 1, else leave unchanged.
    Args:
        a: integer
    Returns:
        a: a increased by 1 if positive, else unchanged.
    """
    if a>0:
        x=a+1
    else:
        x=a
     

    return x
x=main(-7)
print(x)
