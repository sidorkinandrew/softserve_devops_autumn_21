#! /bin/bash

USER=moodlesuper
DB=moodle

currentTime=$(/bin/date '+%Y_%m_%d_%H_%M_%S')
FNAME="moodle_$currentTime.sql"

echo "$currentTime: starting '$DB' DB backup into $FNAME"
mysqldump $DB -u $USER -p > $FNAME
