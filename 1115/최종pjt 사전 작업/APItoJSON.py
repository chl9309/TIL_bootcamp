import requests
import json



URL = 'https://api.themoviedb.org/3/movie/popular?api_key=d6f2a85b7a18b491974d06bcffe4c61c&language=ko-KR&page='
movie_data = []

for i in range(1, 5):

    this_time_URL = URL + str(i)
    # print(this_time_URL)    
    response = requests.get(this_time_URL).json()
    this_movie = (response['results'])
    for j in range(19):
        movie_data.append(this_movie[j])
movie_json = {'movie' : movie_data}

# print(movie_data)
with open('movielist_2', 'w') as f:
    json.dump(movie_json, f)
# print(movie_data)