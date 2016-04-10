import random

class State:
	player_value_sum = 0
	dealer_value_sum = 0
	value_function = 0
	policy = { 'hit': 0.5, 'stick': 0.5 }
	policy_num = len(policy)
	#policy['hit'] = random.random()
	#policy['stick'] = 1-policy['hit']
	policy_value_function = { 'hit': 0, 'stick': 0 }
	reward = 0
	processing = 'draw'

	def __init__(self, player_value_sum=0, dealer_value_sum=0, reward=0, processing='draw'):
		self.player_value_sum = player_value_sum
		self.dealer_value_sum = dealer_value_sum
		self.reward = reward
		self.processing = processing
		
	def getaction(self):
		if random.random() < self.policy['hit']:
			return 'hit'
		else:
			return 'stick'

	def  getplayer_value(self):
		return self.player_value_sum;

	def update_policy_value_function(self, action, value):
		self.policy_value_function[action] = value

	def epsilon_greedy(self, n0, state_num):
		epsilon = float(n0)/float(n0+state_num)
		max_pro = epsilon/float(policy_num) + 1 - epsilon
		min_pro = epsilon/float(policy_num)
		if policy['hit'] > policy['stick']:
			policy['hit'] = max_pro
			policy['stick'] = min_pro
		else:
			policy['hit'] = min_pro
			policy['stick'] = max_pro

