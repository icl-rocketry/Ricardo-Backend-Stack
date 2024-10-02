#!/bin/bash

# Throw error if any command fails
set -e

# Logging functions
log() {
    cat >>$LOG_FILE
}
log_display() {
    cat |
        tee -a $LOG_FILE
}
log_display_indent() {
    cat |
        sed 's/^/  /' |
        log_display
}

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
    log_display
echo "WARNING: This script is not meant for production deployment" |
    log_display

# Ask user whether to proceed
read -r -p "Do you wish to continue? [y/N] " response
echo "Do you wish to continue? [y/N] $response" |
    log
if [[ "$response" =~ ^([yY][eE][sS]|[yY])$ ]]; then
    true
else
    exit
fi
echo "" |
    log_display

# Request sudo password
echo "Elevating permissions (using sudo caching)..." |
    log_display
sudo -v 2>&1 |
    log_display_indent
echo "" |
    log_display

# Set variables
# NOTE: UID already set
echo "Setting variables..." |
    log_display
GID=$UID
read -p "Repository branch: " BRANCH
read -p "Backend domain: " RICARDO_BACKEND_DOMAIN
read -p "Serial path: " SERIAL_PATH
echo "" |
    log_display

# Update repository
echo "Updating repository..." |
    log_display
git checkout $BRANCH 2>&1 |
    log_display_indent
git pull 2>&1 |
    log_display_indent
echo "" |
    log_display

# Update submodules
echo "Updating submodules..." |
    log_display
git submodule update --init --recursive 2>&1 |
    log_display_indent
echo "" |
    log_display

# Update packages
echo "Updating packages..." |
    log_display
sudo apt-get update 2>&1 |
    log_display_indent
echo "" |
    log_display

# Upgrade packages
echo "Upgrading packages..." |
    log_display
sudo apt-get upgrade -y 2>&1 |
    log_display_indent
echo "" |
    log_display

# Install Docker
if [ -x "$(command -v docker)" ]; then
    # Docker already installed
    echo "Docker already installed..." |
        log_display
    echo "" |
        log_display
else
    # Install Docker
    echo "Installing Docker..." |
        log_display
    curl https://get.docker.com 2>&1 |
        bash |
        log_display_indent
    echo "" |
        log_display

    # Ensure Docker group exists
    echo "Creating Docker group..." |
        log_display
    sudo groupadd docker 2>&1 |
        log_display_indent
    echo "" |
        log_display

    # Add user to Docker group
    echo "Adding user to Docker group..." |
        log_display
    sudo usermod -aG docker $USER 2>&1 |
        log_display_indent
    echo "" |
        log_display
fi

# Generate environment file
echo "Generating environment file..." |
    log_display
cat >$ENV_FILE <<EOF
UID=$UID
GID=$UID
RICARDO_BACKEND_DOMAIN=$RICARDO_BACKEND_DOMAIN
SERIAL_PATH=$SERIAL_PATH
EOF
echo "" |
    log_display

# Pull images
# NOTE: Output not saved from pull command
echo "Pulling images..." |
    log_display
docker compose pull 2>&1 |
    log_display_indent
echo "" |
    log_display

# Build images
echo "Building images..." |
    log_display
docker compose --progress plain build 2>&1 |
    log_display_indent
echo "" |
    log_display
