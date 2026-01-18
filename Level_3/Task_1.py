"""
Develop a web scraper that extracts
specific data from websites using libraries
like BeautifulSoup or Scrapy. This task will
improve their knowledge of web scraping
techniques and handling HTML/XML data.
"""

import requests                     # For sending HTTP requests
from bs4 import BeautifulSoup as bs  # For parsing HTML content
import re                           # For discovering available HTML tags


class WebScraper:
    def __init__(self, url: str):
        # Store the target URL and HTML content
        self.url = url
        self.html = None

    def get_url(self) -> bool:
        """
        Fetches the HTML content of the given URL.
        Returns True if the request is successful, otherwise False.
        """
        try:
            # User-Agent header to avoid basic bot blocking
            headers = {"User-Agent": "Mozilla/5.0"}
            response = requests.get(self.url, headers=headers, timeout=10)

            # Raise an exception for HTTP error responses (4xx, 5xx)
            response.raise_for_status()

            # Store HTML content for further processing
            self.html = response.text
            return True

        except requests.exceptions.RequestException as e:
            # Handles all request-related errors gracefully
            print(f"An error occurred: {e}")
            return False

    def valid_tags(self):
        """
        Extracts all valid HTML tags from the page using regex
        and allows the user to choose one.
        """
        # Fetch the page before extracting tags
        if not self.get_url():
            return None

        # Regex is used ONLY to discover tag names (not for parsing structure)
        tags = sorted(set(re.findall(r"<\s*([a-zA-Z0-9]+)", self.html)))
        print(f"Available tags from {self.url}: {tags}")

        # Keep asking until a valid tag is entered
        while True:
            chosen_tag = input("Enter the tag to extract: ").strip()
            if chosen_tag in tags:
                return chosen_tag
            print("Enter a valid tag.")

    def valid_class(self, tag):
        """
        Finds all unique class names associated with a given HTML tag.
        """
        soup = bs(self.html, "html.parser")
        elements = soup.find_all(tag)

        classes = set()
        for el in elements:
            # Check if the element has a 'class' attribute
            if el.has_attr("class"):
                classes.update(el["class"])

        return sorted(classes)

    def choose_class(self, tag):
        """
        Allows the user to optionally choose a class name
        for more precise data extraction.
        """
        classes = self.valid_class(tag)

        # If no classes exist for this tag, skip class filtering
        if not classes:
            print("No classes found for this tag.")
            return None

        print(f"Available classes for <{tag}>:")
        for cls in classes:
            print(f"- {cls}")

        # User can skip class filtering by pressing Enter
        chosen_class = input(
            "Enter a class name to filter by (press Enter to skip): "
        ).strip()

        return chosen_class if chosen_class else None

    def parse_html(self, tag, class_name=None):
        """
        Parses the HTML and extracts text content
        based on the selected tag and optional class.
        """
        soup = bs(self.html, "html.parser")

        # Apply class filter if provided
        if class_name:
            elements = soup.find_all(tag, class_=class_name)
        else:
            elements = soup.find_all(tag)

        # Extract clean text from each matched element
        return [el.get_text(strip=True) for el in elements]


def main():
    # Take URL input from the user
    url = input("Enter the url you wanna scrape: ").strip()
    scraper = WebScraper(url)

    # Ask user to choose a valid HTML tag
    tag = scraper.valid_tags()
    if not tag:
        print("No tag selected. Exiting.")
        return

    # Optionally allow class-based filtering
    class_name = scraper.choose_class(tag)

    # Extract and display results
    results = scraper.parse_html(tag, class_name)

    print("\n--- Extracted Data ---")
    for i, item in enumerate(results, start=1):
        print(f"{i}. {item}")


# Entry point of the program
if __name__ == "__main__":
    main()
