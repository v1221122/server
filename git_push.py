#!/usr/bin/python3

import os
import subprocess

os.chdir("/srv/http/")
subprocess.call("git add --all", shell=True)
subprocess.call('git commit -m "daily"', shell=True)
subprocess.call("git push git master", shell=True)

os.chdir("/php_modules/")
subprocess.call("git add --all", shell=True)
subprocess.call('git commit -m "daily"', shell=True)
subprocess.call("git push git master", shell=True)
