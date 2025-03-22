# Setting Up GitHub Pages

Follow these steps to enable GitHub Pages for your QR code generator:

1. Go to your GitHub repository: https://github.com/SillyXilly/qr_code_generator_bml

2. Click on the **Settings** tab at the top of the repository page.

3. In the left sidebar, click on **Pages** (under "Code and automation" section).

4. Under "Build and deployment" > "Source", select **Deploy from a branch**.

5. Under "Branch", select the **main** branch and keep the folder as **/(root)**.

6. Click **Save**.

7. GitHub will start building your GitHub Pages site. This may take a few minutes.

8. Once the site is published, you'll see a message saying "Your site is live at https://sillyxilly.github.io/qr_code_generator_bml/".

9. Your GitHub Pages site should now be accessible at: https://sillyxilly.github.io/qr_code_generator_bml/

## Testing Your Setup

1. Run the example script to generate a QR code:
   ```
   ./example.sh
   ```

2. Scan the generated QR code (located in the `output` directory).

3. The QR code should open a web browser and display the business information from the parameters.

## Troubleshooting

- If your site is not deploying, check the Actions tab in your GitHub repository to see if there are any errors.
- Make sure you have a `.nojekyll` file in your repository (we've already added this).
- If you make changes to the site, allow a few minutes for GitHub Pages to update after pushing the changes.

## Using Custom Domain (Optional)

If you want to use a custom domain instead of the default GitHub Pages URL:

1. Go to the Pages settings in your repository.
2. Under "Custom domain", enter your domain name.
3. Update your domain's DNS settings to point to GitHub Pages.
4. Update the QR generator script with your custom domain by using the `--url` parameter:
   ```
   python qr_generator.py --business "Your Business" --bml "123456" --viber "123456" --url "https://yourdomain.com"
   ``` 