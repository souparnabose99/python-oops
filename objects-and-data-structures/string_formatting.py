##### @TODO: String Formatting #####

# % Method -> % is referred to as a "string formatting operator":

print("This is a %s string." %"something")
print("This is a %s string for %s formatting." %("sample", "string"))

# Format conversion methods -> 2 methods %s and %r convert any python object to a string using two separate methods: str() and repr()
# %r and repr() deliver the string representation of the object, including quotation marks and any escape characters.

print("His name is  %s" %"ABCD")
print("His name is %r" %"ABC")
print("This is  %s" %"AB \tCD")
print("This is %r" %"AB \tCD")

print("This no is %s" %3.75)
print("This no is %d" %3.75)

# Padding and Precision of Floating Point Numbers:
# Floating point numbers use the format %5.2f
# 5 would be the minimum number of characters the string should contain; these may be padded with whitespace if the entire number does not have this many digits
# Next to this, .2f stands for how many numbers to show past the decimal point

print("This is a floating point number : %5.2f" %11.1111)
print("This is a floating point number : %1.0f" %11.1111)
print("This is a floating point number : %15.8f" %11.1111)
print("This is a floating point number : %1.8f" %11.1111)
print("This is a floating point number : %2.2f" %11.1111)

# .format Method:

print("This is regular {}".format("string"))
print("This {} a {} {}".format("is", "regular", "string"))
print("This {0} a {1} {2}".format("is", "regular", "string"))
print("This {a} a {b} {c}".format(a="is", b="regular", c="string"))
print("This {a} a {a} {a}".format(a="is", b="regular", c="string"))


# ----- @TODO Console Output -----

# This is a something string.
# This is a sample string for string formatting.

# His name is  ABCD
# His name is 'ABC'
# This is  AB 	CD
# This is 'AB \tCD'

# This no is 3.75
# This no is 3

# This is a floating point number : 11.11
# This is a floating point number : 11
# This is a floating point number :     11.11110000
# This is a floating point number : 11.11110000
# This is a floating point number : 11.11

# This is regular string
# This is a regular string
# This is a regular string
# This is a regular string
# This is a is is


