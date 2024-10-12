async def calculate_followers(amount_followers, conversion_rate):
    return (int(amount_followers) / conversion_rate) * 100

async def question(followers, estimated_days):
    followers = input("How much followers you want ? ")
    estimated_days = input("In how much time ? ")
    return followers, estimated_days

async def calculate_days(amount, days):
    return amount / int(days)
