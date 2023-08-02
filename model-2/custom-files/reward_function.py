def reward_function(params):

    if not params["is_offtrack"] and params["steps"] > 0:
        print("Progress:- " + params["progress"])
        print("Steps:- " + params["steps"])
        print("Speed:- " + params["speed"])
        reward = ((params["progress"] / params["steps"]) * 100) + (params["speed"]**2)
    else:
        reward = 0.01
    print("Reward:- " + reward)
    return float(reward)
