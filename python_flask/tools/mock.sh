#!/bin/bash

DIR=$(pwd)
cd "$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
export SECRET_KEY="tRxJwpyVLYQad3U3phqMUKXb3e4sPF"
python mock.py
cd $DIR
