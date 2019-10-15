from graphics import *

def main():
    win = GraphWin()
    rect = Rectangle(Point(85,60), Point(115, 140))
    rect.setFill('white')
    rect.setOutline('black')
    circ1=(Point(100, 75), 20)
    circ1.setFill('red')
    circ1.setOutline('black')
    circ1.draw(win)
    circ2=(Point(100,100), 20)
    circ2.setFill('yellow')
    circ2.setOutline('black')
    circ2.draw(win)
    circ3=(Point(100, 125), 20)
    circ3.setFill('green')
    circ3.setOutline('black')
    circ3.draw(win)

main()
