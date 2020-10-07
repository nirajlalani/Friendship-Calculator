def calculator(start):
    step = []
    for i in range(len(start)//2):
        #adding first and last number in the list
        total = start.pop(0) + start.pop(-1)
        if(total)>9:
            step.append(total//10)
            step.append(total%10)
        else:
            step.append(total)

    for remaining in start:
        step.append(remaining)

    if len(step)>2:
        print(step)
        return calculator(step)
    return step

print("THIS IS A FRIENDSHIP CALCULATOR\n\n")

first_name = list(input("Enter the name of the First Person: \n"))
second_name = list(input("\nEnter the name of the Second Person: \n"))
between_name = ['f','r','i','e','n','d','s']

final_name_list = first_name + between_name + second_name
dictionary1 = {}
for i in final_name_list:
    #Will get value from dictionary1, if not found that set it to zero and than add 1 to it
    dictionary1[i] = dictionary1.get(i, 0) + 1

start = []
for j in dictionary1.values():
    start.append(j)
step = calculator(start)

percentage1 = step[0]
percentage2 = step[1]
final_percentage = str(percentage1) + str(percentage2)

print(final_percentage)
