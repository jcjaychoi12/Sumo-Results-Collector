from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def main() -> None:
    url: str = "https://www.sumo.or.jp/ResultBanzuke/table/"
    chrome_options: Options = Options()
    chrome_options.add_argument("--headless=new")
    driver: WebDriver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get(url)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "table")))
        soup: BeautifulSoup = BeautifulSoup(driver.page_source, "html.parser")
        create_html_file(soup.prettify())
    except Exception as e:
        print(f"[Error] Failed to access {url}\n\n{e}")
    finally:
        driver.quit()

    return


def create_html_file(html: str, filename: str = "source.html") -> None:
    if filename[-5:] != ".html":
        filename += ".html"
    try:
        with open(filename, mode="w", encoding="utf-8") as file:
            file.write(html)
        print(f"[Success] Created {filename}\n")
    except Exception as e:
        print(f"[Error] Failed to create {filename} file\n\n{e}")
    return


if __name__ == "__main__":
    main()