#Your code goes here
coffee  =  75
change  =  coffee
while change > 0 :
    userserchoice =  int(input("isert a coin "))
    if userserchoice == 50 or userserchoice == 20 or userserchoice == 10 or userserchoice == 5 :
        change  =  change - userserchoice
        if change > 0 :
            print("you still owe ", change)
        elif change == 0 :
            print("nochange owed")
        elif change < 0 :
            print("here is your change ", abs(change))
    else :
        print("invalid coin")
