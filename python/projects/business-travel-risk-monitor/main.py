sample_trip = {
    "trip_id": 1234,
    "employee_name": "Swarna",
    "destination": {
        "city": "Kolkata",
        "country": "India"
    },
    "travel_date": "11-09-2026",
    "return_date": "21-09-2026",
    "purpose": "festival"
    
}


print('...................')
print('*****Trip details*****') 
print('...................')
for (key, value) in sample_trip.items():
    if isinstance(value, dict):
        print("Destination: ")
        for (k, v) in value.items():
            print(f"{k}: {v}")
    else:
        print(f"{key} : {value}")