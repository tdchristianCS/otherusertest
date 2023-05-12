from progress.bar import ChargingBar
import time

# max=100 means the number of steps in your process (100 makes sense as a percentage)
bar = ChargingBar('Processing', max=100)

# This number here should match the max=___ value above
for i in range(100):
    
    # Put your code here
    # This one is just busywork so the bar isn't instant for the demo
    time.sleep(0.025)

    # This tells the bar to update another step
    bar.next()
    