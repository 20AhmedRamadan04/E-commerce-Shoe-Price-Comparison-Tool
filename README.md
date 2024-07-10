# E-commerce Shoe Scraper

## Description
This project involves developing a web scraping tool to extract product information from e-commerce websites, specifically focusing on shoe names and prices. The tool scrapes data from Shoeroom and Jumia websites, allowing users to compare shoe details and prices.

## Technologies Used
- **Python:** For writing the main script and handling data processing.
- **BeautifulSoup:** For parsing HTML content and extracting the relevant information.
- **Selenium:** For automating browser interactions with Shoeroom.
- **Requests:** For making HTTP requests to Jumia.
- **CSV:** For storing the extracted data in a structured format.

## Key Features
- **Multi-Site Scraping:** The script extracts shoe names and prices from both Shoeroom and Jumia.
- **Automation with Selenium:** Uses Selenium to handle dynamic content on the Shoeroom website.
- **HTTP Requests with Requests Library:** Uses the Requests library to fetch static content from the Jumia website.
- **Data Storage:** The extracted information is saved into a CSV file for easy access and comparison.

## Challenges Overcome
- Handling different website structures and dynamic content.
- Ensuring data accuracy and completeness across both websites.
- Implementing error handling to manage potential issues such as missing data or changes in the website layout.

## Outcome
The project successfully provided a reliable and efficient tool for comparing shoe prices and details from multiple e-commerce websites, which can be used for market analysis or making informed purchasing decisions.

## Usage
1. Install the required libraries:
    ```bash
    pip install beautifulsoup4 selenium requests
    ```
2. Run the script:
    ```bash
    python shoe_scraper.py
    ```
3. The extracted data will be saved in a `shoes_data.csv` file.

## License
This project is licensed under the MIT License.
