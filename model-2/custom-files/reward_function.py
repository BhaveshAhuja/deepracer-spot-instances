import math
def direction_reward(reward, waypoints, closest_waypoints, heading):
    total_length = len(waypoints)
    prev_index = closest_waypoints[0]
    next_index = closest_waypoints[1]
    print("Actual Prev:- " + str(prev_index))
    print("Actual Next:- " + str(next_index))
    if(prev_index-3>=0):
        prev_index = prev_index-3
    else:
        prev_index = 0
    if(next_index+3<total_length):
        next_index = next_index+3
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

    if direction_diff >= 20 or direction_diff < -5:
        reward *= 0.5
    elif direction_diff >= -5 and direction_diff < -1:
        reward *= 1.2
    elif direction_diff >= -1 and direction_diff < 6:
        reward *= 1.6
    elif direction_diff >= 6 and direction_diff < 10:
        reward *= 1.3
    elif direction_diff >=10 and direction_diff < 20:
        reward *= 0.7

    return float(reward)

def right_lane(reward, is_left_lane):
    print("Is Left Lane:- " + str(is_left_lane))
    if is_left_lane:
        return reward*0.8
    else:
        return reward*1.2

def reward_function(params):
    closest_waypoints = params['closest_waypoints']
    speed = params["speed"]
    steering_angle = params["steering_angle"]
    waypoints = params['waypoints']
    heading = params['heading']
    is_left_of_center = params['is_left_of_center']
    is_offtrack = params["is_offtrack"]
    progress = params["progress"]

    print("Current Progress:- " + str(progress))
    print("Closest Waypoints:- " + str(closest_waypoints[0]) + ":" + str(closest_waypoints[0]))
    
    if is_offtrack:
        reward = 0.0001
        return reward
    else:
        if speed>2.0 and speed<2.6 and abs(steering_angle) > 20:
            reward = 2.0
        elif speed>2.6 and speed<3.0 and abs(steering_angle) > 0:
            reward = 2.0
        elif speed>3.7 and speed<3.9 and steering_angle == 0:
            reward = 1.7
        elif speed>3.9 and speed<4.1 and steering_angle == 0:
            reward = 2.0
        else:
            reward = 0.0001
        print("Speed Reward:- " + str(reward))
        reward = right_lane(reward, is_left_of_center)
        print("Right Lane Reward:- " + str(reward))
        reward = direction_reward(reward,waypoints,closest_waypoints,heading)
    print("Final Reward:- " + str(reward))
    return float(reward)