class Rectangle(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __str__(self):
        return "Rectangle(%s, %s, %s, %s)" % (self.x, self.y, self.width,
                self.height)

    def __repr__(self):
        return "Rectangle(%s, %s, %s, %s)" % (self.x, self.y, self.width,
                self.height)


def overlap(rectA, rectB):
    
    overlapX = 0
    overlapY = 0
    overlapWidth = 0
    overlapHeight = 0

    # determine the left and right rectangles.
    if rectA.x <= rectB.x:
        leftR = rectA
        rightR = rectB
    else:
        leftR = rectB
        rightR = rectA

    # determine the upper and lower rectangles.
    if rectA.y <= rectB.y:
        upperR = rectA
        lowerR = rectB
    else:
        upperR = rectB
        lowerR = rectA

    # determine the overlap along the x co-ordinate
    if leftR.x +leftR.width <= rightR.x:
        return None
    elif leftR.x +leftR.width >= rightR.x + rightR.width:
        # Full overlap
        overlapWidth = rightR.width
    else:
        overlapWidth = leftR.x + leftR.width - rightR.x


    # determine the overlap along the y co-ordinate
    if upperR.y +upperR.height <= lowerR.y:
        return None
    elif upperR.y +upperR.height >= lowerR.y + lowerR.height:
        # Full overlap
        overlapHeight = lowerR.height
    else:
        overlapHeight = upperR.y + upperR.height - lowerR.y

    overlapX = rightR.x
    overlapY = lowerR.y

    return Rectangle(overlapX, overlapY, overlapWidth, overlapHeight)


if __name__ == "__main__":
    r1 = Rectangle(0, 0, 10, 10)
    r2 = Rectangle(7, 7, 10, 10)
    print(overlap(r1, r2))
    r3 = Rectangle(20, 20, 10, 10)
    print(overlap(r1, r3))
    r4 = Rectangle(4, 4, 1, 1)
    print(overlap(r4, r1))
    r5 = Rectangle(8, 8, 13, 12)
    print(overlap(r5, r1))
