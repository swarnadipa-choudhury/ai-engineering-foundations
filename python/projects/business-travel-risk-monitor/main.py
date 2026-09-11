# ============================================================
# PHASE 1 — TRAVEL OPERATIONS CLI
# ============================================================

from pathlib import Path
import json


def load_trips():
    data_dir = Path('data')
    
    json_file = data_dir / 'trips.json'

    with open (json_file, 'r') as f:
        trips = json.load(f)
    return trips


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


def print_trip_details(trip):

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



# ============================================================
# TASK 4 — Find a Business Trip by Trip ID
# ============================================================

def search_trip_id(input_trip_id):

    id_found = False

    for trip in trips:

        if trip["trip_id"] == input_trip_id:

            id_found = True
            print_trip_details(trip)

    if not id_found:
        print('ID not found.')



# ============================================================
# TASK 5 — Display Travel Summary
# ============================================================

def display_travel_summary(trips):

    print('''================================

BUSINESS TRAVEL SUMMARY

================================''')

    total_trips = len(trips)

    total_employees = set()

    destinations = []

    print(f"Total Trips: {total_trips}")

    for trip in trips:

        total_employees.add(trip["employee_name"])

        destinations.append(
            (trip["destination"]["city"], trip["destination"]["country"])
        )

    print(f"Total Employees: {len(total_employees)}")

    print()

    print("Destinations: ")

    for destination in destinations:

        print(f"{destination[0]}, {destination[1]}")





# ============================================================
# TASK 6 — Find a Business Trips by Country
# ============================================================

# find_trips_by_country(trips, country)
# Please enter country: Japan
# It should display Hermione's Tokyo trip.
# Please enter country: Germany
# No trips found for Germany.

def find_trips_by_country(trips, country):
    trip_found = False
    for trip in trips:
        if trip["destination"]["country"].lower() == country.lower():
            print_trip_details(trip)
            trip_found = True
    if not trip_found:
        print(f"No trips found for {country}.")
    



# ============================================================
# TASK 7 — Upcoming Business Trips
# ============================================================

# display_upcoming_trips(trips)
# Please enter date (DD-MM-YYYY):
# If the user enters: 11-09-2026
# It should display Harry's Paris trip.
# If they enter: 15-09-2026
# It should display:
# No trips found for 15-09-2026.

def display_upcoming_trips(trips):
    input_date = input("Please enter date (DD-MM-YYYY): ")
    is_trip_found = False
    for trip in trips:
        if trip["travel_date"] == input_date:
            is_trip_found = True
            print_trip_details(trip)
    if not is_trip_found:
        print(f"No trips found for {input_date}.")

    
#save_trips(trips)

# It should:

# Receive the trips list as a parameter.
# Locate data/trips.json.
# Open the file in write mode.
# Write the complete trips list to JSON.
# Format the JSON so it's human-readable.

def save_trips(trips):
    data_dir = Path('data')
    json_file = data_dir / 'trips.json'
    with open (json_file, 'w') as f:
        json.dump(trips, f, indent=4)
        

try:
    trips = load_trips()
    save_trips(trips)
# Display all trips
    for trip in trips:
        print_trip_details(trip)
    search_trip_id(input("Please enter trip ID: "))
    print()
    display_travel_summary(trips)
    print()
    input_country = input("Please enter country: ")
    print()
    find_trips_by_country(trips, input_country)
    print()
    display_upcoming_trips(trips)  
    print()
except FileNotFoundError:
     print("File doesn't exist")
except json.JSONDecodeError:
    print("Trip data file contains invalid JSON.")
    
    
    

