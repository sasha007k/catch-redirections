import json

def process_browser_logs_for_network_events(logs):
    network_logs = []
    for entry in logs:
        log = json.loads(entry["message"])["message"]
        if ("Network.requestWillBeSent" == log["method"] and log["params"] is not None and 
            "request" in log["params"] and "isSameSite" in log["params"]["request"]):
            isSameSite = log["params"]["request"]["isSameSite"]
            requestType = log["params"]["type"]
            if isSameSite and requestType == "Document":
                    network_logs.append(log)
    return network_logs

def return_main_url_and_redirects(logs):
    network_logs = process_browser_logs_for_network_events(logs);
    links = []
    for log in network_logs:
        link = log["params"]["documentURL"]
        links.append(link)
    return links
