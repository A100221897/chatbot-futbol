from chatbot import respond

print("⚽ Chatbot de Fútbol con IA Basada en Conocimiento\n")

while True:
    user_input = input("Tú: ").strip()

    if user_input.lower() in ["salir", "exit", "quit"]:
        print("👋 Hasta luego!")
        break

    if not user_input:
        continue

    response = respond(user_input)
    print(f"\nBot: {response}\n")