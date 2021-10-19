# this program is written by Vishal Chopade
# any questions can be answered here.

import time
from pythonping import ping
import speedtest  # pip install speedtest-cli
import sys

time_to_check_ping = 300
time_to_check_uplink = 900
filename = "log_Speed.txt"

doPing = False
doUpStream = False

string_to_push = ""

# pip install pythonping
print("Speed and ping tester has started, every 5 and 15 mins ping and uplink will be tested resp.")
while True:
    try:
        print("time: ",time.ctime(), end = '\r')

        if int(time.time()) % time_to_check_ping == 0 or doPing:
            try:
                doPing = False
                #doUpStream = True
                st_demo = ping('8.8.8.8')
                string_to_push = "Time: {}, packet lost: {}\n".format(time.ctime(), st_demo.packets_lost)
            except Exception as ex:
                print("[ Exception 1] ", ex)
                string_to_push = "Time: {}, error in ping: {}\n".format(time.ctime(), str(ex))

            with open(filename, 'a') as log_Internet:
                try:
                    log_Internet.write(string_to_push)
                    print("Ping posted.", string_to_push)
                except Exception as ex:
                    print("[ Exception 1] ", ex)
                    pass

        elif int(time.time()) % time_to_check_uplink == 0:
            try:
                doPing = True
                #doUpStream = False
                st = speedtest.Speedtest()
                upload_speed_MBPS = st.upload()
                upload_speed_MBPS = upload_speed_MBPS/(8*1000000)
                string_to_push = "Time: {}, UPlink(MBps): {:.2f}\n".format(time.ctime(), upload_speed_MBPS)
            except Exception as ex:
                print("[ Exception 2] ", ex)
                string_to_push = "Time: {}, error in UPlink: {}\n".format(time.ctime(), str(ex))
                pass

            with open(filename, 'a') as log_Internet:
                try:
                    log_Internet.write(string_to_push)
                    print("Uplink posted. ", string_to_push)
                except Exception as ex:
                    print("[ Exception 2] ", ex)
                    pass

    except KeyboardInterrupt:
        print("keyboard Interrupt, Exit")
        sys.exit()

