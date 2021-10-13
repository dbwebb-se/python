"""
Solve A5 in marvin1 using dicts
"""
def calculate_points(point_str):
    """
    Calculated points for each player
    """
    player_dict = {}
    
    for index in range(0, len(point_str), 2):
        if point_str[index].isupper():
            current_points = int(point_str[index + 1]) * -1
        else:
            current_points = int(point_str[index + 1])
        
        if point_str[index].lower() in player_dict:
            player_dict[point_str[index].lower()] += current_points
        else:
            player_dict[point_str[index].lower()] = current_points
    
    result_list = []
            
    for key, value in player_dict.items():
        result_list.append(key + " " + str(value))
        
    result_string = ", ".join(result_list)
    
    print(result_string)

if __name__ == "__main__":
    calculate_points("g3l1H5l2G3l1")
