# define CONSTANTS outside of main
DAYS_IN_YEAR = 365
HOURS_IN_DAY = 24
MINUTES_IN_HOUR = 60
SECONDS_PER_MINUTE = 60

def main():
    seconds_in_year = DAYS_IN_YEAR * HOURS_IN_DAY * MINUTES_IN_HOUR * SECONDS_PER_MINUTE
    print("There are " + str(seconds_in_year) + " seconds in a year!")  # show output

if __name__ == "__main__":
    main()
