# Discord Launcher
A simple launcher for Discord, written in Python.

## Features
Automatically re-injects [Better Discord](https://github.com/BetterDiscord/BetterDiscord) when Discord updates.
Automatically applies [OpenASAR](https://github.com/GooseMod/OpenAsar) patch when Discord updates.

## Pre-requisites
- [Git](https://git-scm.com)
- [Node.js](https://nodejs.org/en/) with [pnpm](https://pnpm.io/).
- [Python 3](https://www.python.org/downloads/)

## Installation
1. Launch discord manually for the first time if you haven't
2. Run launch.py
3. Optionally create a shortcut to launch.py that you run every time you want to launch Discord to make injection automatic

### Does the script re-inject every time I launch Discord?
No the script only re-injects if an update is detected.