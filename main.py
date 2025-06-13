import pygame as pg
from core.vector import Vec3
from core.camera import Camera
from core.geometry import create_cube
from core.utility import project_vertex
def main():
    pg.init()
    screen = pg.display.set_mode((1024,768))
    clock = pg.time.Clock()
    camera = Camera()
    vertices, faces = create_cube()
    
    running = True
    while running:
        screen.fill((10, 10, 10))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        mvp = camera.get_mvp_matrix()
        projected = [project_vertex(v, mvp, 1024, 768) for v in vertices]

        for face in faces:
            for i in range(len(face)):
                p1 = projected[face[i]]
                p2 = projected[face[(i + 1) % len(face)]]
                pg.draw.line(screen, (255, 255, 255), p1, p2, 1)

        pg.display.flip()
        clock.tick(60)
        
    pg.quit()




if __name__ == "__main__":
    main()