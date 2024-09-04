#!/bin/bash

# Define variables
REPO_URL="https://github.com/artistxoder/solid-chainsaw"
REPO_DIR="solid-chainsaw"
SCRIPT_PATH="/solid-chainsaw/stock.py"

# Update and upgrade the system
echo "Updating and upgrading the system..."
sudo apt-get update -y
sudo apt-get upgrade -y

# Install required system packages
echo "Installing system packages..."
sudo apt-get install -y python3-pip python3-smbus i2c-tools screen

# Install Python libraries
echo "Installing Python libraries..."
pip3 install requests luma.oled pillow

# Clone the repository
if [ -d "$REPO_DIR" ]; then
    echo "Repository already exists. Pulling latest changes..."
    cd $REPO_DIR
    git pull
else
    echo "Cloning repository..."
    git clone $REPO_URL
    cd $REPO_DIR
fi

# Set up the script to run at startup
echo "Setting up the script to run at startup..."
(crontab -l; echo "@reboot /usr/bin/python3 $SCRIPT_PATH") | crontab -

# Instructions for using screen
echo "Setup complete!"
echo "You can run the script in a screen session with the following commands:"
echo "  screen -S stock_display"
echo "  python3 $SCRIPT_PATH"
echo "To detach from the screen session, press Ctrl+A, then D."
echo "To reattach later, use: screen -r stock_display"

# Final message
echo "All done! Your stock price display setup is complete."

