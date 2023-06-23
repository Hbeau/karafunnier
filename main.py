
import os
import lyrics_data
import genius
import spotify
import functools
import config
import csv

def sum(acc,b):
    return acc+b[1]

def word_repartition(words):
    first = words[:5]
    other = words[5:]
    return functools.reduce(sum,first,0)/functools.reduce(sum,other,0)

def diversity(groupped_stat):
    return len(list(filter(lambda x: list(x.values())[0]['sentences']>2,groupped_stat)))/max(list(map(lambda elem: list(elem.values())[0]['count'],groupped_stat)))

def song_analysis(title,artist):
    lyrics = genius.getGeniusLyrics(title,artist)
    music = spotify.music_statistics(title,artist)
    global_stat = lyrics_data.state_global(lyrics)["global"]
    groupped_stat = lyrics_data.stat_by_part(lyrics)
    wpm =global_stat['words']/(music["duration"]/60000)
    print(f"word per minute : {wpm}")
    word_ratio = global_stat['words_distinct']/global_stat['words']
    print(f" word ratio : {word_ratio}")
    print(f" word repartition : {word_repartition(global_stat['vocabulary'])}")
    print(f"diversity :  {diversity(groupped_stat)}")
    print (f"energy {(music['energy'] + music['dancability'])/2}")
    return { 'artist' : artist,
            'title' : title,
            'wpm' : wpm,
            'word_ratio' : word_ratio,
            'diversity' : word_repartition(global_stat['vocabulary']),
            'variety' : diversity(groupped_stat),
            'energy': music['energy'] 
    }

songs = []
with open('input.csv', newline='') as csvfile:

    reader = csv.reader(csvfile, delimiter=';')

    for row in reader:
        songs.append(song_analysis(row[0],row[1]));

isExist = os.path.exists('out')
if not isExist:
    os.mkdir("out")
with open('out/output.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=';')
    spamwriter.writerow(['artist','title''wpm','word_ratio','diversity','variety','energy'])
    for song in songs:
        spamwriter.writerow([song['artist'],song['title'],song['wpm'],song['word_ratio'],song['diversity'],song['variety'],song['energy']])