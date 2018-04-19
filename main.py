import requests
import time

ses = requests.Session()
headers = {"user-agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
ses.headers.update(headers)
new_submissions = "https://www.artstation.com/projects.json?page={}&sorting=latest"
trending_submissions = "https://www.artstation.com/projects.json?page={}&sorting=trending"
template_json = "https://www.artstation.com/projects/{hash_id}.json"
pics_by_dates = {}  # counts pics for each day
pics_by_hour = {}  # counts picks published by hour
_ = ses.get("https://www.artstation.com/")
for i in range(1,25):
    time.sleep(1.2)
    res = ses.get(trending_submissions.format(i))
    data = res.json()["data"]
    # created_at/published_at, id, likes_count, hash_id/permalink
    for i in range(0,50):
        (date, time_), pic_id = data[i]["published_at"].split("T"), data[i]["id"]
        time_ = time_[:2]
        if pics_by_dates.get(date, 0):
            pics_by_dates[date].add(pic_id)
        else:
            pics_by_dates[date] = set()
            pics_by_dates[date].add(pic_id)
        if pics_by_hour.get(time_, 0):
            pics_by_hour[time_].add(pic_id)
        else:
            pics_by_hour[time_] = set()
            pics_by_hour[time_].add(pic_id)
    ##pic_json = template_json.format(hash_id=data[0]["hash_id"])
    ##pic = ses.get(pic_json)
    ##views = pic.json()
    ##print(views["views_count"])
            
keys1 = list(pics_by_dates.keys())
keys1.sort()
keys2 = list(pics_by_hour.keys())
keys2.sort()

for k in keys1:
    print("{} {}".format(k, len(pics_by_dates[k])))
for k in keys2:
    print("{} {}".format(k, len(pics_by_hour[k])))
