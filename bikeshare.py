import os
import time
import pandas as pd
import numpy as np
import calendar
from datetime import date

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
month_list = {'January':0, 'February':1, 'March':2, 'April':3, 'May':4, 'June':5 }
day_list = {1:'Sunday', 2:'Monday', 3:'Tuesday', 4:'Wednesday', 5:'Thursday', 6:'Friday',7:'Saturday'}
filter_list = {'Month':0, 'Day':1, 'Both':2,'None':3}
restarting = False


def get_filters(restarting):
    """
    Asking user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    correct=False
    i=0
    month=''
    day=''
    filter_type=''

    print('Hello! Let\'s explore some US bikeshare data!')
    city=input('Will you like to see data for Chicago, New York City, or Washington? \n').lower()
    #filter_type=input('Will you like to filter the data by month, day, both, or not all? Type "none" for no time filter. \n')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while correct == False and restarting == False:
        i=i+1

        if city not in CITY_DATA.keys() and i==3:
            print('Wrong city entered 3 times application terminating. kindly restart? \n')

            restarting = True
            break
        elif city not in CITY_DATA.keys():

            print('Wrong city entered please enter Chicago or New York City or Washington? \n')
            city=input('Will you like to see data for Chicago, New York City, or Washington? \n').lower()
        elif city in CITY_DATA.keys():
            correct = True



    correct=False
    i=0

    while correct == False and restarting==False:
        i=i+1
        filter_type=input('Will you like to filter the data by month, day, both, or not all? Type "none" for no time filter. \n').title()
        # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
        if filter_type not in filter_list.keys() and i==3:
            print('Wrong filter entered 3 times application terminating. Kindly restart the program? \n')

            restarting = True
            break
        elif filter_type not in filter_list.keys():

            print('Wrong filter entered please entermonth, day, both, or not all? Type "none" for no time filter. \n')
        elif filter_type in filter_list.keys():
            correct = True


    if filter_type == 'Month' and restarting==False:
        correct=False
        i=0
        month_name=input('Which month January, February, March, April, May, or June? \n.').title()
            # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
        while correct == False:
            i=i+1
            if month_name not in month_list.keys() and i==3:
                print('Wrong month entered 3 times application terminating. Kindly restart the program? \n')
                restarting = True
                break
            elif month_name not in month_list.keys():
                print('Wrong month entered please enter month, day, both, or none?? \n')
                month_name=input('Which month January, February, March, April, May, or June? \n.').title()
            elif month_name in month_list.keys():
                correct = True


    try:
        if filter_type == 'Day' and restarting==False:
            correct=False
            i=0
            day=int(input('Which day? Please type your response as an integer (e.g. 1=Sunday) \n'))
                # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
            while correct == False:
                i=i+1
                if day not in day_list.keys() and i==3:
                    print('Wrong day entered 3 times application terminating. Kindly restart the program? \n')

                    restarting = True
                    break
                elif day not in day_list.keys():

                    print('Wrong day entered Please type your response as an integer (e.g. 1=Sunday) \n')
                    day=int(input('Which day? Please type your response as an integer (e.g. 1=Sunday) \n'))
                elif day in day_list.keys():
                    correct = True
    except ValueError:

        restarting=True
        print ('Wrong Data entered Restarting the program. Please type your response as an integer (e.g. 1=Sunday) \n')




    try:
        if filter_type == 'Both' and restarting==False:
            correct=False
            i=0
            day=int(input('Which day? Please type your response as an integer (e.g. 1=Sunday) \n'))
                # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
            while correct == False:
                i=i+1
                if day not in day_list.keys() and i==3:
                    print('Wrong day entered 3 times application terminating. Kindly restart the program? \n')

                    restarting = True
                    break
                elif day not in day_list.keys():

                    print('Wrong day entered Please type your response as an integer (e.g. 1=Sunday) \n \n')
                    day=int(input('Which day? Please type your response as an integer (e.g. 1=Sunday) \n'))
                elif day in day_list.keys():
                    correct = True


            if filter_type == 'Both' and restarting==False:
                correct=False
                i=0
                month_name=input('Which month January, February, March, April, May, or June? \n').title()
                    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
                while correct == False:
                    i=i+1
                    if month_name not in month_list.keys() and i==3:
                        print('Wrong month entered 3 times application terminating. Kindly restart the program? \n')
                        restarting = True
                        break
                    elif month_name not in month_list.keys():
                        print('Wrong month entered please enter month, day, both, or none?? \n')
                        month_name=input('Which month January, February, March, April, May, or June? \n.').title()
                    elif month_name in month_list.keys():
                        correct = True

    except ValueError:

        restarting=True
        print ('Wrong Data entered Restarting the program. Please type your response as an integer (e.g. 1=Sunday) \n')

    if filter_type == 'none' and restarting==False:
       print('Filter Type none selected')


    return city, month, day,filter_type,restarting


def load_data(city, month, day,filter_type):
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

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday

    # filter by month if applicable
    if filter_type == 'month':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

        # filter by day of week if applicable
    elif filter_type == 'day':
        # use the index of the months list to get the corresponding int
        df = df[df['day_of_week'] == day]


    # filter by day of week if applicable
    elif filter_type == 'both':
        # filter by day of week to create the new dataframe
        df = df[df['month'] == month]
        df = df[df['day_of_week'] == day]
        # filter by day of week if applicable

    elif filter_type == 'none':
        # filter by day of week to create the new dataframe
        df = df

    return df



def time_stats(df, filter_type):
    """Displays statistics on the most frequent times of travel."""

    print('\n\nCalculating The Most Frequent Times of Travel...')
    print('-'*60)
    start_time = time.time()

    # display the most common month
    df['month'] = df['Start Time'].dt.month

    try:
        print('\tCalculating  statistic for month travelling...')

        popular_day_of_the_month = df['month'].mode()[0]
        popular_day_of_the_month=calendar.month_name[popular_day_of_the_month]

        print('\tWhat is the most popular month for travelling?')

        print('\tThe most popular month is : {} : Filtered by {}'.format(popular_day_of_the_month,filter_type))
        end_time =time.time() - start_time
        print("\nThis took {} seconds.".format(end_time))
        print('-'*60)

        #if filter_type==''
        # display the most common day of week
        start_time = time.time()
        df['week_day'] = df['Start Time'].dt.weekday

        popular_day_of_the_week = df['week_day'].mode()[0]
        popular_day_of_the_week=calendar.day_name[popular_day_of_the_week]

        print('\n\nCalculating  statistic for day travelling...')
        print('-'*60)
        print('\n\tWhat is the most popular day for travelling?')
        print('\tThe most popular day is : {} : Filtered by {}'.format(popular_day_of_the_week,filter_type))
        end_time =time.time() - start_time
        print("\nThis took {} seconds.".format(end_time))
        print('-'*60)

        # display the most common start hour
        start_time = time.time()
        # extract hour from the Start Time column to create an hour column
        df['hour'] = df['Start Time'].dt.hour

        # find the most popular hour
        popular_hour = df['hour'].mode()[0]

        print('\n\nCalculating  statistic popular hour for traveling...')
        print('-'*60)
        print('\n\tWhat is the most popular hour for traveling?')
        print('\tThe most popular hour is : {} : Filtered by {}'.format(popular_hour,filter_type))
        end_time =time.time() - start_time
        print("\nThis took {} seconds.".format(end_time))
        print('-'*60)
    except IndexError:
        print('Weekday doesn''t exist')

def station_stats(df,filter_type):
    """Displays statistics on the most popular stations and trip."""

    print('\n\nCalculating The Most Popular Stations and Trip...')
    print('-'*60)
    start_time = time.time()

    try:
        # display most commonly used start station
        popular_start_station = df['Start Station'].mode()[0]

        # display most commonly used end station
        popular_end_station = df['End Station'].mode()[0]

        print('\tWhat is the most popular start and end stations respectively filtered by: {}?.'.format(filter_type))
        print("\t('{}','{}')".format(popular_start_station,popular_end_station))
        end_time =time.time() - start_time
        print("\nThis took {} seconds.".format(end_time))



        # display most frequent combination of start station and end station trip
        popular_trip = df.groupby(['Start Station', 'End Station']).size().idxmax()
        popular_trip_count=df.groupby(['Start Station', 'End Station']).size().max()

        print('\n\tWhat is the most popular start station and end station trip filtered by: {}?.'.format(filter_type))
        print('\tStart Station \t\t\t\tEnd Station')
        print('\t{}\t\t{}\t\t{}'.format(popular_trip[0],popular_trip[1],popular_trip_count))
        end_time =time.time() - start_time
        print("\nThis took {} seconds.".format(end_time))
        print('-'*60)
    except IndexError:
        print('Weekday doesn''t exist')

def trip_duration_stats(df,filter_type):
    """Displays statistics on the total and average trip duration."""

    print('\n\nCalculating Trip Duration...')
    print('-'*60)
    start_time = time.time()

    # display total travel time

    sum_duration = df['Trip Duration'].sum()
    average_duration = df['Trip Duration'].mean()
    count_duration = df['Trip Duration'].count()
    print('\tTotal Duration: {}, Count:{}, Avg Duration: {}'.format(sum_duration, count_duration ,average_duration))
    # display mean travel time
    end_time =time.time() - start_time
    print("\nThis took {} seconds.".format(end_time))
    print('-'*60)


def user_stats(df,filter_type,city):
    """Displays statistics on bikeshare users."""

    print('\n\nCalculating User Stats...')
    print('-'*60)
    start_time = time.time()

    # Display counts of user types
    if city.title()=='Washington':
        print( 'Gender information not available for Washington')
    else:
        gender_details=df['Gender'].value_counts().to_frame()
        print('\tWhat is the breakdown of Gender filtered by: {}?.'.format(filter_type))
        print(gender_details)


        end_time =time.time() - start_time
        print("\nThis took {} seconds.".format(end_time))
        print('-'*60)

     # Display youngest, oldest and most available year
    if city.title() == 'Washington':
        print( 'Year of birth information not available for Washington')
    else:
        start_time = time.time()
        youngest = df['Birth Year'].min()
        oldest = df['Birth Year'].max()
        popular_birth_year = df['Birth Year'].mode()[0]

"""Displays Age statistics on bikeshare users."""

        print('\n\nCalculating Age Stats...')
        print('-'*60)
        print('\tWhat is the breakdown of Birth Year filtered by: {}?.'.format(filter_type))
        print('\tThe earliest Birth Year: {}'.format(youngest))
        print('\tThe oldest Birth Year: {}'.format(oldest))
        print('\tThe Popular Birth Year: {}'.format(popular_birth_year))

        end_time =time.time() - start_time
        print("\nThis took {} seconds.".format(end_time))
        print('-'*60)

def raw_data(df,filter_type,city):
    """Displays bikeshare raw data."""

    response=input('Do you want to see raw data enter yes or no \n').lower()
    head=0
    while response=='yes':

        print('\n\n Display raw data...')
        #raw_data_info=df.[['Start Time','End Time']]
        df = pd.read_csv(CITY_DATA[city])
        raw_data_info = df.iloc[head:head+5,]
        print(raw_data_info)
        head = head+5
        response=input('Do you want to see next 5 raw data enter yes or no\n').lower()



def main():

    while True:
        restarting = False
        city, month, day,filter_type,restarting = get_filters(restarting)

        if restarting == True:
            break
        else:
            df = load_data(city, month, day,filter_type)
            time_stats(df,filter_type)
            station_stats(df,filter_type)
            trip_duration_stats(df,filter_type)
            user_stats(df,filter_type,city)
            raw_data(df,filter_type,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print('\nProgram ending Thanks for running the program.\n')
            break


if __name__ == "__main__":
	main()
