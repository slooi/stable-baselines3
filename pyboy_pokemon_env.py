import gymnasium as gym
from gymnasium import spaces
from pyboy import PyBoy
import numpy as np
from gymnasium.envs.registration import register

register(
    id='pk',
    entry_point='pyboy_pokemon_env:PokemonRedEnv'
)


class PokemonRedEnv(gym.Env):
    metadata = {"render_modes": ["human"], "render_fps": 1}

    def __init__(self, render_mode=False, rom_path="PokemonRed.gb"):
        # super().__init__()
        # self.pyboy = PyBoy(rom_path, window="SDL2" if render else "null", sound=False)
        # with open("has_pokedex.state", "rb") as f:
        #     self.pyboy.load_state(f)
        # self.pyboy.set_emulation_speed(0)
        # self.game = self.pyboy.game_wrapper
        # self.game.start_game()

        # input("asd")
        # self.action_space = spaces.Discrete(8)  # Up, Down, Left, Right, A, B, Start, Select
        # self.observation_space = spaces.Box(low=0, high=255, shape=(144, 160), dtype=np.uint8)
        pass

    def step(self, action):
        # buttons = [
        #     self.pyboy.button.UP,
        #     self.pyboy.button.DOWN,
        #     self.pyboy.button.LEFT,
        #     self.pyboy.button.RIGHT,
        #     self.pyboy.button.A,
        #     self.pyboy.button.B,
        #     self.pyboy.button.START,
        #     self.pyboy.button.SELECT,
        # ]
        # self.pyboy.send_input(buttons[action])
        # for _ in range(5):  # Advance the emulator by a few frames
        #     self.pyboy.tick()

        # obs = self.get_obs()
        # reward = 0  # Start with 0, or add your own reward shaping
        # terminated = False
        # truncated = False
        # return obs, reward, terminated, truncated, {}
        pass

    def reset(self, seed=None, options=None):
        # self.pyboy.stop()
        # self.__init__()
        # return self.get_obs(), {}
        pass

    def get_obs(self):
        # return np.array(self.pyboy.screen.image)
        pass

    def render(self):
        print("RENDER CALLED!")
        pass

    # def close(self):
    #     self.pyboy.stop()


def my_check_env():
    from gymnasium.utils.env_checker import check_env
    env = gym.make('pk',render_mode=None)
    check_env(env)
if __name__ == "__main__":
    my_check_env()