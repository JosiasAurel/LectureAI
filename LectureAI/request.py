import requests
# import csv
# import json as jsons


def request(id_):
    # Then you come here this is where the text will be collected toghether with the chapters
    # arr = []
    # reading the token......

    endpoint = "https://api.assemblyai.com/v2/transcript"
    json = {"audio_url": "https://cdn.assemblyai.com/upload/33964237-34b5-475e-be79-1caee8f3c69a"}
    headers = {
        "authorization": "8ac213c99e23428e84bf7b0801f4dc6a",
        "content-type": "application/json"
    }

    # id_ = row[1]

    endpoint = "https://api.assemblyai.com/v2/transcript/{}".format(id_)

    response = requests.get(endpoint, headers=headers)
    return response.json()
    # still have to make it wait for the status to change to completed
    # print(jsons.dumps(response.json()))
