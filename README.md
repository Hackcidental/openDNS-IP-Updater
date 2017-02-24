# openDNS-IP-Updater
openDNS-IP-Updater is a simple script that allow to automate the updates of your IP to use the openDNS "Home Free" service. Since there is an official software for Windows, this is mainly aimed to be used on Linux.
## Usage
To start the script simply do:
```
python3 openDNS-IP-Updater.py
```
Notice that you must specify your eMail and your password direcly into the script at the moment.
If you want to increase or to decrease the time between every update you have to modify this line
```
time.sleep(1*60*60)
```
The number is in milliseconds.
