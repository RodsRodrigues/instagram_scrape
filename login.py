import instaloader

def login():
    ig = instaloader.Instaloader()

    try:
        ig.login('username', 'password')
        ig.save_session_to_file('session')
        print("Session saved.")
    except instaloader.exceptions.BadCredentialsException:
        print("Invalid credential, check username or password.")
    except instaloader.exceptions.TwoFactorAuthRequiredException:
        print("2FA is required.")
    except Exception as e:
        if 'checkpoint_required' in str(e).lower():
            print(f"Checkpoint required: {e}. Complete the checkpoint on your browser and try again.")
        else:
            print(f"Trying to login failed: {e}")

login()