import matplotlib.pyplot as plt
import sqlite3
from calculations import *


# This function gets the average length of each genre
# and plots it in bar graph form
def plot_lengths(cur, conn):
    rap_avg = category_avg_length(cur, conn, 'Rap')
    pop_avg = category_avg_length(cur, conn, 'Pop')
    rock_avg = category_avg_length(cur, conn, 'Rock')
    dance_avg = category_avg_length(cur, conn, 'Dance')
    country_avg = category_avg_length(cur, conn, 'Country')
    latin_avg = category_avg_length(cur, conn, 'Latin')


    fig = plt.figure()
    ax = fig.add_subplot(111)
    averages = [rap_avg, pop_avg, rock_avg, dance_avg, country_avg, latin_avg]
    categories = ['Rap', 'Pop', 'Rock', 'Dance', 'Country', 'Latin']
    ax.bar(categories, averages, color=['blue', 'red', 'orange', 'green', 'purple', 'brown'])
    ax.set_title('Average Song Length of Each Genre')
    plt.xlabel('Genres')
    plt.ylabel('Average Song Lengths (minutes)')
    plt.savefig('avg_lengths_of_genres.png')
    plt.show()



# This function calculates the average song length of a genre
def category_avg_length(cur, conn, category):
    l = select_lengths(cur, conn, category)
    x = lengths_only(l)
    decimal_lengths = []
    for i in x:
        decimal = str(float(i[-2:]) / 60)[1:]
        minute = i.split(':')[0]
        time = float(minute + decimal)
        decimal_lengths.append(time)

    avg = sum(decimal_lengths) / len(decimal_lengths)
    avg = round(avg, 4)
    return avg


# This function takes a list containing each songs
# title, artist, category, and length and returns 
# a list of just the song lengths
def lengths_only(l):
    lengths = []
    for i in l:
        lengths.append(i[3])
    return lengths


# This function takes a list containing each songs
# title, artist, category, and number of lyrics and returns 
# a list of just the number of lyrics
def lyrics_only(l):
    lyrics = []
    zero_count = 0
    for i in l:
        if i[3] == 0:
            zero_count += 1
        lyrics.append(i[3])
    return lyrics, zero_count


def category_avg_lyrics(cur, conn, category):
    l = select_lyrics(cur, conn, category)
    lyrics, zero_count = lyrics_only(l)
    avg = sum(lyrics) / (len(lyrics) - zero_count)
    avg = round(avg, 4)
    return avg

def plot_lyrics(cur, conn):
    rap_avg = category_avg_lyrics(cur, conn, 'Rap')
    pop_avg = category_avg_lyrics(cur, conn, 'Pop')
    rock_avg = category_avg_lyrics(cur, conn, 'Rock')
    dance_avg = category_avg_lyrics(cur, conn, 'Dance')
    country_avg = category_avg_lyrics(cur, conn, 'Country')
    latin_avg = category_avg_lyrics(cur, conn, 'Latin')


    fig = plt.figure()
    ax = fig.add_subplot(111)
    averages = [rap_avg, pop_avg, rock_avg, dance_avg, country_avg, latin_avg]
    categories = ['Rap', 'Pop', 'Rock', 'Dance', 'Country', 'Latin']
    ax.bar(categories, averages, color=['blue', 'red', 'orange', 'green', 'purple', 'brown'])
    ax.set_title('Average Number of Lyrics per Song for Each Genre (words)')
    plt.xlabel('Genres')
    plt.ylabel('Average Number of Lyrics per Song')
    plt.savefig('avg_lyrics_of_genres.png')
    plt.show()




def avg_ratio(cur, conn, category):
    lengths_list = select_lengths(cur, conn, category)
    lyrics_list = select_lyrics(cur, conn, category)
    ratios = get_all_ratios(lengths_list, lyrics_list)
    average = average_ratios(ratios)
    return average

def plot_ratios(cur, conn):
    rap_avg = avg_ratio(cur, conn, 'Rap')
    pop_avg = avg_ratio(cur, conn, 'Pop')
    rock_avg = avg_ratio(cur, conn, 'Rock')
    dance_avg = avg_ratio(cur, conn, 'Dance')
    country_avg = avg_ratio(cur, conn, 'Country')
    latin_avg = avg_ratio(cur, conn, 'Latin')


    fig = plt.figure()
    ax = fig.add_subplot(111)
    averages = [rap_avg, pop_avg, rock_avg, dance_avg, country_avg, latin_avg]
    categories = ['Rap', 'Pop', 'Rock', 'Dance', 'Country', 'Latin']
    ax.bar(categories, averages, color=['blue', 'red', 'orange', 'green', 'purple', 'brown'])
    ax.set_title('Average Ratio of Number of Lyrics to Song Length for Each Genre')
    plt.xlabel('Genres')
    plt.ylabel('Average Ratio of Number of Lyrics to Song Length (words per minute)')
    plt.savefig('avg_ratios_of_genres.png')
    plt.show()