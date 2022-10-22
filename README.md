# Discord Launcher
A simple launcher for Discord, written in Python.

## Features
Automatically re-injects [Better Discord](https://github.com/BetterDiscord/BetterDiscord) when Discord updates.
Automatically applies [OpenASAR](https://github.com/GooseMod/OpenAsar) patch when Discord updates.

## Pre-requisites
- [Git](https://git-scm.com)
- [Node.js](https://nodejs.org/en/) with [pnpm](https://pnpm.io/).
- [Python 3](https://www.python.org/downloads/)

## Installation
1. Launch discord manually for the first time if you haven't
2. Run launch.py
3. Optionally create a shortcut to launch.py that you run every time you want to launch Discord to make injection automatic

### Does the script re-inject every time I launch Discord?
No the script only re-injects if an update is detected.

### How do I install for other operating systems?
As of right now, the script is written for MacOS. However it should be as easy as changing the directory locations in the script to match your operating system. Please create a pull request if you do this and I'll happily merge it.

### What about the Discord TOS?
Both BetterDiscord and OpenASAR are modifications and technically break the TOS. Use them your own risk.

### Credits
- [BetterDiscord](https://github.com/BetterDiscord/BetterDiscord)
- [OpenASAR](https://github.com/GooseMod/OpenAsar)
