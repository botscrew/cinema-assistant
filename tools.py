GET_MOVIES_TOOL =  {
    "type": "function",
    "function": {
        "name": "get_movies",
        "description": "Дістає список фільмів, які зараз йдуть у прокаті в кінотеатрі."
    }
}

GET_MOVIE_SESSIONS_TOOL ={
    "type": "function",
    "function": {
        "name": "get_movie_sessions",
        "description": "Надає список сеансів в кінотеатрі для вибраного фільму. ",
     "parameters": {
    "type": "object",
    "properties": {
        "selected_movie_id": {
            "type": "string",
            "description": "id вибраного користувачем фільму. id потрібно визначити з результату функції get_movies. ",
        }
    },
    "required": ["selected_movie_id"],
    "additionalProperties": False
},
"strict": True
    }

}
