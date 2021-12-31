def main(temp):
    """
    Display the message according to the following temperature conditions given to you in Celsius:
    Temp<0: "Freezing"
    Temp 1-10: "Very Cold"
    Temp 11-20: "Cold"
    Temp 21-30: "Normal"
    Temp 31-40: "Hot"
    Temp >40: "Very Hot"

    Args:
        temp: integer
    Returns:
        string: the message to print
    """
    if temp<0:
        t="Freezing"
    if 0<temp<11:
        t="Very Cold"
    if 10<temp<21:
        t="Cold"
    if 20<temp<31:
        t="Normal"
    if 30<temp<41:
        t="Hot"
    if temp>40:
        t="Very Hot"    
    
    return t
t=main(40)
print(t)