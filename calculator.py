print("THIS IS A FRIENDSHIP CALCULATOR\n\n")
first_name = list(input("Enter the name of the First Person: \n"))
second_name = list(input("\nEnter the name of the Second Person: \n"))
between_name = ['f','r','i','e','n','d','s']
final_name_list = first_name + between_name + second_name
dictionary1 = {}
k = 0
a = 0
b = 0
for i in final_name_list:
    if i in dictionary1:
        dictionary1[i] += 1
    else:
        dictionary1[i] = 1
start = []
for j in dictionary1:
    x = dictionary1[j]
    start.append(x)
step1 = []
def calculator():
    for p in range(len(start)//2):
        q = start.pop(0)
        w = start.pop(-1)
        z = q + w
        step1.append(z)

    for m in start:
        step1.append(start.pop(0))
    k=1
    if len(step1)>2:
        calculator2()
def calculator2():
    for p2 in range(len(step1)//2):
        q2 = step1.pop(0)
        w2 = step1.pop(-1)
        z2 = q2 + w2
        start.append(z2)

    for m2 in step1:
        start.append(step1.pop(0))
    k=2
    if len(start)>2:
        calculator()
calculator()
if k==2:
    for o in range(len(start)):
        b = start[o]
        if b > 10:
            l = b//10
            m = b % 10
            start.remove(b)
            start.insert(o,l)
            start.insert(o+1,m)
            calculator()
    percentage1 = start[0]
    percentage2 = start[1]
    final_percentage = str(percentage1) + str(percentage2)
else:
    for o in range(0,len(step1)):
        a = step1[o]
        if a>10:
            l=a//10
            m=a%10
            step1.remove(a)
            step1.insert(o,l)
            step1.insert(o+1,m)
            calculator2()
    percentage1 = step1[0]
    percentage2 = step1[1]
    final_percentage = str(percentage1) + str(percentage2)
print("\nYour Friendship percentage is: "+str(final_percentage)+" %")
