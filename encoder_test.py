import RPi.GPIO as GPIO
import signal
import sys

# Initialize counters for both encoders
counter1 = 0
counter2 = 0

# Define GPIO pins for encoders
PIN1 = 27
PIN2 = 23

def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)

def count_encoder1(channel):
    global counter1
    counter1 += 1
    print("Encoder 1 - Number of pulses:", counter1)

def count_encoder2(channel):
    global counter2
    counter2 += 1
    print("Encoder 2 - Number of pulses:", counter2)

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    
    # Setup pins as inputs with pull-up resistors
    GPIO.setup(PIN1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(PIN2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    
    # Add event detection for both encoders
    GPIO.add_event_detect(PIN1, GPIO.FALLING, callback=count_encoder1, bouncetime=50)
    GPIO.add_event_detect(PIN2, GPIO.FALLING, callback=count_encoder2, bouncetime=50)

    # Setup signal handling for Ctrl+C
    signal.signal(signal.SIGINT, signal_handler)
    
    # Keep the program running
    signal.pause()
