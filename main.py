import disnake
from disnake.ext import commands
from disnake.ext.commands import CommandSyncFlags
import os
import sqlite3
from dotenv import load_dotenv

load_dotenv("data/.env")

TOKEN = os.getenv("TOKEN")

intents = disnake.Intents(
    guilds=True,
    members=True,
    messages=True,
    message_content=True
)


sync_flags = CommandSyncFlags.default()
bot = commands.InteractionBot(intents=intents)


def create_db():
    db_path = "data/database.db"
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS voice_rolls (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        creator_id INTEGER,
        gift TEXT,
        end_time TEXT,
        winner_id INTEGER,
        channel_ids TEXT
    )
    """)

    cursor.execute("PRAGMA table_info(voice_rolls)")
    columns = [column[1] for column in cursor.fetchall()]
    if "channel_ids" not in columns:
        cursor.execute("ALTER TABLE voice_rolls ADD COLUMN channel_ids TEXT")

    conn.commit()
    conn.close()


@bot.event
async def on_ready():
    print(f"{bot.user}")
    create_db()

def load_cogs():
    for dirpath, _, filenames in os.walk("./cogs"):
        if "__pycache__" in dirpath:
            continue
        for filename in filenames:
            if filename.endswith(".py") and not filename.startswith("_"):
                cog_path = os.path.relpath(os.path.join(dirpath, filename), start=".").replace(os.sep, ".")[:-3]

                if cog_path in bot.cogs:
                    print(f"⚠️ {cog_path} уже загружен")
                    continue
                try:
                    bot.load_extension(cog_path)
                    print(f"✅ {cog_path} загружен")
                except Exception as e:
                    print(f"❌ Ошибка в {cog_path}: {e}")


if __name__ == "__main__":
    create_db()
    load_cogs()
    bot.run(TOKEN)
    