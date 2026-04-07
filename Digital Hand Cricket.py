import pwinput as qq
import random
print(" hello,cool welcome to the game")
pas=("play the game")
a=qq.pwinput("for security purpose please enter the password ")
while True:
   if a==pas:
     print("game opened ") 
     break
   else:
       a=qq.pwinput("try again ")
while True:       
 print('''please select the game type:
                  #single player(solo)
                  #double player(duo)
                  #team game (team)''')
 ab=input("select your game type here ")
 if ab=="duo" or ab=="double player" or ab=="double":
    print(''' name of the game: handcricket ('double player')
                 welcome
            INFO:
                ----This Game is made only for entertainment purpose only----
                The value  which you will enter for bolwing and batting will be hidden(not show)''')
    n1=input("enter player 1 name ")
    n2=input("enter player 2 name ")
    print("hello",n1,"and",n2)
    print("Lets toss")
    def player():
        return random.choice([n1, n2])
    x=player()
    if x==n1:
        x1=n2
    else:
        x1=n1
    print(x,"please choose from 'head' or 'tail' ")
    while True:
       a=(input("enter your option "))
       if a=='head' or a=='tail':
          break
       else:
          print("plz enter a valid input")
    def cointoss():
        return random.choice(["head", "tail"])
    u=cointoss()
    print("its",u)
    if a==u:
        print(x,"won the toss")
    else :
        print(x1,"won the toss")
    if a==u: 
         print(x,"kindly select your field ('batting' or 'bowling') ")
    else:
        print(x1,"kindly select your field ('batting' or 'bowling') ")
    while True:
       q=(input("enter your field  "))
       if q=="batting":
          print(" you chose batting")
          break
       elif q=="bowling":
          print(" you chose bowling")
          break
       else:
          print("please check your spelling")
    print("  ------------------------------infomatiion about game-------------------------------- ")
    if a==u and q=="batting":
        print(x,"is ++++batting++++and",x1,"is|||bowling ||| ")
        k=x1
        l=x
    elif a==u and q=="bowling":
        print(x1,"is ++++ batting++++ and",x,"is |||bowling||| ")
        l=x1
        k=x
    elif a!=u and q=="batting":
        print(x1,"is ++++batting++++ and",x,"is |||bowling||| ")
        l=x1
        k=x
    elif a!=o and q=="bowling":
        print(x,"is ++++batting++++ and",x1,"is |||bowling||| ")
        l=x
        k=x1
    print("     *****ITS TIME TO START*****")         
    n=0
    while True:
         g=k+" enter value for bowling "
         p=qq.pwinput(g) 
         h=l+" enter value for batting "
         o=qq.pwinput(h)
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
                 print("score = {",n,"}")     
                 continue         
             else:     
                 print("please enter a valid input: ")
                 print("           you entered the value more then 6.")
                 continue
         else:
             print("please enter a valid input:")
             print("               you entered a character or any other,which is not allowed in the game.")
             continue
    m=0
    print("target score to ",k," is [",n+1,"]")
    while m<=n:
        a=l+" enter value for bowling "
        t=qq.pwinput(a)
        b=k+" enter value for batting "
        y=qq.pwinput(b)
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
            print("score = [",m,"]")
            continue
          else:     
                 print("please enter a valid input: ")
                 print("           you entered the value more then 6.")
                 continue
        else:
             print("please enter a valid input:")
             print("               you entered a character or any other,which is not allowed in the game.")
             continue
    if m==n:
        print("The match is end with draw")
    elif m<n:
        print(l,"won the match  ")
    elif m>n:
        print(k,"won the match ")
    ac=(input("enter 're' to 'restart' "))
    if ac=='re':
     print("game has been restarted_")
     print('''


         ''')
     continue
    else:
      break
 elif ab=="solo" or ab=="single player" or ab=="single":
   print("  ....<|WELCOME|>....")
   print("INFORMATION ABOUT GAME :")
   print("               This game is made only for entertainment purpose ")
   print("Name of the game: Handcricket(single player) ")
   print("lets Start")
   a=(input("please enter your sweet name "))
   print(a,"welcome to the game")
   while True :    
       b=(input("plz select your gaming field ('batting','bowling') "))
       if b=='batting' or b=='bowling' :
           break
       else:
           print("please check your spelling")
   if b=='batting':
       print("you chose batting")
   else:
       print("you chose bowling")
   print("Starting...")
   print("info: enter the value between 0 to 6,and no characters")
   print('''
''')
   if b=='batting':
          f=0
          while True:
           print(a,end=" ")   
           c=input("enter your value ('batting') ")
           if c.isdigit():
               c=int(c)
               if c>=7:
                  print("enter the value between 0 to 6")
                  continue
           else:
               print("please enter a valid input:")
               print("               you entered a character or some other ,which is not allowed in the game")
               continue
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
          print(a,"you have to out the computer before",f+1,"runs to win")
          print("starting...")
          j=0
          while j<(f+1):
             print(a,end=" ")
             g=input("enter you value('bowling') ")
             if g.isdigit():
               g=int(g)
               if g>=7:
                  print("please enter your value between 0 to 6 ")
                  continue
             else:
                print("please enter a valid input:")
                print("               you entered a character or some other ,which is not allowed in the game")
                continue
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
                print("you won the match")
          elif j==f:
                print("match has been draw")
          elif j>f:
               print("you loss the match")
   else:            
      j=0
      while True:
        while True:
            print(a,end=" ")
            g=input("enter you value('bowling') ")
            if g.isdigit() :
               g=int(g)
               if g>=7:
                  print("please enter your value between 0 to 6")
                  continue
               else:
                  break
            else:
                print("please enter a valid input:")
                print("               you entered a character or some other ,which is not allowed in the game")
                continue
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
      print(a,"you have to get ",j+1,"runs to win ")
      print("starting...")  
      f=0
      while f<j+1 :
           while True:
            print(a,end=" ")   
            c=input("enter your value('batting') ")
            if c.isdigit() and int(c)<=7:
                c=int(c)
                if c>=7:
                   print("please enter the value between 0 to 6")
                else:   
                   break
            else:
               print("please enter a valid input:")
               print("               you entered a character or some other ,which is not allowed in the game")
               continue 
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
      if j<f:
           print("you won the match")
      elif f<j:
         print("you loss the match")
      elif j==f:
           print("match has been draw")
   ac=(input("enter 're' to 'restart' "))
   if ac=='re':
     print("game has been restarted_")
     print('''


''')
     continue
   else:
      break  
 elif ab=='team game' or ab=='team':
    print("  ....<|WELCOME|>....")
    print("INFORMATION ABOUT GAME :")
    print('''               This game is made only for entertainment purpose
             the value which you enter for batting and bowling will be not showen(hidden)''')
    print("Name of the game: Hand cricket (team game) ")
    print("lets Start")
    a=[]
    b=[]
    while True:
        d=input("enter number of players in a team ")
        if d.isdigit():
            d=int(d)
            if d<12:
                break
            else:
                print("players cant be more then 11")
        else:
            print("please enter a valid input(only digits)")
    e=input("enter team 1's name: ")
    f=input("enter team 2's name: ")
    print("player 1 is treated as |:captain:|")
    print("Enter the players name #team:{",e,"}")
    for g in range(1,(d)+1):
        print("player",g,end='')
        c=input(": ")
        a.append(c)
    print("Enter the players names #team:{",f,"}")
    for g in range(1,int(d)+1):
        print("player",g,end='')
        c=input(": ")
        b.append(c)
    print("players list:")
    print('')
    print('   team:',e)
    m=1
    for q in range(int(d)):
        if m==1:
            print('    ',a[q],'(captain)')
        else:    
            print('    ',a[q])
        m+=1
    m=1
    print("")
    print('   team:',f)
    for q in range(int(d)):
        if m==1:
            print('    ',b[q],'(captain)')                 
        else:    
            print('    ',b[q])
        m+=1
    c1=a[0]
    c2=b[0]
    def y():
        return random.choice([e,f])
    x=y()
    if x==e:
        while True:
            z=(c1+" enter your option ('batting','bowling') ")
            z=input(z)
            if z=='batting' or z=='bowling':
                x1=f
                break
            else:
               print("please check your spelling")
    elif x==f:
        while True:
            z=c2+" enter your option ('batting','bowling') "
            z=input(z)
            if z=='batting' or z=='bowling':
                x1=e
                break
            else:
               print("please check your spelling")               
    if z=='batting'and x==e:
        print('team :',x,'is batting and team :',x1,'is bowling')
    elif z=='bolwing'and x==e:
        print('team :',x1,'is batting and team :',x,'is bowling')
    elif z=='batting' and x==f:
        print('team :',x,'is batting and team :',x1,'is bowling')
    elif z=='bolwing' and x==f:
        print('team :'+x1,'is batting and team :',x,'is bowling')
    print("   ###@@!LETS START!@@##  ")
    m=0
    aa=a[:]
    bb=b[:]
    w=len(a)
    if (z=='batting'and x==e)or(z=='bowling' and x==f):
        while w!=0:
            while True:
                if len(a)==1:
                    s=a[0]
                    break
                else:
                    s=c1+" enter the bats man name #team ("+e+") "
                    s=input(s)
                    if s in a:
                        break
                    else:
                        print("enter the name from your team may be you entered a played bats man name")
            while True:
                g=c2+' enter the bowler name #team ('+f+') '
                g=input(g)
                if g in b:
                    break
                else:
                    print("enter the name from your team ")
            print("score =",m)
            if w==1:
                print("last wicket")
            else:
                print("wickets =",w)
            while True:
                o=s+' enter your value for batting '
                p=g+' enter your value for bowling '
                o=qq.pwinput(o)
                p=qq.pwinput(p)
                if o.isdigit() and p.isdigit():
                    o=int(o)
                    p=int(p)
                    if o>6 or p>6:
                        print("please enter the value less then 6")
                        continue
                else:
                    print("please enter a valid input:")
                    print("               you entered a character or some other ,which is not allowed in the game")
                    continue
                if o==p:
                    print(s,"entered ",o,"and ",g,"also entered ",p)
                    print("bats man out")
                    a.remove(s)
                    print("score =",m)
                    w-=1
                    break
                elif o==0:
                    m+=p
                    print(s,"entered ",o,"and ",g,"entered ",p)
                else:
                    m+=o
                    print(s,"entered ",o,"and ",g,"entered ",p)
                print("score =",m)
        print("wickets out..")
        print("now,team:<",f,">will play batting")
        print("Target score to team :(",f,")is {",m+1,"}")
        n=0
        w=len(b)
        while n<m+1:
              if w==0:
                break
              while True:
                  if len(b)==1:
                      s=b[0]
                      break
                  else:
                      s=c2+" enter the bats man name #team ("+f+") "
                      s=input(s)
                      if s in b:
                          break
                      else:
                        print("enter the name from your team may be you entered a played bats man name")
              while True: 
                  g=c1+' enter the bowler name #Team ('+e+') '
                  g=input(g)
                  if g in aa:
                      break
                  else:
                     print("enter the name from your team ")
              print("score =",n)  
              if w==1:
                  print("last wicket")
              else:
                  print("wickets =",w)
              while True:
                  o=s+' enter your value for batting '
                  p=g+' enter your value for bowling '
                  o=qq.pwinput(o)
                  p=qq.pwinput(p)
                  if o.isdigit() and p.isdigit():
                    o=int(o)
                    p=int(p)
                    if o>6 or p>6:
                        print("please enter the value less then 6")
                        continue
                    
                  else:
                    print("please enter a valid input:")
                    print("               you entered a character or some other ,which is not allowed in the game")
                    continue    
                  if o==p:
                    print(s,"entered ",o,"and ",g,"also entered ",p)
                    print("bats man out")
                    b.remove(s)
                    print("score =",n)
                    w-=1
                    break
                  elif o==0:
                    n+=p
                    print(s,"entered ",o,"and ",g,"entered ",p)
                  else:
                    n+=o
                    print(s,"entered ",o,"and ",g,"entered ",p)
                  print("score =",n)
                  if n>=m+1 or w==0:
                      break
        if n==m:
            print("match was draw")
        elif n<m:
            print("match won by Team :",e)
        elif n>m:
            print("match won by Team :",f)
    elif (z=='batting' and x==f )or (z=='bowling'and x==e):
         while w!=0:
             while True:
                 if len(b)==1:
                     s=b[0]
                     break
                 else:
                    s=c2+" enter the bats man name #team ("+f+") "
                    s=input(s)
                    if s in b:
                        break
                    else:
                        print("enter the name from your team may be you entered a played bats man name")
             while True:
                g=c1+' enter the bowler name #team ('+e+') '
                g=input(g)
                if g in a:
                    break
                else:
                    print("enter the name from your team ")
             print("score =",m)               
             if w==1:
                print("last wicket")
             else:
                print("wickets =",w)
             while True:
                o=s+' enter your value for batting '
                p=g+' enter your value for bowling '
                o=qq.pwinput(o)
                p=qq.pwinput(p)
                if o.isdigit() and p.isdigit():
                    o=int(o)
                    p=int(p)
                    if o>6 or p>6:
                        print("please enter the value less then 6")
                        continue
                else:
                    print("please enter a valid input:")
                    print("               you entered a character or some other ,which is not allowed in the game")
                    continue
                if o==p:
                    print(s,"entered ",o,"and ",g,"also entered ",p)
                    print("bats man out")
                    b.remove(s)
                    print("score =",m)
                    w-=1
                    break
                elif o==0:
                    m+=p
                    print(s,"entered ",o,"and ",g,"entered ",p)
                else:
                    m+=o
                    print(s,"entered ",o,"and ",g,"entered ",p)
                print("score =",m)
         print("wickets out..")
         print("now,team:<",e,">will play batting")
         print("Target score to team :(",e,")is {",m+1,"}")
         n=0
         w=len(a)
         while n<m+1:
            if w==0:
                break
            while True:
                if len(a)==1:
                    s=a[0]
                    break 
                else:
                    s=c1+" enter the bats man name #team ("+e+") "
                    s=input(s)
                    if s in a:
                        break
                    else:
                            print("enter the name from your team may be you entered a played bats man name")
            while True: 
                g=c2+' enter the bowler name #team ('+f+') '
                g=input(g)
                if g in bb:
                    break
                else:
                    print("enter the name from your team ")
            print("score =",n)  
            if w==1:
                print("last wicket")
            else:
                print("wickets =",w)
            while True:
                o=s+' enter your value for batting '
                p=g+' enter your value for bowling '
                o=qq.pwinput(o)
                p=qq.pwinput(p)
                if o.isdigit() and p.isdigit():
                    o=int(o)
                    p=int(p)
                    if o>6 or p>6:
                        print("please enter the value less then 6")
                        continue
                else:
                    print("please enter a valid input:")
                    print("               you entered a character or some other ,which is not allowed in the game")
                    continue    
                if o==p:
                    print(s,"entered ",o,"and ",g,"also entered ",p)
                    print("bats man out")
                    a.remove(s)
                    print("score =",n)
                    w-=1
                    break
                elif o==0:
                    n+=p
                    print(s,"entered ",o,"and ",g,"entered ",p)
                else:
                    n+=o
                    print(s,"entered ",o,"and ",g,"entered ",p)
                print("score =",n)
                if n>=m+1 or w==0:
                        break
         if n==m:
            print("match was draw")
         elif n<m:
            print("team:",f,"wons the match")
         elif n>m:
                print("team:",e,"wons the match")
    ac=(input("enter 're' to 'restart' "))
    if ac=='re':
       print("game has been restarted_")
       print('''


''')
       continue
    else:
      break            
 else:   
   print("Oooo..., you entered the wrong input please wait the game restarting")
   print('''

                  game is started
                                                                           ''')
input()
           
    
    
       


    

         
          
          
        






    
        

        
        
