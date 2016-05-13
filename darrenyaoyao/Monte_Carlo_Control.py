from Model import Model

model = Model(100)
model.monte_carlo_control(100000, 1)
model.dump_states("100000i_result.json")
model.surface_plot()
