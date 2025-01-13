from random import choice, randint

class hgrid:
    def __init__(self,height, width, homecount, hospitalcount):
        self.height = height
        self.width = width
        self.grid = [[' ' for i in range(width)] for i in range(width)]
        self.homecount = homecount
        self.homes = set()
        self.hospitalcount = hospitalcount
        self.hospitals = set()

        while len(self.homes) < homecount:
            column = randint(0, width - 1)
            row = randint(0, height - 1)
            if (row, column) in self.homes:
                continue
            self.homes.add((row, column))
            self.grid[row][column] = '⌂'

        while len(self.hospitals) < hospitalcount:
            column = randint(0, width - 1)
            row = randint(0, height - 1)
            if self.grid[row][column] != ' ':
                continue
            self.hospitals.add((row, column))
            self.grid[row][column] = 'H'

    def __getNeighbors(self, point):
        row,column = point[0],point[1]
        neighbors = set()
        for r in range(row-1,row+2):
            for c in range(column-1,column+1):
                if (r,c) != point and 0 <= r < self.height and  0 <= c < self.height and (r,c) not in self.hospitals and (r,c) not in self.homes:
                    neighbors.add((r,c))
        return neighbors
    def __getDist(self,point1, point2):
        return abs(point1[0]-point2[0])+abs(point1[1]-point2[1])
    def printGrid(self):
        print(f"Cost: {self.__getCost(self.hospitals)}")
        for row in self.grid:
            pass
            print(row)
            #print(''.join(row))

    def __getCost(self,hospitals):
        cost = 0
        for h in self.homes:
            cost+=min([self.__getDist(h,hos) for hos in hospitals])
        return cost

    def __updateGrid(self):
        self.grid = [['H' if (r,c) in self.hospitals else "⌂" if (r,c) in self.homes else ' ' for c in range(self.width)] for r in range(self.height)]


    def steepestAscent(self, maxiterations=None):
        while maxiterations is None or (count:=0) < maxiterations:
            count +=1
            best_neighbor = self.hospitals
            best_cost = self.__getCost(self.hospitals)
            for h in self.hospitals:
                neighbors = self.__getNeighbors(h)

                for neighbor in neighbors:
                    newHosp = self.hospitals.copy()
                    newHosp.remove(h)
                    newHosp.add(neighbor)
                    #print(self.hospitals)
                    #print(newHosp)
                    cost = self.__getCost(newHosp)
                    #print(cost)
                    if cost < best_cost:
                        print(f"{cost} is better than {best_cost}")
                        best_neighbor = newHosp
                        best_cost = cost

            if best_neighbor==self.hospitals:
                print("Best found")
                self.printGrid()
                return
            self.hospitals=best_neighbor
            self.__updateGrid()
            self.printGrid()

                

g = hgrid(10,10,10,2)
g.printGrid()
g.steepestAscent(10)