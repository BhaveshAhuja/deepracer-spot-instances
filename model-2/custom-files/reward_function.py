def reward_function(params):

    if not params["is_offtrack"] and params["steps"] > 0:
        print("Progress:- " + str(params["progress"]))
        print("Steps:- " + str(params["steps"]))
        print("Speed:- " + str(params["speed"]))
        reward = ((params["progress"] / params["steps"]) * 100) + (params["speed"]**2)
    else:
        reward = 0.01
    print("Reward:- " + str(reward))
    return float(reward)
