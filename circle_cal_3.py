import math


def circle_cal():
     area= math.pi *(r**2)
     circumference= 2*math.pi*r
     diameter=2*r
     return area, circumference, diameter
if __name__=="__main__" :
      r=float(input("Enter radius of circle: "))
      a, c, d= circle_cal()
      print(f"Area: {a},\ncircumference: {c},\ndiameter: {d}")    
