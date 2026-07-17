#!/bin/bash
rm -Rf output/*
cp -R styles output
mkdir output/input
cp -R input/svg output/input
cp input/pdf/*.svg input/svg
python build.py
