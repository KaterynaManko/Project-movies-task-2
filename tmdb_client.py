import requests

api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlMzcxZGM0ZjZkMDA4YmFiMTM4MmNhMWE1ODhjMWI0MyIsInN1YiI6IjYzZTYzODUzOTUxMmUxMDBiMmIxOTllZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.BEVaEkce1RDyzmj0xLjSDknXU-qJqPVs_MlR-e0Gb4g"
def get_movies_list(list_type):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    try:
        response = requests.get(endpoint, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
     response = requests.get("https://api.themoviedb.org/3/movie/popular", headers=headers)
     response.raise_for_status()
     return response.json()
    

def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"

def get_movies(how_many, list_type):
    data = get_movies_list(list_type)
    return data["results"][:how_many]

def get_movie_info(list_type):
    data = get_movies_list(list_type)
    for movie in data['results']:
     dict = {'title': movie['title'], 'poster_path': movie['poster_path'], 'id': movie['id']}
     return dict

def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_poster_url_movie(backdrop_path, size="w780"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{backdrop_path}"

def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()["cast"]

def get_poster_url_actor(profile_path, size="w185"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{profile_path}"

def get_actors(movie_id, how_many):
    actors_list = get_single_movie_cast(movie_id)
    return actors_list[:how_many]

def search(search_query):
   base_url = "https://api.themoviedb.org/3/"
   headers = {
       "Authorization": f"Bearer {api_token}"
   }
   endpoint = f"{base_url}search/movie?query={search_query}"

   response = requests.get(endpoint, headers=headers)
   return response.json()['results']
   
def get_airing_today():
    endpoint = f"https://api.themoviedb.org/3/tv/airing_today"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()['results']