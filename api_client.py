import os
import requests
from dotenv import load_dotenv



# ==========================================================
# CONFIGURACIÓN DEL SISTEMA
# Capa de configuración y acceso al conocimiento externo
# ==========================================================


load_dotenv()


# URL base API-Football

BASE_URL = "https://v3.football.api-sports.io"



# API KEY almacenada en archivo .env

API_KEY = os.getenv("API_FOOTBALL_KEY")



# Encabezado requerido por API-Football

HEADERS = {

    "x-apisports-key": API_KEY

}





# ==========================================================
# FUNCIÓN GENERAL DE CONSULTA
# Motor de adquisición de conocimiento
# ==========================================================


def safe_request(endpoint, params=None):

    try:


        response = requests.get(

            f"{BASE_URL}{endpoint}",

            headers=HEADERS,

            params=params

        )


        # Verifica errores HTTP

        response.raise_for_status()



        # Convertimos respuesta a conocimiento estructurado

        data = response.json()



        return data



    except requests.exceptions.RequestException as error:


        print("❌ Error al consultar API-Football")

        print(error)



        return {


            "error": True,

            "message": str(error)

        }





# ==========================================================
# OBTENER TABLA DE POSICIONES
# ==========================================================


def get_standings(league_id, season=2024):


    return safe_request(

        "/standings",

        {

            "league": league_id,

            "season": season

        }

    )







# ==========================================================
# OBTENER PRÓXIMOS PARTIDOS DE UN EQUIPO
# ==========================================================


def get_fixtures_by_team(team_id, next_n=5):


    return safe_request(

        "/fixtures",

        {

            "team": team_id,

            "next": next_n

        }

    )








# ==========================================================
# OBTENER GOLEADORES DE UNA LIGA
# ==========================================================


def get_top_scorers(league_id, season=2024):


    return safe_request(

        "/players/topscorers",

        {

            "league": league_id,

            "season": season

        }

    )








# ==========================================================
# CONSULTAR PARTIDOS EN VIVO
# ==========================================================


def get_live_fixtures():


    return safe_request(

        "/fixtures",

        {

            "live": "all"

        }

    )







# ==========================================================
# PRUEBA DEL SISTEMA
# Validación de adquisición de conocimiento
# ==========================================================


if __name__ == "__main__":



    # Ejemplo:
    # Premier League Inglaterra

    league_id = 39



    print("\n================================")

    print(" TABLA DE POSICIONES ")

    print("================================")



    standings = get_standings(

        league_id

    )


    print(standings)







    print("\n================================")

    print(" PRÓXIMOS PARTIDOS ")

    print("================================")



    fixtures = get_fixtures_by_team(

        team_id=33,

        next_n=5

    )


    print(fixtures)







    print("\n================================")

    print(" GOLEADORES DE LA LIGA ")

    print("================================")



    scorers = get_top_scorers(

        league_id

    )


    print(scorers)







    print("\n================================")

    print(" PARTIDOS EN VIVO ")

    print("================================")



    live = get_live_fixtures()


    print(live)