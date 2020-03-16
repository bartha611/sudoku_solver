from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from svgDict import svg
from solve import backtrack


def main():
    board = []
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.sudoku.com")
    try:
        elements_present = EC.presence_of_all_elements_located(
            (By.CLASS_NAME, "game-cell"))
        WebDriverWait(driver, 5).until(elements_present)
        for row in driver.find_elements_by_class_name('game-row'):
            rowToAppend = []
            for element in row.find_elements_by_class_name("game-cell"):
                try:
                    path = element.find_element_by_tag_name("path")
                    d = path.get_attribute("d")
                    rowToAppend.append(svg[d])
                except:
                    rowToAppend.append("")
            board.append(rowToAppend)
        backtrack(board)
        index = 0
        for element in driver.find_elements_by_class_name('game-cell'):
            if "game-value" in element.get_attribute("class"):
                index += 1
                continue
            else:
                element.click()
                for number in driver.find_elements_by_class_name("numpad-item"):
                    if number.get_attribute("data-value") == board[index // 9][index % 9]:
                        number.click()
                index += 1
        print(board)

    except TimeoutException:
        print("couldn't locate cells")


if __name__ == "__main__":
    main()
