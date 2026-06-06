import pygame as pyg

pyg.init()

scr_size = (500, 1000)
fps = 60

scr = pyg.display.set_mode(scr_size)
clk = pyg.time.Clock()
run = True


circ_pos = [0, 0]
v_x = 0
v_y = 15
a = 1
prigusenje = 1


while run:
    clk.tick(fps)

    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            run = False

    scr.fill("WHITE")

    circ_pos[1] += v_x
    circ_pos[0] += v_y

    if circ_pos[1] + v_x > scr_size[1]:
        circ_pos[1] = scr_size[1]
        v_x = -v_x + prigusenje
    else:
        v_x += a

    if (circ_pos[0] >= scr_size[0]) | (circ_pos[0] <= 0):
        v_y = -v_y

    circ = pyg.draw.circle(scr, "BLACK", circ_pos, 10)

    pyg.display.flip()

pyg.quit()
