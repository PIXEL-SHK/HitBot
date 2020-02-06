import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import bot
import random
import datetime

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('등장!')

@bot.command()
async def 핑(ctx):
    await ctx.send('당신의 핑 정보 : {0}초'.format(bot.latency))  
@bot.command()
async def 명령어(ctx):
    embed = discord.Embed(colour = 0x00f000)
    embed.add_field(name='핑', value='!핑 - 사용자의 핑 정보를 알려줍니다', inline=False)
    embed.add_field(name='프로필', value='!프로필 @원하는 사용자 - 사용자의 프로필 정보를 알려줍니다', inline=False)
    embed.add_field(name='히트야', value='!히트야 - 히트가 랜덤으로 대답해줍니다.', inline=False)
    embed.add_field(name='패치노트', value='!패치노트 - 디스코드 히트봇 패치노트를 보여줍니다', inline=False)
    embed.add_field(name='문의', value='!문의 - 개발자의 연락처를 알려줍니다.', inline=False)

    embed.add_field(name='당근', value='!당근 - 당근이요.:carrot:당근.', inline=False)
    await ctx.send(embed=embed)
@bot.event
async def on_ready():
    while not bot.is_closed():
        number = len(bot.guilds)
        user = len(bot.users)
        await bot.change_presence(activity=discord.Activity(name="%s개의 서버에서 활동"%(number), type=discord.ActivityType.playing))
        await asyncio.sleep(5)
        await bot.change_presence(activity=discord.Activity(name="%s명의 유저들과 함께"%(user), type=discord.ActivityType.playing))
        await asyncio.sleep(5)
        await bot.change_presence(activity=discord.Activity(name='!명령어를 입력해보세요!', type=discord.ActivityType.playing))
        await asyncio.sleep(5)
        await bot.change_presence(activity=discord.Activity(name='문의는 히트#0001', type=discord.ActivityType.playing))
        await asyncio.sleep(5)
        await bot.change_presence(activity=discord.Activity(name='이 메시지는 5초 마다 바뀌어요!', type=discord.ActivityType.playing))
        await asyncio.sleep(5)
@bot.command()
async def 프로필(ctx, member: discord.Member):
    embed = discord.Embed(color = 0x00f000)
    embed.add_field(name='이름', value=member, inline=False)
    await ctx.send(embed=embed)
@bot.command()
async def 히트야(ctx):
        rand=random.randrange(2, 4)
        if rand==1:
            await ctx.send('왜')
        elif rand==2:
            await ctx.send('자는중..:zzz:')
        elif rand==3:
            await ctx.send('히트봇 사망')
@bot.command()
async def 패치노트(ctx):
    embed = discord.Embed(colour = 0x00f000)
    embed.add_field(name='2020.2.4 패치노트', value='2020.2.4 - 디스코드 히트봇 서비스 시작', inline=False)
    embed.add_field(name='2020.2.5 패치노트', value='2020.2.5 - !히트야 명령어 랜덤 업데이트', inline=False)
    embed.add_field(name='2020.2.6 패치노트', value='2020.2.6 - !청소 명령어 추가 (현재 사용 불가능)', inline=False)
    embed.add_field(name='2020.2.6 패치노트', value='2020.2.6 - !문의 명령어 추가', inline=False)
    embed.add_field(name='2020.2.6 패치노트', value='2020.2.6 - !날짜, !시간 명령어 추가', inline=False)
    await ctx.send(embed=embed)
@bot.command()
async def 초대(ctx):
    await ctx.send('```히트봇은 다음 초대 링크로 초대 하실 수 있습니다```https://discordapp.com/api/oauth2/authorize?client_id=674252014242234369&permissions=8&scope=bot')  
@bot.command()
async def 문의(ctx):
    await ctx.send('``디스코드 - 히트#0001``으로 문의/건의내용 DM으로 보내주세요') 
@bot.command()
async def 당근(ctx):
    await ctx.send(':carrot:라드가 좋아하는 당근') 
@bot.command()
async def 청소(ctx):
    varrr=message.ctx.split(' ')
    await message.ctx.purge(limit=int(varrr[2])+1)
    now=datetime.datetime.now()
    msg=await ctx.send(embed=discord.Embed(title=f'메시지 {str(int(varrr[2]))}개 삭제 완료!', descirption='응용 기능', colour=discord.Colour.blue()).set_footer(icon_url=message.author.avatar_url, text=f'{str(message.author)} | {str(now.year)}년 {str(now.month)}월 {str(now.day)}일'))
    await asyncio.sleep(3)
    await msg.delete()
@bot.command()
async def 날짜(ctx):
    now = datetime.datetime.now()
    await ctx.send("오늘 날짜는 ``{}년 {}월 {}일`` 입니다.".format(
        now.year,
        now.month,
        now.day
    ))
@bot.command()
async def 시간(ctx):
    now = datetime.datetime.now()
    await ctx.send("현재 시각은 ``{}시 {}분 {}초`` 입니다.".format(
        now.hour,
        now.minute,
        now.second
    ))

bot.run('token')
