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

def log_success(appName, clientApplication, correlationId, message):
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
            "ClientApplication" : clientApplication,
            "HTTPStatus" : 200,
        }
    }
    response = requests.post(url, json=data, headers={'Content-type': 'application/json'})
    logPrefix =  "{0}:{1}:{2}:{3}".format(now, correlationId, appName, message)
    result = "Log sent" if response.status_code < 300 else "Sending log error"
    print("{0}: {1}".format(logPrefix, result))

def log_error(appName, clientApplication, correlationId, message, httpStatus, errorMessage):
    now = datetime.utcnow().isoformat()
    url = 'http://localhost:9200/{}-000001/_doc'.format(index)
    data = {
    "@timestamp": now,
    "level": "Error",
    "message": message,
        "fields": {
            "Platform": "Talentech",
            "Solution": "Workshop",
            "AppName": appName,
            "EnvironmentName": "Local",
            "CorrelationId": correlationId,
            "ClientApplication" : clientApplication,
            "HTTPStatus" : httpStatus,
            "ErrorMessage": errorMessage
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
    log_success(appAPI, clientApplication, correlationId, "Sending message to webjob.")
    log(appWebJob, clientApplication, correlationId, "Message received.")
    log(appWebJob, clientApplication, correlationId, "Processing message...")
    log(appWebJob, clientApplication, correlationId, "Message processed.")

def log_flow_error(correlationId, clientApplication):
    appClient = 'WorkshopClientApp'
    appAPI = 'WorkshopAPI'

    correlationId = str(uuid.uuid4())

    log(appClient, clientApplication, correlationId, "Sending request to API...")
    log(appAPI, clientApplication, correlationId, "Request received from client.")
    log(appAPI, clientApplication, correlationId, "Processing request...")
    log_error(appAPI, clientApplication, correlationId, "Processing error", 500, "Unexpected exception occured during request processing.")

def log_flow_unauthorized(correlationId, clientApplication):
    appClient = 'WorkshopClientApp'
    appAPI = 'WorkshopAPI'

    correlationId = str(uuid.uuid4())

    log(appClient, clientApplication, correlationId, "Sending request to API...")
    log_error(appAPI, clientApplication, correlationId, "Unauthorized", 401, "Unauthorized.")

log_flow(str(uuid.uuid4()), "Weekly")
log_flow(str(uuid.uuid4()), "Weekly")
log_flow_error(str(uuid.uuid4()), "Weekly")
log_flow(str(uuid.uuid4()), "Weekly")
log_flow_unauthorized(str(uuid.uuid4()), "Weekly")
log_flow_unauthorized(str(uuid.uuid4()), "Weekly")
log_flow_unauthorized(str(uuid.uuid4()), "Weekly")


log_flow(str(uuid.uuid4()), "HRManager")
log_flow(str(uuid.uuid4()), "HRManager")
log_flow_error(str(uuid.uuid4()), "HRManager")
log_flow_error(str(uuid.uuid4()), "HRManager")
log_flow_error(str(uuid.uuid4()), "HRManager")
log_flow_error(str(uuid.uuid4()), "HRManager")
log_flow_error(str(uuid.uuid4()), "HRManager")


log_flow(str(uuid.uuid4()), "Talmundo")
log_flow(str(uuid.uuid4()), "Talmundo")
log_flow(str(uuid.uuid4()), "Talmundo")
log_flow_unauthorized(str(uuid.uuid4()), "Talmundo")
log_flow(str(uuid.uuid4()), "Talmundo")
log_flow_unauthorized(str(uuid.uuid4()), "Talmundo")

log_flow(str(uuid.uuid4()), "PeopleCore")
log_flow(str(uuid.uuid4()), "PeopleCore")
log_flow(str(uuid.uuid4()), "PeopleCore")
log_flow(str(uuid.uuid4()), "PeopleCore")


log_flow(str(uuid.uuid4()), "ReachMe")
log_flow_error(str(uuid.uuid4()), "ReachMe")
log_flow(str(uuid.uuid4()), "ReachMe")
log_flow_error(str(uuid.uuid4()), "ReachMe")
log_flow(str(uuid.uuid4()), "ReachMe")
log_flow_error(str(uuid.uuid4()), "ReachMe")
log_flow(str(uuid.uuid4()), "ReachMe")
log_flow_error(str(uuid.uuid4()), "ReachMe")
