import gym
from keras.layers import Flatten
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
from keras_rl.agents.dqn import DQNAgent
from keras_rl.memory import SequentialMemory
from keras_rl.policy import EpsGreedyQPolicy, LinearAnnealedPolicy

env = gym.make('spades:spades-v0')
nb_actions = env.action_space.n

flattened_env = gym.wrappers.FlattenObservation(env)

weights_fileName = 'test_dqn_spades_weights.h5f'

# Define the agent
model = Sequential()
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
dqn = DQNAgent(model=model, nb_actions=nb_actions, memory=memory, nb_steps_warmup=1000,
               target_model_update=100, policy=policy)
dqn.compile(optimizer=Adam(learning_rate=1e-3), metrics=['mae'])
# # Train the agent
dqn.fit(flattened_env, nb_steps=10000, visualize=False, verbose=2)
