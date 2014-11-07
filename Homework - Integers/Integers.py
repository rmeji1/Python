from random import randrange 

print("INTEGER DIVISIONS");

while(1):
    numerator=randrange(20) ;
    denom=randrange(1,10);
    answer = numerator // denom ;
    userAns=input(str(numerator) + "/" + str(denom) + "=");
    try:
        if answer == int(userAns) :
            print("CORRECT!");
        else:
            print("INCORRECT!");
    except ValueError:
        print("Please enter Integers Only!");
