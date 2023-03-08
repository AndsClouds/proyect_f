import random


def random_string():
    random_list = [
        "Por favor, intenta escribir algo más descriptivo.",
        "Oh! Parece que escribiste algo que todavía no entiendo",
        "¿Le importaría intentar reformularlo?",
        "Lo seinto mucho, no lo he entendido bien.",
        "Todavía no puedo responder, por favor, intente preguntar otra cosa."
    ]

    list_count = len(random_list)
    random_item = random.randrange(list_count)

    return random_list[random_item]