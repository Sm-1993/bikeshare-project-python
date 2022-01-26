import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Ask user to specify acity,month, and day to analyize.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ['chicago', 'new york city', 'washington']
    city = input('which city of cities you like to see?').lower()
    while city not in (CITY_DATA):
        print('you provide incorrect city name')
        

            
            
    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april','may', 'june', 'all']
    month = input('which month from months would you like to choose to filter?').lower()
    while month not in months:
        print('you provid incorrect month')
    
       
    
   


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['monday', 'tuesday', 'wednesday','thursday','friday','saturday','sunday','all']
    day = input('which day from days you want to choose to filter?').lower()
    while day not in days:
        print('you provid incorrect day')
    
   
    

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    
    df = pd.read_csv(CITY_DATA[city])
    
    #convert the Start Time column to datetime
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df['month'] = df['Start Time'].dt.month
    
    df['day_of_week'] =  df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
     
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    else:
        print('no month filter')
    

                                      
    df['day_of_week'] =  df['Start Time'].dt.weekday_name
    
    if day !='all':
        df = df[df['day_of_week'] == day.title()] 
                                      
   
    return df
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
                                     
    print('\n calculating the most frequent times of travel \n')                          

    start_time = time.time()

    # TO DO: display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    month = df['month'].mode()[0]
    print('the most common month is:' , {month})
       
   

    # TO DO: display the most common day of week

    days = ['monday', 'tuesday', 'wednesday','thursday','friday','saturday','sunday']
    day = df['day_of_week'].mode()[0]
    print('the most common day is:' , {day})
    # TO DO: display the most common start hour

    hour = df['hour'].mode()[0]
    print('the most common hour is:' , {hour})  
 
   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    return df
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    start_station = df['Start Station'].mode()[0]
    print('the most common start station is:' ,  {start_station})
    
    # TO DO: display most commonly used end station
    
    end_station = df['End Station'].mode()[0]
    print('common end station is:' , [end_station])

    # TO DO: display most frequent combination of start station and end station trip
    
    the_most_frequent_trip = df['Start Station'] + 'to' + df['End Station']
    print('the_most_frequent_trip is: from' , {the_most_frequent_trip.mode()[0]})
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time'])
    print(total_travel_time)

    # TO DO: display mean travel time
    average_travel_time = (pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time'])).mean()
    
    print(average_travel_time)
   
   

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()

    print(user_types)

    # TO DO: Display counts of gender
    gender = df['Gender'].value_counts()

    print(gender)

    # TO DO: Display earliest, most recent, and most common year of birth
    
    year =df['Birth Year'].fillna(0).astype('int64')
    
    
    print('earlist year is:',{year.min()},'the most recent year is:' ,{year.max()},'the most common year is:' ,{year.mode()[0]})

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_raw_data(df):
    raw_data = input('would you like to see raw data?')
    if raw_data == 'yes':
        count = 0
        while True:
             print(df.iloc[count: count+5])
             count +=5
             ask = input('next 5 raws')
             if ask != 'yes':
                break
            
            
        
       
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
