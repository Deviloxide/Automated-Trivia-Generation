import warnings
import wikipedia
from bs4 import BeautifulSoup

def search_wikipedia():
  warnings.filterwarnings("ignore")

  search_query = input("What would you like to search for? ")

  while True:
    try:
        # Search for the page with the given title
        search_results = wikipedia.search(search_query)

        # If there are multiple results, display them to the user
        print("The following pages were found:")
        for i, result in enumerate(search_results):
            print(f"{i + 1}. {result}")

        # Prompt the user to select the correct page
        selection = int(input("Enter the number of the correct page: ")) - 1

        # Get the selected page
        page_title = search_results[selection]
        page = wikipedia.WikipediaPage(page_title)

        # Get the first paragraph of the page
        content = page.summary

        # Create a BeautifulSoup object using the lxml parser
        # and suppress the warning
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            soup = BeautifulSoup(content, "lxml")

        return content
    except wikipedia.exceptions.DisambiguationError:
        soup = BeautifulSoup(search_query, "lxml")
        search_query = input("There was a DisambiguationError. Please enter a more specific search query: ")

