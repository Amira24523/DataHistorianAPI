from HistorianClient import HistorianClient

api_base_url = 'https://cloudapip.azurewebsites.net'
auth_string_default = "basic Y2xvdWRhcGlwYXNz"

#Initialize a HistorianClient
hc = HistorianClient(api_base_url, "testusername", auth_string_default)

#Make an example call
control_module_data = hc.read_control_module(1)
print(control_module_data)
