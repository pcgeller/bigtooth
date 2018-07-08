import signal
import time

class cleanerUpper:
  kill_now = False
  def __init__(self):
    signal.signal(signal.SIGINT, self.exitAndClean)
    signal.signal(signal.SIGTERM, self.exitAndClean)

  def exitAndClean(self,signum, frame):
    self.kill_now = True

if __name__ == '__main__':
  cleaner = cleanerUpper()
  while True:
    time.sleep(1)
    print("Yada, yada, yada")
    if cleaner.kill_now:
      break

  print("Program shutdown cleanly.")
