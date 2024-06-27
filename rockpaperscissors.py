import random 
m=["rock","paper","scissor"]


while True:
    ccount=0
    ucount=0
    pc=int(input('''
DO You Want To Start the Game....
                 
1 Yes                       2 No | Exit

'''))
    if pc==1:
        for a in range(1,6):
            userInput=int(input('''
Enter Your Choice :
1 rock          2 paper          3 scissor
                                
'''))
            cc=random.choice(m)       
            if userInput==1:
                pc="rock"
            elif userInput==2:
                pc="paper"
            elif userInput==3:
                pc="scissor"
            else :
                print("invalid choice")


            if cc==pc:
                print("Computer Choice -",cc)
                print("Your Choice -", pc)
                print("Tie")
                ucount=ucount+0
                ccount=ccount+0
                print("Your Score :", ucount)
                print("Computer Score :", ccount)

            elif (pc=="rock" and cc=="scissor") or (pc=="paper" and cc=="rock") or (pc=="scissor" and cc=="paper"):
                print("Your Choice -", pc)
                print("Computer's Choice -", cc)
                print("You Win")
                ucount=ucount+1
                print("Your Score :", ucount)
                print("Computer Score :", ccount)

            elif (cc=="rock" and pc=="scissor") or (cc=="paper" and pc=="rock") or (cc=="stone" and pc=="scissor"):
                print("Your Choice -", pc)
                print("Computer's Choice -", cc)
                print("Computer Wins")
                ccount=ccount+1
                print("Your Score :", ucount)
                print("Computer Score :", ccount)

        if ucount==ccount:
            print("Series Draw....")
            print("Your Final Score :-", ucount)
            print("Computer Final Score :-", ccount)
        
        elif ucount>ccount :
            print("You Win The Series")
            print("Your Final Score :-", ucount)
            print("Computer Final Score :-", ccount)

        else:
            print("Computer Win The Series")
            print("Your Final Score :-", ucount)
            print("Computer Final Score :-", ccount)


    else:
        break