import datetime
import requests

api_base_url = 'https://cloudapip.azurewebsites.net'
auth_string_default = "basic Y2xvdWRhcGlwYXNz"

class HistorianClient():
    def __init__(self, base_url, username, auth_string):
        """
        Initializes a new HistorianClient object.
        Verifies the authorization data supplied by the user and throws an exception if it is wrong.
        """
        self.base_url = base_url + "/api"
        self.username = username
        self.auth_string = auth_string
        #Create header for requests
        self.headers = {
            "Authorization": self.auth_string,
            "Username": self.username
        
        }
        #Check wether we have correct authorization data
        response = requests.get(self.base_url + "/authenticationTest" , headers=self.headers)
        if response.status_code != 200:
            raise Exception("Authentication failure")
        #Authentication was successful 
        return

    #Methods for accessing control modules

    def create_control_module(self,
                              equipment_module_path,
                              status_id,
                              name,
                              control_module_type,
                              tolerance,
                              range_lower_end,
                              range_upper_end,
                              physical_unit_id):
        """
        Creates a new control module
        (i.e. a ControlModule entry and a corresponding ControlModuleInfo entry)
        with the given data.
        """
        path_query_string = "?path=" + equipment_module_path
        url = self.base_url + "/controlModule" + path_query_string
        data_object = {
            "statusId": status_id,
            "name": name,
            "type": control_module_type,
            "tolerance": tolerance,
            "rangeLowerEnd": range_lower_end,
            "rangeUpperEnd": range_upper_end,
            "physicalUnitId": physical_unit_id
        }
        response = requests.post(url, headers=self.headers, json=data_object)
        return response
    
    def read_control_module(self,
                            control_module_id):
        """
        Reads all currently active information about the control module with the given id.
        Returns the result in a composite object/dictionary.
        """
        url = self.base_url + "/controlModule/" + str(control_module_id)
        response = requests.get(url , headers=self.headers)
        return response.json()

    def update_control_module(self,
                              control_module_id,
                              status_id,
                              name,
                              control_module_type,
                              tolerance,
                              range_lower_end,
                              range_upper_end,
                              physical_unit_id):
        """
        Updates a control module with the given data.
        """
        url = self.base_url + "/controlModule/" + str(control_module_id)
        data_object = {
            "statusId": status_id,
            "name": name,
            "type": control_module_type,
            "tolerance": tolerance,
            "rangeLowerEnd": range_lower_end,
            "rangeUpperEnd": range_upper_end,
            "physicalUnitId": physical_unit_id
        }
        response = requests.put(url, headers=self.headers, json=data_object)
        return response

    def delete_control_module(self,
                              control_module_id):
        """
        Deletes (i.e. marks as 'deleted') the control module with the given id.
        """
        url = self.base_url() + "/controlModule/" + str(control_module_id)
        response = requests.delete(url, headers=self.headers)
        return response
    
    #Methods for accessing process data

    def create_process_data(self,
                            control_module_id,
                            time, status_id,
                            status_message,
                            error,
                            current_value):
        """
        Creates a new ProcessData entry with the given values.
        """
        url = self.base_url + "/processData"
        data_object = {
            "controlModuleId": control_module_id,
            "timestamp": time.isoformat(),
            "statusId": status_id,
            "statusMessage": status_message,
            "error": error,
            "currentValue": current_value
        }
        response = requests.post(url, headers=self.headers, json=data_object)
        return response

    def read_process_data(self,
                          control_module_id,
                          start_datetime=None,
                          end_datetime=None):
        """
        Returns a list of all ProcessDataEntries for a given Control Module.
        Optionally accepts start and end datetime objects to select only entries from a given time period.
        """
        query_string = ""
        #Check if the user asked for a specific time range and prepare the appropriate query string
        if (start_datetime is not None) or (end_datetime is not None):
            query_string = "?"
            if start_datetime is not None:
                start_query = "start=" + start_datetime.isoformat()
                query_string += start_query
            if end_datetime is not None:
                end_query = "end=" + end_datetime.isoformat()
                if start_datetime is not None:
                    query_string += "&"
                query_string += end_query
        
        url = self.base_url + "/processData/" + str(control_module_id) + query_string
        response = requests.get(url , headers=self.headers)
        return response.json()
