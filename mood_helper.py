import random

challenges = {
    "happy": ["Придумай назву для своєї гри", "Напиши 3 речі, які сьогодні вдалися"],
    "tired": ["Зроби перерву на 5 хвилин", "Намалюй простий план свого дня"],
    "bored": ["Придумай нове правило для улюбленої гри", "Зміни щось маленьке у своїй кімнаті"],
}

study_challenges = [
    "Повторити 3 нові Python-команди",
    "Пояснити другу, що таке змінна",
    "Знайти одну помилку в маленькому коді",
    "Написати 3 рядки коду з print()"
]

default_challenges = ["Випий води", "Запиши одну маленьку ціль на сьогодні"]

def choose_challenge(mood, energy, mode):
    if mode == "study":
        challenge = random.choice(study_challenges)

    elif mood == "happy":
        challenge = random.choice(challenges["happy"])
    elif mood == "tired":
        challenge = random.choice(challenges["tired"])
    elif mood == "bored":
        challenge = random.choice(challenges["bored"])
    else:
        challenge = random.choice(default_challenges)

    if energy > 7:
        challenge = challenge + " і зроби це просто зараз!"

    return challenge

def calculate_points(energy, mode):
    #Базово кожен користувач отримує 5 балів
    score = 5

    #Якщо енергія менша за 1 або більша за 10, повернути 0
    if energy < 1 or energy > 10:
        return 0
    #Якщо енергія від 7 до 10, додати 3 бал
    if 7 <= energy and energy <= 10:
        score += 3
    #якщо енергія від 1 до 3, додати 1 бал
    elif 1 <= energy and energy <= 3:
        score += 1

    #Якщо режим study, додати ще 2 бали
    if mode == "study":
        score += 2

    return score

print("=== Генератор міні-челенджів ===")
name = input("Як тебе звати? ")
mood = input("Який у тебе настрій? happy / tired / bored: ")
energy = int(input("Скільки в тебе енергії від 1 до 10? "))
mode = input("Обери режим fun або study: ")

challenge = choose_challenge(mood, energy, mode)
points = calculate_points(energy, mode)

print()
print(f"{name}, твій челендж:")
print(challenge)
print(f"Бали за виконання: {points}")