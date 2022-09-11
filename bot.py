import discord
from discord.ext import commands
from binance import get_price

intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(command_prefix="$", intents=intents)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.command()
async def binance(ctx, *args):
    arguments = ', '.join(args)
    resp = await get_price(arguments)

    status_code = resp.get('code', 200)

    if status_code == 200:
        await ctx.send(f'{arguments} price is {resp["price"]}')
        return
    await ctx.send(resp['msg'])


@bot.command()
async def second_command(ctx, *args):
    arguments = ', '.join(args)
    await ctx.send(f'{len(args)} arguments: {arguments}')


bot.run('MTAxODA2NzY4MDgxNDY5NDQzMg.GaLe7c.y-KO2xQC_Mw2-TXQCQz4JFVePmHHcK4wBKHgAc')
