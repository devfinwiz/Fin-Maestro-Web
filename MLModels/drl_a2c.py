import numpy as np
import pandas as pd
import gym
from stable_baselines3 import A2C

# Load the stock price data
data = pd.read_csv('stock_prices.csv')

# Extract the relevant features
features = data[['Open', 'High', 'Low', 'Close', 'Volume']].values
target = data['Price'].values

# Define the custom stock trading environment
class StockTradingEnvironment(gym.Env):
    def __init__(self, features, target):
        super(StockTradingEnvironment, self).__init__()

        self.features = features
        self.target = target
        self.max_steps = len(features) - 1
        self.current_step = None
        self.action_space = gym.spaces.Discrete(2)
        self.observation_space = gym.spaces.Box(low=-np.inf, high=np.inf, shape=(len(features[0]),), dtype=np.float32)

    def reset(self):
        self.current_step = 0
        return self.features[self.current_step]

    def step(self, action):
        if self.current_step == self.max_steps:
            return self.features[self.current_step], 0, True, {}

        self.current_step += 1
        done = self.current_step == self.max_steps
        reward = self.target[self.current_step] - self.target[self.current_step - 1]  # Profit as reward
        return self.features[self.current_step], reward, done, {}

# Create the stock trading environment
env = StockTradingEnvironment(features, target)

# Initialize and train the DRL agent (A2C)
model = A2C('MlpPolicy', env, verbose=1)
model.learn(total_timesteps=10000)

# Test the trained agent
obs = env.reset()
done = False
while not done:
    action, _ = model.predict(obs)
    obs, reward, done, _ = env.step(action)

# Obtain the final portfolio value
final_portfolio_value = env.target[env.current_step]
print(f"Final Portfolio Value: {final_portfolio_value}")
