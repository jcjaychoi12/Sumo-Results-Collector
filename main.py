from bs4 import BeautifulSoup
from selenium import webdriver


def main() -> None:
    url: str = "https://www.sumo.or.jp/ResultBanzuke/table/"
    driver: WebDriver = webdriver.Chrome()

    try:
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        create_html_file(soup.prettify())
    except Exception as e:
        print(f"[Error] Failed to access {url}\n\n{e}")
    finally:
        driver.quit()


def create_html_file(html: str) -> None:
    with open("source.html", mode="w", encoding="utf-8") as file:
        file.write(html)
    return


if __name__ == "__main__":
    main()