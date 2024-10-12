import asyncio
from functions import calculate_days, calculate_followers, question


async def main():
    # Main variables
    followers = None
    estimated_days = None
    conversion_rate = 8.8328
    
    # Logic
    followers, estimated_days = await question(followers, estimated_days)
    result = await calculate_followers(followers, conversion_rate)
    posts_per_day = await calculate_days(result, estimated_days)

    # Output
    print(f"followers = {followers}")
    print(f"You need to post {result} images")
    print(f"Posts per day {posts_per_day}, in a range of {estimated_days} days")

asyncio.run(main())


