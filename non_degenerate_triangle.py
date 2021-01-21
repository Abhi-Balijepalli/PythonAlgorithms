# Author: Abhi Balijepalli 
# Non-degenerate triangle − it is a triangle that has a positive area. 
# The condition for a non-degenerate triangle with sides a, b, c is −
    # |a| + |b| > |c|
    # |a| + |c| > |b|
    # |b| + |c| > |a|
# given 3 points a(x1,y1), b(x2,y2), c(x3,y3) and two points p(xp,xy) and q(xq,xy)
    # If the triangle is not non-degenerate [Return 0]
    # If point p is in the triangle and not q [Return 1]
    # If point q is in the triangle and not p [Return 2]
    # If p and q are in the triangle [Return 3]
    # If p and q are NOT in the triangle [Return 4]

# all arguments here are integers
def triangle_area(x1,y1,x2,y2,x3,y3):
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)

def valid_points(x1, y1,x2,y2,x3,y3,x,y):
    initial_area = triangle_area(x1, y1, x2, y2, x3, y3)
    area_1 = triangle_area(x, y, x2, y2, x3, y3)
    area_2 = triangle_area(x1, y1, x, y, x3, y3) 
    area_3 = triangle_area (x1, y1, x2, y2, x, y)
    if (initial_area == (area_1+area_2+area_3)):
        return True
    else:
        return False

def colinear_check(x1, y1,x2,y2,x3,y3):
    degenerate_value = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
    if degenerate_value == 0:
        return True
    else:
        return False

def points_given(x1, y1,x2,y2,x3,y3,xp,yp,xq,yq):
    if colinear_check(x1, y1,x2,y2,x3,y3) == True:
        return 0
    if valid_points(x1, y1,x2,y2,x3,y3,xp,yp) and not (valid_points(x1, y1,x2,y2,x3,y3,xq,yq)):
        return 1
    if not (valid_points(x1, y1,x2,y2,x3,y3,xp,yp)) and (valid_points(x1, y1,x2,y2,x3,y3,xq,yq)):
        return 2
    if valid_points(x1, y1,x2,y2,x3,y3,xp,yp) and (valid_points(x1, y1,x2,y2,x3,y3,xq,yq)):
        return 3
    if not(valid_points(x1, y1,x2,y2,x3,y3,xp,yp) and not(valid_points(x1, y1,x2,y2,x3,y3,xq,yq))):
        return 4

if __name__ == "__main__":
    print("--------------------")
    print("Test #1: \na(0,0) \nb(20,0) \nc(10,30) \np(10,15) and q(4,2)")
    print("Output:", points_given(0, 0, 20, 0, 10, 30, 10, 15,4,2))
    print("Expected Output: 3")
    print("-------------------- ")
    print("Test #2: \na(1,1) \nb(2,3) \nc(4,5) \np(1,3) and q(1,3)")
    print("Output:",points_given(1, 1, 2, 3, 4, 5,1,3,2,3))
    print("Expected Output: 2")
    print("--------------------")
    print("Test #3: \na(1,1) \nb(2,3) \nc(4,5) \np(1,3) and q(1,3)")
    print("Output:",points_given(0, 9, 1, 3, 4, 9,5,9,9,1))
    print("Expected Output: 4")
    print("--------------------")
    print("Test #4: \na(1,1) \nb(1,1) \nc(1,1) \np(1,3) and q(1,3)")
    print("Output:",points_given(1, 1, 1, 1, 1, 1,5,9,9,1))
    print("Expected Output: 0")
    print("--------------------\n")