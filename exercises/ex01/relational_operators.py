""" Relational Operators I Must Undertake Completely Alone"""

__author__ = "730444135"

left: int = int(input("Left-hand side: "))
right: int = int(input("Right-hand side: "))
less: bool = left < right
greater_or: bool = left >= right
equal: bool = left == right
not_equal: bool = left != right
print(str(left) + " < " + str(right) + " is " + str(less))
print(str(left) + " >= " + str(right) + " is " + str(greater_or))
print(str(left) + " == " + str(right) + " is " + str(equal))
print(str(left) + " != " + str(right) + " is " + str(not_equal))