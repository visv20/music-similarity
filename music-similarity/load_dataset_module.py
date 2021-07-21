import csv
import ast
import statistics
from collections import defaultdict

# Only maintaining required column from csv
def load_dataset(data_path): 
    data = []
    needed_columns = {'acousticness', 'artists', 'danceability', 'energy', 'id', 'liveness', 'loudness', 'name', 'popularity', 'speechiness', 'tempo', 'valence'}
    with open(data_path, mode='r',errors='ignore') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            typed_data = dict()
            for k,v in dict(row).items():
                if k in needed_columns:
                    if k == 'artists':
                        typed_data[k] = ast.literal_eval(v)
                    elif k == 'popularity':
                        typed_data[k] = int(v)
                    elif k in ['id','name']:
                        typed_data[k] = str(v)
                    else:
                        typed_data[k] = float(v)
            data.append(typed_data)
    return data

# Creating artist_music dict
def get_artist_music(data):
    ## Artists column contain multiple artist so representing each artist in each column 
    artist_data = []
    for row in data:
        for artist in row['artists']:
            artist_music_data = {k:v for k,v in row.items() if k != 'artists'}
            artist_music_data['artist'] = artist
            artist_data.append(artist_music_data)

    ## Creating unique artist rows
    unique_artist = defaultdict(list)
    for row in artist_data:
        unique_artist[row['artist']].append(row)

    ### Taking median if an artist has multiple music
    artist_music = dict()
    artist_music_columns = {'artist', 'music_names', 'acousticness', 'danceability', 'energy', 'liveness', 'loudness', 'popularity', 'speechiness', 'tempo', 'valence'}
    artist_id = 1
    for artist, features in unique_artist.items():
        artist_music_data = {'artist':artist}
        artist_music_data['music_names'] = [music['name'] for music in features]
        for f in artist_music_columns:
            if f not in artist_music_data.keys():
                artist_music_data[f] = statistics.median([music[f] for music in features])
        artist_music[artist_id] = artist_music_data
        artist_id += 1
    return artist_music

# Creating music_features dict
def get_music_features(data):
    music_features = dict()
    music_features_columns = {'name', 'id', 'artists', 'acousticness', 'danceability', 'energy', 'liveness', 'loudness', 'popularity', 'speechiness', 'tempo', 'valence'}
    music_id = 1
    for row in data:
        music_data = {k:v for k,v in row.items() if k in music_features_columns}
        music_features[music_id] = music_data
        music_id += 1
    return music_features
