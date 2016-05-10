from Environment import Environment
from State import State
import random

states = [[State(i+1, j+1) for j in range(21)] for i in range(10)]
state_win = State(0, 0, 1, "win")
state_lose = State(0, 0, -1, "lose")
state_draw = State(0, 0, 0, "draw")
agent = {"win": state_win, "lose": state_lose, "draw": state_draw, "playing": states}
environment = Environment(agent)
currentState = states[random.randint(0, 9)][random.randint(0, 9)]

while currentState != state_win and currentState != state_lose and currentState != state_draw:
	print ("Dealer sum = " + str(currentState.dealer_sum))
	print ("Player sum = " + str(currentState.player_sum))
	currentState = environment.step(currentState, currentState.getAction())
print ("Dealer sum: " + str(currentState.dealer_sum))
print ("Player sum: " + str(currentState.player_sum))
print ("Result: " + currentState.status)
print ("Reward: " + str(currentState.reward))

