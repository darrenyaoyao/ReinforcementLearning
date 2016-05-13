from Environment import Environment
from State import State
import random

#states = [[State(i+1, j+1) for i in range(21)] for j in range(10)]
states = [[State(i+1, j+1) for j in range(10)] for i in range(21)]
state_win = State(0, 0, 'win')
state_lose = State(0, 0, 'lose')
state_draw = State(0, 0, 'draw')
agent = {'processing': states, 'win': state_win, 'lose': state_lose, 'draw': state_draw}
N0=100

for i in range(1000000):
    print('Iteration : '+str(i))
    environment = Environment(agent)
    stack = []
    currentState = states[random.randint(0,9)][random.randint(0,9)]
    while currentState.status == 'processing':
        takeAction = currentState.getAction()
        stack.append((currentState , takeAction))
        currentState = environment.step(currentState, takeAction)
    
    if currentState == state_win:
        for x in stack:
            x[0].MC_Update_QnN(x[1],1)
            x[0].MC_Update_policy(N0)
    elif currentState == state_lose:
        for x in stack:
            x[0].MC_Update_QnN(x[1],-1)
            x[0].MC_Update_policy(N0)
    else:
        for x in stack:
            x[0].MC_Update_QnN(x[1],0)
            x[0].MC_Update_policy(N0)

