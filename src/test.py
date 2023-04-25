import tensorflow as tf
from gym import spaces

obs_space_tuple = spaces.Tuple([
    spaces.MultiDiscrete([52] * 4),  # The cards in the current trick
    spaces.MultiDiscrete([52] * 13),  # The cards in the player's hand
    spaces.Discrete(2),  # Whether spades have been played yet
    spaces.MultiDiscrete([52] * 52),  # The cards that have been discarded so far in the game
    spaces.MultiDiscrete([501] * 2)  # The score of both teams
])


class ObservationInputLayer(tf.keras.layers.Layer):
    def __init__(self, observation_space, **kwargs):
        super().__init__(**kwargs)
        self.observation_space = observation_space
        self.input_layers = [
            tf.keras.layers.InputLayer(input_shape=obs_space.shape, dtype=obs_space.dtype)
            for obs_space in self.observation_space.spaces
        ]

    def call(self, inputs):
        return [input_layer(inputs[i]) for i, input_layer in enumerate(self.input_layers)]


input_layer = ObservationInputLayer(obs_space_tuple)
print(input_layer)
observation_input = tf.keras.layers.concatenate(input_layer.output)

# You can now use `observation_input` as the input layer for your model.
