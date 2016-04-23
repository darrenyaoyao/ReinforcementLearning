import random

class State:
	def __init__(self, player_value_sum=0, dealer_value_sum=0, reward=0, processing='draw'):
		self.player_value_sum = player_value_sum
		self.dealer_value_sum = dealer_value_sum
		self.reward = reward
		self.processing = processing
		self.value_function = 0
		self.policy = { 'hit': 0.5, 'stick': 0.5 }
		self.policy_num = len(self.policy)
		self.last_policy = 'hit'
		#policy['hit'] = random.random()
		#policy['stick'] = 1-policy['hit']
		self.policy_value_function = { 'hit': 0, 'stick': 0 }
		self.eligibility_traces = { 'hit': 0, 'stick': 0}
		
	def getaction(self):
		if random.random() < self.policy['hit']:
			return 'hit'
		else:
			return 'stick'

	def  getplayer_value(self):
		return self.player_value_sum;

	def update_policy_value_function(self, action, value):
		#print ('Before_update: '+action, self.policy_value_function[action])
		self.policy_value_function[action] = value
		#print ('After_update: '+action, self.policy_value_function[action])

	def epsilon_greedy(self, n0, state_num):
		epsilon = float(n0)/float(n0+state_num)
		max_pro = epsilon/float(self.policy_num) + 1 - epsilon
		min_pro = epsilon/float(self.policy_num)
		if self.policy_value_function['hit'] > self.policy_value_function['stick']:
			self.policy['hit'] = max_pro
			self.policy['stick'] = min_pro
		else:
			self.policy['hit'] = min_pro
			self.policy['stick'] = max_pro

	def update_backwardsarsa(self, step_size_dict, delta, lambda_):
		for policy in self.policy_value_function:
			if step_size_dict[policy] != 0:
				self.policy_value_function[policy] += delta*self.eligibility_traces[policy]/step_size_dict[policy]
			self.eligibility_traces[policy] *= lambda_

	def eligibility_traces_zero(self):
		self.eligibility_traces['hit'] = 0
		self.eligibility_traces['stick'] = 0

	def getmax_value_function(self):
		if self.policy_value_function['hit'] > self.policy_value_function['stick']:
			return self.policy_value_function['hit']
		else:
			return self.policy_value_function['stick']

