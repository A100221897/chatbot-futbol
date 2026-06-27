import os
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://v3.football.api-sports.io"
API_KEY = os.getenv("API_FOOTBALL_KEY")

HEADERS = {
    "x-apisports-key": API_KEY
}

def get_standings(league_id, season=2024):
    response = requests.get(
        f"{BASE_URL}/standings",
        headers=HEADERS,
        params={"league": league_id, "season": season}
    )
    return response.json()

def get_fixtures_by_team(team_id, next_n=5):
    response = requests.get(
        f"{BASE_URL}/fixtures",
        headers=HEADERS,
        params={"team": team_id, "next": next_n}
    )
    return response.json()

def get_top_scorers(league_id, season=2024):
    response = requests.get(
        f"{BASE_URL}/players/topscorers",
        headers=HEADERS,
        params={"league": league_id, "season": season}
    )
    return response.json()

def get_live_fixtures():
    response = requests.get(
        f"{BASE_URL}/fixtures",
        headers=HEADERS,
        params={"live": "all"}
    )
    return response.json()