import psutil
import sys

cpu = psutil.cpu_percent(interval=1)
print("Monitoring CPU usage...")

try:

    while True:
        cpu = psutil.cpu_percent(interval=1)
        if 40 < cpu < 90:
            print("Alert! CPU usage excceds threshold:40%")
        elif cpu > 90:
            print("Alert! CPU usage excceds threshold:90%")
        else:
            continue

except KeyboardInterrupt:
    print("\nProgram interrupted by user (Ctrl+C). Exiting.")
    sys.exit(0)

except Exception as e:
    print("An unexpected error occured: {e}")
    sys.exit(1)
