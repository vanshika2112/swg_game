import random
l = ["snake", "water", "gun"]
i=0
s1=0
s2=0
while i!=5:
     a = random.choice(l)
     b = input("Choose snake, water or gun- ")
     print("  Computer choose: ",a)
     print("  You choose: ",b)
     if a==b:
         print("  Same")
         print("  Computer-> ", s1)
         print("  You-> ", s2)
     if a!=b:
         if a=="water":
             s1=s1+1
             print("  Computer-> ",s1)
             print("  You-> ",s2)
         elif b=="water":
             s2=s2+1
             print("  Computer-> ", s1)
             print("  You-> ", s2)
         elif a=="snake" and b=="gun":
             s2=s2+1
             print("  Computer-> ", s1)
             print("  You-> ", s2)
         else:
             s1=s1+1
             print("  Computer-> ", s1)
             print("  You-> ", s2)
     i=i+1
print("")
if s1>s2:
    print("COMPUTER WON ->")
    print("Computer-> ",s1,"  You-> " ,s2)
elif s1==s2:
    print("DRAW ")
    print("Computer-> ", s1, "  You-> ",s2)
else:
    print("YOU WON -> ")
    print("Computer-> ", s1, "  You-> ", s2)