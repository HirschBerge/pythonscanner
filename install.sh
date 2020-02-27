#!/bin/sh

echo "Correcting permissions!"
sudo chmod +x *
sleep 3
echo "Enabling ability to work anywhere."
sudo ln -s $PWD/scanner.py /usr/local/bin/scanner
sleep 3
echo "..."
sleep 1
echo "And done!"
