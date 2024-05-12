class Location:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    
class Hub (Location):
    def write(self):
        dx = self.x2 - self.x1
        dy = self.y2 - self.y1

        if (abs(dx) > abs(dy)):
            lenght = abs(dx)
            direction = "h"
        else:
            lenght = abs(dy)
            direction = "v"

        dx_init = dx / lenght
        dy_init = dy / lenght

        if (direction == "h"):
            sumb1 = "/"
            sumb2 = "\\"
        else:
            sumb1 = "\\"
            sumb2 = "/"

        for i in range(lenght):
            x = int(self.x1 + i * dx_init)
            y = int(self.y1 + i * dy_init)

            if (i == 0):
                print (" " * x + sumb1)
            if (i == lenght - 1):
                print(" " * x + sumb2)
            else:
                if (direction == "h"):
                    print (" " * x + "|")
                else:
                    print(" " * x + "_")

map = Hub(0, 0, 20, 20)
map.write()