import json
import re
import random_responses


# carga de datos JSON
def load_json(file):
    with open(file) as bot_responses:
        print(f"Base de datos '{file}' cargada con éxito")
        return json.load(bot_responses)


# Almancen de datos JSON
response_data = load_json("bot.json")


def get_response(input_string):
    split_message = re.split(r'\s+|[,;?!.-]\s*', input_string.lower())
    score_list = []

    # comprobar todas las respuestas
    for response in response_data:
        response_score = 0
        required_score = 0
        required_words = response["required_words"]

        # comprueba si hay una pregunta requerida
        if required_words:
            for word in split_message:
                if word in required_words:
                    required_score += 1

        # La cantidad de palabras requeridas debe coincidir con la puntuación requerida
        if required_score == len(required_words):
            # print(required_score == len(required_words))
            # La cantidad de palabras requeridas debe coincidir con la puntuación requerida
            for word in split_message:
                # Si la palabra está en la respuesta, añádala a la puntuación
                if word in response["user_input"]:
                    response_score += 1

        # Añadir puntuación a la lista
        score_list.append(response_score)
        # Depuración: Encontrar la mejor frase
        # print(response_score, response["user_input"])

    # Encuentra la mejor respuesta y la devuelve si no son todas 0
    best_response = max(score_list)
    response_index = score_list.index(best_response)

    # Comprobar si la entrada está vacía
    if input_string == "":
        return "Por favor, escriba algo para que podamos charlar :("

    # Si no hay ninguna respuesta buena, devuelve una aleatoria
    if best_response != 0:
        return response_data[response_index]["bot_response"]

    return random_responses.random_string()


while True:
    user_input = input("You: ")
    print("Bot:", get_response(user_input))