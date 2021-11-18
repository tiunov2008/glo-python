import pygame
import random
import time


class Ball:
    def __init__(self, display):
        self.display = display
        self.color = pygame.Color('red')
        self.center_x = 100
        self.center_y = 100
        self.radius = 30

        self.vx = self.get_speed()
        self.vy = self.get_speed()

    def show(self):
        pygame.draw.circle(display, self.color, (self.center_x, self.center_y), self.radius)

    def get_speed(self):
        speed = random.randint(-3, 3)
        while speed == 0:
            speed = random.randint(-3, 3)
        return speed

    def go(self):
        self.center_x += self.vx
        self.center_y += self.vy

    def clear(self):
        pygame.draw.circle(self.display, pygame.Color('white'), (self.center_x, self.center_y), self.radius)

    def move(self):
        self.clear()
        self.go()
        self.show()

    def stop(self):
        self.vx = 0
        self.vy = 0

    def check_ball(self):
        if self.center_x + self.radius >= width or self.center_x - self.radius <= 0 or self.center_y + self.radius >= height or self.center_y - self.radius <= 0:
            return False
        else:
            return True
class RandomPointBall(Ball):
    def __init__(self, display):
        super().__init__(display)
        self.color = pygame.Color('green')

        width, height = display.get_size()

        self.center_x = random.randint(self.radius, width - self.radius)
        self.center_y = random.randint(self.radius, height - self.radius)
class BillayrdBall(Ball):
    def __init__(self, display):
        super().__init__(display)
        self.color = pygame.Color('green')
    def go(self):
        super().go()
        width, height = self.display.get_size()
        if self.center_x <= self.radius:
            self.vx = -self.vx
            walls[0] += 1
        if self.center_x >= width - self.radius:
            self.vx = -self.vx
            walls[1] += 1

        if self.center_y <= self.radius:
            self.vy = -self.vy
            walls[2] += 1


        if self.center_y >= height - self.radius:
            self.vy = -self.vy
            walls[3] += 1


def write_text(wall, id):
    fontObj = pygame.font.Font('freesansbold.ttf', 20)
    textSurfaceObj = fontObj.render(str(wall), True, red, white)
    textRectObj = textSurfaceObj.get_rect()
    if id == 0:
        textRectObj.bottomright = (15, height // 2)
    elif id == 1:
        textRectObj.bottomright = (width, height  // 2)
    elif id == 2:
        textRectObj.bottomright = (width // 2, 20)
    elif id == 3:
        textRectObj.bottomright = (width // 2, height)
    display.blit(textSurfaceObj, textRectObj)


pygame.init()
walls = [0, 0, 0, 0]
width = 700
height = 400
display = pygame.display.set_mode((width, height))
display.fill(pygame.Color('white'))
balls = []
for i in range(5):
    ball = BillayrdBall(display)
    ball.show()
    balls.append(ball)
pygame.display.flip()

time.sleep(2)


clock = pygame.time.Clock()
red = (255,0, 0)
white = (255, 255, 255)

while True:
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            pygame.quit()
            
    for ball in balls:
        ball.move()
    for i in range(len(walls)):
        write_text(walls[i], i)

    pygame.display.flip()
    clock.tick(60)
