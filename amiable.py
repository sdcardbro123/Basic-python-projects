x = int(input("Enter no. "))
y = int(input("Enter no. "))

xd = []

for i in range(1, x+1):
    if (x%i ==0):
        xd.append(i)
print(xd)

z = int(1)
for j in range(1,len(xd)):
    z += xd[j]
print(z)

if x+y==z:
    print("Amiable")
else:
    print("NOPE")
