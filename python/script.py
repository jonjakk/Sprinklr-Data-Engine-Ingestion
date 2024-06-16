import csv, os, json, requests
from datetime import datetime
from time import sleep
import paramiko

API_URL = os.getenv("SPRINKLR_API_URL")
SFTP_SERVER = os.getenv("SFTP_SERVER")
SFTP_USERNAME = os.getenv("SFTP_USERNAME")
SFTP_PASSWORD = os.getenv("SFTP_PASSWORD")
API_KEY = os.getenv("API_KEY")
BEARER_TOKEN = os.getenv("BEARER_TOKEN")
FILE_NAME = os.getenv("FILE_NAME")
SFTP_PORT = int(os.getenv("SFTP_PORT"))

payload = json.dumps({
  "reportingEngine": "PLATFORM",
  "report": "POST_INSIGHTS",
  "startTime": "1615096800000",
  "endTime": "1617685199999",
  "timeZone": "America/Chicago",
  "pageSize": "20",
  "page": "0",
  "groupBys": [
    {
      "heading": "Post ID",
      "dimensionName": "POST_ID",
      "groupType": "FIELD",
      "details": {}
    },],
  "projections": [
    {
      "heading": "POST_REACH_COUNT",
      "measurementName": "POST_REACH_COUNT",
      "aggregateFunction": "SUM"
    },
  ],
  "jsonResponse": True
})
headers = {
  'key': API_KEY,
  'Authorization': f"Bearer {BEARER_TOKEN}",
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

def call_api():
    response = requests.request("POST", API_URL, headers=headers, data=payload)
    return response.headers.get("X-Plan-Quota-Current")

def write_to_csv(quota):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = [[now, quota]]
    if not os.path.isfile(FILE_NAME):
        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "API Calls per Hour"])
    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

def upload_to_sftp():
    transport = paramiko.Transport((SFTP_SERVER, SFTP_PORT))
    transport.connect(username=SFTP_USERNAME, password=SFTP_PASSWORD)
    sftp = paramiko.SFTPClient.from_transport(transport)
    try:
        sftp.put(FILE_NAME, f'/upload/{FILE_NAME}')
        print("File uploaded successfully")
    except Exception as e:
        print(f'SFTP error: {e}')
    finally:
        sftp.close()
        transport.close()

def main():
    while True:
        quota = call_api()
        write_to_csv(quota)
        upload_to_sftp()
        sleep(3600) 

if __name__ == "__main__":
    main()
