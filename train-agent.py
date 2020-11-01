
import gym
import gfootball

from kaggle_environments import make

env_name = "GFootballBase-v0"
gym.envs.register(id=env_name,
                  entry_point="gfootball.env.football_env:FootballEnv",
                  max_episode_steps=10000)


from gfootball.env import create_environment

# (These are the args set by the kaggle_environments package)
COMMON_KWARGS = {"stacked": False, "representation": 'raw', "write_goal_dumps": False,
                 "write_full_episode_dumps": False, "write_video": False, "render": False,
                 "number_of_left_players_agent_controls": 1, "number_of_right_players_agent_controls": 0}

env = create_environment(env_name='11_vs_11_kaggle')


#env = make("football", configuration={"save_video": True, "scenario_name": "11_vs_11_kaggle", "running_in_notebook": False})

obs = env.reset()


