## How to use

### Train

Syntax: `python main.py <STABLE_BASELINES3_ENVIRONMENT> <STABLE_BASELINES3_ALGORITHM> -t`

```sh
python main.py Pendulum-v1 PPO -t
```

### Test

After you have trained your model, you can then test it!

Syntax: `python main.py <STABLE_BASELINES3_ENVIRONMENT> <STABLE_BASELINES3_ALGORITHM> -s "<PATH_TO_YOUR_TRAINED_MODEL>"`

```sh
python main.py Pendulum-v1 PPO -s "models\Pendulum-v1_2025-06-01_20-34-36\PPO_1275000.zip"
```

## Gotcha - Fix cuda issue

if `torch.cuda.is_available()` is false but you have `nvidia-smi` do the following steps:

1. pip uninstall torch
2. pip install torch --index-url https://download.pytorch.org/whl/cu121
   Note the CUDA version listed in your `nvidia-smi` must be equal or greater than cu121
3. open a python interactive shell by typing `python` in your terminal
4. run the following to check is cuda is available and to see your gpu device

```python
import torch
torch.cuda.is_available()
torch.cuda.get_device_name(0)
```

## Decision flow chart

1. Use nvidia-smi to check that you are using a version of CUDA that is equal or greater than the pytorch CUDA version
2. `pip install` inside the repo
3. if you run into CUDA issues, `pip uninstall torch`
4. Checkout what version of pytorch you need. Then find the most compatible cuda version of pytorch based on surrounding info and if the required pytorch version appears in your corresponding wheel link (i.e: https://download.pytorch.org/whl/cu121/torch/)
5. install CUDA version of pytorch: `pip install torch --index-url https://download.pytorch.org/whl/cu121`
6. DONE!


## CONDA ISSUES
If you get an issue where your paths are borken running `conda activate ENV_NAME` in VSCode, add these settings to your VSCode settings.json
```json
  "python.terminal.activateEnvironment": false,
  "terminal.integrated.inheritEnv": false
```
If you can't find conda in your vscode git-bash terminal, try adding the folowing to your `~/.bashrc` file
```sh
# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/c/Users/YOU_NAME/anaconda3/Scripts/conda.exe' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/c/Users/YOU_NAME/anaconda3/etc/profile.d/conda.sh" ]; then
        . "/c/Users/YOU_NAME/anaconda3/etc/profile.d/conda.sh"
    else
        export PATH="/c/Users/YOU_NAME/anaconda3/Scripts:$PATH"
        # For newer conda versions, condabin is often preferred or also needed.
        # The hook handles this, but if manually setting, consider:
        # export PATH="/c/Users/YOU_NAME/anaconda3/condabin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<

```