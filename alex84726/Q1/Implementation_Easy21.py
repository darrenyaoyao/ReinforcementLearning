from Environment import Environment
from State import State
import random

#states = [[State(i+1, j+1) for i in range(21)] for j in range(10)]
states = [[State(i+1, j+1) for j in range(10)] for i in range(21)]
state_win = State(0, 0, 'win')
state_lose = State(0, 0, 'lose')
state_draw = State(0, 0, 'draw')
agent = {'processing': states, 'win': state_win, 'lose': state_lose, 'draw': state_draw}

for i in range(1):
    print ('Game : '+str(i))
    environment = Environment(agent)
    currentState = states[random.randint(0,9)][random.randint(0,9)]
    print ("Initial condition : ")
    print ("Dealer sum = " + str(currentState.dealer_value_sum))
    print ("Player sum = " + str(currentState.player_value_sum))
    while currentState != state_win and currentState != state_lose and currentState != state_draw:
        currentState = environment.step(currentState, currentState.getAction())
    print ("---------Game set-----------")
    print ("Dealer sum: " + str(currentState.dealer_value_sum))
    print ("Player sum: " + str(currentState.player_value_sum))
    
    if currentState == state_win:
        State.reward+=1
        print ("Player wins")
    elif currentState == state_lose:
        State.reward-=1
        print ("Player loses")
    else:
        print ("Tie Game")

print ("reward :"+str(State.reward))

