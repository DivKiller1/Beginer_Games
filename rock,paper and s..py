import random
x=True
s=0
comp=['rock','paper','scissor']
c=random.choice(comp)
with open("streak.txt","r") as st1:
    z=st1.readlines()
    ser=len(z)
    st1.close()
while(x==True):
    u=input("Enter your choice! ")
    
    if(u in comp): 
        
        if(u==c):
            print("We've got a draw!")
        elif((u=='rock'and c=='paper') or(u=='scissor'and c=='rock') or(u=='paper'and c=='scissor') ):
            print("Sorry, You lost!")
            print("Your streak was :",s )
            break
        else:
            print("Congratulations,You won!!")
            s+=1
            print("Your streak is ",s)
        a=input(f"Do you want to play again?,y/n ")
        if(a=='y'):
            pass
        elif(a=='n'):
            x=False
            break
        else:
            print("No appropiate choice given, closing game!")
            x=False
            break
    else:
        input("Wrong choice!")
        break
if(s>=3):
    n=input("Congratulations,You've Entered our Hall of Fame\nEnter your name: ")
    st=open("streak.txt","a")
    high=str(ser)+". "+str(s)+"       "+n
    h=st.write(high+"\n")
    st.close()

    
 

