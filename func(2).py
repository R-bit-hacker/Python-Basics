def calculate_area(length, width, type="triangle"):
    print("Length= ", length)
    print("Width= ", width)
    print("Type of shape= ",type)

    while type not in ["triangle", "rectangle"]:
        print("Shape not supported, PLease enter again")
        type= input("Only triangle or rectangle: ")

    if type == "triangle":
        area= (1/2)*length*width
        #break
    else:
        area=length*width

    return area
l= float(input("Enter length: "))
w= float(input("Enter width: "))
t=input("Enter type of shape (if dont want to enter then simply type no by default the shape is set to triangle): ")

area_of_shape= calculate_area(l,w,t)
print("Area of shape is= ", area_of_shape)