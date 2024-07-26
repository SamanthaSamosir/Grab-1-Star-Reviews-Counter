# Grab 1-Star Reviews Counter

A Python script to count the total number of recent 1-star reviews related to customer service of the Grab app on the Play Store.

## Features

- Fetches reviews for the Grab app from the Google Play Store in batches.
- Filters reviews to count only those with a 1-star rating related to customer service.
- Combines reviews in English and Indonesian.
- Outputs the count of 1-star reviews for each batch and the total count.

## Prerequisites

- Python 3.6 or higher (I build this with 3.8 tho :p)
- `google-play-scraper` library

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/grab-1-star-reviews-counter.git
    cd grab-1-star-reviews-counter
    ```

2. Install the required library:

    ```bash
    pip install google-play-scraper
    ```

## Usage

1. Open the `count_one_star_reviews.py` file and ensure the `app_id` is set correctly:

    ```python
    app_id = 'com.grabtaxi.passenger'  # Grab's Play Store app ID
    ```

2. Run the script:

    ```bash
    python count_one_star_reviews.py
    ```

3. The script will output the count of 1-star reviews related to customer service for each batch and the total number of such reviews.

## Example Output

```bash
Fetching English reviews...
Batch 1: Found 10 1-star reviews related to customer service (Total: 10)
Batch 2: Found 12 1-star reviews related to customer service (Total: 22)
...
Fetching Indonesian reviews...
Batch 1: Found 8 1-star reviews related to customer service (Total: 8)
Batch 2: Found 15 1-star reviews related to customer service (Total: 23)
...
Total 1-star reviews related to customer service: 123
