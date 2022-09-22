from rtnsns import SUBRTNSBW
import time

sub = SUBRTNSBW(50)

print('Version Tag 0.6.4 installed using otaupdater') 
sub.blink_cnt(3)

sub.Redon()
print("  Congratulations if you can read this  ")
time.sleep(5)
sub.Redoff()
