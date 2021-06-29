# a rock paper scissor game 
import random

nplayed = 0
point_p1 = 0
point_cp = 0
s = 'scissors'
p = 'paper'
r = 'rock'

def play1():
    r=random.random()
    if(r<=0.3334):
        ch = 'r'
    if(0.3334 < r <=0.6667):
        ch = 'p' 
    if(0.6667 < r):
        ch = 's'
    return ch    

def checker(a,ch):
    global dec
    if(a=='s'):
        if(ch=='s'):
            dec = 'Noone gets a point. I also chose '+s
        if(ch=='r'):
            dec = 'I get a point. I chose '+r
        if(ch=='p'):
            dec = 'You get a point. I chose '+p
    if(a=='r'):
        if(ch=='r'):
            dec = 'Noone gets a point. I also chose '+r
        if(ch=='p'):
            dec = 'I get a point. I chose '+p
        if(ch=='s'):
            dec = 'You get a point. I chose '+s
    if(a=='p'):
        if(ch=='p'):
            dec = 'Noone gets a point. I also chose '+p
        if(ch=='s'):
            dec = 'I get a point. I chose '+s
        if(ch=='r'):
            dec = 'You get a point. I chose '+r

def won(p1,cp):
    if(p1>cp):
        return 'You Won'
    elif(cp>p1):
        return 'I Won'
    else:
        return 'It was a Tie'        


while(True):
    a=input('Enter s for scissors, p for Paper, r for Rock -- ')
    a=a.lower()
    if(a != 's' and a!= 'p' and a != 'r'):
        print("enter a valid statement")
        break
    checker(a,play1())
    if 'I get' in dec:
        point_cp+=1
        print('Oh Yeah')
    if 'You get' in dec:
        point_p1+=1
        print('Dangit!!')
    print(dec)    
    nplayed+=1    
    agn = input('wanna play again?? y/n -- ')
    agn = agn.lower()
    if(agn=='n'):
        print('Thanks for playing',nplayed,'times. Ya got',point_p1,'points and I got',point_cp,'points')
        print('Clearly',won(point_p1, point_cp))
        break
    elif(agn=='y'):
        continue
    else:
        print("I'll take that as a No")
        print('Thanks for playing',nplayed,'times. Ya got',point_p1,'and I got',point_cp)
        print('Clearly',won(point_p1, point_cp))
        break



