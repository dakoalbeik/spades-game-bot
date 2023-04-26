import gym
from keras.layers import Flatten
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from rl.agents.dqn import DQNAgent
from rl.memory import SequentialMemory
from rl.policy import EpsGreedyQPolicy, LinearAnnealedPolicy
from tensorflow.keras.optimizers import Adam

env = gym.make('spades:spades-v0')
nb_actions = env.action_space.n

flattened_env = gym.wrappers.FlattenObservation(env)
print(flattened_env.observation_space.shape)

weights_fileName = 'test_dqn_spades_weights.h5f'

# Define the agent
model = Sequential()
# TODO: understand why we are adding a tuple to the shape here
model.add(Flatten(input_shape=(1,) + flattened_env.observation_space.shape))
model.add(Dense(16, activation='relu'))
model.add(Dense(16, activation='relu'))
model.add(Dense(nb_actions, activation='linear'))
print(model.summary())
memory = SequentialMemory(limit=100_000, window_length=1)
policy = LinearAnnealedPolicy(EpsGreedyQPolicy(),
                              attr='eps',
                              value_max=1.,
                              value_min=.1,
                              value_test=.05,
                              nb_steps=20000)
dqn = DQNAgent(model=model, nb_actions=nb_actions, memory=memory, nb_steps_warmup=10,
               target_model_update=100, policy=policy)
dqn.compile(optimizer=Adam(learning_rate=1e-3), metrics=['mae'])
# # Train the agent
# dqn.fit(flattened_env, nb_steps=10000, visualize=False, verbose=2)
