from State import State
from Environment import Environment
import random

class Model:
	states = [[State(i+1, j+1, 0, 'draw') for j in range(10)] for i in range(21)]
	state_win = State(0, 0, 1, 'win')
	state_lose = State(0, 0, -1, 'lose')
	agents = {'draw': states, 'win': state_win, 'lose': state_lose}
	environment = Environment(agents)
	current_state = states[random.randint(0,9)][random.randint(0,9)]
	states_track = []
	n0 = 0
	def __init__(self, n):
		self.n0 = n

	def easy21(self):
		del states_track[:]
		while self.current_state != self.state_win and self.current_state != self.state_lose:
			self.states_track.append(self.current_state);
			print ('Player number: ' + str(self.current_state.getplayer_value()) )
			print ('Dealer number: ' + str(self.current_state.dealer_value_sum) )
			self.current_state = self.environment.step(cself.urrent_state, self.current_state.getaction())
		self.states_track.append(self.current_state);
		print ('Player number: ' + str(self.current_state.getplayer_value()) )
		print ('Dealer number: ' + str(self.current_state.dealer_value_sum) )
		print ('Final: ' + self.current_state.processing)
		print ('Reward: ' + str(self.current_state.reward))
		current_state = states[random.randint(0,9)][random.randint(0,9)]

	def monte_carlo_control(self, iteration):
		states_action_num = {}
		states_action_return = {}
		for i in range(21):
			for j in range(10):
				states_action_num[states[i][j]] = {'hit': 0, 'stick': 0}
				states_action_return[states[i][j]] = {'hit': 0, 'stick': 0}
		for i in range(iteration):
			self.easy21()
			reward = self.states_track[-1].reward
			for x in self.states_track[:len(self.states_track)-2]:
				states_action_num[x]['hit'] += 1
				states_action_return[x]['hit'] += reward
				update_value = float(states_action_return[x]['hit'])/float(states_action_num[x]['hit'])
				x.update_policy_value_function('hit', update_value)
			states_action_num[self.states_track[-2]]['stick'] += 1
			states_action_return[self.states_track[-2]]['stick'] += reward
			update_value = float(states_action_return[self.states_track[-2]]['stick'])/float(states_action_num[self.states_track[-2]]['stick'])
			self.states_track[-2].update_policy_value_function('stick', update_value)
			self.exploration('epsilon_greedy', states_action_num, states_action_return)

	def exploration(self, algorithm, states_action_num, states_action_return):
		if algorithm == 'epsilon_greedy':
			for x in self.states_track[:len(self.states_track)-1]:
				x.epsilon_greedy(self.n0, states_action_num[x]['hit']+states_action_num[x]['stick'])
				


