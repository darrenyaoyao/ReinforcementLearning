from Model import Model

<<<<<<< HEAD
for x in range(9):
	model = Model(100)
	model.backward_sarsa_control(100000, (x+1)*0.1)
	model.dump_states("100000_0."+str(x+1)+"_sarsa_result.json")
	print ("output:"+"100000_0."+str(x+1)+"_sarsa_result.json")
=======
model = Model(100)
model.backward_sarsa_control(100000, 0.1)
model.dump_states("0.1sarsa_result.json")
model.surface_plot()
>>>>>>> 9a79c43df6f2d6de3bea54848537c0d6bf800f68
