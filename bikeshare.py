import time
import pandas as pd
import numpy as np
import datetime as dt


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

 

def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!!!')
     # To do: list down filters
    cities = ["Chicago", "New York", "Washington"]
    months = ["January", "February", "March", "April", "May", "June", "All"]
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "All"]
 
<<<<<<< HEAD
     # HINT: Use a while loop to handle invalid inputs
=======

   
    # TO DO: get user input for city (chicago, new york city, washington). 
>>>>>>> documentation

    while True:
        city = input("Would you like to see data for chicago, new york, or washington?")
        if city.title() in cities:
            break
        else:
            print("Sorry! Please select from chicago, new york, or washington.")
    
    while True:
        month = input("Which month - january, february, march, april, may, june or all?")
        if month.title() in months:
            break
        else:
            print("Sorry!Please select from all or one month from january, february, march, april, may, june.")
    while True:
        day = input("Which day - monday, tuesday, wednesday, thursday, friday, saturday, sunday or all?")
        if day.title() in days_of_week: 
            print("Here you go!")
            break
        else:
            print("Sorry!Please name one weekday or all.")
    
    print('-'*40)
    
    return city, month, day


def load_data(city, month, day):

   
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    
    # extract month, day of week and hour from Start Time to create new columns
    df['months'] = df['Start Time'].dt.month
    df['days_of_week'] = df['Start Time'].dt.day_name
    df['Hour'] = df['Start Time'].dt.hour

    # filter bymonth if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['months'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['days_of_week'] == day.title()]

    return df

def time_stats(df):
    print('\nCalculating The Most Frequent Times of Travel...\n')
    
    start_time = time.time()
       
    common_month = df['months'].mode()[0]
    print("The most common month is", common_month)
        
    common_week = df['days_of_week'].mode()[0]
    print("The most common week is", common_week)

    common_hour = df['Hour'].mode()[0]
    print("The most common hour is", common_hour)
    
    print("\nThis took  %s seconds." % (time.time() - start_time))
  
    print('-'*40)


def station_stats(df):
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    Start_Station = df['Start Station'].mode()[0]
    print("The most commonly used start station is", Start_Station)

    End_Station = df['End Station'].mode()[0]
    print("The most commonly used end station is", End_Station)

    Combination = df['Start Station'] + ' to ' + df['End Station']
    print('The most common start and end station is', Combination.mode()[0])
    
    print("\nThis took %s seconds." % (time.time() - start_time))
        
    print('-'*40)


def trip_duration_stats(df):
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
        
    
    mean_travel = df['Trip Duration'].mean()
    print("The mean of trip duration is", mean_travel)
    
    total_travel = df['Trip Duration'].sum()
    print("The total of trip duration is", total_travel)

    least_travel = df['Trip Duration'].min()
    print("The least trip duration is", least_travel)
    
    most_travel = df['Trip Duration'].max()
    print("The most trip duration is", most_travel)
    
    
    user_type_trip =  df.groupby('User Type')['Trip Duration'].sum()
    print("The total trip per user is:")
    for i in range(len(user_type_trip.index.values)):
      print(user_type_trip.index.values[i], ' : ', list(user_type_trip)[i])
     
    print("\nThis took %s seconds." % (time.time() - start_time))
    
    print('-'*40)


def user_stats(df):

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    if 'User Type' in df.columns:
     counts_user_types = df['User Type'].value_counts()
     print("The counts_user_types is")
     for i in range(len(counts_user_types.index.values)):
      print(counts_user_types.index.values[i], ' : ', list(counts_user_types)[i])
    else:
      print("User Type Data not available")

        
    
    #If user type and gender is missing, print no information found
    if 'Gender' in df.columns:
    
    # Count Gender
      counts_gender = df['Gender'].value_counts()
      print("The counts_gender is:")
      for i in range(len(counts_gender.index.values)):
        print(counts_gender.index.values[i], ' : ', list(counts_gender)[i])
    else:
        print("Gender Data not available")
        

    #If birth day is missing, print no information found
    if 'Birth Year' in df.columns:
        earliest_year = df['Birth Year'].min()
        print("The earliest_year of birth is", int(earliest_year))

        most_recent_year = df['Birth Year'].max()
        print("The most_year of birth is", int(most_recent_year))   
    
        most_common_year = df['Birth Year'].mode()
        print("The most_common_year of birth is", int(most_common_year))
    else:
       print("Birth Year Data not available")   
    
    print("\nThis took %s seconds." % (time.time() - start_time))
        

         
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
 
if __name__ == "__main__":
        main()