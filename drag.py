import pygame as pyg
from numpy.matlib import dtypes
from pygame.color import Color
from pygame.constants import MOUSEBUTTONDOWN

scr_size = (1000, 1000)
fps = 60
RUN = True


class Ball:
    # Inicjalizacija lopte
    def __init__(
        self,
        mass: float = 1,
        x: float = scr_size[0] / 2,
        y: float = scr_size[1] / 2,
        vx: float = 0,
        vy: float = 0,
        drag_coef: float = 1,
    ) -> None:
        self.mass: float = mass
        self.x: float = x
        self.y: float = y
        self.vx: float = vx
        self.vy: float = vy
        self.drag_coef: float = drag_coef

    # Crta grafiku lopte
    def drawBall(self, color=(255, 255, 255), r=10) -> None:
        pyg.draw.circle(scr, color, (self.x, self.y), r)

    # Dejstvo sile
    def applyForce(self, fx: float, fy: float):
        ax = (fx - self.drag_coef * self.vx) / self.mass
        ay = (fy - self.drag_coef * self.vy) / self.mass
        self.vx += ax * dt
        self.vy += ay * dt
        self.x += self.vx * dt
        self.y += self.vy * dt


pyg.init()
scr = pyg.display.set_mode(scr_size)
clk = pyg.time.Clock()

ball = Ball(0.1, 100, 100, 0, 0, 0.1)
forceX: float = 0
forceY: float = 0

while RUN:
    for event in pyg.event.get():
        # Exit condition
        if event.type == pyg.QUIT:
            RUN = False
        # Mouse click
        if event.type == MOUSEBUTTONDOWN:
            pass
        else:
            pass
            # forceX, forceY = 0, 0

    forceX = pyg.mouse.get_pos()[0] - ball.x
    forceY = pyg.mouse.get_pos()[1] - ball.y
    # FPS i Delat time
    clk.tick(fps)
    dt = clk.get_time() / 1000  # dt(s)

    scr.fill("blue")
    ball.applyForce(forceX, forceY)
    ball.drawBall()

    pyg.display.flip()

pyg.quit()
