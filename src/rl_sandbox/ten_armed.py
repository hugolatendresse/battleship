import numpy as np

class TenArmed:
    def __init__(self, k=10, number_of_steps=10000, epsilon=0.1):
        self.k = k
        self.number_of_steps = number_of_steps
        self.q_star = {i: 0 for i in range(self.k)}
        self.q = {i: 0 for i in range(self.k)}
        self.best_action = max(self.q_star, key=self.q_star.get)
        self.actions = np.arange(self.k)
        self.epsilon = epsilon
        self.n = 0

    def select_action(self):
        if np.random.random() < self.epsilon:
            return np.random.choice(self.actions)
        else:
            return max(self.q, key=self.q.get)

    def run(self):
        for self.n in range(self.number_of_steps):
            action = self.select_action()
            reward = self.get_reward(action)
            self.update_q(action, reward)
            self.update_q_star()


    def get_reward(self, action):
        if action not in self.actions:
            raise ValueError("Invalid action.")
        return np.random.normal(self.q_star[action])

    def update_q(self, action, reward):
        self.q[action] = self.q[action] + 1 / self.n[action] * (reward - self.q[action])

    def update_q_star(self):
        for action in self.actions:
            self.q_star[action] += np.random.normal(0, 0.01)
