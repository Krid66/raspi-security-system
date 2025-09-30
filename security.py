import RPi.GPIO as GPIO
import time

# กำหนดพิน
PIR_PIN = 17
BUZZER_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

print("ระบบกันขโมยเริ่มทำงาน...")

try:
    while True:
        if GPIO.input(PIR_PIN):   # ถ้ามีการเคลื่อนไหว
            print("ตรวจพบการเคลื่อนไหว!")
            GPIO.output(BUZZER_PIN, GPIO.HIGH)  # เปิดเสียง buzzer
            time.sleep(1)
        else:
            GPIO.output(BUZZER_PIN, GPIO.LOW)   # ปิด buzzer
        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()
    print("หยุดการทำงาน")
