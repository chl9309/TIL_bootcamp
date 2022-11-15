import json


with open('movielist_2', 'r', encoding='utf-8') as f:
    movie_data = json.load(f)

# for i in range(500):
#     print(movie_data['movie'][i]['original_title'])

for j in range(len(movie_data['movie'])):

    for k in range(len(movie_data['movie'][j]['genre_ids'])):
        genre = movie_data['movie'][j]['genre_ids'][k]

        if genre == 28:
            movie_data['movie'][j]['genre_ids'][k] = '액션'
        elif genre == 12:
            movie_data['movie'][j]['genre_ids'][k] = '모험'
        elif genre == 16:
            movie_data['movie'][j]['genre_ids'][k] = '애니메이션'
        elif genre == 35:
            movie_data['movie'][j]['genre_ids'][k] = '코미디'
        elif genre == 80:
            movie_data['movie'][j]['genre_ids'][k] = '범죄'
        elif genre == 99:
            movie_data['movie'][j]['genre_ids'][k] = '다큐멘터리'
        elif genre == 18:
            movie_data['movie'][j]['genre_ids'][k] = '드라마'
        elif genre == 10751:
            movie_data['movie'][j]['genre_ids'][k] = '가족'
        elif genre == 14:
            movie_data['movie'][j]['genre_ids'][k] = '판타지'
        elif genre == 36:
            movie_data['movie'][j]['genre_ids'][k] = '역사'
        elif genre == 27:
            movie_data['movie'][j]['genre_ids'][k] = '공포'
        elif genre == 10402:
            movie_data['movie'][j]['genre_ids'][k] = '음악'
        elif genre == 9648:
            movie_data['movie'][j]['genre_ids'][k] = '미스터리'
        elif genre == 10749:
            movie_data['movie'][j]['genre_ids'][k] = '로맨스'
        elif genre == 878:
            movie_data['movie'][j]['genre_ids'][k] = 'SF'
        elif genre == 10770:
            movie_data['movie'][j]['genre_ids'][k] = 'TV영화'
        elif genre == 53:
            movie_data['movie'][j]['genre_ids'][k] = '스릴러'
        elif genre == 10752:
            movie_data['movie'][j]['genre_ids'][k] = '전쟁'
        elif genre == 37:
            movie_data['movie'][j]['genre_ids'][k] = '서부'
        


with open('movie_genre_list', 'w', encoding='utf-8') as f:
    json.dump(movie_data, f, indent="\t", ensure_ascii=False)
