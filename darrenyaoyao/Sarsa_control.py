from Model import Model

for x in range(9):
	model = Model(100)
	model.backward_sarsa_control(100000, (x+1)*0.1)
	model.dump_states("100000_0."+str(x+1)+"_sarsa_result.json")
	print ("output:"+"100000_0."+str(x+1)+"_sarsa_result.json")