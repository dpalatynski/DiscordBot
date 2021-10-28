from discord.ext import commands
from discord import Embed
from bs4 import BeautifulSoup
import pandas as pd
import requests


class Stats(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name='covid-statistics',
                      brief='Get COVID-19 stats',
                      description='-> ".covid" - returns COVID-19 statistics for the whole world \n'
                                  '-> ".covid world" - returns COVID-19 statistics for the whole world \n'
                                  '-> ".covid [country]" - returns COVID-19 statistics for a specific country',
                      aliases=['covid', 'coronavirus', 'covid-stats', 'covid-stat'])
    async def covid_statistics(self, ctx, country=None):
        if country is None:
            country = 'world'
        else:
            country = country.lower()
        df = create_table_statistics('https://www.worldometers.info/coronavirus/',
                                     'table table-bordered table-hover main_table_countries', 8)
        information = ['TotalCases', 'NewCases', 'TotalDeaths', 'NewDeaths', 'TotalRecovered', 'NewRecovered',
                       'ActiveCases', 'Serious,Critical']
        values = []
        for info in information:
            value = df.loc[df['Country'] == country][info].values[0]
            values.append('0' if len(value) == 0 else value)

        embed = await create_message(values, country, information, 'covid')

        await ctx.send(embed=embed)

    """@covid_statistics.error
    async def covid_statistics_eror(self, ctx, error):
        if error:
            embed = Embed(color=0xff0000)
            embed.add_field(name='Error', value=':no_entry: Unable to find statistics for your entry.')

            await ctx.send(embed=embed)"""

    @commands.command(name='population-statistics',
                      brief='Number of population in a specific country',
                      description='-> ".population_statistics [country]" - returns information about a country \n',
                      aliases=['population', 'people', 'people-stats', 'population-stats'])
    async def population_statistics(self, ctx, country):
        country = country.lower()
        df = create_table_statistics('https://www.worldometers.info/world-population/population-by-country/',
                                     'table table-striped table-bordered', 1)
        information = ['Population (2020)', 'Yearly Change', 'Net Change', 'Migrants (net)', 'Med. Age']
        values = []
        for info in information:
            value = df.loc[df['Country'] == country][info].values[0]
            values.append('0' if len(value) == 0 else value)

        embed = await create_message(values, country, information, 'population')

        await ctx.send(embed=embed)

    @population_statistics.error
    async def covid_statistics_eror(self, ctx, error):
        if error:
            embed = Embed(color=0xff0000)
            embed.add_field(name='Error', value=':no_entry: Unable to find statistics for your entry.')

            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Stats(client))


def create_table_statistics(url, table_name, starting_row):
    """
        Create table with statistics from https://www.worldometers.info/
    :param url: direct website to scrap table
    :param table_name: name of table to get
    :param starting_row: starting row from table
    :return: table with statistics
    """
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    table = soup.find('table', table_name)

    headers = []
    for header in table.find_all('th'):
        headers.append(header.text)

    headers[1] = 'Country'
    df = pd.DataFrame(columns=headers)

    for i in table.find_all('tr')[starting_row:]:
        row = [tr.text for tr in i.find_all('td')]
        length = len(df)
        df.loc[length] = row
    df['Country'] = df['Country'].str.lower()

    return df


async def create_message(values, country, information, stats):
    """
    Creates message to be sent by a bot
    :param values: values of statistics
    :param country: name of country
    :param information: columns
    :param stats: type of statistics
    :return: embed message ready to sent by a bot
    """
    if country == 'usa' or country == 'uk':
        country = country.upper()
    elif country == 'world':
        country = 'the whole world'
    else:
        country = country[0].upper() + country[1:]

    if stats == 'covid':
        embed = Embed(title='COVID-19 Statistics for ' + country, color=0x2ca5f1)
        embed.set_thumbnail(url='https://www.nps.gov/aboutus/news/images/CDC-coronavirus-image-23311-for-web.jpg?'
                                'maxwidth=650&autorotate=false')
    else:
        embed = Embed(title='Population of ' + country, color=0x2ca5f1)
        embed.set_thumbnail(url='https://www.mcicon.com/wp-content/uploads/2021/01/People_Human_1-copy-5.jpg')
    for i in range(len(information)):
        if values[i][0] == "+":
            values[i] = values[i][1:]
        embed.add_field(name=information[i], value=values[i])

    return embed
