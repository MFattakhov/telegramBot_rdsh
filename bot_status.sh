#!/bin/bash
FILE='RDSHa'
DIRECTORY='/root/telebot/RDSHa/log/2019'
PAUSE='15s'

while [ true ] #если ИСТИНА, цикл работает
do

BOT_NAME='telebot_rdsha'
STATUS="$(systemctl is-active $BOT_NAME)"
DATE=$(date +%F)
TIME=$(date +%T)
echo "$DATE $TIME | Service $BOT_NAME status - $STATUS" >> $DIRECTORY/$FILE-$DATE.log

if [[ $STATUS == 'active' ]]
then
  echo #заглушка
else
  echo 'Перезагрузка сервиса Telebot'
  DATE=$(date +%F)
  TIME=$(date +%T)
  echo "$DATE $TIME | Service $BOT_NAME RESTARTED!!!" >> $DIRECTORY/$FILE-$DATE.log
  systemctl restart $BOT_NAME
fi

sleep $PAUSE
done

exit 0
