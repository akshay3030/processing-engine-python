import pandas as pd
import numpy as np

def calculate(json_input_string):
	dataframe=pd.read_json("["+json_input_string+"]")

	dataframe["input1_c"]=dataframe["input1"]
	dataframe["input1_c"].where(dataframe["input1_c"]<>998,-9998,inplace=True)
	dataframe["input2_c"]=dataframe["input2"]
	dataframe["input2_c"].where(dataframe["input2_c"]>=0,1,inplace=True)
	dataframe["input1_c"].where(dataframe["input1_c"]>=0,0,inplace=True)
	#dataframe.rename(columns={"inputx":"inputy"},inplace=True)

	dataframe["input3_c"]=dataframe["input3"]
	dataframe["input4_c"]=dataframe["input4"]
	dataframe["input3_c"].where(dataframe["input3_c"]<>99,-9999,inplace=True)
	dataframe["input4_c"].where(dataframe["input4_c"]<>99,-9999,inplace=True)
	dataframe["input3_c_1"]=150*dataframe["input3_c"]/dataframe["input4_c"]
	dataframe["input3_c_1"].where(dataframe["input3_c"]>=0,-9996,inplace=True)
	dataframe["input3_c_1"].where(dataframe["input4_c"]>=0,-9997,inplace=True)
	dataframe["input3_c_1"].where(dataframe["input4_c"]<>0,-9998,inplace=True)

	#output
	dataframe["output1"]=1* -0.123456+dataframe["input1_c"]* 0.1567 + dataframe["input2_c"]* -0.235
	dataframe["output2"]=1* -0.552588+dataframe["input3_c"]* -0.25 + dataframe["input4_c"]* -0.567
	dataframe["output3"]=np.exp(dataframe["output1"])/1+np.exp(dataframe["output2"])
	dataframe["output4"]=(np.exp(dataframe["output1"])/1-np.exp(dataframe["output2"]*5))*1000

	return dataframe.reset_index().to_json(orient='records')[1:-1]

#json_string="""{"input1":2,"input2":3,"input3":4,"input4":5}"""

#output=calculate(json_string)
#print output








