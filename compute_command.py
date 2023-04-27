def compute_command(x1, y1, x2, y2):
    '''Function to compute the linear and angular velocities that 
    sent to the robot. 
    
    
    Author: TODO: Fill in your name here
    
    
    Example of Image percived by the robot:
    
    (0, 0)          (640, 0)
    *----------------*
    | x1 y1          |
    |  *--------*    |
    |  |   bb   |    |
    |  *--------*    |
    |          x2 y2 |
    |                |
    *----------------*
    (0, 480)        (640, 480)
    
    "bb" is the bounding box of the person detected by the robot.
    
    Args:
        x1 (float): x upper left corner of the bounding box
        y1 (float): y upper left corner of the bounging box
        x2 (float): x lower right corner of the bounding box
        y2 (float): y lower right corner of the bounding box
        
    Returns: 
        linear (float): linear velocity in range (0, 0.1)
        angular (float): angular velocity in range (-0.1, 0.1)
    '''
    
    linear = 0
    angular = 0
    
    return linear, angular