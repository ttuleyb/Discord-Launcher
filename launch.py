import os
import time
import requests
import subprocess

if not os.path.exists("old_build_info.json"):
    oldBuildInfo = None #No  build info
else:
    with open("old_build_info.json", "r") as f:
        oldBuildInfo = f.read()

with open("/Applications/Discord.app/Contents/Resources/build_info.json") as f:
    buildInfo = f.read()

if oldBuildInfo != buildInfo:
    print("Hold on, Reinjecting BD after Discord update...")

    #Kill Discord
    os.system("killall Discord")

    #Clone or update BetterDiscord
    if os.path.exists("BetterDiscord"):
        #Update it
        os.system("cd BetterDiscord && git pull")
    else:
        #Clone it
        os.system("git clone https://github.com/BetterDiscord/BetterDiscord")

    commandsToExecute = ["cd BetterDiscord && ",
                         "pnpm recursive install && ", #Install dependencies
                         "pnpm run build && ", #Build
                         "pnpm run inject"] #Inject into stable
    payload = ""
    for command in commandsToExecute:
        payload += command

    os.system(payload)

    #Replace asar file with OpenASAR
    with open("/Applications/Discord.app/Contents/Resources/app.asar", "wb") as f: #Write as binary
        f.write(requests.get("https://github.com/GooseMod/OpenAsar/releases/download/nightly/app.asar").content)

    #Save build_info.json to old_build_info.json
    with open("old_build_info.json", "w") as f:
        f.write(buildInfo)

    #Launch discord
    os.system("open /Applications/Discord.app")

else:
    #Check if discord is open
    process = subprocess.Popen('pgrep Discord', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    my_pid, err = process.communicate() #Get PID of Discord

    processExists = my_pid != b''
    if processExists:
        #Kill Discord
        pid = str(my_pid.decode("utf-8")) #Convert bytes to string
        os.system("kill -9 " + pid)
        time.sleep(0.1)
    #Launch discord
    os.system("open /Applications/Discord.app")
