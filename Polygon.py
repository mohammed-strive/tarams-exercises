from abc import ABC, abstractmethod

class GeometricalShape(ABC):
    def __init__(self, spec={}):
        self.spec = spec

    @abstractmethod
    def getPerimeter(self):
        pass

class Polygon(GeometricalShape):
    def __init__(self, spec):
        assert spec.get('noSides')
        assert spec.get('sides')
        assert type(spec.get('sides')) == list
        assert (len(spec.get('sides')) == 1 or
                len(spec.get('sides')) == spec.get('noSides'))
        self.spec = spec
        super().__init__(spec)

    def getPerimeter(self):
        # If the sides is only 1 then we assume its an
        # equilateral polygon.
        if len(self.spec['sides']) == 1:
            return self.spec['sides'][0] * self.spec['noSides']
        else:
            return sum(self.spec['sides'])


class Circle(GeometricalShape):
    def __init__(self, spec):
        assert spec.get('radius')
        self.spec = spec
        super().__init__(spec)

    def getPerimeter(self):
        import math
        return 2 * math.pi * self.spec['radius']

class Cylinder(GeometricalShape):
    def __init__(self, spec):
        assert spec.get('radius')
        assert spec.get('height')
        self.spec = spec

    def getPerimeter(self):
        import math
        return 2 * (2 * math.pi * self.spec['radius'] + self.spec['height'])

if __name__ == '__main__':
    triangle = Polygon({'noSides': 3, 'sides': [2, 4, 6]})
    print(triangle.getPerimeter())
    rectangle = Polygon({'noSides': 4, 'sides': [5]})
    print(rectangle.getPerimeter())
    octagon = Polygon({'noSides':8, 'sides': [4, 5, 6, 7, 8, 3, 4, 5]})
    print(octagon.getPerimeter())
