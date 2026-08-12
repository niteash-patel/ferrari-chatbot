import json

with open("ferrari_data.json", "r", encoding="utf-8") as f:
    data=json.load(f)

print(f"totale cars: {len(data)}")

missing_summary=[car["model"] for car in data if not car["summary"]]
print(f"missing summary: {len(missing_summary)}")

missing_image=[car["model"] for car in data if not car["image_url"]]
print(f"missing image: {len(missing_image)}")

cleaned_data=[car for car in data if car["summary"]]
print(f"data after clean {len(cleaned_data)} cars")

with open("ferrari_data.json","w", encoding="utf-8") as f:
    json.dump(cleaned_data, f, ensure_ascii=False, indent=2)

print("clean data save")

luce_found = [car["model"] for car in data if "Luce" in car["model"]]
print(luce_found)

exclude_keywords = ["engine", "film", "soundtrack", "World", "Formula One", 
                     "Challenge", "Virtual", "Evolution", "Club", "factory", 
                     "Sigma", "Modulo", "Vision Gran Turismo"]

final_data = []
for car in cleaned_data:
    name = car["model"]
    if not any(keyword in name for keyword in exclude_keywords):
        final_data.append(car)

print(f"Before: {len(cleaned_data)}, After removing non-cars: {len(final_data)}")

with open("ferrari_data.json", "w", encoding="utf-8") as f:
    json.dump(final_data, f, ensure_ascii=False, indent=2)

print("Final cleaned data saved!")