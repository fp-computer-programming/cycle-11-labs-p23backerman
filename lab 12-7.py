
# needed: 
#1. dictionary
 
#5 5 built in functions
#6 1 functions with over 15 lines in length
#Got:
#For loop, enumerate, 3 lists, 4 over 15, while loop

#Function #1, for loop check, list
def double_stuff(x):
  #doubles whatever is put into the list regardless if its an index or not
  for b in x:
    b *= 2
    print(b)
  return x
print(double_stuff([6.7, 5,"seven"]))
#Function #2, enumerate, and a list
c12 = ["John", "Jane", "Bob"]
b2 = []
def indexed_names(x):
  for i, v in enumerate(x):
    a = "{0}: {1}".format(i, v)
    b2.append(a)
  return b2
print(indexed_names(c12))

#Function #3, over 15 lines
def add_foods(x):
    #sets the lists to equal nothing but forced into list format
    sixth_letter = []
    short_foods = []
    not_foods = [] 
    #it will check the 6th letter of each value in the list and will add that letter to the end of the sixt_letter list
    for index in x:  
        try:  
            c = index[5]
            sixth_letter.append(c)
            #if it gives an index error, that means the value is too short and does not have a sixth letter. so it adds that string to the end of the list "short_foods"
        except IndexError: 
            short_foods.append(index)
            #if it gives a Type error, it is not a string and will add it the list "not_foods"
        except TypeError:
            not_foods.append(index)
print(("sixth_letter : {0}, not_foods : {1}, short_foods {2}").format(sixth_letter, not_foods, short_foods))
#function #4, over 15, while loop
def Ten_One():
    total = 0
    ele = 0
    list = [0, 0]  
    A1 = 0
    while A1 == A1:
  #asks the user for a number and that number will be added to the end of the list 
        print("give a number")
        A = input()
        A1 = int(A) 
        list.append(A1)
  #once the used puts in -1, the loop ends and it will be printed
        if A1 == -1:
            break
    print(list)
#while the list length is still greater than the number being added, the loop continues until all of the numbers have been added together
    while(ele < len(list)):
        total = total + list[ele]
        ele += 1
#adds an extra one to get rid of the -1 input
    Sum = total + 1
    print(Sum)
#function #5 over 15
def Five(a13):
    b13 = a13 + [1, 5, 9]
    c13 = b13 * 2
    d13 = 10 * 10
    c13 *= d13
    print("give a number")
    e13 = input()
    f13 = int.e13
    c13 *= f13
    l13 = 57 + c13
    m13 = l13 - 27 * 227
    n13 = m13 / 23
    o13 = n13 + 676
    p13 = o13 ** 4
    q13 = p13 / 4
    print("give me another number")
    r13 = input()
    s13 = int.r13
    t13 = q13 ** s13
    z13 = "its been 5 + {0} years since I saw u".format(t13)
    return z13
#function #6 over 15 linesd
def Seven(a14):
    b14 = a14 + [1, 5, 9]
    c14 = b14 * 2
    d14 = 10 * 10
    c14 *= d14
    print("give a number")
    e14 = input()
    f14 = int.e14
    c14 *= f14
    l14 = 57 + c14
    m14 = l14 - 27 * 227
    n14 = m14 / 23
    o14 = n14 + 676
    p14 = o14 ** 4
    q14 = p14 / 4
    print("give me another number")
    r14 = input()
    s14 = int.r14
    t14 = q14 ** s14
    z14 = "its been 7 + {0} years since I saw u".format(t13)
    return z14

#function #7 11-4
def 11_4():
  weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
  weekends = ("Saturday", "Sunday")
  days_of_the_week = weekdays + weekends
  return days_of_the_week

function #8 11-5
def day_to_date(day_date):
  day_date = [2, 3, 4, 5, 6]
  thu = day_date[0]
  fri = day_date[1]
  sat = day_date[2]
  sun = day_date[3]
  mon = day_date[4]
  dt = (thu, fri, sat, sun, mon)
  return dt

