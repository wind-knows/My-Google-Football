# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 15:50:29 2023

@author: HuYiHang
"""


import gfootball.env as football_env
env = football_env.create_environment(
     env_name='11_vs_11_stochastic',
     representation='raw',
     stacked=False,
     logdir='/tmp/football',
     write_goal_dumps=False,
     write_full_episode_dumps=False,
     write_video=False,
     render=False,
     number_of_right_players_agent_controls=1
)


env.reset()
steps = 0
done = False
while not done:
    action = env.action_space.sample()
    obs, rew, done, info = env.step(action)
    steps += 1
    if steps % 100 == 0:
        print("Step {0} Reward: {1}".format(steps, rew))

print("Steps: {0} Reward: {1}".format(steps, rew))

# obs = env.observations()
# action = get_action(obs) # your model
# next_obs, reward, done, info = env.step(action)


