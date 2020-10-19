#currency.py

# noinspection PyUnusedLocal
from datetime import datetime

import discord

from foundation import client
from currency_converter import CurrencyConverter

def fixed(abr):
    fee = {
        pp_aud_fee = 0.30
        pp_brl_fee = 0.60
        pp_cad_fee = 2.99
        pp_czk_fee = 10.00
        pp_dkk_fee = 2.60
        pp_eur_fee = 0.35
        pp_hkd_fee = 2.35
        pp_nzd_fee = 0.45
        pp_nok_fee = 2.80
        pp_php_fee = 15.00
        pp_pln_fee = 1.35
        pp_rub_fee = 10.00
        pp_sgd_fee = 0.50
        pp_sek_fee = 3.25
        pp_gbp_fee = 0.30
        pp_usd_fee = 0.30
        pp_huf_fee = 90
        pp_ils_fee = 1.20
        pp_jpy_fee = 40
        pp_myr_fee = 2.00
        pp_mxn_fee = 4.00
        pp_chf_fee = 0.55
        pp_twd_fee = 10.00
        pp_thb_fee = 11.00
    }
    return fee('pp_{str.tolower(abr)}_fee', 0)

@client.command()
async def convert(ctx, amount=0.0, currency_one='', currency_two=''):
    author = ctx.author
    tax_fee = 0
    fixed_fee = fixed(currency_one)
    
    #fixed fee & tax overrides
    if currency_one == 'AUD':
        if amount < 50:
            fixed_fee = 0.99
        if amount >= 50 <= 99.99:
            fixed_fee = 2.99
        if amount >= 100:
            fixed_fee = 5.99
        tax_fee = 2.6
    if currency_one == 'CAD':
        fixed_fee += 0.30
        tax_fee = 2.9
    if currency_one == 'GBP':
        if amount < 50:
            fixed_fee = 0.99
        if amount >= 50 <= 99.99:
            fixed_fee = 1.99
        if amount >= 100:
            fixed_fee = 1.99
            tax_fee = 0.0
    if currency_one == 'USD':
        tax_fee = 2.9
    
    conversion_fee = 3.5
    tax_fee = tax_fee / 100
    conversion_fee = conversion_fee / 100
    tax_combined = tax_fee + conversion_fee
    tax_amount = amount
    tax_amount += fixed_fee
    tax_amount += tax_amount * tax_combined

   # converted_rate = c.convert(amount, currency_one, currency_two)
   # tax_converted_rate = c.convert(tax_amount, currency_one, currency_two)

    embed = discord.Embed(title=f"Currency Conversion, requested by {author}",
                          description=f"{currency_one} ➡ {currency_two}", color=0x6be66e)
    embed.add_field(name=f"{currency_one}", value=f"{amount}", inline=False)
    embed.add_field(name=f'{currency_two}', value=f"{converted_rate}", inline=False)
    # embed.add_field(name="⬇️With PayPal⬇️", value="Conversion Fee,Fixed Fee,Tax",
    # inline=True)
    # embed.add_field(name=f"{currency_one} `Send`", value=f"{tax_amount}", inline=False)
    # embed.add_field(name=f"{currency_two} `Receive`", value=f"{converted_rate}", inline=False)
    embed.timestamp = datetime.utcnow()
    await ctx.send(embed=embed)


@client.command()
async def send_usd(ctx, amount=0.0, foreign_currency=''):
    
    author = ctx.author
    tax_fee = 0
    fixed_fee = fixed(currency_one)
    
    #fixed fee and tax overrides
    if foreign_currency == 'AUD':
        if amount < 50:
            fixed_fee = 0.99
        if amount >= 50 <= 99.99:
            fixed_fee = 2.99
        if amount >= 100:
            fixed_fee = 5.99
        tax_fee = 2.6
    if foreign_currency == 'CAD':
        fixed_fee = pp_cad_fee
        fixed_fee += 0.30
        tax_fee = 2.9
    if foreign_currency == 'GBP':
        if amount < 50:
            fixed_fee = 0.99
        if amount >= 50 <= 99.99:
            fixed_fee = 1.99
        if amount >= 100:
            fixed_fee = 1.99
            tax_fee = 0.0
    if foreign_currency == 'USD':
        tax_fee = 2.9
        fixed_fee = pp_usd_fee
    
    c = CurrencyConverter()

    raw_convert = c.convert(amount, 'USD', foreign_currency)
    raw_convert += fixed_fee
    conversion_fee = 3.5
    tax_fee = tax_fee / 100
    conversion_fee = conversion_fee / 100
    tax_combined = tax_fee + conversion_fee

    raw_convert += raw_convert * tax_combined

    embed = discord.Embed(title=f"PayPal Send Fee Estimate, requested by {author}",
                          description=f"Sending {foreign_currency} to USD"
                                      f" | Friends & Family", color=0x6be66e)
    embed.add_field(name=f"For the recipient to receive {amount} USD, you will pay (estimate):",
                    value=f"{raw_convert} {foreign_currency}", inline=False)

    await ctx.send(embed=embed)


