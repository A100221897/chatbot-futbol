
RULES={


"clasificacion":
{
"if":
[
"tabla",
"posición",
"clasificación"
],

"then":
"consultar tabla"
},



"partidos":
{
"if":
[
"partido",
"juega",
"fixture"
],

"then":
"consultar partidos"
},



"goleadores":
{
"if":
[
"gol",
"goleador"
],

"then":
"consultar goleadores"
}



}



def get_rule(intent):

    return RULES.get(intent)