from knowledge_base import get_rule



def infer(intent):

    rule=get_rule(intent)


    if rule:

        return rule["then"]


    return "No existe regla"