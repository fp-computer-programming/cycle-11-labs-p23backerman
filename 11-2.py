#Gives dictionary "grades"
grades = {95 : "11-2", 100 : "11-1", 54 : "10-2" }
print(grades)
#sets elel to be set to the initial value of 0 before the for loop
elel = 0
#prints all the values in grades that are greater than 70
for (k, v) in grades.items():
    print(v)
for (k, v) in grades.items():
    if k > 70:
        print(k)