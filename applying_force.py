import pygame as pyg

#   #   #   #   #   #   #   #   #   #
_ = pyg.init()
scr_size = (500, 500)
fps = 60
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
        self.vx += ax * dt
        self.vy += ay * dt
        self.x += self.vx * dt
        self.y += self.vy * dt

    def drawSubject(self) -> None:  # funkcija za crtanje subjekta
        r = pyg.Rect(self.x, self.y, 5, 5)
        _ = pyg.draw.rect(scr, "white", r)


#   instance subjekata
s1 = Subject(1, round(scr_size[0] / 2), round(scr_size[1] / 2))
s2 = Subject(2, 100, 200)


while run:
    #   #   #   #   #   #   #   #   #
    dt = clk.tick(fps) / 1000.0
    # clk.tick(fps) vraca broj milisekundi izmedju svakog frejma tj vraca frejmtajm u ms, deljenjem sa 1000 se konvertuje u sekunde
    # zatim mnozenje bilokoje operacije koja treba da se odvija u skladu sa vremenom sa dt se ostvaruje to da simulacija ne zavisi od fps

    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            run = False
    #   #   #   #   #   #   #   #   #

    _ = scr.fill((60, 60, 60))
    _ = pyg.draw.circle(
        scr, (100, 0, 0), (round(scr_size[0] / 2), round(scr_size[1] / 2)), 10, 2
    )  # crveni krug na sredini da se zna gde je centar

    #   IZRACUNAVANJE SILE NA OSNOVU POZICIJE KURSORA
    mouse_pos = pyg.mouse.get_pos()
    fx = mouse_pos[0] - scr_size[0] / 2
    fy = mouse_pos[1] - scr_size[1] / 2
    # print(fx, " ", fy)

    s1.applyForce(fx, fy)
    s1.drawSubject()
    s2.applyForce(fx, fy)
    s2.drawSubject()

    print("Stvarni fps:", clk.get_fps())

    pyg.display.flip()  # updajtuje grafiku


pyg.quit()
