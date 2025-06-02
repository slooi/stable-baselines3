import gymnasium as gym
import stable_baselines3
import argparse
import os
import sys
import datetime
from pyboy_pokemon_env import PokemonRedEnv

print("ARGS:", sys.argv)


def get_time():
    return "_".join(str(datetime.datetime.now()).replace(":", "-").split(".")[0].split(" "))


def train(env, algo, env_name):
    full_model_dir = f"models/{env_name}_{get_time()}"
    full_log_dir = f"logs/{env_name}_{get_time()}"
    os.makedirs(full_model_dir, exist_ok=True)
    os.makedirs(full_log_dir, exist_ok=True)

    print("env", env)
    model = sb3_class("MlpPolicy", env, verbose=1, device="cpu", tensorboard_log=full_log_dir)
    TIMESTEPS = 25000
    iters = 0
    while True:
        iters += 1
        model.learn(total_timesteps=TIMESTEPS, reset_num_timesteps=False)
        model.save(f"{full_model_dir}/{algo}_{TIMESTEPS * iters}")


def test(env, path_to_model):
    model = sb3_class.load(path_to_model, env)
    obs = env.reset()[0]
    extra_steps = 500
    while True:
        action, _ = model.predict(obs)
        obs, _, terminated, truncated, _ = env.step(action)
        if terminated or truncated:
            extra_steps -= 1
            if extra_steps == 0:
                break


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train or test model")
    parser.add_argument("algo", help="Algorithm: PPO, SAC, TD3")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-t", "--train", action="store_true")
    group.add_argument("-s", "--test", metavar="MODEL_PATH", help="Simulate using the specified model file")
    args = parser.parse_args()

    sb3_class = getattr(stable_baselines3, args.algo)

    env_name = "PokemonRed"
    env = PokemonRedEnv(render=bool(args.test))

    if args.train:
        train(env, args.algo, env_name)

    if args.test:
        if os.path.isfile(args.test):
            test(env, args.test)
        else:
            print(f"{args.test} not found")
