from Model import Model

model = Model(100)
model.monte_carlo_control(500000, 200)
model.surface_plot()
