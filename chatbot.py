from nlp_engine import detect_intent, detect_league, detect_team

from api_client import (
    get_standings,
    get_fixtures_by_team,
    get_top_scorers,
    get_live_fixtures
)

from database import guardar




# ==========================================================
# CONTEXTO DEL SISTEMA
# Memoria temporal del conocimiento adquirido
# ==========================================================


context = {

    "league": None,

    "team": None

}





# ==========================================================
# ESTILO COMENTARISTA DEPORTIVO
# Capa de presentación del conocimiento
# ==========================================================


def commentator(text):

    return f"🎙️ Analista deportivo: {text}"







# ==========================================================
# ANALIZADOR DE TABLA DE POSICIONES
# ==========================================================


def analyze_standings(data):

    try:


        response = data.get("response", [])



        if not response:

            return commentator(
                "No hay datos de la tabla en este momento."
            )



        standings = response[0]["league"]["standings"][0]



        result = "Tabla de posiciones:\n\n"



        for team in standings[:5]:


            result += (

                f"{team['rank']}. "

                f"{team['team']['name']} "

                f"— {team['points']} pts\n"

            )



        top = standings[0]

        second = standings[1]



        result += (

            f"\nAnálisis: "

            f"{top['team']['name']} lidera la liga "

            f"con {top['points']} puntos, "

            f"seguido por {second['team']['name']}."

        )



        return commentator(result)



    except Exception:


        return commentator(
            "No se pudo analizar la tabla."
        )








# ==========================================================
# ANALIZADOR DE PARTIDOS
# ==========================================================


def analyze_fixtures(data):

    try:


        fixtures = data.get("response", [])



        if not fixtures:


            return commentator(

                "No encontré próximos partidos para ese equipo."

            )



        result = "Próximos partidos:\n\n"



        for match in fixtures[:3]:


            home = match["teams"]["home"]["name"]

            away = match["teams"]["away"]["name"]


            date = match["fixture"]["date"][:10]



            result += (

                f"{home} vs {away}"

                f" — {date}\n"

            )



        first = fixtures[0]


        return commentator(

            result +

            "\nEl próximo encuentro promete intensidad."

        )



    except Exception:


        return commentator(

            "No se pudieron analizar los partidos."

        )








# ==========================================================
# ANALIZADOR DE GOLEADORES
# ==========================================================


def analyze_scorers(data):

    try:


        scorers = data.get("response", [])



        if not scorers:


            return commentator(

                "No hay goleadores disponibles."

            )



        result = "Top goleadores:\n\n"



        for scorer in scorers[:5]:


            name = scorer["player"]["name"]


            goals = scorer["statistics"][0]["goals"]["total"]



            result += (

                f"{name} "

                f"— {goals} goles\n"

            )



        player = scorers[0]



        return commentator(

            result +

            f"\nJugador destacado: "

            f"{player['player']['name']}"

        )



    except Exception:


        return commentator(

            "No se pudieron analizar los goleadores."

        )








# ==========================================================
# ANALIZADOR PARTIDOS EN VIVO
# ==========================================================


def analyze_live(count):


    if count == 0:


        return commentator(

            "No hay partidos en vivo en este momento."

        )



    return commentator(

        f"Hay {count} partidos en vivo ahora mismo."

    )









# ==========================================================
# MOTOR PRINCIPAL DE INFERENCIA
# Entrada → Procesamiento → Respuesta → Aprendizaje
# ==========================================================


def respond(message):



    # Detectar intención del usuario

    intent = detect_intent(message)



    # Obtener entidades

    league = detect_league(message)

    team = detect_team(message)





    # Actualización del conocimiento temporal


    if league:

        context["league"] = league



    if team:

        context["team"] = team






    # Valores por defecto


    league = context["league"] or 39

    team = context["team"]







    # ======================================================
    # REGLAS DEL SISTEMA
    # ======================================================


    if intent == "clasificacion":



        data = get_standings(

            league

        )



        response = analyze_standings(

            data

        )







    elif intent == "partidos":



        if not team:



            response = commentator(

                "Dime un equipo para analizar sus partidos."

            )



        else:



            data = get_fixtures_by_team(

                team

            )



            response = analyze_fixtures(

                data

            )








    elif intent == "goleadores":




        ligas_validas = [


            "premier",

            "premier league",

            "la liga",

            "liga española",

            "champions",

            "champions league",

            "liga mx",

            "liga mexicana",

            "bundesliga",

            "serie a",

            "ligue 1"


        ]





        if not any(

            liga in message.lower()

            for liga in ligas_validas

        ):



            response = commentator(

                "Para consultar goleadores necesito que indiques una liga."

            )



        else:



            data = get_top_scorers(

                league

            )



            response = analyze_scorers(

                data

            )








    elif intent == "en_vivo":



        data = get_live_fixtures()



        count = len(

            data.get("response", [])

        )



        response = analyze_live(

            count

        )








    else:



        response = commentator(

            """

No entendí tu pregunta.

Puedo analizar:

- Tabla de posiciones
- Próximos partidos
- Goleadores
- Partidos en vivo

Ejemplos:

"Tabla de la Premier"

"Cuándo juega Barcelona"

"Goleadores de Champions"

"Hay partidos en vivo"

"""

        )







    # Guardar interacción

    guardar(

        message,

        response

    )



    return response