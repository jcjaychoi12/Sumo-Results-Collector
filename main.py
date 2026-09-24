from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def main() -> None:
    url: str = "https://www.sumo.or.jp/ResultBanzuke/table/"
    chrome_options: Options = Options()
    chrome_options.add_argument("--headless")
    driver: WebDriver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get(url)
        soup: BeautifulSoup = BeautifulSoup(driver.page_source, "html.parser")
        create_html_file(soup.prettify())
    except Exception as e:
        print(f"[Error] Failed to access {url}\n\n{e}")
    finally:
        driver.quit()

    return


def create_html_file(html: str) -> None:
    try:
        with open("source.html", mode="w", encoding="utf-8") as file:
            file.write(html)
        print("[Success] Created source.html")
    except Exception as e:
        print(f"[Error] Failed to create source.html file\n\n{e}")
    return


if __name__ == "__main__":
    main()