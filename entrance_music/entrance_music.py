from signal import pause
from subprocess import PIPE, Popen, run
from time import sleep

from gpiozero import MotionSensor

sleep(600)  # This gives you 10 minutes to leave your home
pir = MotionSensor(24)

while True:
    p1 = Popen(["ping", "-c", "1", "192.168.43.178"], stdout=PIPE)
    stdout_value = p1.communicate()[0]
    if b'Destination Host Unreachable' not in stdout_value:
        break
    sleep(2)

sleep(5)

pir.wait_for_motion()
run("mpg123 ./entrancemusic/'mononoke.mp3'", shell=True)
