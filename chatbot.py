from nlp_engine import detect_intent, detect_league, detect_team
from api_client import (
    get_standings,
    get_fixtures_by_team,
    get_top_scorers,
    get_live_fixtures
)

def format_standings(data):
    try:
        standings = data["response"][0]["league"]["standings"][0]

        result = "Tabla de posiciones:\n"

        for team in standings[:5]:
            result += f"{team['rank']}. {team['team']['name']} — {team['points']} pts\n"

        return result

    except Exception:
        return "No pude obtener la tabla de posiciones."

def format_fixtures(data):
    try:
        fixtures = data["response"][:3]

        if not fixtures:
            return "No encontré próximos partidos para ese equipo."

        result = "Próximos partidos:\n"

        for match in fixtures:
            home = match["teams"]["home"]["name"]
            away = match["teams"]["away"]["name"]
            date = match["fixture"]["date"][:10]

            result += f"{home} vs {away} — {date}\n"

        return result

    except Exception:
        return "No pude obtener los próximos partidos."

def format_top_scorers(data):
    try:
        scorers = data["response"][:5]

        if not scorers:
            return "No encontré goleadores para esa liga."

        result = "Top goleadores:\n"

        for scorer in scorers:
            name = scorer["player"]["name"]
            goals = scorer["statistics"][0]["goals"]["total"]

            result += f"{name} — {goals} goles\n"

        return result

    except Exception:
        return "No pude obtener la lista de goleadores."

def respond(user_input):
    intent = detect_intent(user_input)
    league_id = detect_league(user_input)
    team_id = detect_team(user_input)

    if intent == "clasificacion":
        data = get_standings(league_id)
        return format_standings(data)

    elif intent == "partidos" and team_id:
        data = get_fixtures_by_team(team_id)
        return format_fixtures(data)

    elif intent == "goleadores":
        ligas = [
            "premier", "premier league", "la liga", "liga española",
            "champions", "champions league", "liga mx", "liga mexicana",
            "bundesliga", "serie a", "ligue 1"
        ]

        if not any(liga in user_input.lower() for liga in ligas):
            return "Para consultar goleadores necesito que indiques una liga."

        data = get_top_scorers(league_id)
        return format_top_scorers(data)

    elif intent == "en_vivo":
        data = get_live_fixtures()
        count = len(data.get("response", []))
        return f"Hay {count} partidos en vivo ahora mismo."

    else:
        return """No entendí tu pregunta.
Puedes preguntarme sobre:
- Tabla de posiciones: tabla de la Premier
- Próximos partidos: cuándo juega el Barcelona
- Goleadores: goleadores de la Champions
- Partidos en vivo: hay partidos en vivo"""