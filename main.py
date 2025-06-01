import gymnasium as gym
import stable_baselines3
import argparse
import os
import sys
import datetime

print("ARGS:", sys.argv)


def get_time():
    return "_".join(str(datetime.datetime.now()).replace(":", "-").split(".")[0].split(" "))


def train(env, algo, env_name):
    full_model_dir = f"models/{env_name}_{get_time()}"
    full_log_dir = f"logs/{env_name}_{get_time()}"
    os.makedirs(full_model_dir, exist_ok=True)
    os.makedirs(full_log_dir, exist_ok=True)

    print("env", env)
    model = sb3_class("MlpPolicy", env, verbose=1, device="cuda", tensorboard_log=full_log_dir)
    TIMESTEPS = 25000
    iters = 0
    while True:
        iters += 1
        model.learn(total_timesteps=TIMESTEPS, reset_num_timesteps=False)
        model.save(f"{full_model_dir}/{algo}_{TIMESTEPS*iters}")


def test(env, path_to_model):
    model = sb3_class.load(path_to_model, env)

    obs = env.reset()[0]
    # done=False
    extra_steps = 500
    while True:
        action, _ = model.predict(obs)
        obs, _, terminated, truncated, _ = env.step(action)
        if terminated or truncated:
            extra_steps -= 1
            if extra_steps == 0:
                break


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="train or test model")

    # Positional argument: environment name
    parser.add_argument("gymenv", help="The Gym environment ID: Humanoid-v5 Pendulum-v1")
    parser.add_argument("algo", help="Algorithm: PPO SAC TD3")

    # Optional flags
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-t", "--train", action="store_true")
    group.add_argument("-s", "--test", metavar="MODEL_PATH", help="Simulate using the specified model file")

    args = parser.parse_args()
    # python main.py Pendulum-v1 PPO -s "models\Pendulum-v1_2025-06-01_20-34-36\PPO_1275000.zip"
    # python main.py Pendulum-v1 PPO -t

    sb3_class = getattr(stable_baselines3, args.algo)

    if args.train:
        gymenv = gym.make(args.gymenv, render_mode=None)
        train(gymenv, args.algo, args.gymenv)

    if args.test:
        if os.path.isfile(args.test):
            gymenv = gym.make(args.gymenv, render_mode="human")
            test(gymenv, args.test)
        else:
            print(f"{args.test} not found")
