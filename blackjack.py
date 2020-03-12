import random

def shuffle(arr):
    n = len(arr)
    for i in range(n-1,0,-1): 
        j = random.randint(0,i+1) 
        arr[i],arr[j] = arr[j],arr[i]

def deal():
    d=[]
    s=["♠","♥","♦","♣"]
    f={1:"A",11:"J",12:"Q",13:"K"}
    for i in range(4):
        for j in range(1,14):
            d.append(f"{f[j] if j in f else j}{s[i]}")
    return d

def dealcards(cards):
    h=[]
    h.append(cards[0])
    del cards[0]
    h.append(cards[0])
    del cards[0]
    return h

def hit(cards):
    h = []
    h.append(cards[0])
    del cards[0]
    return h

def handvalue(arr):
    value = 0
    for x in range(len(arr)):
        if "A" in arr[x]:
            value = value + 11
        if "2" in arr[x]:
            value = value + 2
        if "3" in arr[x]:
            value = value + 3
        if "4" in arr[x]:
            value = value + 4
        if "5" in arr[x]:
            value = value + 5
        if "6" in arr[x]:
            value = value + 6
        if "7" in arr[x]:
            value = value + 7
        if "8" in arr[x]:
            value = value + 8
        if "9" in arr[x]:
            value = value + 9
        if "10" in arr[x]:
            value = value + 10
        if "J" in arr[x]:
            value = value + 10
        if "Q" in arr[x]:
            value = value + 10
        if "K" in arr[x]:
            value = value + 10
    return value

bank = 100
betchoice = 0
betting = 0
game = 0
exitchoice = 0
dealchoice = 0
replaychoice = 0


while game == 0:
    turn1 = 0
    cards = deal()
    hvalue = 0
    dvalue = 0
    gambling = 0
    dgambling = 0
    shuffle(cards)
    print("balance:")
    print(bank)
    print("how much do you want to bet")
    betting = 0
    while betting == 0:
        betchoice = int(input())
        if(bank-betchoice < 0):
            print("you dont have enough for that")
            print("bet again")
        else:
            bank = bank-betchoice
            betting = 1
            print("your balance is now:")
            print(bank)
    hand = 0
    print("")
    print("your hand:")
    hand = dealcards(cards)
    print(hand)
    print("value:")
    print(handvalue(hand))
    print("")
    print("dealers hand:")
    dhand = hit(cards)
    print(dhand)
    print("value:")
    print(handvalue(dhand))
    dvalue = handvalue(dhand)
    print ("")
    while(gambling == 0):
        print("hit(0) or stand(1)?")
        dealchoice = int(input())
        if(dealchoice == 0 and handvalue(hand) <= 21):
            hand.extend(hit(cards))
            print("hand:")
            print(hand)
            print("value:")
            print(handvalue(hand))
        if(dealchoice == 1 and handvalue(hand) <= 21):
            hvalue = handvalue(hand)
            gambling = 1
        if(handvalue(hand) > 21):
            print("bust")
            print("dealer won")
            print("")
            dvalue = handvalue(hand)
            gambling = 1
    while(dgambling == 0):
        if(handvalue(dhand)<17):
            dhand.extend(hit(cards))
            print("dealers hand:")
            print(dhand)
            print("value:")
            print(handvalue(dhand))
        if(handvalue(dhand)<22 and handvalue(dhand)>16):
            dvalue = handvalue(dhand)
            dgambling = 1
        elif(handvalue(dhand)>21):
            print("dealer busts")
            dgambling = 1
    print(" ")
    print("result:")
    print("dealers hand:")
    print(dhand)
    print("dealer value:")
    print(dvalue)
    print(" ")
    print("your hand:")
    print(hand)
    print("value:")
    print(hvalue)
    print(" ")
        
    if(hvalue>dvalue):
        print("you win")
        bank += betchoice
        bank += betchoice
        print("balance:")
        print(bank)
    elif(hvalue==dvalue):
        print("you tie")
        bank += betchoice
        print("balance:")
        print(bank)
    else:
        print("you lose")
        print("balance:")
        print(bank)
                
    print("do you want to play agian?")
    print("yes(0) or no(1)")
    replaychoice = int(input())
    if(replaychoice == 1):
        game = 1
    
    
            
            
        
        
        
        
