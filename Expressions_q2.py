def Cube(i): #functipn to cube a number, this didnt have to be a function but i cant think of anything else to make as a function
    return i ** 3

# Take 5 integer inputs
num1 = int(input("Enter a integer: "))
num2 = int(input("Enter a integer: "))
num3 = int(input("Enter a integer: "))
num4 = int(input("Enter a integer: "))
num5 = int(input("Enter a integer: "))

minimum = min(num1, num2, num3, num4, num5)#find min
maximum = max(num1, num2, num3, num4, num5)#find max
average = (num1 + num2 + num3 + num4 + num5) / 5 #find average

cubic = Cube(minimum)#find cube uisng cube function with minumum in mind

sqrt_max = (maximum % maximum) ** 0.5 #find squareroot

print("Minimum:", minimum)#results
print("Maximum:", maximum)
print("Average:", average)
print("Cubic value of the minimum:", cubic)
print("Square root of the absolute value of the maximum:", sqrt_max)
