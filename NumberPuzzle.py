#!/usr/bin/python
# Created by Joao A. Jesus Jr. <joao29a@gmail.com>
#            Joao M. Velasques Faria
import sys
import math
import AStar

class NumberPuzzle(AStar.AStar):
    def distBetween(self,current,neighbor):
        coord = []
        for i in range(len(current)):
            for j in range(len(current[i])):
                if current[i][j] == 0 or neighbor[i][j] == 0:
                    coord.append([i,j])
                if len(coord) == 2:
                    firstPosition = pow(coord[0][0] - coord[1][0],2)
                    secondPosition = pow(coord[0][1] - coord[1][1],2)
                    return math.sqrt(firstPosition + secondPosition)
        return 0

    def firstHeuristic(self,start,goal,i,j):
        if start[i][j] != goal[i][j]:
            self.cost += 1

    def secondHeuristic(self,start,goal,i,j):
        if j + 1 < len(start[i]):
            if start[i][j] != start[i][j+1] - 1:
                self.cost += 1
        elif i + 1 < len(start):
            if start[i][j] != start[i+1][0] - 1:
                self.cost += 1

    def thirdHeuristic(self,start,goal,i,j):
        if start[i][j] != goal[i][j]:
            correctI = None
            correctJ = None
            if start[i][j] == 0:
                correctI = len(start) - 1
                correctJ = len(start[i]) - 1
            else:
                correctI = (start[i][j] - 1) / len(start)
                correctJ = (start[i][j] - 1) % len(start[i])
            self.cost += math.sqrt(pow(correctI - i,2) + pow(correctJ - j,2))

    def heuristicEstimate(self,start,goal):
        self.cost = 0
        for i in range(len(start)):
            for j in range(len(start[i])):
                self.firstHeuristic(start,goal,i,j)
                self.secondHeuristic(start,goal,i,j)
                self.thirdHeuristic(start,goal,i,j)
        return self.cost

    def neighborNodes(self,current):
        for i in range(len(current)):
            for j in range(len(current[i])):
                if current[i][j] == 0:
                    nodes = []
                    if i-1 >= 0:
                        nodes.append(self.makeMove(current,i-1,j,i,j))
                    if i+1 < len(current):
                        nodes.append(self.makeMove(current,i+1,j,i,j))
                    if j-1 >= 0:
                        nodes.append(self.makeMove(current,i,j-1,i,j))
                    if j+1 < len(current[i]):
                        nodes.append(self.makeMove(current,i,j+1,i,j))
                    return nodes
        return []

    def makeMove(self,current,i,j,x,y):
        lst = map(list,current)
        temp = lst[x][y]
        lst[x][y] = lst[i][j]
        lst[i][j] = temp
        return tuple(map(tuple,lst))

    def printPath(self,path):
        for i in path:
            for j in i:
                for k in j:
                    print "%2d" % k,
                print
            print
        print "%d Movements" % (len(path) - 1)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        finalState = ((1,2,3,4),(5,6,7,8),(9,10,11,12),(13,14,15,0))

        puzzle = NumberPuzzle()

        if sys.argv[1] == "1":
            example1 = ((1,6,2,3),(5,10,7,4),(9,14,11,8),(13,0,15,12))
            path = puzzle.aStar(example1,finalState)
        
        elif sys.argv[1] == "2":
            example2 = ((2,0,3,4),(1,6,7,8),(5,9,10,11),(13,14,15,12))
            path = puzzle.aStar(example2,finalState)
        
        elif sys.argv[1] == "3":
            example3 = ((2,6,8,3),(1,14,9,11),(7,12,13,0),(5,15,4,10))
            path = puzzle.aStar(example3,finalState)
        
        elif sys.argv[1] == "re4":
            residentEvil4 = ((2,3,6),(5,0,8),(1,4,7))
            residentEvil4Final = ((1,2,3),(4,5,6),(7,8,0))
            path = puzzle.aStar(residentEvil4,residentEvil4Final)
        
        else:
            print "Invalid arg."
            sys.exit(0)
        
        puzzle.printPath(path)
    
    else:
        print "Insert an arg. (1, 2, 3, or re4)"
