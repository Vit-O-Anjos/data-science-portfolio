# Create functions to get user inputs, while instructing the program to except possible errors.
def get_city_flight():
    global city_flight
    while True:
        try:
            city_flight = input("Enter Lisbon, Porto, Faro, Santa Cruz ou Santa Maria: ").lower()
            if city_flight not in ("lisbon", "porto", "faro", "santa cruz", "santa maria"):
                raise TypeError("\nPlease choose a city from the list provided.\n")
            return city_flight
        except TypeError as c:
            print(f"\nError: {c}")



def get_hotel_location():
    hotel_location = city_flight
    return hotel_location



def get_num_nights():
    while True:
        try:
            num_nights = int(input("\nEnter the number of nights: "))
            return num_nights
        except ValueError:
            print("\nError:","\nPlease enter a whole number.")
            
            
            
def get_rental_days():
    while True:
        try:
            rental_days = int(input("\nCar rental days: "))
            return rental_days
        except ValueError:
            print("\nError:","\nPlease enter a whole number.")



def get_custom_rental():
    global custom_rental
    while True:
        try:
            custom_rental = input("\nWould you like to customize your rental ride? Y/N: ").lower()
            if custom_rental == "y":
                custom_rental = True
            elif custom_rental == "n":
                custom_rental = False
            else:
                raise TypeError("\nPlease enter 'Y' (for yes) or 'N' (for no):")
            return custom_rental
        except TypeError as cu:
            print(f"\nError: {cu}")



def get_chosen_rental():
    global chosen_rental
    if custom_rental == True:
            while True:
                try:
                    chosen_rental = (input("\nChoose between Ferrari, Bugatti, Bentley, Lamborghini, 4L or Cupra: ")).lower()
                    if chosen_rental not in ["ferrari", "bugatti", "bentley", "lamborghini", "4l", "cupra"]:
                        raise TypeError("\nPlease choose one of the vehicle brands from the list provided.")
                    return chosen_rental
                except TypeError as ch:
                    print(f"\nError: {ch}")
            
            
            
            
# Create a function to define hotel price.
def price_per_night():
    hotel_location = get_hotel_location()
    if hotel_location == "lisbon":
        daily_charge = 630
        return daily_charge
    elif hotel_location == "porto":
        daily_charge = 540
        return daily_charge
    elif hotel_location == "faro":
        daily_charge = 520
        return daily_charge
    elif hotel_location == "santa cruz":
        daily_charge = 490
        return daily_charge
    elif hotel_location == "santa maria":
        daily_charge = 460
        return daily_charge



# Create a functions to define the price per night.
def hotel_cost():
    daily_charge = price_per_night()
    num_nights = get_num_nights()
    hotel_total = num_nights * daily_charge
    return hotel_total


    
# Create a function to find the flight price.
def plane_cost():
    print("\nChoose your dream holiday destination. ")
    city_flight = get_city_flight()
    if city_flight == "lisbon":
        plane_price = 590
        return plane_price
    elif city_flight == "porto":
        plane_price = 430
        return plane_price
    elif city_flight == "faro":
        plane_price = 650
        return plane_price
    elif city_flight == "santa cruz":
        plane_price = 780
        return plane_price
    elif city_flight == "santa maria":
        plane_price = 980
        return plane_price
    
    
    
# Create a function to define car rental daily charge.  
def which_car():
    chosen_rental = get_chosen_rental()
    if chosen_rental == "ferrari":
        rental_charge = 1700
        return rental_charge
    elif chosen_rental == "bugatti":
        rental_charge = 2400
        return rental_charge
    elif chosen_rental == "bentley":
        rental_charge = 1200
        return rental_charge
    elif chosen_rental == "lamborghini":
        rental_charge = 1550
        return rental_charge
    elif chosen_rental == "4l":
        rental_charge = 10
        return rental_charge
    elif chosen_rental == "cupra":
        rental_charge = 150
        return rental_charge
    
    
    
# Create a function to find the total car rental price.
def car_rental():
    rental_days = get_rental_days()
    custom_rental = get_custom_rental()
    if custom_rental == True:
        rental_charge = which_car()
        total_rental = rental_days * rental_charge
        return total_rental
    else:
        total_rental = rental_days * 90
        return total_rental
    


# Create a function to return the total holiday cost.
def holiday_cost():
    plane_price = plane_cost()
    hotel_total = hotel_cost()
    total_rental = car_rental()
    total = hotel_total + plane_price + total_rental
    return total



# Print/return the total value.
print(f"\nThe total cost for the holiday is £{holiday_cost()}.\n")


#V