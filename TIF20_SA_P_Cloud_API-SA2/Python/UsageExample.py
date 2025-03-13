from HistorianClient import HistorianClient

api_base_url = 'cloudapi-p-apf6a5abfdcpe2hd.germanywestcentral-01.azurewebsites.net'

#Initialize a HistorianClient
hc = HistorianClient(api_base_url, "testusername")

#Make an example call
control_module_data = hc.read_control_module(1)
print(control_module_data)
