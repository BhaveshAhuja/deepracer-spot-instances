def reward_function(params):

    if not params["is_offtrack"] and params["steps"] > 0:
        reward = ((params["progress"] / params["steps"]) * 100) + (params["speed"]**2)
    else:
        reward = 0.01
        
    return float(reward)
