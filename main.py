# Импортируем библиотеку pygame
import pygame
from player import *
from blocks import *

# Объявляем переменные
WIN_WIDTH = 800  # Ширина создаваемого окна
WIN_HEIGHT = 640  # Высота
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)  # Группируем ширину и высоту в одну переменную
BACKGROUND_COLOR = "#004400"

# Платформа
PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32
PLATFORM_COLOR = "#FF6262"


def main():
    hero = Player(55, 55)
    up = left = right = False

    entities = pygame.sprite.Group()
    platforms = []
    entities.add(hero)
    level = [
        "-------------------------",
        "-                       -",
        "-                       -",
        "-                       -",
        "-        ------         -",
        "-                       -",
        "--                      -",
        "-                       -",
        "-                   --- -",
        "-                       -",
        "-                       -",
        "-      ---              -",
        "-                       -",
        "-   -----------        --",
        "-                       -",
        "-                -      -",
        "-                   --  -",
        "-                       -",
        "-                       -",
        "-------------------------"]

    pygame.init()  # Инициация PyGame, обязательная строчка
    screen = pygame.display.set_mode(DISPLAY)  # Создаем окошко
    pygame.display.set_caption("Super Mario Boy")  # Пишем в шапку
    bg = Surface((WIN_WIDTH, WIN_HEIGHT))  # Создание видимой поверхности
    # будем использовать как фон
    bg.fill(Color(BACKGROUND_COLOR))  # Заливаем поверхность сплошным цветом

    x = y = 0  # координаты



    for row in level:  # вся строка
        for col in row:  # каждый символ
            if col == "-":
                # создаем блок, заливаем его цветом и рисеум его
                # pf = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
                # pf.fill(Color(PLATFORM_COLOR))
                # screen.blit(pf, (x, y))

                pf = Blocks(x, y)
                entities.add(pf)
                platforms.append(pf)


            x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
        y += PLATFORM_HEIGHT  # то же самое и с высотой
        x = 0  # на каждой новой строчке начинаем с нуля




    x = y = 0  # координаты
    for row in level:  # вся строка
        for col in row:  # каждый символ
            if col == "-":
                # создаем блок, заливаем его цветом и рисеум его
                pf = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
                pf.fill(Color(PLATFORM_COLOR))
                screen.blit(pf, (x, y))

            x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
        y += PLATFORM_HEIGHT  # то же самое и с высотой
        x = 0  # на каждой новой строчке начинаем с нуля




    timer = pygame.time.Clock()
    while 1:  # Основной цикл программы
        timer.tick(60)
        screen.blit(bg, (0, 0))  # Каждую итерацию необходимо всё перерисовывать
        for e in pygame.event.get():  # Обрабатываем события
            if e.type == QUIT:
                raise SystemExit("QUIT")
            if e.type == KEYDOWN and e.key == K_LEFT:
                left = True
            if e.type == KEYUP and e.key == K_LEFT:
                left = False

            if e.type == KEYDOWN and e.key == K_RIGHT:
                right = True
            if e.type == KEYUP and e.key == K_RIGHT:
                right = False

            if e.type == KEYDOWN and e.key == K_UP:
                up = True
            if e.type == KEYUP and e.key == K_UP:
                up = False


        hero.update(left, right, up, platforms)

        entities.draw(screen)
        pygame.display.update()  # обновление и вывод всех изменений на экран




if __name__ == "__main__":
    main()
