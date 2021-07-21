from load_dataset_module import get_artist_music, get_music_features, load_dataset
from similarity_module import euclidean_similarity,cosine_similarity,jaccard_similarity,manhattan_similarity,pearson_similarity,compute_similarity


data_path = "./data.csv"
data = load_dataset(data_path)
artist_music = get_artist_music(data)
music_features = get_music_features(data)
max_artist_music_id = len(artist_music.keys())
max_music_features_id = len(music_features.keys())
similarity_map = {
    1:cosine_similarity,
    2:euclidean_similarity,
    3:jaccard_similarity,
    4:manhattan_similarity,
    5:pearson_similarity
}
data_map = {
    1:artist_music,
    2:music_features
}

print("Welcome To Similarity Finder")
print("============================")
print("You can find similarity within artist or music.")
print("\nBasic Info")
print("----------")
print(f"Artist index start from 1 and ends at {max_artist_music_id}")
print(f"Music index start from 1 and ends at {max_music_features_id}")
print("\nAvailable Similarity Functions")
print("------------------------------")
for k,v in similarity_map.items():
    print(f"{k}.{v.__name__}")
print("\nAvailable Data")
print("----------------")
print("1.artist_music")
print("1.music_features")
inp = 'y'
while inp not in ['n','no']:
    condition_unmet = True
    while condition_unmet:
        sim_fun = int(input("\nEnter similarity function number:"))
        if sim_fun in similarity_map.keys():
            condition_unmet = False
        else:
            print("Invalid input! Please enter a value from 1-5")
    condition_unmet = True
    while condition_unmet:
        sim_data = int(input("Enter data number:"))
        if sim_data in data_map.keys():
            condition_unmet = False
        else:
            print("Invalid input! Please enter a value 1 or 2")
    id_max = max_artist_music_id if sim_data == 1 else max_music_features_id
    condition_unmet = True
    while condition_unmet:
        id_data1 = int(input("Enter first id:"))
        if id_data1 >= 1 or id_data1 <= id_max:
            condition_unmet = False
        else:
            print(f"Invalid input! Please enter a value from 1 and {id_max}")
    condition_unmet = True
    while condition_unmet:
        id_data2 = int(input("Enter second id:"))
        if id_data2 >= 1 or id_data2 <= id_max:
            condition_unmet = False
        else:
            print(f"Invalid input! Please enter a value from 1 and {id_max}")
    print(f"Similarity: {compute_similarity(similarity_map[sim_fun],data_map[sim_data],id_data1,id_data2)}")
    inp = input("\nDo you want to continue(y/n):")
