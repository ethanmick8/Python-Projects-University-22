# Midterm Project: Music Analyzer
# Author: Ethan Mick
# Instructor: Dale Musser
# Description: This program reads and evaluates data from iTunes/music playlist files that are
# formatted like playlist exports. It provides functions that display a variety of statistics regarding 
# the contents of the file.

from collections import Counter
from array import *

# This function creates a 2D array from a passed in file. It expects the file to be encoded as 'utf-16',
# and it strips newlines and separates the elements of each successive "line" by \t characters.
def create_array_from_file(filename):
    with open(filename, 'r', encoding='utf-16') as file:
        array = [line.strip('\n').split('\t') for line in file] # list comp the file into a 2D array
    return array; # return it

# This function takes an array of iTunes playlist data (without headers) and calculates the length of
# the list, which is equivalent to the number of songs in the playlist.
def number_of_songs(array):
    number = len(array)
    print('The number of songs is:', number)
    return

# This function creates a sublist for the 'Year' column of the passed in playlist array. It sorts the
# sublist, and then uses Counter from the 'collections' module to easily create a dict that counts the
# number of songs for each year in the sublist. After that is done, the function just displays the data.
def songs_per_year(array):
    year = [x[16] for x in array]
    year.sort()
    d = Counter(year) # create a dict to count elements from a string with Counter
    n, m = d.keys(), d.values() # assign variables
    print( "The number of songs that were released each year in the playlist:")
    for n, m in d.items(): # print the data
        if (n == ''): # account for empty year case
            n = 'Year not Specified'
        print('   *', n, ':', m) # pretty format
    return

# This function creates a sublist for the 'Time' column in the passed in playlist array. It then converts
# the strings of the sublist to ints, so that the maximum value can then be found. The max value is then
# cross-checked with the list to locate the index value(s) of the found maximum. Once that is located,
# the function then creates sublists for names and artists in the playlist array and prints out the
# values for those sublists at the index value(s) we found.    
def longest_song(array):
    length = [x[11] for x in array]
    for i in range(len(length)):
        if (length[i] == ''): # ignore case of no length (iTunes_Music.txt has this)
            continue
        length[i] = int(length[i])
        # length = [int(i) for i in length] -> see below comment as to why I didn't just write this
    m = 0
    for num in length:
        if (num == ''): 
            continue
        if (num > m):
            m = num
    # m = max(length) -> I would've just wrote this, as well as list comprehension for the for loop
    # earlier, had iTunes_Music.txt not had an empty song length present at some point. I didn't
    # know how else to handle that so I just used an if statement where it was needed.
    h = [i for i, j in enumerate(length) if j == m]
    name = [y[0] for y in array]
    artist = [z[1] for z in array]
    # note: I realize i probably could've done this with a sub-2D array to make it a bit simpler, but
    # i wrote this before i realized that I needed to convert the length list to ints and so what I had
    # tried to write wasn't working
    print('Longest Song(s) - Name and Artist:')
    for i in range(len(h)):
        w = h[i]
        print('   *', name[h[i]], 'by', artist[h[i]], '->', m, 'seconds long')
    return

# (refer to documentation for longest_song() for a similar outline, except this function deals with minimum)
def shortest_song(array):
    length = [x[11] for x in array]
    for i in range(len(length)):
        if (length[i] == ''): # ignore case of no length (iTunes_Music.txt has this)
            continue
        length[i] = int(length[i])
    m = length[0] # start at the beginning
    for num in length:
        if (num == ''): 
            continue
        if (m > num):
            m = num
    h = [i for i, j in enumerate(length) if j == m]
    name = [y[0] for y in array]
    artist = [z[1] for z in array]
    print('Shortest Song(s) - Name and Artist:')
    for i in range(len(h)):
        w = h[i]
        print('   *', name[h[i]], 'by', artist[h[i]], '->', m, 'seconds long')
    return

# This function creates a sublist for the 'genres' column of the passed in array of playlist data, strips it of duplicates,
# and iterates through the array, organizing and printing songs by genre
def genre_stats(array):
    genres_raw = [x[9] for x in array] # get genre strings for every song
    genres = []
    [genres.append(x) for x in genres_raw if x not in genres] # remove duplicates
    current_genre = []
    print("Number of Songs and Longest/Shortest Songs by Genre:")
    # loop through the list of genres, creating a sub-array for each genre that contains all
    # information for each playlist track that is in the current genre
    for genre in genres:
        current_genre = [array[i] for i in range(len(array)) if genre == array[i][9]]
        if(genre == ''): # account for empty genre
            genre = 'No Genre Specified'
        # print out info for the genre array using pre-defined functions
        print('') # spacing between genres
        print(genre, ':')
        number_of_songs(current_genre)
        longest_song(current_genre)
        shortest_song(current_genre)
    return
        
# This function creates a sublist for the 'plays' from the passed in array of playlist data and prints data accordingly
def number_played(array):
    plays = [x[25] for x in array if x[25] != ''] # get elements for 'plays' column for every song, but only if applicable
    total = len(plays)
    print("The number of songs that have been played is", total)
    return

# This function creates a sublist for the 'plays' from the passed in array of playlist data and prints data accordingly
def number_not_played(array):
    plays = [x[25] for x in array if x[25] == ''] # get elements for 'plays' column for every song, but only if applicable
    total = len(plays)
    print("The number of songs that haven't been played is", total)
    return
    # Note: could also just do something like len(array) - number_played(array)

# The main function in this program prompts the user to input an accepted file path for a playlist, and then calls functions
# to calculate and display a variety of statistics regarding the data. After that, it prompts the user if they would like to
# evaluate another file. If so, the while loop reiterates. If not, the program ends. 
def main():
    print("Welcome to the Music Analyzer!\n")
    while(True):
        filename = input("Please enter the path of an Apple Music or iTunes playlist data file: ")
        array = create_array_from_file(filename) # calculate and display data
        array.pop(0) # pop the column headers off the list
        print("\nPlaylist Stats:\n")
        # call functions to print out statstics regarding the user's file
        number_of_songs(array)
        print('')
        songs_per_year(array)
        print('')
        longest_song(array)
        print('')
        shortest_song(array)
        print('')
        genre_stats(array)
        print('')
        number_played(array)
        print('')
        number_not_played(array)
        print('')
        
        another_file = input("Would you like to evaluate another playlist file? ")
        if(another_file != 'y'): # user answered no, end the program
            print("\nThank you and have a nice day!")
            break
        else: # user answered yes, go through another iteration
            continue 

main()


