# This function gets day and k value as arguments and calculates the day K days after for weekday.
def solution(day, k):
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    # K must be between 0 and 500, inculsively
    if k < 0 or k > 500:
        return "k must be between 0 and 500"
        
    if day not in days:
        return day + " is not on the list"
    # Gets the index of the input day
    idx = days.index(day.capitalize())

    # Returns a true value based on 7 mod 
    return days[(idx + k) % 7]
