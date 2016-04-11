from State import State
from Environment import Environment
import random
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np

class Model:
	states = [[State(i+1, j+1, 0, 'draw') for j in range(10)] for i in range(21)]
	state_win = State(0, 0, 1, 'win')
	state_lose = State(0, 0, -1, 'lose')
	agents = {'draw': states, 'win': state_win, 'lose': state_lose}
	environment = Environment(agents)
	current_state = states[random.randint(0,9)][random.randint(0,9)]
	states_action_num = {}
	states_action_return = {}
	for i in range(21):
		for j in range(10):
			states_action_num[states[i][j]] = {'hit': 0, 'stick': 0}
			states_action_return[states[i][j]] = {'hit': 0, 'stick': 0}
	states_track = []
	n0 = 0
	def __init__(self, n0):
		self.n0 = n0

	def easy21(self):
		del self.states_track[:]
		while self.current_state != self.state_win and self.current_state != self.state_lose:
			self.states_track.append(self.current_state);
			print ('Player number: ' + str(self.current_state.getplayer_value()) )
			print ('Dealer number: ' + str(self.current_state.dealer_value_sum) )
			self.current_state = self.environment.step(self.current_state, self.current_state.getaction())
		self.states_track.append(self.current_state);
		print ('Player number: ' + str(self.current_state.getplayer_value()) )
		print ('Dealer number: ' + str(self.current_state.dealer_value_sum) )
		print ('Final: ' + self.current_state.processing)
		print ('Reward: ' + str(self.current_state.reward))
		self.current_state = self.states[random.randint(0,9)][random.randint(0,9)]

	def monte_carlo_control(self, iteration, one_epoch_num):
		for i in range(iteration):
			self.run_easy21(one_epoch_num)
			for i in range(21):
				for x in self.states[i]:
					if self.states_action_num[x]['hit'] != 0:
						update_value = float(self.states_action_return[x]['hit'])/float(self.states_action_num[x]['hit'])
						x.update_policy_value_function('hit', update_value)
					if self.states_action_num[x]['stick'] != 0:
						update_value = float(self.states_action_return[x]['stick'])/float(self.states_action_num[x]['stick'])
						x.update_policy_value_function('stick', update_value)
			self.exploration('epsilon_greedy')

	def exploration(self, algorithm):
		if algorithm == 'epsilon_greedy':
			for x in self.states_track[:len(self.states_track)-1]:
				x.epsilon_greedy(self.n0, self.states_action_num[x]['hit']+self.states_action_num[x]['stick'])

	def run_easy21(self, num):
		for k in range(num):
			self.easy21()
			reward = self.states_track[-1].reward
			for x in self.states_track[:len(self.states_track)-2]:
				self.states_action_num[x]['hit'] += 1
				self.states_action_return[x]['hit'] += reward
			self.states_action_num[self.states_track[-2]]['stick'] += 1
			self.states_action_return[self.states_track[-2]]['stick'] += reward

	def surface_plot(self):
		fig = plt.figure()
		ax = fig.gca(projection='3d')
		x = np.arange(1, 11, 1)
		y = np.arange(1, 22, 1)
		z = np.arange(210).reshape(21, 10)
		x, y = np.meshgrid(x, y)
		for i in range(10):
			for j in range(21):
				z[j][i] = self.states[j][i].getmax_value_function()
		surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
		ax.set_zlim(0, 1)
		ax.zaxis.set_major_locator(LinearLocator(10))
		ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
		fig.colorbar(surf, shrink=0.5, aspect=5)
		plt.show()





