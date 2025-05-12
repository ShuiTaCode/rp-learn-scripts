import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
LED_PIN = 17
GPIO.setup(LED_PIN, GPIO.OUT)

try:
    frequency = 10  # Startfrequenz in Hz
    max_frequency = 100  # Obergrenze, falls du eine willst
    increase_interval = 10  # Alle 10 Sekunden Frequenz erhöhen
    last_increase_time = time.time()

    while True:
        # Berechne die Periodendauer basierend auf der aktuellen Frequenz
        period = 1.0 / frequency
        on_time = period / 2  # 50% Duty Cycle
        off_time = period / 2

        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(on_time)
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(off_time)

        # Frequenz alle 10 Sekunden um 1 Hz erhöhen
        if time.time() - last_increase_time >= increase_interval:
            frequency += 1
            last_increase_time = time.time()
            print(f"Frequenz erhöht auf: {frequency} Hz")

            if frequency > max_frequency:
                frequency = max_frequency  # Deckeln, wenn gewünscht

except KeyboardInterrupt:
    GPIO.cleanup()
