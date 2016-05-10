from Environment import Environment
from State import State
import random
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np

class Model:
	def __init__(self, n0):
		self.n0 = n0
		self.states = [[State(i+1, j+1) for j in range(21)] for i in range(10)]
		self.state_win = State(0, 0, 1, "win")
		self.state_lose = State(0, 0, -1, "lose")
		self.state_draw = State(0, 0, 0, "draw")
		self.agent = {"win": self.state_win, "lose": self.state_lose, 
						"draw": self.state_draw, "playing": self.states}
		self.environment = Environment(self.agent)
		self.state_track = []
		self.action_track = []

	def easy21(self):
		del self.state_track[:]
		del self.action_track[:]
		self.currentState = self.states[random.randint(0, 9)][random.randint(0, 9)]
		while self.currentState.status == "playing":
			#print ("Dealer sum = " + str(self.currentState.dealer_sum))
			#print ("Player sum = " + str(self.currentState.player_sum))
			self.state_track.append(self.currentState) 
			self.action_track.append(self.currentState.getAction())
			self.currentState = self.environment.step(self.currentState, self.action_track[-1])
		self.state_track.append(self.currentState)
		#print ("Dealer sum: " + str(self.currentState.dealer_sum))
		#print ("Player sum: " + str(self.currentState.player_sum))
		#print ("Result: " + self.currentState.status)
		#print ("Reward: " + str(self.currentState.reward))

	def exploration(self, algorithm):
		if algorithm == "epsilonGreedy":
			for state in self.state_track[:-1]:
				state.epsilonGreedy(self.n0, state.state_action_num["hit"] + state.state_action_num["stick"])
	
	def mc_policy_evaluation(self):
		self.easy21()
		reward = self.state_track[-1].reward
		for state, action in zip(self.state_track[:-1], self.action_track):
			state.update_state_action_num(action)
			state.update_action_value_function(action, reward)
			#print ("State(" + str(state.dealer_sum) + "," + str(state.player_sum) + ") hit num: " +
					#str(state.state_action_num["hit"]) + ", hit value: " + 
					#str(state.action_value_function["hit"]))
			#print ("State(" + str(state.dealer_sum) + "," + str(state.player_sum) + ") stick num: " +
					#str(state.state_action_num["stick"]) + ", stick value: " +
					#str(state.action_value_function["stick"]))
		#print ("Reward: " + str(reward))
				
	def mc_control(self, iteration):
		for i in range(iteration):
			self.mc_policy_evaluation()
			self.exploration("epsilonGreedy")
			print ('Iteration: '+str(i))

	def surfacePlot(self):
		fig = plt.figure()
		ax = fig.gca(projection='3d')
		x = np.arange(1, 11, 1)
		y = np.arange(1, 22, 1)
		x, y = np.meshgrid(x, y)
		z = np.arange(210, dtype = np.float32).reshape(21, 10)
		for i in range(21):
			for j in range(10):
				z[i][j] = self.states[j][i].getMaxValueFunction()
		surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)
		ax.set_zlim(-1, 1)
		ax.zaxis.set_major_locator(LinearLocator(10))
		ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
		fig.colorbar(surf, shrink=0.5, aspect=5)
		plt.show()		
