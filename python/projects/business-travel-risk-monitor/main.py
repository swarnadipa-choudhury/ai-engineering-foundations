# ============================================================
# PHASE 1 — TRAVEL OPERATIONS CLI
# ============================================================


# ============================================================
# TASK 1 & 2 — Create and display a single business trip
# ============================================================

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

# ============================================================
# TASK 3 — Add multiple business trips
# ============================================================

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

},
{

    "trip_id": "TR004",

    "employee_name": "Severus Snape",

    "destination": {
        "city": "Paris",
        "country": "France"
    },

    "travel_date": "1-09-2026",
    "return_date": "10-09-2026",
    "purpose": "Potions conference"

}
]


# ============================================================
# TASK 2/3 — Format and display trip details
# ============================================================

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


# Display all trips
for trip in trips:
    print_trip_details(trip)

print()


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


search_trip_id(input("Please enter trip ID: "))

print()


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


display_travel_summary(trips)


# ============================================================
# TASK 5 — Find a Business Trips by Country
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
    
input_country = input("Please enter country: ")
find_trips_by_country(trips, input_country)