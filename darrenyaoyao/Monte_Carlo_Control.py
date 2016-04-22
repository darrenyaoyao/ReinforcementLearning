from Model import Model

model = Model(100)
model.monte_carlo_control(1, 1)
model.dump_states("result")
#model.surface_plot()
