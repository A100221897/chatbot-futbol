import os
import requests
from dotenv import load_dotenv

load_dotenv()

# URL base de la API-Football
BASE_URL = "https://v3.football.api-sports.io"

# en el archivo .env esta la contra
API_KEY = os.getenv("API_FOOTBALL_KEY")

#Encabezados necesarios para autenticar las peticiones
#segun la documentacion de la API-Football
HEADERS = {
    "x-apisports-key": API_KEY
}

#Obtenemos la tabla de posiciones de una liga especifica
def get_standings(league_id, season=2024):
    response = requests.get(
        f"{BASE_URL}/standings",
        headers=HEADERS,
        params={"league": league_id, "season": season}
    )
    return response.json()

#Obtenemos los próximos partidos de un equipo especifico
def get_fixtures_by_team(team_id, next_n=5):
    response = requests.get(
        f"{BASE_URL}/fixtures",
        headers=HEADERS,
        params={"team": team_id, "next": next_n}
    )
    return response.json()

#obtenemos los goleadores de una liga especifica
def get_top_scorers(league_id, season=2024):
    response = requests.get(
        f"{BASE_URL}/players/topscorers",
        headers=HEADERS,
        params={"league": league_id, "season": season}
    )
    return response.json()

#podemos consultar los partidos en vivo de todas las ligas (si hubiera)
def get_live_fixtures():
    response = requests.get(
        f"{BASE_URL}/fixtures",
        headers=HEADERS,
        params={"live": "all"}
    )
    return response.json()