import pandas as pd

def calculate(json_input_string):
	dataframe=pd.read_json("["+json_input_string+"]")
	dataframe["output"]=dataframe["input1"]+dataframe["input2"]
	return dataframe.reset_index().to_json(orient='records')