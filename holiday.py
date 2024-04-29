'''
This project calculates the total cost for a holiday based on the users 
chosen criteria for their chosen holiday.
'''

def hotel_cost(num_nights):
    '''
    This function allows the user to calculate the hotel cost.
    '''
    price_per_night = 200
    total = (num_nights*price_per_night)
    return total


def plane_cost(city_flight):
    '''
    This function returns the plane cost based on the country chosen.
    '''
    if city_flight == "Paris":
        price = 60
    elif city_flight == "Berlin":
        price = 80
    elif city_flight == "Rome":
        price = 40
    elif city_flight == "Lisbon":
        price = 100
    else:
        price = None
        print("Unknown pricing as the city isn't listed as one of our "
              "destinations")
    return price


def car_rental(rental_days):
    '''
    This function allows the user to calculate the car rental price.
    '''
    price_per_day = 80
    total_cost = (rental_days*price_per_day)
    return total_cost


def holiday_cost(num_nights,city_flight,rental_days):
    '''
    This function allows a user to calculate the cost of going
    on a holiday.
    '''
    total_cost = (hotel_cost(num_nights) + 
                  plane_cost(city_flight) + 
                  car_rental(rental_days))
    return total_cost


city_flight = input(("These are the city's we have flights to: Paris, Berlin,"
                     "Rome, or Lisbon. Which city are you flying to? "
                     ).lower()).capitalize()
num_nights = int(input("How many nights are you going to stay at your chosen"
                       " hotel? "))
rental_days = int(input("How many days will you be hiring a car? "))


print(f"For your flight to {city_flight} the price for a ticket is £"
      f"{plane_cost(city_flight)}.")

print(f"For your hotel the total cost of {num_nights} nights is £"
      f"{hotel_cost(num_nights)}.")

print(f"For your car rental the total cost to use it for {rental_days} days is"
      f" £{car_rental(rental_days)}")

print(f"Thus the final cost for your holiday is:\n£{hotel_cost(num_nights)} +" 
      f"£{plane_cost(city_flight)} + £{car_rental(rental_days)} = £"
      f"{holiday_cost(num_nights,city_flight,rental_days)}.")
