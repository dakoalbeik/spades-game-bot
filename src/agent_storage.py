from agent import Agent


# NOTE: Class will store versions of agents so that they can be selected for play.
#       During prototyping, only "idiot agents" (i.e., agents that act randomly) are stored.
class AgentStorage:
    def __init__(self):
        self.idiot_agents = []

        agent1_version = "agent0_0_0"
        agent2_version = "agent0_0_0dup"
        agent3_version = "agent0_0_0dup2"

        agent0_0_0 = Agent(agent1_version)
        agent0_0_0dup = Agent(agent2_version)
        agent0_0_0dup2 = Agent(agent3_version)

        self.idiot_agents.append(agent0_0_0)
        self.idiot_agents.append(agent0_0_0dup)
        self.idiot_agents.append(agent0_0_0dup2)
