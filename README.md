# QR Code Generator for Business Information

This is a simple web-based QR code generator that creates QR codes linking to a business information page. The business information page displays the business name, BML account number, MIB account number (optional), and Viber contact number.

## Features

- Generate QR codes directly in the browser - no server required
- QR codes link to a business information page with copy buttons
- Support for BML, MIB, and Viber account information
- Dark/light mode toggle for better user experience
- Responsive design that works on mobile and desktop
- Instant QR code preview and download
- All processing happens client-side with JavaScript
- Modern UI built with Tailwind CSS

## Usage

1. Simply open `index.html` in a web browser
2. Fill in the business information:
   - Business Name (required)
   - BML Account Number (required if MIB not provided)
   - MIB Account Number (required if BML not provided)
   - Viber Account Number (required)
3. Click "Generate QR Code"
4. The QR code will be displayed on the page
5. Click "Download QR Code" to save the image to your device

## How It Works

1. The QR code contains a URL to the `business.html` page with business information encoded as URL parameters
2. When scanned, the QR code opens a web browser to display the business information
3. The business page displays all the information with copy buttons for easy sharing
4. The page is styled with a responsive design and features dark/light mode toggle

## Hosting

You can:

1. Use the files locally, opening them directly in a browser
2. Host on any web server or static site hosting service (GitHub Pages, Netlify, etc.)
3. No backend or server-side processing is required

## Customizing

You can customize the appearance by modifying the Tailwind classes in the HTML files:
- `index.html` - The QR code generator page
- `business.html` - The business information display page

The project uses Tailwind CSS via CDN for styling, making it easy to modify the appearance by simply changing the utility classes in the HTML.

## Files

- `index.html` - The QR code generator interface
- `business.html` - The business information display page
- `logo/` - Directory containing logo images for display on the business page
  - `bml_logo.png` - Bank of Maldives logo
  - `mib_logo.png` - Maldives Islamic Bank logo
  - `viber_logo.png` - Viber logo

## Browser Compatibility

Works in all modern browsers that support:
- JavaScript ES6+
- HTML5 Canvas (for QR code generation)
- Flexbox layouts 