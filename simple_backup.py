#!/usr/bin/env python3
# coding=utf-8

import logging
import os
import ruamel.yaml
import shutil
from datetime import datetime

def main():
    backup_script_path = os.path.dirname(os.path.realpath(__file__))
    yaml = ruamel.yaml.YAML()
    try:
        with open(f'{backup_script_path}/conf.yaml', 'r') as yml_file:
            conf = ruamel.yaml.safe_load(yml_file)
    except FileNotFoundError as e:
        logger.error(e)

    source_dir = conf['backup']['source']
    target_dir = conf['backup']['target']
    log_dir = conf['backup']['log']

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s: %(message)s')
    file_handler = logging.FileHandler(log_dir)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    datetime_string = datetime.now().strftime("%m-%d-%y_%H-%M-%S")

    try:
        backup = shutil.copytree(source_dir, f'{target_dir}/{datetime_string}')
        logger.info(f"new backup: {backup}")
    except FileExistsError as e:
        logger.error(e)

if __name__ == '__main__':
    main()
