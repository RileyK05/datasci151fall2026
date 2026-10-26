def leagues_to_miles(L):
    # This function converts a value in metric leagues (L)
    # to the corresponding value in miles.

    # Convert metric leagues to kilometers
    km = 4*L

    # Convert kilometers to miles
    miles = km/1.609344
    
    return miles

