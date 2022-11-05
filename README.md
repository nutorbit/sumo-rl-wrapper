# SUMO Environment

This repository built on top of [SUMO-RL](https://github.com/LucasAlegre/sumo-rl) 
which is a reinforcement learning environment for SUMO. It provides a set of tools to train and test reinforcement learning agents in SUMO.

## Development setup

Please install [poetry](https://python-poetry.org/) first. Then run the following commands:

```zsh
$ poetry install
```

## Usage

### Import external (OpenStreetMap) map to SUMO

```zsh
$ poetry run python -m sumo.scripts.gen_data_from_map
```

### Test map files

```zsh
$ poetry run python -m sumo.scripts.open_gui
```

