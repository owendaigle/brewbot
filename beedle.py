from discord.ext import commands
import random, discord, asyncio, time
from miscfunc import *
from addBrewcoin import addbrewcoin
import logging

class beeedleCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    def check(self, reaction, user): #https://stackoverflow.com/questions/63171531/how-do-you-check-if-a-specific-user-reacts-to-a-specific-message-discord-py
        return user == self.BeedleCtx.author and str(reaction.emoji) in ["🔨"] and reaction.message == self.beetle
    async def fail(self, context, laterTime, currentTime, times):
        await context.send(embed=SetEmbed(title="You failed.", description="The beetle has already eaten you.\nGo to jail and do not collect $200.", footer=f"Missed it by {abs((laterTime - currentTime) - times)}. :("))
        #raise RuntimeError("Fatal: User is a failure.")

    @commands.command(name='beedle')
    async def beedle(self, context):
        """Type brew help beedle for more information!
        When you run this command, it waits a few seconds. Then,
        a beetle will appear! You must STOP! Hammertime in a few
        seconds. This will destroy the beetle. Sorry, animal
        rights activists."""
        ctx = context
        self.BeedleCtx = ctx
        await context.send("You have found the beedle game...")
        score = 0
        current = 0
        beedleAmount = random.randint(10,30)
        for i in range(0, beedleAmount):
            await asyncio.sleep(random.randint(10,20))
            times = random.randint(3,6)
            beetle = await context.send(f"Oh no, there's an annoying beetle! **Swat it in the next {times} seconds!**")
            await beetle.add_reaction("🔨")
            self.beetle = beetle
            currentTime = int(time.time())
            confirmation = False
            while not confirmation:
                try:
                    confirmation = await self.bot.wait_for("reaction_add",check=self.check, timeout=times)
                except asyncio.TimeoutError:
                    await self.fail(ctx, currentTime, int(time.time()), times)
                    addbrewcoin(score, context.author)
                    return "Awwww.... I'm a failure!"
            laterTime = int(time.time())
            if (laterTime - currentTime) <= times and confirmation:
                await ctx.send(f"You got it by {abs((laterTime - currentTime) - times)} seconds! :beetle:")
                if abs((laterTime - currentTime) - times) == 0:
                    await ctx.send("In other words, you got it by the skin of your teeth! Nice job.")
                current += 1
                if current % 3 == 0:
                    score += 1
                continue
            if (laterTime - currentTime) > times:
                confirmation = False
        if not fail: await context.send(embed=SetEmbed(title="YOU WIN!", description="The beetles realised that this wasn't helping them in the slightest. You Win :D", footer=f"Take {score} brewcoin kind stranger"))
        addbrewcoin(score, context.author)

def setup(bot):
    bot.add_cog(beeedleCog(bot))
