#hand cricket single player
print("  ....<|WELCOME|>....")
print("INFORMATION ABOUT GAME :")
print("               This game is made only for entertainment purpose ")
print("Name of the game: Hand cricket (single player) ")
print("lets Start")
a=(input("enter your name "))
print(a,"welcome to the game")
while True :    
    b=(input("plz select your gaming field ('batting','bolwing') "))
    if b=='batting' or b=='bolwing' :
        break
    else:
        print("plz enter a vaild field")
if b=='batting':
    print("you chose batting")
    print("info: enter the value between 0 to 6,and no characters")
    print("Starting...")
else:
    print("you chose bolwing")
    print("info: enter the value between 0 to 6,and no characters")
    print("Starting...")
   
if b=='batting':
    f=0
    while True:
        
        while True:
         print(a,end=" ")   
         c=input("enter your value ")
         if c.isdigit() and int(c)<=7:
             c=int(c)
             break
         else:
             print("info: enter the value between 0 to 6,and no characters")
        import random
        def d():
            return random.choice([5,2,4,1,3,0,6])
        e=d()
        print("computer's value ",e)

        
        if c==e:
            print("out..")
            break
        else:
         if c==0:
            f=f+e
         else :
            f=f+c
            print("score =",f)
    print(a,"you have to out the computer before",f+1)
    print("starting...")
    j=0
    while j<(f+1):
    
     
     while True:
         print(a,end=" ")
         g=input("enter you value ")
         if g.isdigit() and int(g)<=7:
            g=int(g)
            break
         else:
             print("info: enter the value between 0 to 6,and no characters")
     import random
     def h():
         return random.choice([2,5,6,3,4,0,1])
     i=h()
     print("computer's value ",i)

     if i==g:
         print("out...")
         break
     elif i==0:
         j+=g
     else:
         j+=i        
     
     print("score =",j)

            
    if j<(f+1):
      print("you win")
    elif j==f:
     print("draw")
    elif j>f:
      print("you loss")
       
else:            

    j=0
    while True:
    
     
     while True:
         print(a,end=" ")
         g=input("enter you value ")
         if g.isdigit() and int(g)<=7:
            g=int(g)
            break
         else:
             print("info: enter the value between 0 to 6,and no characters")
     import random
     def h():
         return random.choice([2,5,6,3,4,0,1])
     i=h()
     print("computer's value ",i)
     if i==g:
         print("out...")
         break
     elif i==0:
         j+=g
     else:
         j+=i

     
     print("score =",j)        
    print(a,"you have to get ",j+1,"runs to win the computer ")
    print("starting...")  

    f=0
    while f<j+1 :
        
        while True:
         print(a,end=" ")   
         c=input("enter your value ")
         if c.isdigit() and int(c)<=7:
             c=int(c)
             break
         else:
             print("info: enter the value between 0 to 6,and no characters")
        import random
        def d():
            return random.choice([5,2,4,1,3,0,6])
        e=d()
        print("computer's value ",e)

        
        if c==e:
            print("out..")
            print("the winner is computer")
            break
        else:
         if c==0:
            f=f+e
         else :
            f=f+c
         print("score =",f)

    if j<f:
        print("you win the match")
    elif j==f:
        print("the match is draw")
