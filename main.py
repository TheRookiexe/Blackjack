import random
from logo import logo

print(logo)
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]

def playerPick():
        
    score=0
    listCard=[]
        
    playerCards=random.choice(cards)
    listCard.append(playerCards)
    score+=playerCards
    playerCards=random.choice(cards)
    listCard.append(playerCards)
    score+=playerCards
        
    print("your cards: ",listCard,", current score: ",score)
        
    hit=int(input(f'do you want hit? if yes then enter "1" if no enter "0" :'))
    while hit==1:
        playerCards=random.choice(cards)
        listCard.append(playerCards)
        score+=playerCards
        print("your cards: ",listCard,", current score: ",score)
        # if score>21:
        #     print('busted! you lost.')
        #     exit
        hit=int(input(f'do you want hit? if yes then enter "1" if no enter "0" :'))
        
    # print("your cards: ",listCard,", current score: ",score)

    return score

def computerPick():
    Cscore=0
    Clist=[]

    CompCards=random.choice(cards)
    Clist.append(CompCards)
    Cscore+=CompCards
    print(f"Computer's first cards: ",CompCards,", computer's current score: ",Cscore)

    while Cscore < 17:
        CompCards=random.choice(cards)
        Clist.append(CompCards)
        Cscore+=CompCards

    print(f"Computer's final cards: ",Clist,", computer's current score: ",Cscore)

    return Cscore



temp='y'
while temp=='y':
    sc=0
    temp=input(f"Do you want to play the game? Enter 'y' for yes and 'N' for no. : ").lower()
    if temp=='n':
        exit(0)
    
    sc=playerPick()

    Comp_score=computerPick()

    if Comp_score>sc and Comp_score==21:
        print("computer wins!")
    elif sc==21:
        print("Blackjack player won!")
    elif Comp_score==sc:
        print("Draw push")
    elif sc>Comp_score and sc<=21:
        print("Player wins!")
    elif sc>21 and Comp_score<=21:
        print("Bust! you lost, computer wins!")



    
    

    






