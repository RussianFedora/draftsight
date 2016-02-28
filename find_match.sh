#!/bin/sh
for TARGET_FILES in $(ls -l $1 | grep -v ^d | cut --delimiter=: --fields=2 | cut --delimiter=\  --fields=2); do
    echo "$TARGET_FILES"
    sed -e "s|$(echo $TARGET_FILES)|#$(echo $TARGET_FILES)|g" -i $2 
done
