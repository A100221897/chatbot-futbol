import spacy
import nltk
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer

nltk.download("stopwords", quiet=True)

nlp = spacy.load("es_core_news_sm")

stop_words = set(stopwords.words("spanish"))
stemmer = SnowballStemmer("spanish")

INTENT_KEYWORDS = {
    "clasificacion": [
        "tabla", "clasificación", "clasificacion", "posición",
        "posicion", "lugar", "puesto", "standings"
    ],
    "partidos": [
        "partido", "partidos", "juego", "juegos", "fixture",
        "próximo", "proximo", "cuándo", "cuando", "juega"
    ],
    "goleadores": [
        "goleador", "goleadores", "gol", "goles",
        "scorer", "máximo", "maximo", "anotador"
    ],
    "en_vivo": [
        "vivo", "ahora", "live", "jugando", "curso"
    ],
    "equipos": [
        "equipo", "equipos", "club", "teams"
    ],
}

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
    "ligue 1": 61,
}

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
    "borussia dortmund": 165,
    "america": 1772,
    "chivas": 1773,
    "tigres": 1403,
    "monterrey": 2282,
    "pumas": 1921,
    "cruz azul": 1771
}

def preprocess(text):
    words = text.lower().split()
    return [stemmer.stem(w) for w in words if w not in stop_words]

def detect_intent(text):
    doc = nlp(text.lower())

    lemmas = {token.lemma_ for token in doc}
    stems = set(preprocess(text))
    words = set(text.lower().split())

    combined = lemmas | stems | words

    for intent, keywords in INTENT_KEYWORDS.items():
        for keyword in keywords:
            if keyword in combined:
                return intent

    return "desconocido"

def detect_league(text):
    text_lower = text.lower()

    for name, league_id in LEAGUE_MAP.items():
        if name in text_lower:
            return league_id

    return 39

def detect_team(text):
    text_lower = text.lower()

    for name, team_id in TEAM_MAP.items():
        if name in text_lower:
            return team_id

    return None