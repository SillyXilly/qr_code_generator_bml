#!/bin/bash

# Make output directory if it doesn't exist
mkdir -p output

# Generate QR code for example business
python qr_generator.py --business "Coffee House" --bml "7730000012345" --viber "+9607123456"

echo "QR code generated! Check the output directory." 