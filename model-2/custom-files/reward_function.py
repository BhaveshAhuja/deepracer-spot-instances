import math
def direction_reward(reward, waypoints, closest_waypoints, heading):
    total_length = len(waypoints)
    prev_index = closest_waypoints[0]
    next_index = closest_waypoints[1]
    print("Actual Prev:- " + str(prev_index))
    print("Actual Next:- " + str(next_index))
    
    if(next_index+10<total_length):
        next_index = next_index+10
    else:
        next_index = total_length-1
    
    print("Modified Prev:- " + str(prev_index))
    print("Modified Next:- " + str(next_index))
    next_point = waypoints[next_index]
    prev_point = waypoints[prev_index]

    print("Previous waypoint:- " + str(prev_point))
    print("Next waypoint:- " + str(next_point))

    direction = math.degrees(math.atan2(next_point[1] - prev_point[1], next_point[0] - prev_point[0]))
    direction_diff = direction - heading

    print("Calculated angle:- " + str(direction))
    print("Heading angle:- " + str(heading))
    print("Direction Diff:- " + str(direction_diff))

    if direction_diff < -7:
        reward *= 0.5
    elif direction_diff >= -7 and direction_diff < -3:
        reward *= 0.8
    elif direction_diff >= -3 and direction_diff < -1:
        reward *= 1.2
    elif direction_diff >= -1 and direction_diff <= 2:
        reward *= 1.5
    elif direction_diff > 2 and direction_diff <= 6:
        reward *= 1.2
    elif direction_diff > 6 and direction_diff <= 10:
        reward *= 0.8
    elif direction_diff > 10:
        reward *= 0.5
    
    return float(reward)

def reward_function(params):
    closest_waypoints = params['closest_waypoints']
    waypoints = params['waypoints']
    heading = params['heading']
    is_offtrack = params["is_offtrack"]
    progress = params["progress"]

    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("Current Progress:- " + str(progress))
    print("Closest Waypoints:- " + str(closest_waypoints[0]) + ":" + str(closest_waypoints[1]))
    
    if is_offtrack:
        reward = 0.0001
        return reward
    reward = 10.0
    reward = direction_reward(reward,waypoints,closest_waypoints,heading)
    print("Final Reward:- " + str(reward))
    return float(reward)
