#!/bin/bash

find $1 -mindepth 1 \( ! -regex '.*/\..*' \) -type d -exec sh -c 'for d; do touch "$d/.NOMEDIA"; done' _ {} +

