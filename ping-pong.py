from pygame import*
class GameSprite(sprite.Sprite):
    def __init__(self, sprite_image, sprite_x, sprite_y, sprite_width, sprite_height, sprite_speed):
        super().__init__()
        self.image = transform.scale(image.load(sprite_image), (sprite_width, sprite_height))
        self.speed = sprite_speed

        self.rect = self.image.get_rect()
        self.rect.x = sprite_x
        self.rect.y = sprite_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height-80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height-80:
            self.rect.y += self.speed

back = (51, 153, 102)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)

game = True
finish = False
clock = time.Clock()
FPS = 60

racket1 = Player("racket2.png",0, 200, 50, 100 ,4)
racket2 = Player("racket2.png", 500, 200,  50, 100,4)
ball = GameSprite("tenis-remove.png", 200, 200,  50, 50,2)

font.init()
font = font.Font(None,35)
lose1 = font.render("PLAYER 1 LOSE!", True, (180,0,0))
lose2 = font.render("PLAYER 2 LOSE!", True, (180,0,0))

ball_speed_x = ball.speed
ball_speed_y = ball.speed


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()


        ball.rect.x += ball_speed_x
        ball.rect.y += ball_speed_y

        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            ball_speed_y *= -1

        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            ball_speed_x *= -1

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
            game_over = True

        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2, (200, 200))
            game_over = True


        racket1.reset()
        racket2.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)
