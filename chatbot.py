from nlp_engine import detect_intent, detect_league, detect_team
from api_client import (
    get_standings,
    get_fixtures_by_team,
    get_top_scorers,
    get_live_fixtures
)
from database import guardar


# =========================
# MEMORIA
# =========================
context = {
    "league": None,
    "team": None
}


# =========================
# ESTILO HUMANO
# =========================
def commentator(text):
    return f"🎙️ Analista deportivo: {text}"


# =========================
# TABLA
# =========================
def analyze_standings(data):
    try:
        response = data.get("response", [])

        if not response:
            return commentator("No hay datos de la tabla en este momento.")

        table = response[0]["league"]["standings"][0]

        top = table[0]
        second = table[1]

        return commentator(
            f"{top['team']['name']} lidera la competencia con {top['points']} puntos, "
            f"pero {second['team']['name']} lo sigue muy de cerca, lo que mantiene la liga muy competitiva."
        )

    except:
        return commentator("No se pudo analizar la tabla en este momento.")


# =========================
# PARTIDOS
# =========================
def analyze_fixtures(data):
    try:
        response = data.get("response", [])

        if not response:
            return commentator("No hay próximos partidos disponibles para este equipo.")

        match = response[0]

        home = match["teams"]["home"]["name"]
        away = match["teams"]["away"]["name"]

        return commentator(
            f"Se viene un partido interesante entre {home} y {away}, "
            f"un encuentro que puede ser clave para ambos equipos."
        )

    except:
        return commentator("No se pudo analizar los partidos en este momento.")
    print(data)


# =========================
# GOLEADORES
# =========================
def analyze_scorers(data):
    try:
        response = data.get("response", [])

        if not response:
            return commentator("No hay datos de goleadores disponibles.")

        player = response[0]

        name = player["player"]["name"]
        goals = player["statistics"][0]["goals"]["total"]

        return commentator(
            f"{name} está teniendo una gran temporada con {goals} goles, "
            f"consolidándose como una de las figuras ofensivas del torneo."
        )

    except:
        return commentator("No se pudieron analizar los goleadores.")


# =========================
# EN VIVO
# =========================
def analyze_live(count):
    if count == 0:
        return commentator("No hay partidos en vivo en este momento.")
    return commentator(f"Tenemos {count} partidos en vivo ahora mismo, la jornada está activa.")


# =========================
# MOTOR PRINCIPAL
# =========================
def respond(message):

    intent = detect_intent(message)
    league = detect_league(message)
    team = detect_team(message)

    # memoria
    if league:
        context["league"] = league
    if team:
        context["team"] = team

    league = context["league"]
    if league is None:
        league = 39
    team = context["team"]

    # =========================
    # DECISIONES
    # =========================

    if intent == "clasificacion":
        data = get_standings(league)
        response = analyze_standings(data)

    elif intent == "partidos":
        if not team:
            response = commentator("Dime un equipo para analizar sus partidos.")
        else:
            data = get_fixtures_by_team(team)
            response = analyze_fixtures(data)

    elif intent == "goleadores":
        data = get_top_scorers(league)
        response = analyze_scorers(data)

    elif intent == "en_vivo":
        data = get_live_fixtures()
        count = len(data.get("response", []))
        response = analyze_live(count)

    else:
        response = commentator(
            "Puedo analizar la tabla de posiciones, los partidos, los goleadores o los partidos en vivo. "
            "Solo dime qué quieres saber."
        )

    guardar(message, response)

    return response