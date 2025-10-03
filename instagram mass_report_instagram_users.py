import time
import random
import requests
from insta_api_client import InstaApiClient  # Hypothetical client library
import logging
# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)
def report_username(api, username):
    """Report a single username with proper checks."""
    
    try:
        # Check if already reported in the last 7 days
        recent_reports = api.get_recent_reports(username)
        
        for report in recent_reports:
            if (time.time() - report['report_time']) < 86400 * 7:  # Past week
                logger.info(f"{username}: Recently reported.")
                return False
        
        payload = {
            'reason': 'spam',  # Replace with specific reason if needed
            'comment': f"Reported {username} for policy violations."
        }
        
        # Simulate rate limiting by adding random delay
        sleep_time = random.uniform(4, 6)
        logger.info(f"Sleeping for {sleep_time:.2f} seconds to avoid detection.")
        time.sleep(sleep_time)
        
        # Attempt report
        api.report_user(username, payload)
        logger.info(f"{username}: Reporting successful.")
        return True
        
    except Exception as e:
        logger.error(f"Error reporting {username}: {str(e)}")
        return False
def main():
    """Main function to run the Instagram mass reporting script."""
    
    # Replace with actual username list and API credentials
    usernames = [
        "username1",
        "username2",
        "username3"
    ]
    
    api = InstaApiClient()  # Placeholder for proper authentication
    
    total_reported = 0
    for username in usernames:
        # Add a random delay between 4-6 seconds to avoid detection
        sleep_time = random.uniform(4, 6)
        logger.info(f"Sleeping for {sleep_time:.2f} seconds for user: {username}")
        time.sleep(sleep_time)
        
        if report_username(api, username):
            total_reported += 1
            logger.info(f"{username}: Successfully reported.")
        else:
            logger.warning(f"{username}: Failed to report due to possible violation or other reasons.")
    logger.info(f"Completed: Reported {total_reported}/{len(usernames)} accounts.")
    
if __name__ == "__main__":
    main()
