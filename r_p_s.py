import rand


count_you = 0
count_comp = 0
flag = 1
flag2 = 2

while flag==1:
    item = input("\nchoose: rock, paper or scissors? ")
    if item != "rock" and item != "paper" and item != "scissors":
        print("\noops something is wrong, try again\n")
        continue
    ans = rand.rando(5)
    if ans == 0:
        comp_item= "rock"
        print("rock")
        if item == comp_item:
            print("it's a tie!\n")
        elif item == "paper":
            print("you won!\n")
            count_you +=1
        elif item == "scissors":
            print("you lost!\n")
            count_comp +=1
    if ans == 1:
         comp_item = "paper"
         print("paper")
         if item == comp_item:
              print("it's a tie!\n")
         elif item == "scissors":
            print("you won!\n")
            count_you +=1
         elif item == "rock":
             print("you lost!\n")
             count_comp +=1
    if ans == 2:
        comp_item = "scissors"
        print("scissors")
        if item == comp_item:
            print("it's a tie!\n")
        elif item == "rock":
            print("you won!\n")
            count_you +=1
        elif item == "paper":
            print("you lost!\n")
            count_comp +=1
    print("you =", count_you, "computer =", count_comp, "\n")
    while flag2 == 2:
        ans2 = input("do you want to leave? yes\\no")
        if ans2 == "YES" or ans2 == "yes":
            flag=0
            break
        elif ans2 == "NO" or ans2 == "no":
            break
        else:
            print("\noops something is wrong, try again\n")
