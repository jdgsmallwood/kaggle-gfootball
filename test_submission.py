"""
This was taken from https://www.kaggle.com/garethjns/gfootball-apis-and-linear-q-learner-example
with thanks as a script to test an agent.

This script will get the kaggle environment, then run the environment. It will
"""
from kaggle_environments import make


def run_submission_simulation(submission_file_name, opponent='run_right'):
    env = make("football", configuration={"save_video": True,
                                          "scenario_name": "11_vs_11_kaggle"})

    # Define players
    left_player = submission_file_name  # A custom agent, eg. random_agent.py or example_agent.py
    right_player = opponent  # eg. A built in 'AI' agent

    # Run the whole sim
    # Output returned is a list of length n_steps. Each step is a list containing the output for each player as a dict.
    # steps
    output = env.run([left_player, right_player])

    for s, (left, right) in enumerate(output):

        # Just print the last few steps of the output
        if s > 2990:
            print(f"\nStep {s}")

            print(f"Left player ({left_player}): \n"
                  f"actions taken: {left['action']}, "
                  f"reward: {left['reward']}, "
                  f"status: {left['status']}, "
                  f"info: {left['info']}")

            print(f"Right player ({right_player}): \n"
                  f"actions taken: {right['action']}, "
                  f"reward: {right['reward']}, "
                  f"status: {right['status']}, "
                  f"info: {right['info']}\n")

    left_score, right_score = output[-1][0]['observation']['players_raw'][0]['score']
    print(f"Final score: {left_score} : {right_score}")
    return [left_score, right_score]
