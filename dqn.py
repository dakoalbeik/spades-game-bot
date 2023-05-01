import datetime
import json

import gym
from keras.layers import Dense
from keras.layers import Flatten
from keras.models import Sequential
from keras.optimizers import Adam

from keras_rl.agents.dqn import DQNAgent
from keras_rl.memory import SequentialMemory
from keras_rl.policy import EpsGreedyQPolicy, LinearAnnealedPolicy

ENV_NAME = 'spades:spades-v0'


def get_weights_fn():
    now = datetime.datetime.now()
    formatted_date = now.strftime("%m-%d %H-%M-%S")
    return f'dqn_weights/{formatted_date}/dqn_spades_weights.h5f'


def make_env():
    env = gym.make(ENV_NAME)
    nb_actions = env.action_space.n
    flattened_env = gym.wrappers.FlattenObservation(env)
    return flattened_env, nb_actions


def save_array_to_json(array, file_path):
    with open(file_path, 'w') as f:
        json.dump(array, f)


def create_model(env, nb_actions):
    # Define the agent

    model = Sequential()
    model.add(Flatten(input_shape=(1,) + env.observation_space.shape))
    model.add(Dense(16, activation='relu'))
    model.add(Dense(16, activation='relu'))
    model.add(Dense(nb_actions, activation='linear'))
    print(model.summary())
    memory = SequentialMemory(limit=200_000, window_length=1)
    policy = LinearAnnealedPolicy(EpsGreedyQPolicy(),
                                  attr='eps',
                                  value_max=1.,
                                  value_min=.1,
                                  value_test=.05,
                                  nb_steps=1_000_000)
    return model, memory, policy, nb_actions


def create_dqn(emit=None):
    env, nb_actions = make_env()
    env.set_emit(emit)
    model, memory, policy, nb_actions = create_model(env, nb_actions)
    agent = DQNAgent(model=model, nb_actions=nb_actions, memory=memory, nb_steps_warmup=1000,
                     target_model_update=100, policy=policy)
    agent.compile(optimizer=Adam(learning_rate=1e-3), metrics=['mae'])
    return env, agent


def train_dqn(env, agent):
    # Train the agent
    agent.fit(env, nb_steps=2_000_000, visualize=False, verbose=2)
    # Save the history
    history = env.get_history()
    save_array_to_json(history, 'history.json')
    # Save the weights
    agent.save_weights(filepath=get_weights_fn(), overwrite=False)

#
# environment, dqn_agent = create_dqn()
# train_dqn(environment, dqn_agent)
