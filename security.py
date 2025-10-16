import RPi.GPIO as GPIO
import time
import requests
import json

# --- ตั้งค่าขา GPIO ---
PIR_PIN = 17
BUZZER_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

# สร้าง PWM สำหรับ Passive Buzzer
pwm = GPIO.PWM(BUZZER_PIN, 1000)  # 1kHz

# --- ตั้งค่า LINE Messaging API ---
ACCESS_TOKEN = 'TokenLINE'
USER_ID = 'UserID'

def send_line_message(message):
    url = "https://api.line.me/v2/bot/message/push"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }
    data = {
        "to": USER_ID,
        "messages": [{"type": "text", "text": message}]
    }
    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        if response.status_code == 200:
            print("ส่งข้อความสำเร็จ")
        else:
            print("เกิดข้อผิดพลาด:", response.status_code, response.text)
    except Exception as e:
        print("ไม่สามารถส่งข้อความได้:", e)

# --- เริ่มระบบตรวจจับ ---
print("🚨 ระบบตรวจจับเริ่มทำงานแล้ว...")

try:
    while True:
        if GPIO.input(PIR_PIN):
            print("ตรวจพบการเคลื่อนไหว!")
            pwm.start(50)  # duty cycle 50%
            send_line_message("🚨 ตรวจพบการเคลื่อนไหวในพื้นที่!")
            time.sleep(1)
            pwm.stop()
            time.sleep(5)
        else:
            time.sleep(0.1)

except KeyboardInterrupt:
    print("ปิดระบบแล้ว")

finally:
    pwm.stop()
    GPIO.cleanup()
