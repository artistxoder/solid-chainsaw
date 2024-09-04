import time
import requests
import json
import socket
import subprocess
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306

# Initialize the display
serial = i2c(port=1, address=0x3C)  # Update if different address is found
device = ssd1306(serial)

def get_ip_address():
    """Get the IP address of the Raspberry Pi."""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        s.connect(('10.254.254.254', 1))  # Doesn't need to be reachable
        ip = s.getsockname()[0]
    except Exception:
        ip = 'No IP found'
    finally:
        s.close()
    return ip

def get_uptime():
    """Get the system uptime."""
    uptime_output = subprocess.check_output("uptime -p", shell=True)
    return uptime_output.decode("utf-8").strip()

def show_system_status():
    """Display system IP address and uptime on the OLED."""
    ip_address = get_ip_address()
    uptime = get_uptime()

    with canvas(device) as draw:
        draw.text((0, 0), "System Status", fill="white")
        draw.text((0, 20), f"IP: {ip_address}", fill="white")
        draw.text((0, 40), f"Uptime: {uptime}", fill="white")
    
    time.sleep(5)  # Show for 5 seconds

def reset_display():
    with canvas(device) as draw:
        draw.rectangle(device.bounding_box, outline="white", fill="black")

def read_price(stock_name):
    try:
        http_request_address = f"https://finnhub.io/api/v1/quote?symbol={stock_name}&token=YOUR_API_KEY"
        response = requests.get(http_request_address)
        data = response.json()

        previous_close_price = data["pc"]
        current_price = data["c"]
        difference_in_price = ((current_price - previous_close_price) / previous_close_price) * 100.0

        with canvas(device) as draw:
            draw.text((0, 0), f"{stock_name}", fill="white")
            draw.text((0, 20), f"{current_price:.2f} USD", fill="white")
            draw.text((0, 40), f"{difference_in_price:.2f}%", fill="white")

    except Exception as e:
        with canvas(device) as draw:
            draw.text((0, 0), "Error fetching data", fill="white")
            draw.text((0, 20), str(e), fill="white")

def main():
    # Show system status first
    show_system_status()

    # Then proceed to display stock prices
    while True:
        read_price("AAPL")   # Apple
        time.sleep(5)

        read_price("AMZN")   # Amazon
        time.sleep(5)

        read_price("GOOGL")  # Google
        time.sleep(5)

        read_price("MSFT")   # Microsoft
        time.sleep(5)

        read_price("INTC")   # Intel
        time.sleep(5)

        read_price("NVDA")   # Nvidia
        time.sleep(5)

        read_price("AMD")    # AMD
        time.sleep(5)

if __name__ == "__main__":
    main()
