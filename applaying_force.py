import pygame as pyg

#   #   #   #   #   #   #   #   #   #
_ = pyg.init()
scr_size = (500, 500)
fps = 30
scr = pyg.display.set_mode(
    scr_size
)  # napravi objekat scr koji predstavlja ekran na kojem se crta
clk = pyg.time.Clock()  # napravi objekat clk koji predstavlja vreme tj clokc
run = True
#   #   #   #   #   #   #   #   #   #


class Subject:  # klasa objekat na kojeg deluje sila
    def __init__(
        self, m: int = 1, x: float = 0, y: float = 0, vx: float = 0, vy: float = 0
    ) -> None:
        self.m: int = m  # masa
        self.x: float = x  # x koordinata pozicije
        self.y: float = y  # y koordinata pozicije
        self.vx: float = vx  # x koord brzine
        self.vy: float = vy  # y koord brzine

    def applyForce(
        self, fx: float = 0, fy: float = 0
    ) -> None:  # funkcija nad subjektom koja izracunava poziciju na osnovu sile koje deluje na subjekat
        ax = fx / self.m
        ay = fy / self.m
        self.vx += ax
        self.vy += ay
        self.x += self.vx
        self.y += self.vy

    def drawSubject(self) -> None:  # funkcija za crtanje subjekta
        r = pyg.Rect(self.x, self.y, 5, 5)
        _ = pyg.draw.rect(scr, "white", r)


#   instance subjekata
s1 = Subject(1, round(scr_size[0] / 2), round(scr_size[1] / 2))
s2 = Subject(2, 100, 200)


while run:
    #   #   #   #   #   #   #   #   #
    _ = clk.tick(fps)
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            run = False
    #   #   #   #   #   #   #   #   #

    _ = scr.fill("black")
    _ = pyg.draw.circle(
        scr, (100, 0, 0), (round(scr_size[0] / 2), round(scr_size[1] / 2)), 10
    )  # crveni krug na sredini da se zna gde je centar

    #   IZRACUNAVANJE SILE NA OSNOVU POZICIJE KURSORA
    mouse_pos = pyg.mouse.get_pos()
    fx = (mouse_pos[0] - scr_size[0] / 2) / 5000
    fy = (mouse_pos[1] - scr_size[1] / 2) / 5000
    # print(fx, " ", fy)

    s1.applyForce(fx, fy)
    s1.drawSubject()
    s2.applyForce(fx, fy)
    s2.drawSubject()

    pyg.display.flip()  # updajtuje grafiku


pyg.quit()
