"""Numbers in python that suprisingly didn't make me cry."""

__author__ = "730444135"

left: int = int(input("Left-hand side: "))
right: int = int(input("Right-hand side: "))
exponent: int = left ** right
division: float = left / right
integer_division: int = left // right
remainder: int = left % right
print(str(left) + " ** " + str(right) + " is " + str(exponent))
print(str(left) + " / " + str(right) + " is " + str(division))
print(str(left) + " // " + str(right) + " is " + str(integer_division))
print(str(left) + " % " + str(right) + " is " + str(remainder))