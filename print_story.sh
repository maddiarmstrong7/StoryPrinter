#!/bin/bash

#fetches story

python3 fetch.py > story.txt
lp story.txt
