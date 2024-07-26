import instaloader
import csv

ig = instaloader.Instaloader()

# Load login session
ig.load_session_from_file('username', 'sessao')

comments = []

user_profile = 'profile'

try:
    profile = instaloader.Profile.from_username(ig.context, user_profile)
    
    for post in profile.get_posts():
        if post.date_utc.year == 2024:
            for comment in post.get_comments():
                comments.append((comment.created_at_utc, comment.text))
                
except instaloader.exceptions.BadResponseException:
    print("Metadados search failed. Check if the shortcode is correct.")
except Exception as e:
    print(f"Error: {e}")


# Save comments and created_at on CSV
csv_file = 'comments.csv'

try:
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Date', 'Comments'])
        for comment in comments:
            writer.writerow([comment[0], comment[1]])
    print(f'Comments saved on file {csv_file}')
except Exception as e:
    print(f'An error has occurred on save csv file {e}')