from decimal import Decimal

print(-0.9//0.123)
# prints -8.0
print(Decimal('-0.9')//Decimal('0.123'))
# prints -7
print(-10//4.2)
# prints -3.0
print(Decimal('-10')//Decimal('4.2'))
# prints -2