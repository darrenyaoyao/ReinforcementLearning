from State import State
from Environment import Environment
import random

states = [[State(i+1, j+1, 0, 'draw') for j in range(10)] for i in range(21)]
state_win = State(0, 0, 1, 'win')
state_lose = State(0, 0, -1, 'lose')
agents = {'draw': states, 'win': state_win, 'lose': state_lose}
environment = Environment(agents)

current_state = states[random.randint(0,9)][random.randint(0,9)]

while current_state != state_win and current_state != state_lose:
	print ('Player number: ' + str(current_state.getplayer_value()) )
	print ('Dealer number: ' + str(current_state.dealer_value_sum) )
	current_state = environment.step(current_state, current_state.getaction())
	

print ('Player number: ' + str(current_state.getplayer_value()) )
print ('Dealer number: ' + str(current_state.dealer_value_sum) )
print ('Final: ' + current_state.processing)
print ('Reward: ' + str(current_state.reward))