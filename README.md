# QR Code Generator for Business Information

This tool generates QR codes that link to a web page displaying business information including name, BML account number, and Viber account number. The web page is hosted on GitHub Pages.

## Features

- Generate QR codes with business information encoded in URL parameters
- Single HTML page that can be used for multiple businesses
- Copy buttons for account numbers on the web page
- Customizable business name, BML account number, and Viber account number

## Requirements

- Python 3.6 or higher
- Required packages (install with `pip install -r requirements.txt`):
  - qrcode
  - pillow

## Setup

1. Clone this repository:
   ```
   git clone https://github.com/SillyXilly/qr_code_generator_bml.git
   cd qr_code_generator_bml
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

Run the script with the following command line arguments:

```
python qr_generator.py --business "Your Business Name" --bml "Your BML Account Number" --viber "Your Viber Number"
```

For example:
```
python qr_generator.py --business "My Coffee Shop" --bml "7730000012345" --viber "+9607123456"
```

## Output

The script will generate:
1. A QR code image in the `output` directory (named based on the business name)
2. The QR code contains a URL to the GitHub Pages site with your business information as parameters

When someone scans the QR code, they will see your business information page with copy buttons for the account numbers.

## How It Works

1. The Python script generates a QR code with a URL to the GitHub Pages site
2. The URL includes the business name, BML account number, and Viber number as query parameters
3. When scanned, the QR code opens a web browser with the GitHub Pages URL
4. The JavaScript on the page reads the URL parameters and displays the business information

## GitHub Pages Setup

The web page is hosted on GitHub Pages. To update the page:

1. Make changes to the `index.html` file
2. Commit and push changes to the repository
3. GitHub will automatically update the Pages site

## Customizing

You can customize the web page appearance by modifying the CSS in the `index.html` file. 