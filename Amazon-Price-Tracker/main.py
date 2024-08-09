from bs4 import BeautifulSoup
import requests
import smtplib

EMAIL = "unsecureemail679@gmail.com"
PASSWORD = "qsal lhlp rfpg xhcy"
url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}
r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, "html.parser")
whole = soup.find(class_="a-price-whole")
frac = soup.find(class_="a-price-fraction")

if whole and frac:
    price = float(whole.getText() + frac.getText())
    if price < 100:
        prod_title = soup.find(id="productTitle")
        if prod_title:
            prod_title = prod_title.getText().strip()
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(EMAIL, PASSWORD)
                message = f"Subject:Amazon Price Alert!\n\n{prod_title} is now {price}\n{url}"
                connection.sendmail(
                    from_addr=EMAIL,
                    to_addrs="atijmahesh914@gmail.com",
                    msg=message.encode('utf-8')
                )
