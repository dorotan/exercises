# List Less Than Fice
# Take a list, say for example this one:
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# solution no1
def less_than_five(a):
	m = []
	for number in a:
		if number < 5:
			m.append(number)
	return m

print(less_than_five(a))


# solution no2
b = [a.append(number) for number in a if number < 5]
print(b)



# Divisors
# Create a program that asks the user for a number and then prints out a list of all 
# the divisors of that number. (If you don’t know what a divisor is, it is a number that 
# divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

# solution no1
a = int(input("Enter a number: "))
b = list(range(1,a+1))
divisors = []


for number in b:
	if a % number == 0:
		divisors.append(number)

print(divisors)
