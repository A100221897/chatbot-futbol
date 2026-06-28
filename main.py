from chatbot import respond



# ==========================================================
# INICIO DEL SISTEMA
# Chatbot de Fútbol basado en conocimiento
# ==========================================================


print(
    "⚽ Chatbot de Fútbol con IA Basada en Conocimiento\n"
)



print(
    "Escribe 'salir' para finalizar la conversación.\n"
)





# ==========================================================
# MOTOR DE INTERACCIÓN CON EL USUARIO
# ==========================================================


while True:



    # Entrada del usuario

    user_input = input("Tú: ").strip()





    # ======================================================
    # REGLA DE FINALIZACIÓN DEL SISTEMA
    # ======================================================


    if user_input.lower() in [

        "salir",

        "exit",

        "quit"

    ]:


        print(

            "👋 Hasta luego!"

        )


        break






    # ======================================================
    # VALIDACIÓN DE ENTRADA VACÍA
    # ======================================================


    if not user_input:


        continue






    # ======================================================
    # PROCESAMIENTO DEL CONOCIMIENTO
    # chatbot.py
    # ======================================================


    response = respond(

        user_input

    )






    # ======================================================
    # RESPUESTA DEL SISTEMA
    # ======================================================


    print(

        f"\nBot: {response}\n"

    )