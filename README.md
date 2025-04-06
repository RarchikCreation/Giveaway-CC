# Giveaway-CC

## Overview
This bot provides a system for managing giveaways

## Installation
### Requirements
- Python 3.8+
- `disnake` library
- SQLite3
- `python-dotenv`

### Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/RarchikCreation/Giveaway-CC.git
   cd Giveaway-CC
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Create a `.env` file in data and add your bot token:
   ```sh
   TOKEN=your-bot-token
   ```
4. Configure your bot settings in `config.py`:
   ```python
   moderation_role_id = [1234567890]  # List of role IDs allowed to managed rolls
   ```
5. Run the bot:
   ```sh
   python3 main.py
   ```

## Commands
| Command | Description |
|---------|-------------|
| `/roll` | Creates a roll |
| `/rollv` | distribution among those who were in the voice channel the most | 
| `/end_roll` | complete the roll |



