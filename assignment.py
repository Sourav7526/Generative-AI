import random
f=open("score.txt","r")
score=f.read().split(",")
f.close()

win=int(score[0])
lose=int(score[1])
tie=int(score[2])

opt=["rock","paper","scissor"]

while True:
    user=input("Choose your option rock,paper,scissor or quit :").lower()
    if user=="quit":
        # win,lose,tie=0,0,0
        f=open("score.txt","w")
        f.write("0,0,0")
        print('Score reset,THANKYOU')
        break
    computer_opt=random.choice(opt)
    print(computer_opt)
    if user==computer_opt:
            print("TIE")
            tie+=1
    elif (user=="rock" and computer_opt=="scissor") or (user=="paper" and computer_opt=="rock") or (user=="scissor" and computer_opt=="paper"):
            print("WIN")
            win+=1
    else:
            print("LOSE")
            lose+=1
    

    f=open("score.txt","w")
    f.write(str(win)+","+str(lose)+","+str(tie))


    print("Current Score")
    print("Wins:", win)
    print("Losses:", lose)
    print("Ties:", tie)
