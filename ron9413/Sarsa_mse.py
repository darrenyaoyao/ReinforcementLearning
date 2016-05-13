from Model import Model
import numpy as np
import json

mse = np.zeros(11)
for l in range(11):
	model_mc = Model(100)
	model_mc.mc_control(1000000)
	model_sarsa = Model(100)
	model_sarsa.backward_sarsa_control(100000, l/10.0)
	#mse_hit = np.arange(210, dtype = np.float32).reshape(10, 21)
	#mse_stick = np.arange(210, dtype = np.float32).reshape(10, 21)
	#mse = {"hit": mse_hit, "stick": mse_stick}
	for i in range(10):
		for j in range(21):
			for action in model_mc.states[i][j].action_value_function:
				mse[l] += ((model_sarsa.states[i][j].action_value_function[action] - 
								model_mc.states[i][j].action_value_function[action]) ** 2)
with open("mean_square_error", 'w') as outfile:
	for i in range(11):
		outfile.write("lambda=" + str(i/10.0) + ": ")
		json.dump(mse[i], outfile)
		outfile.write("\n")

				
