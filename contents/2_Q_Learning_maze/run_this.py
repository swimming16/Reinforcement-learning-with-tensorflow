"""
Reinforcement learning maze example.

Red rectangle:          explorer.
Black rectangles:       hells       [reward = -1].
Yellow bin circle:      paradise    [reward = +1].
All other states:       ground      [reward = 0].

This script is the main part which controls the update method of this example.
The RL is in RL_brain.py.

View more on my tutorial page: https://morvanzhou.github.io/tutorials/
"""

from maze_env import Maze
from RL_brain import QLearningTable

#test!!!

def update():
    for episode in range(100):
        # initial observation
        observation = env.reset()
        print('q_table\n',RL.q_table)

        while True:
            # fresh env
            env.render()
            #print(str(observation))

            # RL choose action based on observation
            #迷宫游戏的state是一个list,表示探索者的位置
            action = RL.choose_action(str(observation))

            # RL take action and get next observation and reward
            observation_, reward, done = env.step(action)

            # RL learn from this transition
            RL.learn(str(observation), action, reward, str(observation_))

            # swap observation
            observation = observation_

            # break while loop when end of this episode
            if done:
                break

    # end of game
    print('game over')
    env.destroy()

if __name__ == "__main__":
    env = Maze()
    print(list(range(env.n_actions)))

    RL = QLearningTable(actions=list(range(env.n_actions)))
    #print('q_table',RL.q_table)

    env.after(100, update)
    env.mainloop()