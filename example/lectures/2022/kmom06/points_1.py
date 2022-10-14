"""
Solve A5 in marvin1 using dictionaries
"""
def calculate_points(point_str):
    """
    Calculated points for each player
    """
    
    # loop in step of 2, [index] <=> player and [index + 1] <=> its points
    for index in range(0, len(point_str), 2):
        # Count the points, if upper subtract the points and if lower add the points
        print("Player " + point_str[index] + " with points: " + point_str[index + 1])
    

if __name__ == "__main__":
    calculate_points("g3l1H5l2G3l1")
