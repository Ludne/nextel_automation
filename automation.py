from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
from pprint import pprint
import chromedriver_binary

class NextelAutomation:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def read_file(self):
        json_list = '{"google-me": ["nextel", "telefonia do futuro", "selenium python"]}'
        return json.loads(json_list)

    def write_file(self, json_object):
        with open("output.json", "w") as json_file:
            json_file.write(json.dumps(json_object, ensure_ascii=False))

    def python_selenium_exam(self):
        get_words_json = self.read_file()

        final_result = []

        for key in get_words_json["google-me"]:
            self.driver.get("https://google.com.br/")
            self.driver.find_element_by_name("q").send_keys(key + Keys.ENTER)

            results = []

            for i in range(3):
                result_item = self.driver.find_element_by_xpath("(//a/h3)[{}]".format(i+1))
                results.append(result_item.text)

            final_result.append({key: results})

        get_words_json["google-me"] = final_result
        pprint(get_words_json)
        self.write_file(get_words_json)


if __name__ == "__main__":
    automation = NextelAutomation()
    automation.python_selenium_exam()

