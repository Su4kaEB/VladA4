#Влад а4 бот для дискорда

#Импортируем библиотеки
import re
import random
import discord
import asyncio
import aiohttp
from discord.ext import commands

intents = discord.Intents.all()
client = commands.Bot(
	command_prefix = '/',
	case_insensitive = True,
	help_command = None, #обязательно
	intents = intents,
	description = "Я - крутой бот написанный на пайтоне. Я влад а4 и ненавижу хауди хо он пидорас ебаный нахуй пусть его выебут блять он сдохнуть должен сука. Олег шпагин лучше"
)


#список плохих слов
nigga_words = [
"Нигер", "Хуесос", "Блять", "Ебал", "Ебать", "Даун", "Гондон","Шлюха","Пидор","Пидорас","Сука","Уебок","Аутист","Говно", "Хауди хо", "Нахуй"
]

async def mat_filter(msg):
	content = msg.content.lower()
	eblan = False #Если будет True - Значит юзер ЕБАНЫЙ МАТЕРШИННИК ЧТОБ ОН СДОХ

	for word in nigga_words:
		if word.lower() in content:
			eblan = True

	if eblan:
		await msg.delete()
		#Угрожаем юзеру
		await msg.channel.send(f"{msg.author.mention} ЕБЛАН, Базар фильтруй клоун уебок!")


async def howdy_ho_daun(msg):
	#фильтрует ссылки на хауди хо
	regex = r'((http|https):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])?)'
	results = re.findall(regex, msg.content)
	if len(results) > 0:
		async with aiohttp.ClientSession() as session:
			for result in results:
				if result[2] == 'www.youtube.com' or 'youtu.be':
					url = result[0]
					try:
						async with session.get(url) as r:
							if r.status == 200:
								c = (await r.read()).decode('utf-8')
								channel_id = re.search(r'"browseId":"(\w+)"', c)
								if channel_id:
									print(channel_id.group(1))
									if channel_id.group(1) == "UC7f5bVxWsm3jlZIPDzOMcAg": #проверка на хавди хо
										await msg.delete()
										await msg.channel.send(f"{msg.author.mention} Бан захотел еблан? Хауди хо тут запрещён!!!!! 🖕🖕🖕🖕🖕🖕🖕🖕🖕🖕🖕🖕🖕🖕🖕🖕")

									elif channel_id.group(1) == "SPunlimited":
										await msg.channel.send(f"{msg.author.mention} Влад а4 избил хауди хо")

					except Exception as e:
						print("Ебаная ошибка", e)

@client.command(name = "who_is_predophile")
async def command_who_is_pedophile(ctx):
	members = ctx.guild.members
	pedophile = random.choice(members)
	embed = discord.Embed(
		title = "Педофил найден",
		description = f"Педофил это {pedophile}"
	).set_thumbnail(url = pedophile.avatar_url)
	await ctx.send(f"{ctx.author.mention}",embed = embed)

@client.event
async def on_message(msg):
	if msg.author.id != client.user.id:
		#фильтр мата
		await mat_filter(msg)
		await howdy_ho_daun(msg)
	await client.process_commands(msg)

@client.event
async def on_ready():
	print("Запущен")
	await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Тик ток видосики :)"))


print("Запускаюсь епта!")
client.run("ODQ4NjM1ODk0NzYzODgwNDg4.YLPfxA.cjc7VCG17oBaR7H8oB-xmgpHJ1k")
