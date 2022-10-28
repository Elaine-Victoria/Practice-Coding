#Python Indentation
if 9 > 3:
 print("Nine is greater than three!")     
print("\n") 
print("--------------------------------------------------------------------------------")     
print("\n")

#many values to multiple variables
x, y, z = "Kitty", "Chitty", "Tuksi"
print(x)
print(y)
print(z)
print("\n") 
print("---------------------------------------------------------------------------------")     
print("\n")

#one value to multiple variables
x = y = z = "cat"
print(x)
print(y)
print(z)
print("\n") 
print("---------------------------------------------------------------------------------")     
print("\n")

#unpack a list
Itblocks = ["2101", "2102", "2103", "2104", "2105", "2106", "2107", "2108", "2109", "2110"]
a, b, c, d, e, f, g, h, i, j = Itblocks
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
print(j)
print("\n") 
print("---------------------------------------------------------------------------------")     
print("\n")

#output variables
x = "Goodmorning!"
print(x)

x = "I"
y = "am"
z = "Elaine"
print(x, y, z)

x = "Information"
y = "Technology"
z = "Student"
print(x, y, z)

x = 18
y = 1
print(x + y)
print("\n") 
print("---------------------------------------------------------------------------------")     
print("\n")

#global variables
x = "cute"

def myfunc():
  print("I am " + x)

myfunc()
print("\n") 
print("---------------------------------------------------------------------------------")     
print("\n")

#check string
txt = "You are going to make it, Trust me. PSALM 23"
if "PSALM" in txt:
  print("Yes, 'PSALM' is present.")

#check if not
txt = "You are going to make it, Trust me. PSALM 23"
if "Isiah 60:22 " not in txt:
  print("No, 'Isiah 60:22' is NOT present.")
print("\n") 
print("---------------------------------------------------------------------------------")     
print("\n")

#slicing strings
b = "Hi Im Eleyna!"
print(b[:2])

b = "Hi Im Eleyna!"
print(b[-4:-1])
print("\n") 
print("---------------------------------------------------------------------------------")     
print("\n")

#modify strings
a = "meow meow"
print(a.upper())

a = "MEOW MEOW"
print(a.lower())
print("\n") 
print("---------------------------------------------------------------------------------")     
print("\n")

#replace string
a = "Hi Im Eleyna!"
print(a.replace("Eleyna", "Elaine"))

#split string
a = "Im, Elaine!"
print(a.split(","))
print("\n") 
print("---------------------------------------------------------------------------------")     
print("\n")

#string concatenation
a = "Information "
b = "Technology"
c = a + b
print(c)
print("\n") 
print("---------------------------------------------------------------------------------")     
print("\n")

#python list
mlsuppherolist = ["rafaela", "estes", "diggie", "angela", "carmilla", "floryn"]
print(mlsuppherolist)
print("\n") 
print("---------------------------------------------------------------------------------")     
print("\n")

mlsupplist = ["rafaela", "estes", "diggie", "angela", "carmilla", "floryn"]
mlsupplist.sort(reverse = True)
print(mlsupplist)
print("\n") 
print("---------------------------------------------------------------------------------")     
print("\n")
