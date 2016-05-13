from Model import Model

model = Model(100)
model.mc_control(1000000)
model.dump_state("1000000i_result.json")
model.surface_plot()
