from bs4 import BeautifulSoup
import requests
import lxml
import smtplib

URL = "https://www.amazon.com/Instant-Pot-Pressure-Steamer-Sterilizer/dp/B08PQ2KWHS/ref=dp_prsubs_1?pd_rd_i=B08PQ2KWHS&psc=1"
BUY_PRICE = 100
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/96.0.4664.45 Safari/537.36 ",
    "Accept-Language": "en-US,en;q=0.9"
}


response = requests.get(URL, headers=header)

soup = BeautifulSoup(response.content, "lxml")
# print(soup.prettify())

price = soup.find(class_="a-offscreen").get_text()
price_no_currency = price.split("$")[1]
price_in_float = float(price_no_currency)
print(price_in_float)

title = soup.find(id="productTitle").get_text().strip()
print(title)

if price_in_float < BUY_PRICE:
    message = f"{title} is now at {price}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login("panda.sas20@gmail.com", "4735o874ferkj")
        connection.sendmail(
            from_addr="panda.sas20@gmail.com",
            to_addrs="panda.sas20@gmail.com",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}"
        )

