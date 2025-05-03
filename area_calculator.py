class trapezoid:
    def __init__(shape, a, b, height):
        shape._a = a
        shape._b = b
        shape._height = height

    def area(shape):
        return shape._a+shape._b/2*shape._height
    
t = trapezoid(2,2,2)
print(t. area())
        
