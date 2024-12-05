#list#
var = list()
var = []
 
var.append(12)
var.append(13)
var.append(14)
var.append(20)
print(var)
print("First element.", var[0])
print("Last element.", var[-1])

var1=["Rishi", 10, 4.11, True]
var1.remove(True)
print(var1)

var1.pop(1)
print(var1)

var1.insert(0, 4.1)
print(var1)

var.reverse()
print(var)

var.sort()
print(var)

print("Minimum value", min(var))
print("Maximum value", max(var))
print("Length value", len(var))
print("Count value", var.count(14))

#membership#
var2=input("Enter a word to check:")
if var2 in var1:
    print("Found.")
else:
    print("Not found.")