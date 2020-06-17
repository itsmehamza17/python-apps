num1 = 20
num2 = 18
print(num1 < num2)
print(num1 > num2)
print(17 > 71)
print(98 == 98)
print(98 != 98)
print(12 >= 11)
print(12 >= 13)
print(12 >= 11)
print(11 <= 11)

print(True and True) #True
print(True and False) #False
print(False and False) #False

a,b = 1,2
print(a == a and b == b ) #True
print(a == a and b >= a  ) #True
print(a > b and b == b ) # False
print(a == b and b < a) # False

print(True or True) #True
print(True or False) #True
print(False or False) #False

print(a == a or b == b ) #True
print(a == a or b >= a  ) #True
print(a > b or b == b ) # True
print(a == b or b < a) # False

print(not True) #False
print(not False) #True

print(not(a != 4)) #False
print(not(b == a)) #True
print(not(b == 3)) #true

