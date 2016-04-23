from State import State
from Environment import Environment
import random
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np
import json
from pprint import pprint

class Model:
	def __init__(self, n0):
		self.n0 = n0
		self.states = [[State(i+1, j+1, 0, 'draw') for j in range(10)] for i in range(21)]
		self.state_win = State(0, 0, 1, 'win')
		self.state_lose = State(0, 0, -1, 'lose')
		self.state_tie = State(0, 0, 0, 'tie')
		self.agents = {'draw': self.states, 'win': self.state_win, 
			'lose': self.state_lose, 'tie': self.state_tie}
		self.environment = Environment(self.agents)
		self.current_state = self.states[random.randint(0,9)][random.randint(0,9)]
		self.states_action_num = {}
		self.states_action_return = {}
		for i in range(21):
			for j in range(10):
				self.states_action_num[self.states[i][j]] = {'hit': 0, 'stick': 0}
				self.states_action_return[self.states[i][j]] = {'hit': 0, 'stick': 0}
		self.states_track = []
		self.n0 = 0

	def easy21(self):
		del self.states_track[:]
		while (self.current_state != self.state_win and self.current_state != self.state_lose 
			and self.current_state != self.state_tie):
			self.states_track.append(self.current_state)
			#print ('Player number: ' + str(self.current_state.getplayer_value()) )
			#print ('Dealer number: ' + str(self.current_state.dealer_value_sum) )
			action = self.current_state.getaction()
			self.current_state.last_policy = action
			self.current_state = self.environment.step(self.current_state, action)
		self.states_track.append(self.current_state)
		#print ('Player number: ' + str(self.current_state.getplayer_value()) )
		#print ('Dealer number: ' + str(self.current_state.dealer_value_sum) )
		#print ('Final: ' + self.current_state.processing)
		#print ('Reward: ' + str(self.current_state.reward))
		self.current_state = self.states[random.randint(0,9)][random.randint(0,9)]

	def monte_carlo_control(self, iteration, one_epoch_num):
		for i in range(iteration):
			print ('Iteration: '+str(i))
			self.monte_carlo_prediction(one_epoch_num)
			self.exploration('epsilon_greedy')

		#self.states[0][0].epsilon_greedy(self.n0, 5)

	def exploration(self, algorithm):
		if algorithm == 'epsilon_greedy':
			for x in self.states_track[:len(self.states_track)-1]:
				x.epsilon_greedy(self.n0, self.states_action_num[x]['hit']+self.states_action_num[x]['stick'])

	def monte_carlo_prediction(self, num):
		for k in range(num):
			print ('Epo: '+str(k))
			self.easy21()
			reward = self.states_track[-1].reward
			for x in self.states_track[:len(self.states_track)-2]:
				self.states_action_num[x]['hit'] += 1
				self.states_action_return[x]['hit'] += reward
			self.states_action_num[self.states_track[-2]][self.states_track[-2].last_policy] += 1
			self.states_action_return[self.states_track[-2]][self.states_track[-2].last_policy] += reward
		for i in range(21):
			for x in self.states[i]:
				if self.states_action_num[x]['hit'] != 0:
					update_value = (float(self.states_action_return[x]['hit'])
									/float(self.states_action_num[x]['hit']))
					x.update_policy_value_function('hit', update_value)
				if self.states_action_num[x]['stick'] != 0:
					update_value = (float(self.states_action_return[x]['stick'])
									/float(self.states_action_num[x]['stick']))
					x.update_policy_value_function('stick', update_value)

	def backward_sarsa_control(self, epo, lambda_):
		for x in range(epo):
			for i in range(21):
					for j in range(10):
						self.states[i][j].eligibility_traces_zero()
			action = self.current_state.getaction()
			while (self.current_state != self.state_win and self.current_state != self.state_lose 
				and self.current_state != self.state_tie):
				self.states_action_num[self.current_state][action] += 1
				step_size_dict = self.states_action_num[self.current_state]
				#Sarsa algorithm
				self.current_state.last_policy = action
				new_state = self.environment.step(self.current_state, action)
				new_action = new_state.getaction()
				delta = (new_state.reward + new_state.policy_value_function[new_action] - 
					self.current_state.policy_value_function[action])
				self.current_state.eligibility_traces[action] += 1
				for i in range(21):
					for j in range(10):
						self.states[i][j].update_backwardsarsa(step_size_dict, delta, lambda_)
				self.current_state = new_state
				action = new_action
			self.current_state = self.states[random.randint(0,9)][random.randint(0,9)]

	def surface_plot(self):
		fig = plt.figure()
		ax = fig.gca(projection='3d')
		x = np.arange(1, 11, 1)
		y = np.arange(1, 22, 1)
		z = np.arange(210, dtype = np.float32 ).reshape(21, 10)
		x, y = np.meshgrid(x, y)
		for i in range(10):
			for j in range(21):
				z[j][i] = self.states[j][i].getmax_value_function()
		surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)
		ax.set_zlim(-1, 1)
		ax.zaxis.set_major_locator(LinearLocator(10))
		ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
		fig.colorbar(surf, shrink=0.5, aspect=5)
		plt.show()

	def dump_states(self, output):
		with open(output, 'w') as outfile:
			for i in range(21):
				for j in range(10):
					json.dump(self.states[i][j].__dict__, outfile)
					outfile.write("\n")

	def load_states(self, datafile):
		self.targetstates = [[State(i+1, j+1, 0, 'draw') for j in range(10)] for i in range(21)]
		with open(datafile) as data_file: 
			for i in range(21):
				for j in range(10):  
					self.targetstates[i][j].__dict__ = json.loads(data_file.readline())






