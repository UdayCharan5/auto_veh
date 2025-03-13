import RPi.GPIO as GPIO
import time

# GPIO pin definitions for the encoders
LEFT_ENCODER_A = 17
LEFT_ENCODER_B = 18
RIGHT_ENCODER_A = 22
RIGHT_ENCODER_B = 23

# Initialize tick counters
left_ticks = 0
right_ticks = 0

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(LEFT_ENCODER_A, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LEFT_ENCODER_B, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(RIGHT_ENCODER_A, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(RIGHT_ENCODER_B, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def update_left_encoder(channel):
    global left_ticks
    if GPIO.input(LEFT_ENCODER_B):
        left_ticks += 1
    else:
        left_ticks -= 1

def update_right_encoder(channel):
    global right_ticks
    if GPIO.input(RIGHT_ENCODER_B):
        right_ticks += 1
    else:
        right_ticks -= 1

# Attach interrupts
GPIO.add_event_detect(LEFT_ENCODER_A, GPIO.RISING, callback=update_left_encoder)
GPIO.add_event_detect(RIGHT_ENCODER_A, GPIO.RISING, callback=update_right_encoder)

# Main loop
try:
    print("Reading encoder values. Press Ctrl+C to stop.")
    while True:
        print(f"Left encoder ticks: {left_ticks}, Right encoder ticks: {right_ticks}")
        time.sleep(0.1)

except KeyboardInterrupt:
    print("\nExiting...")
    GPIO.cleanup()
