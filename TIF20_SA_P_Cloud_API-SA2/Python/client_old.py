import time
import requests

api_url_Steuerungselemente = 'https://cloudapi-p.azurewebsites.net/api/Steuerungselemente'
api_url_Machine_Data = 'https://cloudapi-p.azurewebsites.net/api/Maschinendaten'
headers = {"authorization": "Basic" + " " + "Y2xvdWRhcGlwYXNz"}

# Funktionen, mit denen HTTP-Anfragen an die API gesendet werden können.

# Anfragen an den Steuerungselemente-Controller

# Alle Daten, die mit jedem Steuerungselement assoziiert sind, werden abgerufen.
def get_all_controller_data():
    response = requests.get(api_url_Steuerungselemente , headers=headers)
    return response.json()

# Alle exisitierenden Steuerungselemente werden abgerufen.
def get_only_controller():
    response = requests.get(api_url_Steuerungselemente, headers=headers)
    response = response.json()
    for i in range(len(response)):
        print({"sensorId": response[i]['sensorId']}, {"sensorName": response[i]['sensorName']})

# Ein spezifisches Steuerungselemente wird abgerufen. Dafür wird die ID des Steuerungselementes benötigt.
def get_only_specific_controller(id):
    response = requests.get(api_url_Steuerungselemente + "/" + id, headers=headers)
    return response.json()

# Steuerungselement bearbeiten
def put_controller(id, name, typ, toleranz, messbereich, einheit):
    data_object = {
        'id': int(id),
        "name": name,
        "typ": typ,
        "toleranz": float(toleranz),
        "messbereich": float(messbereich),
        "status": "bearbeitet",
        "einheit": einheit,
        "timestamp": time.strftime('%Y-%m-%d %H:%M:%S')
    }
    response = requests.put(api_url_Steuerungselemente + "/" + str(id), headers=headers, json=data_object)

    return response

# Steuerungselement erstellen. Ausgehend von den übergegeben Argumenten wird ein Objekt erstellt, das an die API gesendet wird.
#Beim erstellen eines Steuerungselements wird der status entsrichtend auf erstellt gesetzt und ein timestamp erstellt.
def post_create_controller(name, typ, toleranz,messbereich, einheit):
    data_object = {
        "name": name,
        "typ": typ,
        "toleranz": float(toleranz),
        "messbereich": float(messbereich),
        "status": "erstellt",
        "einheit": einheit,
        "timestamp": time.strftime('%Y-%m-%d %H:%M:%S')
    }
    response = requests.post(api_url_Steuerungselemente, headers=headers, json=data_object)
    return response.json()

# Einen spezfischen Sensor löschen ausgehend von seiner Id
def delete_controller(id):
    response = requests.delete(api_url_Steuerungselemente + "/" + str(id), headers=headers)
    return response




# Anfragen an den Maschinendaten-Controller

# Alle existierenden Maschinendaten werden abgerufen.

def get_machine_data():
    response = requests.get(api_url_Machine_Data, headers=headers)
    return response.json()

# Spezifische Maschinendaten wird abgerufen.
def get_machine_data_of_specific_id(id):
    response = requests.get(api_url_Machine_Data + "/" + str(id), headers=headers)
    return response.json()

# Maschinendaten eines spezifischen Steuerungselements abrufen.
def get_machine_data_of_specific_sensor(id):
    response = requests.get(api_url_Machine_Data, headers=headers)
    response = response.json()
    for i in range(len(response)):
        if response[i]['controllerId'] == id:
            print(response[i])

# Maschinendaten zu spezifischem Steuerungselement erstellen
def post_create_machine_data(regelventil, schaltungVentil, schaltungMotor,temperatur, feuchtigkeit, fehler, controllerId):
    response = requests.post(api_url_Machine_Data, headers=headers, json={ "status": "erstellt",
                                                                           "regelventil": float(regelventil),
                                                                           "schaltungVentil": schaltungVentil,
                                                                           "schaltungMotor": schaltungMotor,
                                                                           "temperatur": float(temperatur),
                                                                           "feuchtigkeit": float(feuchtigkeit),
                                                                           "fehler": fehler,
                                                                           "timestamp": time.strftime('%Y-%m-%d %H:%M:%S'),
                                                                           "controllerId": int(controllerId)})
    return response.json()

# Maschinendaten ausgehend von seiner Id löschen
def delete_machine_data(id):
    response = requests.delete(api_url_Machine_Data + "/" + str(id), headers=headers)
    return response
