
trips = [{
    "trip_id": "TR001",
    "employee_name": "Harry Potter",
    "destination": {
        "city": "Paris",
        "country": "France"
    },
    "travel_date": "11-09-2026",
    "return_date": "21-09-2026",
    "purpose": "World Aurors convention"
},
         {
    "trip_id": "TR002",
    "employee_name": "Hermione Granger",
    "destination": {
        "city": "Tokyo",
        "country": "Japan"
    },
    "travel_date": "11-10-2026",
    "return_date": "16-10-2026",
    "purpose": "Witch/Wizard of the century Awards"
},
         {
    "trip_id": "TR003",
    "employee_name": "Ron Weasley",
    "destination": {
        "city": "Buenos Aires",
        "country": "Argentina"
    },
    "travel_date": "23-09-2026",
    "return_date": "29-09-2026",
    "purpose": "Quidditch finals"
}]

def display_formatted_trip_details(key):
    if key == 'employee_name':
        return 'Employee'
    elif key == 'destination':
        return 'Destination'
    elif key == 'city':
        return 'City'
    elif key == 'country':
        return 'Country'
    elif key == 'travel_date':
        return 'Travel Date'
    elif key == 'return_date':
            return 'Return Date'
    elif key == 'purpose':
        return 'Purpose'
    else:
        return "invalid key"

for trip in trips:
    print('================================')
    for (key, value) in trip.items():
        if key == 'trip_id':
             print(f'BUSINESS TRIP: {value}')
             print('================================')
        elif isinstance(value, dict):
            for (k, v) in value.items():
                print(f"{display_formatted_trip_details(k)} : {v}")  
        else:
            print(f"{display_formatted_trip_details(key)} : {value}")
    
    print()
