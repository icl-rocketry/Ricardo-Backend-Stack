#!/bin/bash

# Throw error if any command fails
set -e

# Ensure working directory matches script location
cd "$(dirname "$0")"

# Ensure script not running as root
if [[ "$EUID" == 0 ]]; then
    echo "Please do not run as superuser"
    exit
fi

# Set environment file
ENV_FILE=.env

# Set log file (and clear)
LOG_FILE=dirty-provision.log
>$LOG_FILE

# Print start message
echo "Ricardo-Backend-Stack dirty provisioning script" |
    tee -a $LOG_FILE
echo "WARNING: This script is not meant for production deployment" |
    tee -a $LOG_FILE

# Ask user whether to proceed
read -r -p "Do you wish to continue? [y/N] " response
echo "Do you wish to continue? [y/N] $response" >>$LOG_FILE
if [[ "$response" =~ ^([yY][eE][sS]|[yY])$ ]]; then
    true
else
    exit
fi
echo "" |
    tee -a $LOG_FILE

# Set variables
# NOTE: UID already set
echo "Setting variables..." |
    tee -a $LOG_FILE
GID=$UID
read -p "Backend domain: " RICARDO_BACKEND_DOMAIN
read -p "Serial path: " SERIAL_PATH
echo "" |
    tee -a $LOG_FILE

# Request sudo password
sudo -v

# Update packages
echo "Updating packages..." |
    tee -a $LOG_FILE
sudo apt-get update 2>&1 |
    sed 's/^/  /' |
    tee -a $LOG_FILE
echo "" |
    tee -a $LOG_FILE

# Upgrade packages
echo "Upgrading packages..." |
    tee -a $LOG_FILE
sudo apt-get upgrade -y 2>&1 |
    sed 's/^/  /' |
    tee -a $LOG_FILE
echo "" |
    tee -a $LOG_FILE

# Install Docker
if [ -x "$(command -v docker)" ]; then
    # Docker already installed
    echo "Docker already installed..." |
        tee -a $LOG_FILE
    echo "" |
        tee -a $LOG_FILE
else
    # Install Docker
    echo "Installing Docker..." |
        tee -a $LOG_FILE
    curl https://get.docker.com 2>&1 |
        bash |
        sed 's/^/  /' |
        tee -a $LOG_FILE
    echo "" |
        tee -a $LOG_FILE

    # Ensure Docker group exists
    echo "Creating Docker group..." |
        tee -a $LOG_FILE
    sudo groupadd docker 2>&1 |
        tee -a $LOG_FILE
    echo "" |
        tee -a $LOG_FILE

    # Add user to Docker group
    echo "Adding user to Docker group..." |
        tee -a $LOG_FILE
    sudo usermod -aG docker $USER 2>&1 |
        tee -a $LOG_FILE
    echo "" |
        tee -a $LOG_FILE
fi

# Generate environment file
echo "Generating environment file..." |
    tee -a $LOG_FILE
cat >$ENV_FILE <<EOF
UID=$UID
GID=$UID
RICARDO_BACKEND_DOMAIN=$RICARDO_BACKEND_DOMAIN
SERIAL_PATH=$SERIAL_PATH
EOF
echo "" |
    tee -a $LOG_FILE

# Pull images
# NOTE: Output not saved from pull command
echo "Pulling images..." |
    tee -a $LOG_FILE
docker compose pull 2>&1 |
    sed 's/^/  /' |
    tee -a $LOG_FILE
echo "" |
    tee -a $LOG_FILE

# Build images
echo "Building images..." |
    tee -a $LOG_FILE
docker compose --progress plain build 2>&1 |
    sed 's/^/  /' |
    tee -a $LOG_FILE
echo "" |
    tee -a $LOG_FILE
