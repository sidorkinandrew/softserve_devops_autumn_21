sudo apt-get update
sudo apt-get remove --purge man-db -y
sudo apt-get install apache2 -y
sudo systemctl start apache2