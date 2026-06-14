#!/usr/bin/env bash

cd "$(dirname "$0")"

if [ -n "$1" ]; then
    micromamba run -n sci python "./sim/$1/sim.py"
else
    micromamba run -n sci python "./sim/sim.py"
fi
