# KOLO.TV Telegram Bot

The KOLO.TV Telegram Bot is designed to monitor mentions of the company in Telegram chats and send notifications to a technical chat when such mentions are detected.

## Technology Stack

- Python 3.10
- aiogram 3.0.0
- pydantic 2.3.0
- sqlalchemy 2.0.20
- alembic 1.12.0

## Getting Started

### Prerequisites

Before running the bot, ensure you have the following prerequisites installed:

- Python 3.10
- pip
- Docker (optional)

### Installation

To install the necessary Python dependencies, you can use the provided `requirements.txt` file:  
`pip install -r requirements.txt`

### Running Locally

You can run the bot locally using the following command:
```
alembic upgrade head
python3 bot.py
```

### Run the Docker container:
Alternatively, you can run the bot in a Docker container.  

```
docker build -t kolobot .
docker run -d kolobot:latest
```

## Mention Tracking and Database Storage
The KOLO.TV Telegram Bot uses regular expressions to track mentions of approximately 10 different keywords related to the company.
When a mention is detected, the bot stores the information in an SQLite database `kolo.db` with the following structure:

### WORD Table:
id (Primary Key)  
title (Keyword)  
regex pattern  

### Mention Table:
id (Primary Key)  
text (message text)  
word_id (Foreign Key)  
chat_id (Foreign Key)  
user_id (Foreign Key)  
link to the message (Link to the original message)  
datetime (Timestamp of when the mention was detected)    

### Chat Table:
id (Chat ID Primary Key)  
title (Chat title where the mention occurred) 

### User Table:
id (User ID Primary Key)  
full_name (user full name)
nickname (optional username)  

#### These database tables store information about detected mentions for later analysis and reference.

### Usage
To use the bot, you need to configure it with your Telegram API token and destinations chat.  
Modify the .env file to include your API token and other necessary configurations and add bot to different chats for monitoring.

### Contact
For questions or inquiries, please contact [@doodko](https://t.me/doodko)