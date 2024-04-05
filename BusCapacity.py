import json
with open('data.json') as f:
    data = json.load(f)

count_total = 0
count_above_90 = 0

for item in data:
    if not item.get("Route") or not item.get("Journey Time") or not item.get("Bus Number") or not item.get("Direction") or not item.get("Driver"):
        continue
    
    count_total += 1
    
    if item.get("Passenger Numbers") and int(item["Passenger Numbers"]) >= 90:
        count_above_90 += 1
        cleaned_item = {k: ''.join(c for c in str(v) if c.isalnum() or c.isspace()) for k, v in item.items()}
        print(', '.join([f'{k} {v}' for k, v in cleaned_item.items()]))
    else:
        continue

percent_above_90 = count_above_90 / count_total * 100 if count_total > 0 else 0
print(f"Total items: {count_total}")
print(f"Percentage of items above 90 passengers: {percent_above_90:.2f}%")
