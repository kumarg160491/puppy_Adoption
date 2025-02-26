#!/bin/bash

# Update package lists
echo "Updating system packages..."
sudo apt update -y

# Install required dependencies
echo "Installing dependencies..."
sudo apt install -y ca-certificates curl gnupg

# Create directory for Docker's GPG key
sudo install -m 0755 -d /etc/apt/keyrings

# Add Docker's official GPG key
echo "Adding Docker GPG key..."
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo tee /etc/apt/keyrings/docker.asc > /dev/null
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add Docker repository
echo "Adding Docker repository..."
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Update package lists again
echo "Updating package lists after adding Docker repo..."
sudo apt update -y

# Install Docker
echo "Installing Docker..."
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin

# Enable and start Docker service
echo "Enabling and starting Docker service..."
sudo systemctl enable docker
sudo systemctl start docker

# Verify installation
echo "Docker installation complete. Verifying..."
docker --version

echo "Docker installed successfully! 🚀"

