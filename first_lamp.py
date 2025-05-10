import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
LED_PIN = 17  # GPIO 17, physischer Pin 11

GPIO.setup(LED_PIN, GPIO.OUT)

try:
    while True:
        GPIO.output(LED_PIN, GPIO.HIGH)  # LED an
        time.sleep(1)                    # 1 Sekunde warten
        GPIO.output(LED_PIN, GPIO.LOW)   # LED aus
        time.sleep(1)                    # 1 Sekunde warten
except KeyboardInterrupt:
    GPIO.cleanup()