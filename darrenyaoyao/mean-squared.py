import json

mc_data = []

with open("100000i_result.json") as data_file: 
	for i in range(21):
		for j in range(10):  
			jsondata = json.loads(data_file.readline())
			mc_data.append(jsondata["policy_value_function"]["hit"])
			mc_data.append(jsondata["policy_value_function"]["stick"])

with open("100000_0_sarsa_result.json") as data_file: 
	mean_squared = 0
	index = 0
	for i in range(21):
		for j in range(10):  
			jsondata = json.loads(data_file.readline())
			mean_squared += (mc_data[index]-jsondata["policy_value_function"]["hit"])*(mc_data[index]-jsondata["policy_value_function"]["hit"]) 
			index += 1
			mean_squared += (mc_data[index]-jsondata["policy_value_function"]["stick"])*(mc_data[index]-jsondata["policy_value_function"]["stick"])
			index += 1
	print (mean_squared)

for x in range(9):
	with open("100000_0."+str(x+1)+"_sarsa_result.json") as data_file: 
		mean_squared = 0
		index = 0
		for i in range(21):
			for j in range(10):  
				jsondata = json.loads(data_file.readline())
				mean_squared += (mc_data[index]-jsondata["policy_value_function"]["hit"])*(mc_data[index]-jsondata["policy_value_function"]["hit"]) 
				index += 1
				mean_squared += (mc_data[index]-jsondata["policy_value_function"]["stick"])*(mc_data[index]-jsondata["policy_value_function"]["stick"])
				index += 1
		print (mean_squared)