@client.command()
async def currencies(ctx):
    embed = discord.Embed(title="ISO Currency Codes")
    embed.add_field(name='AUD', value='Australian Dollar', inline=False)
    embed.add_field(name='BRL', value='Brazilian Real', inline=False)
    embed.add_field(name='CAD', value='Canadian Dollar', inline=False)
    embed.add_field(name='CZK', value='Czech Koruna', inline=False)
    embed.add_field(name='DKK', value='Danish Krone', inline=False)
    embed.add_field(name='EUR', value='Euro', inline=False)
    embed.add_field(name='HKD', value='Hong Kong Dollar', inline=False)
    embed.add_field(name='NZD', value='New Zealand Dollar', inline=False)
    embed.add_field(name='NOK', value='Norwegian Krone', inline=False)
    embed.add_field(name='PHP', value='Philippine Peso', inline=False)
    embed.add_field(name='PLN', value='Polish Złoty', inline=False)
    embed.add_field(name='RUB', value='Russian Ruble', inline=False)
    embed.add_field(name='SGD', value='Singapore Dollar', inline=False)
    embed.add_field(name='SEK', value='Swedish Krona', inline=False)
    embed.add_field(name='GBP', value='British Pound', inline=False)
    embed.add_field(name='USD', value='United States Dollar', inline=False)
    embed.add_field(name='HUF', value='Hungarian Forint', inline=False)
    embed.add_field(name='ILS', value='Israeli New Shekel', inline=False)
    embed.add_field(name='JPY', value='Japanese Yen', inline=False)
    embed.add_field(name='MYR', value='Malaysian Ringgit', inline=False)
    embed.add_field(name='MXN', value='Mexican Peso', inline=False)
    embed.add_field(name='CHF', value='Swiss Franc', inline=False)
    embed.add_field(name='TWD', value='New Taiwan Dollar', inline=False)
    embed.add_field(name='THB', value='Thai baht', inline=False)
    await ctx.send(embed=embed)
    
# PAYMENT METHODS
@client.command()
async def payment_methods(ctx):
    paypal = client.get_emoji(724642807473635449)
    transferwise = client.get_emoji(741602664860876820)
    venmo = client.get_emoji(741604610137128991)
    btc = client.get_emoji(741368827048231012)
    zelle = client.get_emoji(741368374474571837)
    revolut = client.get_emoji(724644260951097347)
    cashapp = client.get_emoji(741602915050848377)

    embed = discord.Embed(title="Payment Methods", description="You can use following methods of online payment",
                          color=0xe7e4e4)
    embed.set_author(name="Oxygen's Bazaar")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/736374327607296111/741606439964901446"
                            "/BazaarBluePay.png")
    embed.add_field(name=f"Options",
                    value=f"{transferwise} TransferWise\n"
                          f"{revolut} Revolut\n"
                          f"{zelle} Zelle\n"
                          f"{cashapp} CashApp\n"
                          f"{paypal} PayPal\n"
                          f"{btc} Bitcoin\n"
                          f"{venmo} Venmo")
    embed.set_footer(text="The following currencies can be sent via bank transfer with no fees: USD, EUR, GBP, CAD, "
                          "AUD, NZD, SGD")
    await ctx.send(embed=embed)
    warnembed = discord.Embed(title="Warning",
                              description="Please remember to change the 'Receiving Amount' to match "
                                          "our prices.\n"
                                          "PayPal must be sent as Friends & Family",
                              color=discord.colour.Color.red())
    await ctx.send(embed=warnembed)
    await ctx.message.delete()
    umbed = discord.Embed(title="Payment Updated", description=f"New Option: {venmo} Venmo")
    embed.set_footer(text="Auto Delete in 24 hours")
    await ctx.send(embed=umbed, delete_after=86400)

def setup(client)
    bot.add_command(convert)
    bot.add_command(send_usd)
    bot.add_command(currencies)
    bot.add_command(payment_methods)