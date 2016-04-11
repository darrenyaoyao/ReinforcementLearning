import random

class Environment:
	def __init__(self, agents):
		self.agents = agents;

	def getcard(self):
		num = int(random.random()*10+1)
		if random.random() < 1.0/3.0:
			#print ('Get card = color: red  num: ' + str(num))
			return -1*num #red
		else:
			#print ('Get card = color: black  num: ' + str(num))
			return 1*num  #black

	def agenthit(self, state):
		new_player_value_sum = state.player_value_sum + self.getcard()
		#print('='*36);
		if (new_player_value_sum > 21) or (new_player_value_sum < 0) :
			self.agents['lose'].player_value_sum = new_player_value_sum
			return self.agents['lose']
		else:
			return self.agents['draw'][new_player_value_sum-1][state.dealer_value_sum-1]

	def agentstick(self, state):
		terminal = False
		new_dealer_value_sum = state.dealer_value_sum
		while not terminal:
			new_dealer_value_sum += self.getcard()
			if new_dealer_value_sum > 17 or new_dealer_value_sum < 0:
				terminal = True
		#print('='*38);
		if (new_dealer_value_sum > 21) or (new_dealer_value_sum < 0):
			self.agents['win'].dealer_value_sum = new_dealer_value_sum
			self.agents['win'].player_value_sum = state.player_value_sum
			return self.agents['win']
		else:
			if new_dealer_value_sum > state.player_value_sum:
				self.agents['lose'].dealer_value_sum = new_dealer_value_sum
				self.agents['lose'].player_value_sum = state.player_value_sum
				return self.agents['lose']
			else:
				self.agents['win'].dealer_value_sum = new_dealer_value_sum
				self.agents['win'].player_value_sum = state.player_value_sum
				return self.agents['win']

	def step(self, state, action):
		#print('='*15 + 'In '+ action +'='*15);
		if action == 'hit':
			return self.agenthit(state)
		else:
			return self.agentstick(state)
