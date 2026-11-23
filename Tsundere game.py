import sys
import time
class Character:
    def __init__(self, name):
        self.name = name
        self.points = 0

    def say(self, text, speed=0.04):
        full_text = f"{self.name}: {text}"
        for letter in full_text:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(speed)
        print()
class Scene:
    def __init__(self, speaker, text, choices):
        self.speaker = speaker
        self.text = text
        self.choices = choices

    def play(self):
        print()
        self.speaker.say(self.text)
        for i, choice in enumerate(self.choices, 1):
            print(f"{i}. {choice[0]}")

        answer = int(input("Чё говоришь: ")) - 1
        chosen = self.choices[answer]

        self.speaker.points += chosen[1]
        print(f"[Отношения с {self.speaker.name}: {self.speaker.points}]")
        return chosen[2]
player_name = input("Введи имя: ")
if not player_name.strip():
    player_name = "Тунг Тунг Сахур"
player = Character(player_name)
tsundere = Character("Цундере")
scene_4 = Scene(
    tsundere,
    f"Я тут случайно приготовила слишком много синабонов… Не пропадать же добру! Съешь, пока не остыло, {player.name}. И не вздумай воображать себе лишнего, б-б-бака!",
    [
        ("Мммм синабоны люблю", +15, None),
        ("Я не голоден", -10, None),
        ("Нет (Макс штирнер ларп 333)", -30, None),
    ],
)
scene_3 = Scene(
    tsundere,
    f"Мне надо забрать книги из библиотеки... не поможешь, {player.name}?",
    [
        ("Конечно, проси больше", +15, scene_4),
        ("У меня дела, не могу", -5, scene_4),
        ("Нет, отстань", -15, scene_4),
    ],
)
scene_2 = Scene(
    tsundere,
    f"Вообще-то я тут обедать собиралась... У тебя есть планы, {player.name}?",
    [
        ("Нету, так что с радостью поем", +15, scene_3),
        ("Не могу, занят", +5, scene_3),
        ("Нет (Типо макс штирнер)", -15, scene_3),
    ],
)
scene_1 = Scene(
    tsundere,
    f"Б-б-бака! Что ты здесь делаешь, {player.name}?!",
    [
        ("Мимо шёл", +10, scene_2),
        ("Отстань, цундере", -10, scene_2),
    ],
)
current_scene = scene_1
while current_scene is not None:
    current_scene = current_scene.play()
print("\n" + "=" * 55)
print(f"Итоговые очки отношений с цундере: {tsundere.points}")
if tsundere.points >= 50:
    tsundere.say(f"Ладно, {player.name}... Ты не такой уж и бака.")
    print("Ура, победа!")
elif tsundere.points > 0:
    tsundere.say("Ну, увидимся завтра, наверно.")
    print("Ну ты лох")
else:
    tsundere.say("Хмпф! Глаза бы мои тебя не видели, бака!")
    print("Конец")
input("\nНажмите Enter, чтобы выйти.")
sys.exit()
