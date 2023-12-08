# Bitcoin-NewsArticles-Sentiment-Analysis

## Overview

This project is an extensive analysis of online articles related to Bitcoin, aiming to extract meaningful insights from the ever-evolving discourse surrounding this cryptocurrency. It's a two-part process involving web scraping to collect data and then applying various data analysis techniques, including sentiment analysis, to interpret this data.

## Features

- **Data Scraping**: Implemented in `scarping_data.py`, this module uses libraries like BeautifulSoup and Selenium to efficiently extract Bitcoin-related articles from the web.

- **Data Analysis and Visualization**: The Jupyter Notebook `bitcoin_articles_analysis.ipynb` takes the scraped data to perform an in-depth analysis. It includes the use of libraries such as Pandas, NumPy, Matplotlib, Seaborn, and NLTK for data processing, statistical analysis, and visualization.

## Getting Started

To get started with this project:

1. Clone the repository.
2. Install the required Python libraries listed in `requirements.txt`.
3. Run `scarping_data.py` to scrape data.
4. Open `bitcoin_articles_analysis.ipynb` in Jupyter Notebook or Jupyter Lab to view and run the analysis.

## Libraries

- Python 3.x
- Libraries: BeautifulSoup, Selenium, Pandas, NumPy, Matplotlib, Seaborn, NLTK, TextBlob

### Data Scraping

- **Script**: `scarping_data.py`
- **Technologies Used**: Python, BeautifulSoup, Selenium
- **Process**: This script is designed to navigate the web and programmatically gather articles about Bitcoin. Using BeautifulSoup and Selenium, it can handle both static and dynamic content on web pages. The script fetches articles, extracts relevant information like the article's text, and then stores this data for analysis.

### Data Analysis & Visualization

- **Notebook**: `bitcoin_articles_analysis.ipynb`
- **Key Libraries**: Pandas, NumPy, Matplotlib, Seaborn, NLTK, TextBlob, Statsmodels
- **Analysis Flow**:
  1. **Data Preprocessing**: Cleansing and structuring the scraped data for analysis.
  2. **Statistical Analysis**: Employing libraries like Pandas and NumPy to perform statistical computations and derive basic insights from the data.
  3. **Visualization**: Using Matplotlib and Seaborn to create graphs and plots that visually represent trends and patterns in the data.

### Sentiment Analysis

A key component of this project is sentiment analysis on the collected articles. This process involves:

- **Text Processing**: Using NLTK (Natural Language Toolkit), the script preprocesses the text data from articles. This includes tokenizing (breaking down the text into words or sentences), removing stopwords (common words that don't contribute to the overall meaning), and normalizing (converting to a consistent format).

- **Sentiment Scoring with TextBlob**: TextBlob is used for deriving sentiment scores. Each piece of text is analyzed to determine the polarity (ranging from -1 for negative to +1 for positive) and subjectivity (ranging from 0 to 1, where 0 is very objective and 1 is very subjective). This helps in understanding the general sentiment and objectivity in the discourse around Bitcoin.

- **Correlation and Trend Analysis**: By correlating sentiment scores with other factors like publication date, author, or source, we can derive insights into how sentiment varies over time or across different mediums.


## Contributing

Contributions to the project are welcome! Whether it's improving the scraping script, enhancing the data analysis, or suggesting new data sources, your input is valuable.


___






