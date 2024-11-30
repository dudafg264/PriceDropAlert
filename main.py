from bs4 import BeautifulSoup
import requests
import smtplib
import os

my_email = os.getenv("my_email")
password = os.getenv("password")

URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

response = requests.get(URL, headers={"Accept-Language": "en-US", "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"})

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "lxml")
    full_price = soup.find(class_="a-price")

    if full_price:
        price = str(full_price.getText()).split("$")
        price_number = price[1]
        product_name = soup.find(id="title").getText()

        if float(price_number) < 100:
            msg = f"Subject: Special Price! \n\nDon't miss out! The product {product_name} is now available for the unbeatable price of ${price_number}!\nGrab yours now by clicking here: {URL}."
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=msg.encode("utf-8"))

            print("Email sent successfully!")

        else:
            print("The price is higher than $100.")

    else:
        print("Price not found on the page.")
