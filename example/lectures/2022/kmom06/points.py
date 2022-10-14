"""
Solve A5 in marvin1 using dictionaries
"""
def calculate_points(point_str):
    """
    Calculated points for each player
    """
    player_dict = {}
    
    # loop in step of 2, [index] <=> player and [index + 1] <=> its points
    for index in range(0, len(point_str), 2):
        # Count the points, if upper subtract the points and if lower add the points
        if point_str[index].isupper():
            current_points = int(point_str[index + 1]) * -1
        else:
            current_points = int(point_str[index + 1])
        
        if point_str[index].lower() in player_dict:
            player_dict[point_str[index].lower()] += current_points
        else:
            player_dict[point_str[index].lower()] = current_points
    
    result_list = []

    # create a list, which can be sorted if wanted later       
    for key, value in player_dict.items():
        result_list.append(key + " " + str(value))
        
    result_string = ", ".join(result_list)
    
    print(result_string)

if __name__ == "__main__":
    calculate_points("a2b4A5s3B1")
    calculate_points("g3l1H5l2G3l1")
