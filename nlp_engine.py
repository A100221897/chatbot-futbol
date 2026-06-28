import spacy

import nltk

from nltk.corpus import stopwords

from nltk.stem import SnowballStemmer






# ==========================================================
# CONFIGURACIÓN NLP
# Procesamiento de lenguaje natural
# ==========================================================



# Descargar palabras vacías en español

nltk.download(
    "stopwords",
    quiet=True
)




# Modelo de lenguaje español spaCy

nlp = spacy.load(
    "es_core_news_sm"
)




# Stopwords y Stemmer

stop_words = set(
    stopwords.words("spanish")
)


stemmer = SnowballStemmer(
    "spanish"
)







# ==========================================================
# INTENCIONES DEL SISTEMA
# Base de conocimiento lingüística
# ==========================================================



INTENT_KEYWORDS = {


    "clasificacion": [

        "tabla",

        "clasificación",

        "clasificacion",

        "posición",

        "posicion",

        "lugar",

        "puesto",

        "standings"

    ],




    "partidos": [

        "partido",

        "partidos",

        "juego",

        "juegos",

        "fixture",

        "próximo",

        "proximo",

        "cuando",

        "cuándo",

        "juega"

    ],





    "goleadores": [

        "goleador",

        "goleadores",

        "gol",

        "goles",

        "scorer",

        "máximo",

        "maximo",

        "anotador"

    ],





    "en_vivo": [

        "vivo",

        "live",

        "ahora",

        "jugando",

        "curso"

    ],





    "equipos": [

        "equipo",

        "equipos",

        "club",

        "teams"

    ]

}








# ==========================================================
# MAPEO DE LIGAS
# Nombre humano → ID API-Football
# ==========================================================



LEAGUE_MAP = {


    "premier": 39,

    "premier league": 39,


    "la liga": 140,

    "liga española": 140,


    "champions": 2,

    "champions league": 2,


    "liga mx": 262,

    "liga mexicana": 262,


    "bundesliga": 78,


    "serie a": 135,


    "ligue 1": 61

}









# ==========================================================
# MAPEO DE EQUIPOS
# Nombre humano → ID API-Football
# ==========================================================



TEAM_MAP = {


    "real madrid": 541,

    "barcelona": 529,


    "manchester city": 50,

    "manchester united": 33,


    "liverpool": 40,


    "arsenal": 42,


    "chelsea": 49,


    "tottenham": 47,


    "juventus": 496,


    "milan": 489,


    "inter": 505,


    "psg": 85,


    "bayern munich": 157,

    "bayern": 157,


    "borussia dortmund": 165,



    # Liga MX

    "america": 1772,

    "américa": 1772,


    "chivas": 1773,


    "tigres": 1403,


    "monterrey": 2282,


    "pumas": 1921,


    "cruz azul": 1771

}








# ==========================================================
# PREPROCESAMIENTO DE TEXTO
# Limpieza y normalización
# ==========================================================



def preprocess(text):


    words = text.lower().split()



    return [

        stemmer.stem(word)

        for word in words

        if word not in stop_words

    ]









# ==========================================================
# DETECCIÓN DE INTENCIÓN
# Motor NLP
# ==========================================================



def detect_intent(text):



    text = text.lower()



    # spaCy

    doc = nlp(text)



    # Lemas

    lemmas = {


        token.lemma_

        for token in doc

    }





    # Stemming

    stems = set(

        preprocess(text)

    )





    # Palabras normales

    words = set(

        text.split()

    )





    # Unión de conocimiento lingüístico

    combined = (

        lemmas |

        stems |

        words

    )






    for intent, keywords in INTENT_KEYWORDS.items():


        for keyword in keywords:



            if keyword in combined:


                return intent






    return "desconocido"










# ==========================================================
# DETECCIÓN DE LIGA
# ==========================================================



def detect_league(text):


    text_lower = text.lower()



    for name, league_id in LEAGUE_MAP.items():


        if name in text_lower:


            return league_id





    # Liga por defecto

    return 39










# ==========================================================
# DETECCIÓN DE EQUIPO
# ==========================================================



def detect_team(text):


    text_lower = text.lower()



    for name, team_id in TEAM_MAP.items():


        if name in text_lower:


            return team_id





    return None
