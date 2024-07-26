from google_play_scraper import reviews, Sort

# Keywords related to customer service
customer_service_keywords = [
    'customer service','support','help','service','assistance','response','can"t','report','rude'
    'contact','complaint','issue','problem','representative','agent','staff','cancel','reliable',
    'customer','handling','fraud','accuse','answer','bermasalah','slow','forgot','ticket','avoid',
    'privasi','overcharged','lazy','refund','scam','grabhemat' 'worse','sulit','cs','tidak ramah',
    'not responding','emergency','days','berhari-hari','inconvenience','different','not reliable',
    'complaining','purely automated','stupid','worst','bad','missing order','cannot','not friendly',
    'tidak user friendly','terrible','can"t be contacted','all bots','admin tdk ada respon','komplain',
    'tidak ditanggapi secara serius','horrible',"error"
]

def is_related_to_customer_service(review_text, keywords):
    """Check if a review mentions customer service-related keywords."""
    review_text_lower = review_text.lower()
    return any(keyword in review_text_lower for keyword in keywords)


def count_one_star_reviews(app_id, lang='en', batch_size=100, max_reviews=1350000):
    one_star_reviews_count = 0
    continuation_token = None
    batch_number = 0

    while True:
        try:
            # Fetch a batch of reviews
            result, continuation_token = reviews(
                app_id,
                lang=lang,  # Language
                country='id',  # Country (Indonesia)
                sort=Sort.NEWEST,  # Sort by newest first
                count=batch_size,
                continuation_token=continuation_token
            )

            # Filter for 1-star reviews related to customer service
            one_star_reviews = [
                review for review in result
                if review['score'] == 1 and is_related_to_customer_service(review['content'], customer_service_keywords)
            ]
            one_star_reviews_count += len(one_star_reviews)

            # Output the count for the current batch
            batch_number += 1
            print(
                f"Batch {batch_number}: Found {len(one_star_reviews)} 1-star reviews related to customer service (Total: {one_star_reviews_count})")

            # Break if no more reviews to fetch or reached max_reviews
            if not continuation_token or one_star_reviews_count >= max_reviews:
                break

        except Exception as e:
            print(f"An error occurred: {e}")
            break

    return one_star_reviews_count


# Example usage
app_id = 'com.grabtaxi.passenger'  # Grab's Play Store app ID
print("Fetching English reviews...")
one_star_review_count_en = count_one_star_reviews(app_id, lang='en')
print("Fetching Indonesian reviews...")
one_star_review_count_id = count_one_star_reviews(app_id, lang='id')

total_one_star_review_count = one_star_review_count_en + one_star_review_count_id
print(f"Total 1-star reviews related to customer service: {total_one_star_review_count}")
