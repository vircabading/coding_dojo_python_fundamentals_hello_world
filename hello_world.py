# ////////////////////////////////////////////////////////////
#   Coding Dojo > Python > Fundamentals > Hello World
#   By: Virgilio D. Cabading Jr.    Created: October 24, 2021
# ////////////////////////////////////////////////////////////

message = "Hello World Python!"
print(message)

# ////////////////////////////////////////////////////////////
print("Running Python Example")

print("4 + 5 : ")
print(4+5)
print();

print("31/2:")
print(31/2)
print();

print("If x=9 and y='hello'")
x=9                                                             # Assign 9 to var x
y="hello"                                                       # Assign 'hello' to var y

print("x * y :")
print(x * y)                                                    # Prints 9 times "hello"
print()

print("x = 'Hello Python'")                                     # Shows var re-assignments
x="Hello Python"
print(x)

print("y: 42")
y= 42
print(y)
print()

print("Type of 3j:")
print(type(3j))
print()

print("*** Conversion ***")
int_to_float = float(35)
float_to_int = int(44.2)
int_to_complex = complex(35)
print(int_to_float)
print(float_to_int)
print(int_to_complex)
print(type(int_to_float))
print(type(float_to_int))
print(type(int_to_complex))

# /////////////////////////////////
print("String concatination test")

num1 = 8
print("this , 8 is:", num1)
# print("this + 8 is:" + num1)                  # Can not concatinate a number onto a string
print("this str(8) is: " + str(num1))
print()

# /////////////////////////////////
print("String Interpolation")
first_name = "Zen"
last_name = "Coder"
age = 27
print(f"My name is {first_name} {last_name} and I am {age} years old.") # Literal string interpolation
print()

# /////////////////////////////////
print("String Format")
first_name = "Zen"
last_name = "Coder"
age = 27
print("My name is {} {} and I am {} years old.".format(first_name, last_name, age))
# output: My name is Zen Coder and I am 27 years old.
print("My name is {} {} and I am {} years old.".format(age, first_name, last_name))
# output: My name is 27 Zen and I am Coder years old.
print()

# ////////////////////////////////////////
print("% formating")
hw = "Hello %s" % "world" 	# with literal values
py = "I love Python %d" % 3 
print(hw, py)
# output: Hello world I love Python 3
name = "Zen"
age = 27
print("My name is %s and I'm %d" % (name, age))		# or with variables
# output: My name is Zen and I'm 27
print()

#//////////////////////////////////////
print("usinf f for print strings")
f_name = "Val"
l_name = "Cabading"
print(f"full name: {f_name} {l_name}")
print()

