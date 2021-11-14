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



pygame.init()

width = 700
height = 400
display = pygame.display.set_mode((width, height))
display.fill(pygame.Color('white'))
balls = []
for i in range(10):
    ball = RandomPointBall(display)
    ball.show()
    balls.append(ball)
pygame.display.flip()

time.sleep(2)


clock = pygame.time.Clock()
red = (255,0, 0)
white = (255, 255, 255)
fontObj = pygame.font.Font('freesansbold.ttf', 20)
stopped_balls = 0

while True:
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            pygame.quit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(balls)):
                pos = pygame.mouse.get_pos()
                if max(pos[0], balls[i].center_x) - min(pos[0], balls[i].center_x) <= balls[i].radius:
                    if max(pos[1], balls[i].center_y) - min(pos[1], balls[i].center_y) <= balls[i].radius and balls[i].check_ball():
                        stopped_balls +=1
                        balls[i].stop()
                        balls.pop(i)
                        textSurfaceObj = fontObj.render('Ваш счет: ' + str(stopped_balls), True, red, white)
                        textRectObj = textSurfaceObj.get_rect()
                        textRectObj.topright = (width, 0)
                        display.blit(textSurfaceObj, textRectObj)
                        break
                

            
    for ball in balls:
        ball.move()
    pygame.display.flip()
    clock.tick(60)
