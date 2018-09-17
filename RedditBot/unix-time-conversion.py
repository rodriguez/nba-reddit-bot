import requests
import datetime
import json

def convert_to_unix(raw_date):
    # date: MM/DD/YYYY
    date = raw_date.split('/')
    if len(date[0]) < 2:
        date[0] = '0' + date[0]
    if len(date[1]) < 2:
        date[1] = '0' + date[1]
    assert(len(date[2]) == 4)
    date = date[2] + '-' + date[0] + '-' + date[1]
    url = build_url(date)
    response = requests.get(url)
    json_result = json.loads(response.content)
    result = json_result['timestamp']
    print(result)
def convert_now_to_unix():
    now = str(datetime.datetime.now()).split()
    now_date = now[0]
    now_time = now[1].split('.')[0]
    url = build_url(now_date, now_time)
    response = requests.get(url)
    json_result = json.loads(response.content)
    result = json_result['timestamp']
    print(result)
def build_url(date, time=None):
    if time is None:
        selected_time = '00:00:01'
    else:
        selected_time = time
    base_uri = 'http://www.convert-unix-time.com/api?'
    date = 'date=' + date
    url = base_uri + date + '%20' + selected_time + '&timezone=New_York'
    return url