import time
import random

print("Hi! This is a magical 8BALL")
time.sleep(2)
input("Ask me a question: ")

responses = [
        'It is certain.', 'It is decidedly so.', 'Without a doubt.',
        'Yes - definitely.', 'You may rely on it.', 'As I see it, yes.',
        'Most likely.', 'Outlook good!', 'Yes.', 'Signs point to yes.',
        'Reply hazy, try again.', 'Ask again later...',
        'Better not tell you now.', 'Cannot predict now.',
        "Don't count on it.", 'My reply is no.', 'My source say no.',
        'Outlook not so good.', 'Very doubtful.']

print (f"🎱 {random.choice(responses)} 🎱")