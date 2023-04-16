# # Initialize Agent which will act and learn
# q_agent = Agent()
# q_agent.fetch_random_version()
#
# # Initialize Environment with which Agents will interact
# # Environment returns rewards and states in response to Agent action
# q_environment = Environment(q_agent)

from src.spades_env import SpadesEnv

env = SpadesEnv()
env.play_game()
