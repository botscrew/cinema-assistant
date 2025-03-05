import os

from dotenv import load_dotenv, find_dotenv
from supabase import create_client, Client

from config import SUPABASE_URL, SUPABASE_KEY

load_dotenv(find_dotenv())

url: str = SUPABASE_URL
key: str = SUPABASE_KEY
supabase: Client = create_client(url, key)

def get_movies():
    response = (
        supabase.table("movies")
        .select("*")
        .execute()
    )
    return response.data

def get_sessions(movie_id):
    response = (supabase.table("movie_sessions")
                .select("*")
                .eq("movie_id", movie_id)
                .execute()
                )
    return response.data



