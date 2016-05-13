import random

class State:
	def __init__(self, dealer_sum = 0, player_sum = 0, reward = 0, status = "playing"):
		self.dealer_sum = dealer_sum
		self.player_sum = player_sum
		self.reward = reward
		self.status = status
		self.policy = {"hit": 0.5, "stick": 0.5}
		self.policy_num = len(self.policy)
		self.state_action_num = {"hit": 0, "stick": 0}
		self.action_value_function = {"hit": 0, "stick": 0}
		self.eligibility_traces = {"hit": 0, "stick": 0}

	def setValues(self, dealer_sum, player_sum):
		self.dealer_sum = dealer_sum
		self.player_sum = player_sum

	def getAction(self):
		if random.uniform(0, 1) <= self.policy["hit"]:
			return "hit"
		else:
			return "stick"

	def epsilonGreedy(self, n0, state_num):
		epsilon = float(n0) / float(n0 + state_num)
		greedyAct = epsilon / float(self.policy_num) + 1 - epsilon
		randomAct = epsilon / float(self.policy_num)
		if self.action_value_function["hit"] > self.action_value_function["stick"]:
			self.policy["hit"] = greedyAct
			self.policy["stick"] = randomAct
		else:
			self.policy["hit"] = randomAct
			self.policy["stick"] = greedyAct

	def update_state_action_num(self, action):
			self.state_action_num[action] += 1

	def update_action_value_function(self, action, reward):
		self.action_value_function[action] += ( 
			float(reward - self.action_value_function[action])
			/ float(self.state_action_num[action]))

	def update_backward_sarsa(self, delta, lamda):
		for action in self.action_value_function:
			if self.state_action_num[action] != 0:
				self.action_value_function[action] += (delta * self.eligibility_traces[action] / 
																	self.state_action_num[action])
			self.eligibility_traces[action] *= lamda

	def getMaxValueFunction(self):
		if self.action_value_function["hit"] > self.action_value_function["stick"]:
			return self.action_value_function["hit"]
		else:
			return self.action_value_function["stick"]
	
	def eligibility_traces_zero(self):
		self.eligibility_traces["hit"] = 0
		self.eligibility_traces["stick"] = 0
		
