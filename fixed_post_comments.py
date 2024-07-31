import instaloader
import csv
from login import login

def extract_comments(username, shortcode):
    ig = instaloader.Instaloader()

    # Load login session
    ig.load_session_from_file(username, 'session')

    comments = []

    try:
        fixed_post = instaloader.Post.from_shortcode(ig.context, shortcode)
        
        for comment in fixed_post.get_comments():
            comments.append((comment.created_at_utc, comment.text))
                    
    except instaloader.exceptions.BadResponseException:
        print("Metadata search failed. Check if the shortcode is correct.")
    except Exception as e:
        print(f"Error: {e}")
    
    print("Extraction of comments successful.")
    return comments

def create_csv(comments, csv_file='fixed_post_comments.csv'):
    # Save comments and created_at in a CSV file
    try:
        with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Date', 'Comments'])
            for comment in comments:
                writer.writerow([comment[0], comment[1]])
        print(f'Comments saved in file {csv_file}')
    except Exception as e:
        print(f'An error occurred while saving the CSV file: {e}')


if __name__ == '__main__':
    print("Starting login.")
    login()

    print("Starting extraction of comments.")
    comments = extract_comments('username', 'shortcode')

    print("Writing CSV.")
    create_csv(comments)