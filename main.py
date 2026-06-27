from chatbot import respond

print("Chatbot de Fútbol — escribe 'salir' para terminar\n")

while True:
    user_input = input("Tú: ").strip()

    if user_input.lower() in ["salir", "exit", "quit"]:
        print("Hasta luego!")
        break

    if not user_input:
        continue

    response = respond(user_input)
    print(f"\nBot: {response}\n")