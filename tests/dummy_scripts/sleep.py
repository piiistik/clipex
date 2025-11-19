import time
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <seconds>")
        sys.exit(1)

    try:
        s = int(sys.argv[1])
        time.sleep(s)
    except ValueError:
        print("Please provide a valid integer for seconds.")
