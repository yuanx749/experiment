#!/bin/bash

log_file=./logs/$(date +%Y%m%d-%H%M%S).log
python -u ${1} 2>&1 | tee $log_file