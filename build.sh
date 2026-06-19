#!/bin/bash
rm -Rf output/*
cp -R styles output
mkdir output/input
cp -R input/svg output/input
python build.py
