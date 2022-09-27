#Jamison Talley
#1-12-21
#Doomsday.py

#notes
#The purpose of this program is to take any user given date, and
#output the day of the week upon which it lands. 
#This program utilizes something called The Doomsday Algorithm
#and knowledge of it is integral to understanding this code


#defines a function to calculate the difference
#in day of the week based on how far into the century
# the specified year is

def year_doomsday_mod(year):
    century = (year // 100) * 100
    year_mod = (year - century) + ((year - century) // 4)
    return year_mod


#defines a function to calculate the difference in 
#day of the week based on a repeating pattern 
#that resets every four centuries

def cent_doomsday_mod(century):
    position_list = [2, 0, 5, 3]
    cent_position = (((century // 100) - 20) % 4)
    cent_doomsday_mod = position_list[cent_position]
    return cent_doomsday_mod


#defines a function that determines if a year is a leap
#year or not, as that is important in calculating the
#doomsday

def is_leap_year(year):
    if (year % 4) == 0:
        return True
    else:
        return False


#defines a function that
#uses a series of if else statements to determine the
#difference in day based on the day of the month given
#by the user. Note this value sometimes depends on
#whether the year is a leap year

def day_doomsday_mod(day, month, year):
    if month == 1:
        if is_leap_year(year) == True:
            day_doomsday_mod = (day - 4)
        else: 
            day_doomsday_mod = (day - 3)
    elif month == 2:
        if is_leap_year(year) == True:
            day_doomsday_mod = (day - 29)
        else:
            day_doomsday_mod = (day - 28)
    elif month == 3:
        day_doomsday_mod = (day - 14)
    elif month == 4:
        day_doomsday_mod = (day - 4)
    elif month == 5:
            day_doomsday_mod = (day - 9)
    elif month == 6:
        day_doomsday_mod = (day - 6)
    elif month == 7:
        day_doomsday_mod = (day - 11)
    elif month == 8:
        day_doomsday_mod = (day - 8)
    elif month == 9:
        day_doomsday_mod = (day - 5)
    elif month == 10:
        day_doomsday_mod = (day - 10)
    elif month == 11:
        day_doomsday_mod = (day - 7)
    elif month == 12:
        day_doomsday_mod = (day - 12)
    else:
        print("That's not a month!")
    return day_doomsday_mod


#defines a function that combines the previous
#functions of the program to take an input of 
#any date, and return the day of the week using
#the doomsday algorithm

def day_of_week(day, month, year):
    day_table = ["Sunday", "Monday", "Tuesday",
    "Wednesday", "Thursday", "Friday", "Saturday"]
    end_mod = cent_doomsday_mod(year)
    end_mod += year_doomsday_mod(year)
    end_mod += day_doomsday_mod(day, month, year)
    end_mod = end_mod % 7
    weekday = day_table[end_mod]
    return weekday


#defines a main function for the program that utilizes
#the functions, and manages errors in input format.

def main():
    print("\nThis program will tell you the day of the week")
    print("of any given date: past, present, or future!")
    continue_bool = True
    while continue_bool == True:
        print("Please enter your chosen date")
        print("For example: July 4th 1980 would be \'04-07-1980\'")
        user_date = input().split("-")
        try:
            for i1 in range(len(user_date)):
                user_date[i1] = int(user_date[i1])
            print(day_of_week(user_date[0], user_date[1], user_date[2]))
        except:
            print("Your date doesn't appear to be in the correct format...")
        print("Would you like to enter another date? (yes or no)")
        continue_val = input()
        if 'y' not in continue_val:
            continue_bool = False
    print("\nThanks for using the Doomsday Algorithm!\n")


if __name__ == "__main__":
    main()