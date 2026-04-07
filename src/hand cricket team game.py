from getpass import getpass
if True:
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
            print("please enter a valid input")
    e=input("enter team 1's name: ")
    f=input("enter team 2's name: ")
    print("player 1 is treated as |:captain:|")
    print("Enter the players name for team:{",e,"}")
    for g in range(1,(d)+1):
        print("player",g,end='')
        c=input(": ")
        a.append(c)
    print("Enter the player names for team:{",f,"}")
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
    import random
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
    elif x==f:
        while True:
            z=c2+" enter your option ('batting','bowling') "
            z=input(z)
            if z=='batting' or z=='bowling':
                x1=e
                break
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
                    s=c1+" enter the bats man name from your team ("+e+") "
                    s=input(s)
                    if s in a:
                        break
                    else:
                        print("enter the name from your team may be you entered a played bats man name")
            while True:
                g=c2+' enter the bowler name from your team ('+f+') '
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
                o=getpass(o)
                p=getpass(p)
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
        print("now,team:",f,"will play batting")
        print("Target score to team :",f,"is {",m+1,"}")
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
                      s=c2+" enter the bats man name from your team ("+f+") "
                      s=input(s)
                      if s in b:
                          break
                      else:
                        print("enter the name from your team may be you entered a played bats man name")
              while True: 
                  g=c1+' enter the bowler name from your team ('+e+') '
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
                  o=getpass(o)
                  p=getpass(p)
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
            print("draw")
        elif n<m:
            print("team:",e,"wons the match")
        elif n>m:
            print("team:",f,"wons the match")
        input()
    elif (z=='batting' and x==f )or (z=='bowling'and x==e):
         while w!=0:
             while True:
                 if len(b)==1:
                     s=b[0]
                     break
                 else:
                    s=c2+" enter the bats man name from your team ("+f+") "
                    s=input(s)
                    if s in b:
                        break
                    else:
                        print("enter the name from your team may be you entered a played bats man name")
             while True:
                g=c1+' enter the bowler name from your team ('+e+') '
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
                o=getpass(o)
                p=getpass(p)
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
         print("now,team:",e,"will play batting")
         print("Target score to team :",e,"is {",m+1,"}")
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
                    s=c1+" enter the bats man name from your team ("+e+") "
                    s=input(s)
                    if s in a:
                        break
                    else:
                            print("enter the name from your team may be you entered a played bats man name")
            while True: 
                g=c2+' enter the bowler name from your team ('+f+') '
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
                o=getpass(o)
                p=getpass(p)
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
            print("match has been draw")
         elif n<m:
            print("team:",f,"wons the match")
         elif n>m:
                print("team:",e,"wons the match")
         input()
          






















                
