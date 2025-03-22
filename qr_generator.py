import argparse
import qrcode
import os
from pathlib import Path
import urllib.parse

def generate_qr_code(business_name, bml_account, viber_account, base_url):
    """
    Generate a QR code for the business information.
    The QR code links to the GitHub Pages URL with the business info as parameters.
    """
    # Create output directory if it doesn't exist
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)
    
    # URL encode parameters
    params = {
        'business': business_name,
        'bml': bml_account,
        'viber': viber_account
    }
    
    # Build full URL with parameters
    query_string = urllib.parse.urlencode(params)
    full_url = f"{base_url}?{query_string}"
    
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(full_url)
    qr.make(fit=True)
    
    # Create QR code image
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save QR code image with business name in filename
    safe_business_name = business_name.replace(" ", "_").lower()
    qr_file_path = output_dir / f"{safe_business_name}_qr_code.png"
    img.save(qr_file_path)
    
    return qr_file_path, full_url

def main():
    # Set up command-line argument parser
    parser = argparse.ArgumentParser(description="Generate QR code for business information")
    parser.add_argument("--business", required=True, help="Name of the business")
    parser.add_argument("--bml", required=True, help="BML account number")
    parser.add_argument("--viber", required=True, help="Viber account number (phone)")
    parser.add_argument("--url", default="https://sillyxilly.github.io/qr_code_generator_bml", 
                       help="Base URL of the GitHub Pages site (default: https://sillyxilly.github.io/qr_code_generator_bml)")
    
    # Parse arguments
    args = parser.parse_args()
    
    # Generate QR code
    qr_file, full_url = generate_qr_code(args.business, args.bml, args.viber, args.url)
    
    # Print results
    print(f"Generated QR code: {qr_file}")
    print(f"QR code URL: {full_url}")
    print(f"Scan the QR code to view business information")

if __name__ == "__main__":
    main() 