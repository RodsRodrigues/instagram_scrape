import instaloader
import csv

ig = instaloader.Instaloader()

# load login session
ig.load_session_from_file('username', 'sessao')

comments = []

post = 'shortcode'

try:
    fixed_post = instaloader.Post.from_shortcode(ig.context, post)
    
    for comment in fixed_post.get_comments():
        comments.append((comment.created_at_utc, comment.text))
                
except instaloader.exceptions.BadResponseException:
    print("Metadados search failed. Check if the shortcode is correct.")
except Exception as e:
    print(f"Error: {e}")


# Save comments and created_at on CSV
csv_file = 'fixed_post_comments.csv'

try:
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Date', 'Comments'])
        for comment in comments:
            writer.writerow([comment[0], comment[1]])
    print(f'Comments saved on file {csv_file}')
except Exception as e:
    print(f'An error has occurred on save csv file {e}')

