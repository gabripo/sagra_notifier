import re
import requests
import time
import bs4

RETRY_PAUSE_S = 1
MAX_RETRIES = 5
VALID_RESPONSE_STATUS = 200
class SagraPageContent:
    def __init__(
            self,
            url: str,
            ):
        self.content = None
        self.url = None

        self.fetch_sagra_content(url)

    def fetch_sagra_content(self,url: str = None):
        if not SagraPageContent.is_valid_url(url):
            print(f"Invalid sagra-URL given: {url}")
            return
        
        response = SagraPageContent.get_webpage_response(
            url=url,
        )

        if response:
            soup = bs4.BeautifulSoup(response.text, 'html.parser')

            sagra_html_class = "col-sm-6 col-md-4"
            sagra_elements = soup.find_all(class_=sagra_html_class)

            self.content = []
            for sagra in sagra_elements:
                sagra_info = SagraPageContent.parse_sagra_info(
                    sagra_text=sagra.text,
                )
                if sagra_info:
                    self.content.append(sagra_info)

    @staticmethod
    def parse_sagra_info(sagra_text: str):
        sagra_lines = [
            line.strip()
            for line in sagra_text.split('\n')
            if line.strip() != ''
        ]

        sagra_info = {}
        if len(sagra_lines) == 4:
            sagra_info['month'] = sagra_lines[0]
            sagra_info['event'] = sagra_lines[1]
            sagra_info['date'] = sagra_lines[2]
            sagra_info['location'] = sagra_lines[3]
        return sagra_info
        
    @staticmethod
    def get_webpage_response(url: str = None, max_restries: int = MAX_RETRIES):
        response = None
        attempts = 0
        while response is None and attempts <= max_restries:
            try:
                response = requests.get(
                    url=url
                )
            except Exception as exc:
                print(f"Error while fetching webpage response from url {url} .\nThe reason was: {exc}\n Retrying in {RETRY_PAUSE_S} seconds...")
                attempts += 1
                time.sleep(RETRY_PAUSE_S)
        
        if response and isinstance(response, requests.models.Response):
            if response.status_code != VALID_RESPONSE_STATUS:
                print(f"Response from request to url {url} was invalid!")
                return None
        return response

    @staticmethod
    def is_valid_url(url: str) -> bool:
        # django url validation regex - https://github.com/django/django/blob/stable/1.3.x/django/core/validators.py#L45
        regex = re.compile(
                r'^(?:http|ftp)s?://' # http:// or https://
                r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
                r'localhost|' #localhost...
                r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
                r'(?::\d+)?' # optional port
                r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        return re.match(regex, url) is not None
    
    def print_sagra_content(self):
        if self.content is None:
            print("No sagra content is available!")
            return
        if not isinstance(self.content, list):
            print("Sagra content is corrupted!")
            return
        
        for sagra in self.content:
            print(f"\n")
            print(f"Information about {sagra['event']} :")
            print(f"Month: {sagra['month']}")
            print(f"Date: {sagra['date']}")
            print(f"Location: {sagra['location']}")
            print(f"\n")