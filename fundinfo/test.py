import subprocess
import os
import time

down_url = r'''magnet:?xt=urn:btih:62847e43ad0226c8ed16d42b556625d68fd7640b&dn=[电影天堂www.dytt89.com]周处除三害-2024_HD国语中字.mp4'''

# subprocess.call(["Thunder.exe", "-StartType:DesktopIcon", "-Url:" + down_url])

os.system(r'"C:\Program Files (x86)\Thunder Network\Thunder\Program\Thunder.exe" {url}'.format(url=down_url))
# time.sleep(20)

