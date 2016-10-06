#!/usr/bin/env python3

import shlex, subprocess, urllib, urllib.request, time, datetime;


while True:
    def internet_on(reference):
        try:
            urllib.request.urlopen(reference, timeout=1)
            return True
        except  urllib.request.URLError:
            return False

        while internet_on("http://www.opendns.com/")==False: #Keep trying until a connection with the Internet is connected.
            time.sleep(9);

    #Update opendns IP address
    command=shlex.split("curl -u mail:password https://updates.opendns.com/nic/update");
    subprocess.call(command);
    print("");
    tm = time.asctime()
    print(tm)
    time.sleep(1*60*60) 
