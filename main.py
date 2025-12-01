import discord
import os
from discord.ext import commands
from core.models import init_db

intents = discord.Intents.default()
intents.members = True  # สำคัญ! เพื่อให้แก้ชื่อ & จัดการ role ได้

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("🔧 Initializing database...")
    init_db()
    print("📦 Database ready.")
    
    await bot.tree.sync()
    print(f"🤖 Bot ready as {bot.user}")

# ======================
# ตรงนี้ยังไม่ต้อง load commands อื่น
# ======================

bot.run(os.getenv("DISCORD_TOKEN"))