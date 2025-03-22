# QR Code Generator

This is a simple web-based QR code generator that creates customizable QR codes linking to an account information page. The information page displays the account name, BML account number, MIB account number (optional), and Viber contact number.

## Features

- Generate QR codes directly in the browser - no server required
- QR codes link to an account information page with copy buttons
- Support for BML, MIB, and Viber account information
- Dark/light mode toggle for better user experience
- Responsive design that works on mobile and desktop
- Automatic QR code download with customizations
- All processing happens client-side with JavaScript
- Modern UI built with Tailwind CSS
- Tabbed interface for better organization of information
- Customization options including:
  - Custom letter overlay in the center of the QR code
  - Custom color selection with color picker
  - Custom message to be displayed under the QR code

## Usage

1. Simply open `index.html` in a web browser
2. Fill in the account information in the "Info" tab:
   - Account Name (required) - same as the name in BML or MIB account
   - BML Account Number (required if MIB not provided)
   - MIB Account Number (required if BML not provided)
   - Viber Account Number (required)
3. Switch to the "Customize QR" tab to set appearance options:
   - Business Name (required) - will appear above the QR code
   - Letter (optional) - will appear in the center of the QR code
   - Message (optional) - will appear below the QR code
   - QR Code Color - choose any color using the color picker
4. Click "Generate QR Code"
5. The QR code will be automatically downloaded to your device
6. A confirmation message will be displayed on the page

## How It Works

1. The QR code contains a URL to the `business.html` page with account information encoded as URL parameters
2. When scanned, the QR code opens a web browser to display the account information
3. The information page displays all the details with copy buttons for easy sharing
4. The page is styled with a responsive design and features dark/light mode toggle
5. The QR code includes customizations such as your chosen letter in the center and your selected color

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
- Input type "color" for the color picker 