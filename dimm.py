import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
LED_PIN = 17
GPIO.setup(LED_PIN, GPIO.OUT)

try:
    while True:
        # Von langsam (1s) zu schnell (0.01s) -> Beschleunigung
        delay = 1.0
        while delay >= 0.01:
            GPIO.output(LED_PIN, GPIO.HIGH)
            time.sleep(delay)
            GPIO.output(LED_PIN, GPIO.LOW)
            time.sleep(delay)
            delay -= 0.05
            if delay < 0.01:
                delay = 0.01  # Untere Grenze setzen

        # Von schnell (0.01s) wieder zu langsam (1s) -> Verlangsamung
        while delay <= 1.0:
            GPIO.output(LED_PIN, GPIO.HIGH)
            time.sleep(delay)
            GPIO.output(LED_PIN, GPIO.LOW)
            time.sleep(delay)
            delay += 0.05
            if delay > 1.0:
                delay = 1.0  # Obere Grenze setzen

except KeyboardInterrupt:
    GPIO.cleanup()
