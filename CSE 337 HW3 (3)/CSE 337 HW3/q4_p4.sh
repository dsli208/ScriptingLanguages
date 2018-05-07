#!/bin/bash

cd $1
find $1 -type f -name '*.sh' | wc –l
