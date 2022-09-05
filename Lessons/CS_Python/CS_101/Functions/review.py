# defined a function with name as the parameter
def quick_route(name):
    print("Welcome to Quick Route " +name)

# called the function with "Victor" as the argument
quick_route("Victor")

# defined a function that returns the rounded time
def estimated_time_rounded(estimated_time):
    rounded_time = round(estimated_time)
    return rounded_time

# created a variable to store the rounded time
estimate = estimated_time_rounded(4379.5)

# defined a function with the parameters shown
def trip_info(origin, destination, estimated_time, mode_of_transport="Tesla Roadster"):
    print("Your trip starts off in " +origin)
    print("And you are traveling to " +destination)
    print("You will be traveling by " +mode_of_transport)
    print("It will take approximately " +str(estimated_time) +" hours at 60 mph")

# called the function with my chosen arguments
trip_info("Houston", "The Moon", estimate)