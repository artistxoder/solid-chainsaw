# Stock Price Display on Raspberry Pi

## Overview

This project features a Python script designed to display real-time stock prices on an OLED screen connected to a Raspberry Pi. The script fetches and displays stock data for major companies, including Apple, Amazon, Google, Microsoft, Intel, Nvidia, and AMD. Additionally, it shows system status information, such as the IP address and system uptime, upon startup.

## Features

* **Real-time Stock Prices**: Fetches and displays the latest stock prices and percentage changes for selected companies.
* **System Status Display**: Shows the Raspberry Pi's IP address and system uptime on the OLED display when the device boots up.
* **OLED Display Integration**: Utilizes the `luma.oled` library for rendering information on an OLED display connected via I2C.
* **Automated Startup**: Configured to run automatically on system startup using `crontab`.
* **Screen Session**: Use `screen` to keep the script running in the background or to manage multiple terminal sessions.

## Requirements

* Raspberry Pi with Raspbian or compatible OS
* OLED display (SSD1306) connected via I2C
* Python 3
* Required Python libraries:
  * `requests`
  * `luma.oled`
  * `Pillow`
* API key from Finnhub or other stock price providers
* `screen` (optional, for managing script execution)

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/your-repository.git
    cd your-repository
    ```

2. **Install Dependencies**:
    ```bash
    sudo apt-get update
    sudo apt-get install python3-pip python3-smbus i2c-tools screen
    pip3 install requests luma.oled pillow
    ```

3. **Update API Key**:
    * Edit `stock.py` and replace `YOUR_API_KEY` with your actual API key.

4. **Run the Script**:
    * You can run the script directly in a terminal:
        ```bash
        python3 stock.py
        ```

    * **Using `screen`**:
        * Start a new `screen` session:
            ```bash
            screen -S stock_display
            ```

        * Run the script inside the `screen` session:
            ```bash
            python3 stock.py
            ```

        * Detach from the `screen` session (leave it running in the background) by pressing `Ctrl+A`, then `D`.

        * To reattach to the `screen` session later:
            ```bash
            screen -r stock_display
            ```

5. **Set Up Automatic Startup**:
    * Add the script to `crontab` to run on reboot:
        ```bash
        crontab -e
        ```
      Add the following line:
        ```bash
        @reboot /usr/bin/python3 /path/to/your/stock.py
        ```

## Usage

* Upon boot, the OLED display will show system status information (IP address and uptime) for 5 seconds.
* After the initial display, the screen will cycle through stock prices for Apple, Amazon, Google, Microsoft, Intel, Nvidia, and AMD, updating every 5 seconds.

## Contributing

Feel free to fork this repository and submit pull requests. Issues and feature requests are welcome.

## License

This software is unlicensed. You can use, modify, and distribute it freely without restriction.


