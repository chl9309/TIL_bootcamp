import json
import csv

with open("./movie_genre_list.json", 'r', encoding='utf8') as f:
    data = json.load(f)

fname = "moviedata.csv"

with open(fname, "w", newline='', encoding='utf-8') as f:
    csv_file = csv.writer(f)
    csv_file.writerow(["adult", "backdrop_path", "genre_ids", "id", "original_language", "original_title", "overview", "popularity", "poster_path", "release_date", "title", "video", "vote_average", "vote_count"])
    for item in data["movie"]:
        csv_file.writerow([item.get("adult", ""), item.get("backdrop_path", ""), item.get("genre_ids",""),
        item.get("id",""), item.get("original_language",""), item.get("original_title",""), item.get("overview",""),
        item.get("popularity",""), item.get("poster_path",""), item.get("release_date",""), item.get("title",""), item.get("video",""), item.get("vote_average",""), item.get("vote_count","")])
