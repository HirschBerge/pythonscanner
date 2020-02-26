#!/bin/sh
echo "Changing permissions"
sudo chmod +x *
sleep 2
echo "Enabling anywhere usage"
sleep 2
sudo ln -s $PWD/scanner.py /usr/local/bin/scanner
echo "... and done!"
