from pygame import *
window = display.set_mode((600,400))
bg = (0,0,255)
window.fill(bg)
display.set_caption("Ping-Pong")
fps = time.Clock()

game = True
while game is True:
    for e in event.get():
        if e.type == QUIT:
            game = False

    fps.tick(60)
    display.update()