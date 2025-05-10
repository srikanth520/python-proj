#!/usr/bin/python3
import os, sys
from global_constants import DB_NAME

# Catch before other imports to avoid confusing error msgs
if not os.path.exists(DB_NAME):
    sys.exit("ERROR: No database detected. Please execute setup.py first!")


def main():
    # Start Voice Recognition
    live_speech()


if __name__ == '__main__':
    main()
