f = int(input("Enter a number:"))
o = (input("Enter a operator +,-,*,%:"))
s = int(input("Enter a number:"))

if o == "+":
    sum = f+s
elif o == "-":
    sum = f-s
elif o == "*":
    sum = f*s
elif o == "%":
    sum = f%s
    print(sum)
    
else:
    print("Invailad")