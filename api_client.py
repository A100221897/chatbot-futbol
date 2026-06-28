import os
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://v3.football.api-sports.io"
API_KEY = os.getenv("API_FOOTBALL_KEY")
print("API KEY CARGADA:", API_KEY)  # debug

HEADERS = {
    "x-apisports-key": API_KEY
}

def safe_request(endpoint, params=None):
    try:
        r = requests.get(
            f"{BASE_URL}{endpoint}",
            headers=HEADERS,
            params=params,
            timeout=10
        )

        data = r.json()

        # 🔥 DEBUG REAL
        if "errors" in data and data["errors"]:
            print("API ERROR:", data["errors"])

        if "response" not in data:
            return {"response": []}

        return data

    except Exception as e:
        print("REQUEST ERROR:", e)
        return {"response": []}


def get_standings(league_id, season=2024):
    return safe_request("/standings", {
        "league": league_id,
        "season": season
    })


def get_fixtures_by_team(team_id, next_n=5):
    return safe_request("/fixtures", {
        "team": team_id,
        "next": next_n
    })


def get_top_scorers(league_id, season=2024):
    return safe_request("/players/topscorers", {
        "league": league_id,
        "season": season
    })


def get_live_fixtures():
    return safe_request("/fixtures", {
        "live": "all"
    })