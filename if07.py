def main(a):
    """
    Given an integer a, check the following conditions:
    "positive odd number",
    "positive even number",
    "negative odd number",
    "negative even number",
    "the number is zero"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    if a>0 and a%2==0:
        return print('positive even number')
    if a>0 and a%2!=0:
        return print('positive odd number')
    if a<0 and a%2==0:
        return print('negative even number')
    if a<0 and a%2!=0:
        return print('negative odd number')
    if a==0:
        return print("the number is zero")
main(-91)


    