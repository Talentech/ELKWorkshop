import requests
from datetime import datetime
from pprint import pprint
import uuid

index = 'my-index'

def log(appName, clientApplication, correlationId, message):
    now = datetime.utcnow().isoformat()
    url = 'http://localhost:9200/{}-000001/_doc'.format(index)
    data = {
    "@timestamp": now,
    "level": "Information",
    "message": message,
        "fields": {
            "Platform": "Talentech",
            "Solution": "Workshop",
            "AppName": appName,
            "EnvironmentName": "Local",
            "CorrelationId": correlationId,
            "ClientApplication" : clientApplication
        }
    }
    response = requests.post(url, json=data, headers={'Content-type': 'application/json'})
    logPrefix =  "{0}:{1}:{2}:{3}".format(now, correlationId, appName, message)
    result = "Log sent" if response.status_code < 300 else "Sending log error"
    print("{0}: {1}".format(logPrefix, result))

def log_flow(correlationId, clientApplication):
    appClient = 'WorkshopClientApp'
    appAPI = 'WorkshopAPI'
    appWebJob = 'WorkshopWebJob'

    log(appClient, clientApplication, correlationId, "Sending request to API...")
    log(appAPI, clientApplication, correlationId, "Request received from client.")
    log(appAPI, clientApplication, correlationId, "Processing request...")
    log(appAPI, clientApplication, correlationId, "Sending message to webjob.")
    log(appWebJob, clientApplication, correlationId, "Message received.")
    log(appWebJob, clientApplication, correlationId, "Processing message...")
    log(appWebJob, clientApplication, correlationId, "Message processed.")

for i in range(0, 2):
    log_flow(str(uuid.uuid4()), "Weekly")

for i in range(0, 4):
    log_flow(str(uuid.uuid4()), "HRManager")

for i in range(0, 6):
    log_flow(str(uuid.uuid4()), "Talmundo")

for i in range(0, 6):
    log_flow(str(uuid.uuid4()), "PeopleCore")

for i in range(0, 3):
    log_flow(str(uuid.uuid4()), "ReachMe")

