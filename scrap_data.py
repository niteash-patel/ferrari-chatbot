import requests
from bs4 import BeautifulSoup
import json

# this is first line to get the data 
url="https://en.wikipedia.org/wiki/List_of_Ferrari_road_cars"
headers={"user-agent": "myferrariproject/1.0 (niteshpatel5354@gmail.com)"}
response=requests.get(url, headers=headers)

shoup=BeautifulSoup(response.text, "html.parser")
content=shoup.find("div",{"id": "mw-content-text"})

links=content.find_all("a", href=True)

cars_name=[]

for link in links:
    href=link["href"]
    if "/wiki/Ferrari_" in href and "File:" not in href:
        cars_name.append(link.get("title"))

unique_car_name=list(set(cars_name))
unique_car_name = [name for name in unique_car_name if name is not None]

all_cars_data=[]

for car in unique_car_name:
    safe_title=car.replace(" ", "_")
    summary_url=f"https://en.wikipedia.org/api/rest_v1/page/summary/{safe_title}"
    summary_response=requests.get(summary_url, headers=headers)
    data=summary_response.json()

    image_info=data.get("originalimage")
    image_url=image_info["source"] if image_info else None

    car_data={
        "model": car,
        "summary": data.get("extract"),
        "image_url": image_url
    }
    
    all_cars_data.append(car_data)
    print(f"done:{car}")

with open("ferrari_data.json", "w", encoding="utf-8") as f:
    json.dump(all_cars_data, f, ensure_ascii=False, indent=2)
print("data saved")

