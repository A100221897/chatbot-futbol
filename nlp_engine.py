import re

INTENT_KEYWORDS = {
    "clasificacion": ["tabla", "clasificación", "posicion", "standings"],
    "partidos": ["partido", "juega", "fixture"],
    "goleadores": ["gol", "goleador"],
    "en_vivo": ["vivo", "live", "ahora"]
}

LEAGUE_MAP = {
    "premier": 39,
    "la liga": 140,
    "liga mx": 262,
    "champions": 2
}

TEAM_MAP = {
    "barcelona": 529,
    "real madrid": 541,
    "liverpool": 40,
    "psg": 85,
    "bayern": 157
}


def detect_intent(text):
    text = text.lower()

    for intent, words in INTENT_KEYWORDS.items():
        for w in words:
            if w in text:
                return intent

    return "desconocido"


def detect_league(text):
    text = text.lower()

    for name, id_ in LEAGUE_MAP.items():
        if name in text:
            return id_

    return None


def detect_team(text):
    text = text.lower()

    for name, id_ in TEAM_MAP.items():
        if name in text:
            return id_

    return None