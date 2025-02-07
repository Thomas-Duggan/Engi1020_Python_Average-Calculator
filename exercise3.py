# Copyright (c) 2025 Thomas Duggan
# This work is licensed under CC BY-SA 4.0


# Requests input from user to use in the expression below
chem1050 = float(input("Chemestry 1050 mark: "))
engi1010 = float(input("Engineering 1010 mark: "))
engi1020 = float(input("Engineering 1020 mark: "))
engi1030 = float(input("Engineering 1030 mark: "))
engi1040 = float(input("Engineering 1040 mark: "))
la1090 = float(input("English 1090 mark: ")) # Note: "la" stands for Language Arts. Changed due to "engl" looking too similar to "engi".
math1001 = float(input("Math 1001 mark: "))
math2050 = float(input("Math 2050 mark: "))
phys1050 = float(input("Physics 1050 mark: "))

# Uses typical average formula to 
average = (chem1050 + engi1010 + engi1020 + engi1030 + engi1040 + la1090 + math1001 + math2050 + phys1050) / 9
print(int(average))


if (chem1050 or engi1010 or engi1020 or engi1030 or engi1040 or la1090 or math1001 or math2050 or phys1050) >= 55:
    #print("check succeeded") # Used to tell what path was used in "if" statement, can be removed
    if average >= 65:
        promotable = True
        
    else:
        promotable = False
        
else:
    #print("check failed") # Used to tell what path was used in "if" statement, can be removed
    promotable = False
    
if promotable == True:
    print("Congratulations!")
if promotable == False:
    print("Not promotable.")
    
    