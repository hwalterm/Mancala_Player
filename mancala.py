# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 10:47:50 2018

@author: halterman
"""
import numpy as np
from random import choice
from itertools import cycle

score = [0,0]
gameboard =[[4,4,4,4,4,4],[4,4,4,4,4,4]]
score = [0,0]
totalturns=0
winningmoves = []
moves=[[],[]]
turnsli = [0,1]
turns= cycle(turnsli)
turn=next(turns)
countchoices = 0
def debugcheck(gameboard,score,hole,inhand,side):
    if ((sum(gameboard[0])+sum(gameboard[1]))+sum(score)+inhand)!= 48:
        print("Miiiiistaaaaaake")
        print(gameboard)
        print("inhand: " + str(inhand))
        print("side: " + str(side))
        print("hole: " + str(hole))
        print("score: " + str(score))
        print("turn: " + str(turn))
        print("sum gameboard: " + str(sum(gameboard[turn])))
        return True
    else:
        return False
    
def manchoice(gameboard,turn, score):
    print(gameboard)
    print("Turn: " +str(turn))
    print("enter the your choice of holes: ")
    print("score: " +str(score))
    x = int(input())
    
    return [turn,x]
    
def choose(gameboard):
    global winningmoves
    global moves
    global countchoices
    a = gameboard[turn]
    nonzeroind = np.nonzero(a)[0]
    goodopts = [i for i in nonzeroind if a[i]==(6-i)]
    if sum(nonzeroind)> 0:
        if countchoices<len(winningmoves):
            moves[turn].append(winningmoves[countchoices])
            countchoices+=1
            return [turn,winningmoves[countchoices-1]]
        else:
            v=choice(nonzeroind)
            moves[turn].append(v)
            countchoices+=1
            return [turn,v]

        

    else:
        return [turn,0]



def move(gameboard,score,turn):
    loop=0
    #pos=manchoice(gameboard,turn,score)
    pos=choose(gameboard)
    side = pos[0]
    hole = pos[1]
    inhand = gameboard[side][hole]
    gameboard[side][hole]=0
    while ((inhand>=0) and sum(gameboard[turn])):
        #print(inhand)
        #try:
        loop = loop+1
        if loop>10000:
            print("mistakes were made")
            break
        if debugcheck(gameboard,score,hole,inhand,side):
            print("sum gboard: " + str(sum(gameboard[turn])))
            print(turn)
            print(gameboard)
            break
        hole=hole+1

        
        
        if (hole==6) and (inhand==1) and (side==turn) :
            score[turn]=score[turn]+1
            inhand = inhand-1

            pos=choose(gameboard)
            #pos=manchoice(gameboard,turn,score)
            side = pos[0]
            hole = pos[1]
            inhand = gameboard[side][hole]
            gameboard[side][hole]=0
            

            

        elif (hole==6) and (inhand>=1) and (side!=turn):
            
            side=(0 if side==1 else 1)
            hole=-1
            
        elif (hole==6) and (inhand>1) and (side==turn):
            score[turn]=score[turn]+1
            inhand-=1
            hole=-1
            side=(0 if side==1 else 1)
       
        elif (inhand>0) and (hole<=5):
            gameboard[side][hole] = ((gameboard[side][hole])+1)
            inhand=inhand-1
        
        elif inhand==0:
            print(gameboard)
            if hole>0:
                hole=hole-1
                if gameboard[side][hole]==1:
                    inhand=-1
                elif gameboard[side][hole]>1:
                    inhand = gameboard[side][hole]
                    gameboard[side][hole]=0
            elif hole == 0:
                side=(0 if side==1 else 1)
                hole=5
                if gameboard[side][hole]==1:
                    inhand=-1
                elif gameboard[side][hole]>1:
                    inhand = gameboard[side][hole]
                    gameboard[side][hole]=0
            
                    
           
#        except IndexError as err:
#            print("Index error hole:" + str(hole) +" side: "+str(side) + " turn: " +str(turn))
#            print(gameboard)
#            print("score:" +str(score))
#            print("inhand:" +str(inhand))
#            break
                
 
    
                
    #print(gameboard)
    return gameboard
        
            

def playgame():
    gameboard =[[4,4,4,4,4,4],[4,4,4,4,4,4]]
    score = [0,0]
    moves=[[],[]]
    totalturns=0
    turnsli=[0,1]
    turns=cycle(turnsli)
    turn=next(turns)
    turn=next(turns)
    global countchoices
    countchoices= 0
    
    while totalturns<1: #len(np.nonzero(gameboard[turn])[0]) >0:
        turn=next(turns)
        gameboard=move(gameboard,score,turn)
        #print(turn)
        totalturns+=1
    
    
    return score


    
finalscore=[0,0]
gamesplayed = 0
finalscorelist=[]
for gamesplayed in range(5):
    gameboard =[[4,4,4,4,4,4],[4,4,4,4,4,4]]
    score = [0,0]
    totalturns=0
    turnsli=[0,1]
    turns=cycle(turnsli)
    turn=next(turns)
    

    finalscore=playgame()
    print(finalscore)
    finalscorelist.append(finalscore)
    if gamesplayed>0 and finalscorelist[gamesplayed]>finalscorelist[gamesplayed-1]:
        winningmoves=moves[0]
        #print(winningmoves)
#    if finalscore[0]>35:
#        print(finalscore)
#        break
    #print(gameboard)
    print("Gamesplayed: " + str(gamesplayed))
print(finalscorelist)



    
            
        
                
            


     
     