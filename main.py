import os
import csv
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def measure_network_speed(name="wyniki", repeats=10, interval=60, headless=False):
    file_exists = os.path.isfile(f'{name}.csv')
    if not file_exists:
        with open(f'{name}.csv', mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Data", "Opóźnienie [ms]", "Pobieranie [Mb/s]", "Wysyłanie [Mb/s]"])

    for i in range(repeats):
        driver = None
        try:
            options = Options()

            if headless:
                options.add_argument("--headless=new")
            driver = webdriver.Chrome(options=options)
            driver.get("https://www.speedtest.pl")
            wait = WebDriverWait(driver, 120)

            try:
                cookie_button = wait.until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[2]/div[2]/button[1]'))
                )
                cookie_button.click()

            except Exception as e:
                print("Nie udało się kliknąć zgody:", e)

            try:
                start_button = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="tester"]/div[1]/div/div/div/div[1]')))
                start_button.click()
                print(f"▶️ Rozpoczęto pomiar nr. {i+1}.")

                ping_result = wait.until(EC.visibility_of_element_located(
                    (By.XPATH, '/html/body/div[1]/main/div/div[2]/div[2]/div[1]/div/div[1]/div[4]')
                ))
                download_result = wait.until(EC.visibility_of_element_located(
                    (By.XPATH, '/html/body/div[1]/main/div/div[2]/div[2]/div[1]/div/div[2]/div[4]/div')
                ))
                upload_result = wait.until(EC.visibility_of_element_located(
                    (By.XPATH, '/html/body/div[1]/main/div/div[2]/div[2]/div[1]/div/div[3]/div[4]/div/span')
                ))

                wait.until(lambda d: ping_result.text.strip() != "")
                wait.until(lambda d: download_result.text.strip() != "")
                wait.until(lambda d: upload_result.text.strip() != "")

                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                ping = ping_result.text.strip()
                download = download_result.text.strip()
                upload = upload_result.text.strip()

                print(f"📶 Wyniki pomiaru nr. {i+1}:")
                print("Opóźnienie [ms]:", ping)
                print("Pobieranie [Mb/s]:", download)
                print("Wysyłanie [Mb/s]:", upload)

                with open(f'{name}.csv', mode='a', newline='', encoding='utf-8') as file:
                    writer = csv.writer(file)
                    writer.writerow([timestamp, ping, download, upload])

            except Exception as e:
                print("❌ Nie udało się odczytać wyników:", e)
        except Exception as e:
            print("❌ Nie udało się odczytać wyników:", e)
        finally:
            if i == repeats-1:
                print(f"\n✅ Koniec wykonywania pomiarów.")
            driver.quit()

        if i < repeats-1:
            print(f"\nOczekiwanie {interval}s przed kolejnym pomiarem.\n")
            time.sleep(interval)

if __name__ == "__main__":
    measure_network_speed()
