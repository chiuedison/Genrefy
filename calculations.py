import sqlite3



def select_lengths(cur, conn, category):
    cur.execute('SELECT Categories.title, Categories.artist, Categories.category, Lengths.length FROM Categories JOIN Lengths ON Categories.title = Lengths.title WHERE Categories.category = ?', (category,))
    l = cur.fetchall()
    conn.commit()
    return l


def select_lyrics(cur, conn, category):
    cur.execute('SELECT * FROM Lyrics WHERE category = ?', (category,))
    l = cur.fetchall()
    conn.commit()
    return l

def calc_ratio(length, num_lyrics):
    decimal = str(float(length[-2:]) / 60)[1:]
    minute = length.split(':')[0]
    time = float(minute + decimal)

    ratio = num_lyrics / time
    ratio = round(ratio, 4)
    return ratio

def get_all_ratios(length_list, lyrics_list):
    l  = []
    for i in range(len(length_list)):
        song = length_list[i][0]
        ratio = calc_ratio(length_list[i][3], lyrics_list[i][3])
        l.append((song, ratio))
    return l

def average_ratios(ratio_list):
    l = []
    for i in ratio_list:
        l.append(i[1])
    average = sum(l) / len(l)
    average = round(average, 4)
    return average


def write_to_file(average, category):
    f = open('lyrics_to_time_ratios.txt', 'a')
    f.write('The average ratio of number of lyrics to time in minutes of songs in the ' + category + ' genre is ' + str(average) + ' words per minute.\n')
    f.close()

def write_avg_ratio_of_category(cur, conn, category):
    lengths_list = select_lengths(cur, conn, category)
    lyrics_list = select_lyrics(cur, conn, category)
    ratios = get_all_ratios(lengths_list, lyrics_list)
    average = average_ratios(ratios)
    write_to_file(average, category)
    return average