#!/bin/bash

mp4path="dataset/mp4"

for filename in dataset/mov/*.MOV; do
	base=$(basename "$filename" .MOV)
	ffmpeg -i "$filename" -vcodec h264 -acodec mp2 "${mp4path}/${base}.mp4"
done
