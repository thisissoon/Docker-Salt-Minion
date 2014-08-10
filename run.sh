#!/bin/bash

#
# Salt-Minion Run Script
#

set -e

# Log Level
LOG_LEVEL=${LOG_LEVEL:-"error"}

# Run Salt as a Deamon
exec sudo /usr/bin/salt-minion --log-level=$LOG_LEVEL
