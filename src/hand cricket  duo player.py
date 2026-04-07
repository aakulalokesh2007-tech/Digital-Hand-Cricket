from getpass import getpass
if True:
    print(''' name of the game: handcricket ('double player')
                 welcome
            INFO:
                ----This Game is made only for entertainment purpose only----
                The value  which you will enter for bolwing and batting will be hidden(not show)''')
    n1=input("enter player 1 name ")
    n2=input("enter player 2 name ")
    print("hello",n1,"and",n2)
    print("Lets toss")
    import random
    def player():
        return random.choice([n1, n2])
    x=player()
    if x==n1:
        x1=n2
    else:
        x1=n1
    print(x,"please choose from 'head' or 'tail' ")
    a=(input("enter your option "))
    import random
    def cointoss():
        return random.choice(["head", "tail"])
    u=cointoss()
    print("its ",u)
    if a==u:
        print(x,"win the toss")
    else :
        print(x1,"win the toss")
    if a==u: 
         print(x,"kindly choose from 'batting' or 'bolwing' ")
    else:
        print(x1,"kindly choose from 'batting' or 'bolwing' ")
    q=(input("enter your choice  "))
    if q=="batting":
       print(" you chose batting")
    elif q=="bolwing":
       print( " you chose bolwing")
    else:
     while True:
           q=(input("enter your choice  "))
           if q=="batting" or q=="bolwing":
            break
           if q=="batting":
             print("you chose batting")
    print("  ------------------------------infomatiion about game-------------------------------- ")
    if a==u and q=="batting":
        print(x,"is ++++batting++++and",x1,"is|||bolwing ||| ")
        k=x1
        l=x
    elif a==u and q=="bolwing":
        print(x1,"is ++++ batting++++ and",x,"is |||bolwing||| ")
        l=x1
        k=x
    elif a!=u and q=="batting":
        print(x1,"is ++++batting++++ and",x,"is |||bolwing||| ")
        l=x1
        k=x
    else:
        print(x,"is ++++batting++++ and",x1,"is |||bolwing||| ")
        l=x
        k=x1
    print("INFO:")
    print("     The value  which you will enter for bolwing and batting will be hidden(not show)")
    print("     *****ITS TIME TO START*****")         
    n=0
    while True:
         g=k+" enter value for bolwing "
         p=getpass(g) 
         h=l+" enter value for batting "
         o=getpass(h)
         if p.isdigit()and o.isdigit():
             p=int(p)
             o=int(o)
             if p<=6 and o<=6:
                 if p==o:
                     print(l," entered ",o,"and",k,"also entered ",p)
                     print("bats man out")
                     print(l,"out, so now ",k," will play batting")
                     break
                 elif o==0:
                      n+=p
                 else: 
                      n+=o
                 print(l," entered ",o,"and",k," entered ",p)
                 print("score =",n)     
                 continue         
             else:     
                 print("please enter a valid input: ")
                 print("           you entered the value more then 6.")
                 continue
         else:
             print("please enter a valid input:")
             print("               you entered a character or any other,which is not allowed in the game")
             continue
    m=0
    print("target score to ",k," is [",n+1,"]")
    print("now,",k,"will play  batting")
    while m<=n:
        a=l+" enter value for bolwing "
        t=getpass(a)
        b=k+" enter value for batting "
        y=getpass(b)
        if t.isdigit() and y.isdigit():
          t=int(t)
          y=int(y)
          if t<=6 and y<=6:
            if t==y:
                print("bats man out")
                print(l,"entered",t,"and",k,"also entered",y)
                break
            elif y==0:
                m+=t
            else:
                m+=y
            print(l,"entered",t,"and",k,"entered",y)
            print("score =",m)
            continue
          else:     
                 print("please enter a valid input: ")
                 print("           you entered the value more then 6.")
                 continue
        else:
             print("please enter a valid input:")
             print("               you entered a character or any other,which is not allowed in the game")
             continue
    if m==n:
        print("The match is end with draw")
    elif m<n:
        print(l,"won the match  ")
    elif m>n:
        print(k,"won the match ")
        
input()            
