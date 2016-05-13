from Model import Model

model = Model(500)
model.mc_control(5000000)
model.dump_states("5000000i_result.json")
model.surface_plot()
