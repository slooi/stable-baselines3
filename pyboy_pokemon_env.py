import gymnasium as gym
from gymnasium import spaces
from pyboy import PyBoy
import numpy as np


class PokemonRedEnv(gym.Env):
    metadata = {"render_modes": ["human"], "render_fps": 1}

    def __init__(self, rom_path="PokemonRed.gb", render=False):
        # super().__init__()
        self.pyboy = PyBoy(rom_path, window="SDL2" if render else "null", sound=False)
        with open("has_pokedex.state", "rb") as f:
            self.pyboy.load_state(f)
        self.pyboy.set_emulation_speed(0)
        self.game = self.pyboy.game_wrapper
        self.game.start_game()

        input("asd")
        self.action_space = spaces.Discrete(8)  # Up, Down, Left, Right, A, B, Start, Select
        self.observation_space = spaces.Box(low=0, high=255, shape=(144, 160), dtype=np.uint8)

    def step(self, action):
        buttons = [
            self.pyboy.button.UP,
            self.pyboy.button.DOWN,
            self.pyboy.button.LEFT,
            self.pyboy.button.RIGHT,
            self.pyboy.button.A,
            self.pyboy.button.B,
            self.pyboy.button.START,
            self.pyboy.button.SELECT,
        ]
        self.pyboy.send_input(buttons[action])
        for _ in range(5):  # Advance the emulator by a few frames
            self.pyboy.tick()

        obs = self.get_obs()
        reward = 0  # Start with 0, or add your own reward shaping
        terminated = False
        truncated = False
        return obs, reward, terminated, truncated, {}

    def reset(self, seed=None, options=None):
        self.pyboy.stop()
        self.__init__()
        return self.get_obs(), {}

    def get_obs(self):
        return np.array(self.pyboy.screen.image)

    def render(self):
        print("RENDER CALLED!")
        pass

    def close(self):
        self.pyboy.stop()
