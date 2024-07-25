# Grab 1-Star Reviews Counter
A Python script to count the total number of recent 1-star reviews of the Grab app on the Play Store.

## Features
- Fetches all reviews for the Grab app from the Google Play Store.
- Filters reviews to count only those with a 1-star rating.
- Outputs the count of 1-star reviews.

## Prerequisites
- Python 3.6 or higher (Personally, I use 3.8)
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
    app_id = 'com.grabtaxi.passenger' # Grab's Play Store app ID
    ```
2. Run the script:
    ```bash
    python count_one_star_reviews.py
    ```
3. The script will output the total number of 1-star reviews.

## Example Output
```bash
Total 1-star reviews: 123
