import random
from pygame import *

init()


class Sprite:
    def __init__(self, img, x, y, width, height):
        self.image = transform.scale(image.load(img), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def draw_rect(self):
        draw.rect(window, (255, 0, 0,), self.rect, 3)


size = 600, 800
window = display.set_mode(size)
clock = time.Clock()

font1 = font.Font(None, 50)

start_platforms = [(250, 750), (50, 550), (450, 550), (250, 350), (50, 100), (450, 100)]
platforms = list()
for x, y in start_platforms:
    platform = Sprite('platform.png', x, y, 120, 30)
    platforms.append(platform)

player = Sprite('player.png', 280, 600, 80, 90)
is_jump = False
jump_velocity = 0
gravity = 0.5
jump_height = 15
score = 0
high_score = 0
finish = False
while True:
    for e in event.get():
        if e.type == QUIT:
            quit()
        if e.type == KEYDOWN:
            if e.key == K_SPACE and finish:
                finish = False
                score = 0
                start_platforms = [(250, 750), (50, 550), (450, 550), (250, 350), (50, 100), (450, 100)]
                platforms = list()
                for x, y in start_platforms:
                    platform = Sprite('platform.png', x, y, 120, 30)
                    platforms.append(platform)
                player = Sprite('player.png', 280, 600, 80, 90)

    window.fill((255, 255, 255))
    if not finish:
        for platform in platforms:
            platform.reset()
            #platform.draw_rect()
            if player.rect.colliderect(platform.rect) and jump_velocity > 0 and player.rect.y - player.rect.height <= player.rect.y:
                is_jump = False
                jump_velocity = -jump_height
            if player.rect.y <= 300:
                platform.rect.y += 10
                if platform.rect.top > 800:
                    platform.rect.y = random.randint(-200, -20)
                    platform.rect.x = random.randint(0, 480)
                    score += 3
                    if score > high_score:
                        high_score = score

        if not is_jump:
            player.rect.y += jump_velocity
            jump_velocity += gravity

        if player.rect.y <= 200:
            is_jump = False

        keys = key.get_pressed()
        if keys[K_d]:
            player.rect.x += 6
        if keys[K_a]:
            player.rect.x -= 6
        if player.rect.y >= 800:
            finish = True

        score_text = font1.render(f'Рахунок {score}', True, (0, 0, 0))
        window.blit(score_text, (400, 20))

        player.reset()
        #player.draw_rect()

    if finish:
        score_text = font1.render(f'Рахунок {score}', True, (0, 0, 0))
        window.blit(score_text, (220, 200))
        high_score_text = font1.render(f'Найкращий результат {high_score}', True, (0, 0, 0))
        window.blit(high_score_text, (130, 250))
        text = font1.render('Тисни пробіл для рестарту', True, (0, 0, 0))
        window.blit(text, (100, 400))

    display.update()
    clock.tick(60)
