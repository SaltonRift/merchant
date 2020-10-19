#_merchant.py
import discord
from discord.ext import commands
__path__ = 'cogs/merchant.py'
# SERVER RULES
@commands.command(name="rules")
async def server_rules(ctx):
    embed = discord.Embed(title="```Server Rules```", description="**Accept for Access**", color=0x67D550)
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/736374327607296111/740221988353736754/BazaarGreenSafe.png")
    embed.add_field(name="Rule One", value="Respect others", inline=False)
    embed.add_field(name="Rule Two", value="Do not post links for any purpose, whether it be for advertisement, "
                                           "fun, or harmful material (ip grabbers, malware, viruses).",
                    inline=False)
    embed.add_field(name="Rule Three", value="Refrain from spamming, or mentioning roles. Individuals may be "
                                             "mentioned with purpose, if they request not to be mentioned do not "
                                             "mention them at all.", inline=False)
    embed.add_field(name="Rule Four", value="Do not discriminate against any members or racial, political, ethnic, "
                                            "or sexuality groups.", inline=False)
    embed.add_field(name="Rule Five", value="Do not DM members to promote or advertise")
    embed.set_footer(text="👇 - React below for access")
    await ctx.send(embed=embed)
    await ctx.message.delete()

# DISCLAIMER / 2FA
@commands.command()
async def disclaimer(ctx):
    server_rules = ctx.get_channel(712629525954953297)
    embed = discord.Embed(title="Disclaimer", description="Customers are required to agree to this message.",
                          color=0xe4cc4b)
    embed.set_author(name="Oxygen's Bazaar")
    embed.add_field(name="General Terms", value=f"`◆` Payment in advance\n"
                                                "\n"
                                                f"`◆` We will never share your information. We ask you to do the same.\n"
                                                "\n"
                                                f"`◆` Breaking {server_rules.mention} will forfeit an order.\n"
                                                "\n"
                                                f"`◆` PayPal payment sent as Friends & Family.\n"
                                                "\n"
                                                f"`◆` Refunds are not accepted once your order has begun.\n")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/736356825124831385/736356933799379115"
                            "/BazaarLogo_copy.png")
    embed.set_footer(text="👇 - Press below to agree")
    await ctx.send(embed=embed)
    await ctx.message.delete()


@commands.command(name="twofactor")
async def two_factor(ctx):
    embed = discord.Embed(title="Setting up 2-Factor Authentication",
                          description="We highly recommend setting this "
                                      "up before having us log into your "
                                      "account. If your FaceBook is "
                                      "locked and you did not follow "
                                      "these steps, we are not "
                                      "responsible.",
                          color=discord.colour.Color.blue())
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/736374327607296111/743267900156149790"
                            "/BazaarFaceBook.png")
    embed.set_author(name="Account Security")
    embed.add_field(name="**What is 2FA?**", value="2FA is an additional security setting you can enable in your "
                                                   "FaceBook account. It will require a code from a list of codes you "
                                                   "will get every time someone tries to log into the account.\n "
                                                   "\n"
                                                   "This is not only important for protecting your account against "
                                                   "intruders, but FaceBook will be less likely to lock your account "
                                                   "for suspicious activity if they notice multiple ip addresses "
                                                   "logging in.")
    embed1 = discord.Embed(title="**Step 1**",
                           description="Click the top three bars on the right.",
                           color=discord.colour.Color.blue())
    embed1.set_image(url="https://cdn.discordapp.com/attachments/743280026278953021/743280100782374972/Step1.png")
    embed2 = discord.Embed(title="**Step 2**",
                           description="Find account settings at the bottom.",
                           color=discord.colour.Color.blue())
    embed2.set_image(url="https://cdn.discordapp.com/attachments/743280026278953021/743280100824580136/Step2.png")
    embed3 = discord.Embed(title="**Step 3**",
                           description="Go to account 'Security & Login'.",
                           color=discord.colour.Color.blue())
    embed3.set_image(url="https://cdn.discordapp.com/attachments/743280026278953021/743280102481330257/Step3.png")
    embed4 = discord.Embed(title="**Step 4**",
                           description="Select 'Use two-factor authentication'.",
                           color=discord.colour.Color.blue())
    embed4.set_image(url="https://cdn.discordapp.com/attachments/743280026278953021/743280103626375258/Step4.png")
    embed5 = discord.Embed(title="**Step 5**",
                           description="You can choose either of the following ways to enable 2FA.",
                           color=discord.colour.Color.blue())
    embed5.set_image(url="https://cdn.discordapp.com/attachments/743280026278953021/743280105719332905/Step5.png")
    embed6 = discord.Embed(title="**Step 6**",
                           description="After you have followed the steps to set up 2-Factor Authentication, follow "
                                       "the first steps until you find yourself on the 2-FA page again.",
                           color=discord.colour.Color.blue())
    embed7 = discord.Embed(title="**Step 7**",
                           description="This time you will see 'Recovery Codes'. When logging into your account "
                                       "during an order, we will ask for a code. Press it.",
                           aaaaaaaaaaaaaaaaaaacolor=discord.colour.Color.blue())
    embed7.set_image(url="https://cdn.discordapp.com/attachments/743280026278953021/743280105769402368/Step6.png")
    embed8 = discord.Embed(title="**Step 8**",
                           description="Here are ten codes. Once used they are not reusable. When you run out of "
                                       "codes or are low, you can 'Get New Codes'.",
                           color=discord.colour.Color.blue())
    embed8.set_image(url="https://cdn.discordapp.com/attachments/743280026278953021/743280106725965894/Step7.png")
    await ctx.send(embed=embed)
    await ctx.send(embed=embed1)
    await ctx.send(embed=embed2)
    await ctx.send(embed=embed3)
    await ctx.send(embed=embed4)
    await ctx.send(embed=embed5)
    await ctx.send(embed=embed6)
    await ctx.send(embed=embed7)
    await ctx.send(embed=embed8)
    await ctx.message.delete()

    
def setup(bot):
    bot.add_command(server_rules)
    bot.add_command(disclaimer)
    bot.add_command(two_factor)
    
def teardown(bot):
    print('Merchant unloaded.')    