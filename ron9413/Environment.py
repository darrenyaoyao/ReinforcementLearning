import random

class Environment:
	def __init__(self, agent):
		self.agent = agent
	def getCard(self):
		num = random.randint(1, 10)
		if random.uniform(0, 1) <= 1.0 / 3.0:
			return -1 * num
		else:
			return num
	def agentHit(self, state):
		player_sum = state.player_sum + self.getCard()
		if player_sum > 21 or player_sum < 1:
			self.agent["lose"].setValues(state.dealer_sum, player_sum)
			return self.agent["lose"]
		else:
			return self.agent["playing"][state.dealer_sum-1][player_sum-1]
	def agentStick(self, state):
		dealer_sum = state.dealer_sum
		while dealer_sum < 17:
			dealer_sum += self.getCard()
			if dealer_sum > 21 or dealer_sum < 1:
				self.agent["win"].setValues(dealer_sum, state.player_sum)
				return self.agent["win"]
		if state.player_sum > dealer_sum:
			self.agent["win"].setValues(dealer_sum, state.player_sum)
			return self.agent["win"]
		if state.player_sum == dealer_sum:
			self.agent["draw"].setValues(dealer_sum, state.player_sum)
			return self.agent["draw"]
		if state.player_sum < dealer_sum:
			self.agent["lose"].setValues(dealer_sum, state.player_sum)
			return self.agent["lose"]
	def step(self, state, action):
		if action == "hit":
			return self.agentHit(state)
		else:
			return self.agentStick(state)
