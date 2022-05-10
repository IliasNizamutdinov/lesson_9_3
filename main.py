import datetime
import requests
import time
from pprint import pprint

def main():
    current_data = datetime.datetime.today().date()
    data_start = current_data - datetime.timedelta(2)

    unixtime = int(time.mktime(data_start.timetuple()))

    url = "https://api.stackexchange.com/2.3/questions"
    params = {"fromdate": unixtime, "order": "desc", "sort": "activity", "tagged": "python", "site": "stackoverflow"}

    resp = requests.get(url, params=params)

    if resp.status_code != 200:
        print("Error!!!")
    else:
        for dic_anse in resp.json()["items"]:
            pprint(dic_anse['title'])

if __name__ == '__main__':
    main()


