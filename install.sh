#!/bin/sh
echo "Changing permissions"
sudo chmod +x *
sleep 2
echo "Enabling anywhere usage"
sleep 2
sudo cp scanner.py /usr/local/bin/scanner
echo "... and done!"
