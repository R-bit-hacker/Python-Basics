b=float(input("Enter base= "))
h=float(input("Enter height= "))

def calculate_area(base,height):
    print("Base= ",base)
    print("Height= ",height)
    area=(1/2)*base*height
    return area

area_of_triangle= calculate_area(b,h)
print("Area of triangle= ",area_of_triangle)