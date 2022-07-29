# backup_util
CLI directory backup utility.

## Installation
Download the project and install the dependencies (yaml):

`pip install -r requirements.txt`

## Usage
Set the log, source and target directories in the `conf.yaml` file. Give execution permission to the script, add the script to your PATH variable, and simply run it. You will get a logged result (whether successfull or if there is any error) to the log file specified in the conf.yaml file.

This utility is useful to run with a scheduler, like a cronjob. Works with Windows, MacOS, and Windows.