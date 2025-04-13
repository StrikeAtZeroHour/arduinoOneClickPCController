import serial
import webbrowser
import time

try:
    ser = serial.Serial('COM3', 9600, timeout=1)  # Replace COM3 with your Arduino's port
    print("Serial port opened successfully!")
except serial.SerialException as e:
    print(f"Error opening serial port: {e}")
    exit()

while True:
    try:
        line = ser.readline().decode('utf-8').strip()
        if "OPEN_YOUTUBE" in line:
            print("Trigger detected! Opening YouTube...")
            webbrowser.open("https://youtube.com")
            time.sleep(1)  # Debounce
    except UnicodeDecodeError:
        print("Received non-UTF-8 data. Skipping...")
    except KeyboardInterrupt:
        print("Exiting...")
        break
    except Exception as e:
        print(f"Error: {e}")

ser.close()