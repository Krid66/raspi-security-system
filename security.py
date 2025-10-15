import RPi.GPIO as GPIO
import time

PIR_PIN = 17
BUZZER_PIN = 18
BUZZER_FREQUENCY = 1000
BUZZER_DURATION = 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

motion_detected = False

print("ระบบกันขโมยเริ่มทำงาน...")

try:
    while True:
        if GPIO.input(PIR_PIN):
            if not motion_detected:
                print("ตรวจพบการเคลื่อนไหว!")
                # ใช้ PWM แบบ local object แทน global
                buzzer = GPIO.PWM(BUZZER_PIN, BUZZER_FREQUENCY)
                buzzer.start(50)
                time.sleep(BUZZER_DURATION)
                buzzer.stop()
                buzzer = None  # ป้องกัน destructor เรียก stop อีกครั้ง
                motion_detected = True
        else:
            motion_detected = False
        time.sleep(0.1)

except KeyboardInterrupt:
    print("หยุดการทำงาน...")

finally:
    GPIO.cleanup()
    print("GPIO ถูกเคลียร์เรียบร้อยแล้ว")
