def main(a):
    """
    Given an integer a, check the following conditions:
    "two-digit odd number",
    "two-digit even number",
    "three-digit odd number",
    "three-digit even number"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    if 9<a<100 and a%2==0:
        s="two-digit even number"
    if 9<a<100 and a%2!=0:
        s="two-digit odd number"
    if 99<a<1000 and a%2==0:
        s="three-digit even number"
    if 99<a<1000 and a%2!=0:
        s="three-digit odd number"
    if a>999 and a>10:
        s='dhdl'
    return s

s=main(1000)
print(s)




    