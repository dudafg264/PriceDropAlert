# Amazon Price Alert

A Python script that monitors the price of a product on Amazon and sends an email notification when the price drops below a specified threshold.

## Features

- Scrapes the product page from Amazon.
- Extracts the product price.
- Sends an email notification if the price is below $100.
- Uses environmental variables for email credentials, ensuring that sensitive data is not exposed in the code.

## Prerequisites

- Python 3.x
- Libraries:
  - `requests`
  - `beautifulsoup4`
  - `lxml`
  - `smtplib`

To install the required libraries, use:

```bash
pip install requests beautifulsoup4 lxml
```

## Setting Up

1. **Clone this repository**:
   ```bash
   git clone https://github.com/yourusername/amazon-price-alert.git
   cd amazon-price-alert
   ```

2. **Set up your environment variables**:
   - `MY_EMAIL`: Your email address used for sending notifications.
   - `PASSWORD`: Your email password or app-specific password (recommended if you're using Gmail with 2FA enabled).

   You can set these environment variables in your terminal or create a `.env` file (make sure to add `.env` to `.gitignore`).

   Example:
   ```bash
   export MY_EMAIL="your-email@gmail.com"
   export PASSWORD="your-email-password"
   ```

3. **Edit the script**:
   - Update the `URL` variable in the script to the Amazon product page URL you want to monitor.
   - You can modify the price threshold (currently set to $100) in the code as needed.

## Usage

Run the script in your terminal:

```bash
python price_alert.py
```

If the price of the product is below the specified threshold, you will receive an email notification with a link to the product.

## Example Output

```
Email sent successfully!
```

If the price is higher than the threshold, the script will print:

```
The price is higher than $100.
```

## Notes

- Ensure that your email account allows less secure apps (for Gmail, you may need to generate an "App Password" if using two-factor authentication).
- Make sure the Amazon page structure does not change significantly, or the script may fail to parse the correct price.


---