from circle import *
from time import sleep
class Shaded(Circle):
    def __init__(self, screen, center_x, center_y, radius,smallest_radius, color='BLUE', background_color="WHITE"):
        super().__init__(screen, center_x, center_y, radius, color, background_color)
        self.smallest =smallest_radius
        self.list =["blue", "green", "red", "white", "blue"]

    def draw(self):
        z =0
        val =super().get_radius()
        for i in range(val, self.smallest, -10):
            if z>4:
                z =0
            py.draw.circle(self.screen, self.list[z], super().get_center(), i)
            z +=1

            
            sleep(2)
            py.display.update()
def main():
    
    screen = py.display.set_mode((800, 600))
    screen.fill('white')
    py.display.update()
    #line = Line(screen, 100, 100, 200, 200)
    s = Shaded(screen, 450, 250, 50, 0)
    s.draw()



main()