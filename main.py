from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path
import csv


def main() -> None:
    url: str = "https://www.sumo.or.jp/ResultBanzuke/table/"
    chrome_options: Options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.binary_location = str(Path.home() / r"AppData\Local\BraveSoftware\Brave-Browser\Application\brave.exe")
    driver: WebDriver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get(url)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "table")))

        soup: BeautifulSoup = BeautifulSoup(driver.page_source, "html.parser")
        banzuke_table = soup.find("tbody")
        for tag in banzuke_table.find_all(True):
            tag.attrs = {}

        headers_list = []
        for th in banzuke_table.find_all("th"):
            headers_list.append(th.get_text(strip=True))
        headers = ",".join(headers_list)
        
        table_list = [headers]
        for tr in banzuke_table.find_all("tr"):
            row_list = []
            for td in tr.find_all("td"):
                row_list.append(td.get_text(separator="::", strip=True))
            if len(row_list) != 0:
                table_list.append(",".join(row_list))
        table_csv = "\n".join(table_list)
        create_file(table_csv, "current_banzuke.csv")
        print(convert_csv_banzuke(Path(r"./localfiles/current_banzuke.csv")))
    except Exception as e:
        print(f"[Error] Failed to access {url}\n\n{e}")
    finally:
        driver.quit()

    return


def create_file(body: str, filename: str = "body.txt") -> None:
    try:
        local_file_path = Path.cwd() / "localfiles"
        local_file_path.mkdir(exist_ok=True)

        with open(local_file_path / filename, mode="w", encoding="utf-8") as file:
            file.write(body)
        print(f"[Success] Created {filename}\n")
    except Exception as e:
        print(f"[Error] Failed to create {filename} file\n\n{e}")
    return


def convert_csv_banzuke(file_path: Path) -> list:
    return_list: list = []  # {Shikona; Shushin; Heya; Status (opt)}
    with open(file_path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            rank: str = row["番付"]
            east: list = row["東"].split("::") # East doesn't need empty check as east slot is always filled
            west: list = row["西"].split("::") if row["西"] != "" else []

            if len(east) == 4:  # Status exists
                return_list.append({
                    "status": east[0],
                    "shikona": east[1],
                    "shushin": east[2],
                    "heya": east[3]
                })
            else:  # Status doesn't exist
                return_list.append({
                    "status": "",
                    "shikona": east[0],
                    "shushin": east[1],
                    "heya": east[2]
                })

            if len(west) > 0 and len(west) == 4:  # Status exists
                return_list.append({
                    "status": west[0],
                    "shikona": west[1],
                    "shushin": west[2],
                    "heya": west[3]
                })
            elif len(west) > 0:  # Status doesn't exist
                return_list.append({
                    "status": "",
                    "shikona": west[0],
                    "shushin": west[1],
                    "heya": west[2]
                })

    return return_list


if __name__ == "__main__":
    main()