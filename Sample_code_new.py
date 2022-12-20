#%% import
import numpy as np
import gym

#%% hyperparameters
REPS = 20
EPISODES = #2000
EPSILON = 0.1
LEARNING_RATE = 0.1
DISCOUNT = 0.9
STUDENT_NUM = #123

#%%environment
env = gym.make('Taxi-v3')
env.seed(seed = STUDENT_NUM)
Initial_State = env.reset()

#%% get familiar with the environment
print("you can see the environment in each step by render command :")
env.render()

#%% base code for Q-learning

env = gym.make('Taxi-v3')
env.seed(seed = STUDENT_NUM)


for rep in range(REPS): 
    agent = # Agent Object instance from Algorithm_name(e.g Q_learning_agent) class which has inherited from Agentbase.
    for episode in range(EPISODES):
        Initial_state = env.reset()

        for ... :

            bestAction = np.random.choice(ACTIONS)

            next_state,rew,done,_ = environment.step(bestAction)
            
            if done:
                break
