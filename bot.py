
# All the used libararies
import hikari
import lightbulb
import requests
from main import outfit_recommender
from main import weather_data
import re


# Create a GatewayBot instance
bot = hikari.GatewayBot("your_bot_token_here")

client = lightbulb.client_from_app(bot)

bot.subscribe(hikari.StartingEvent, client.start)
# Register the command with the client
@client.register()

class Weather(
    # Command type - builtins include SlashCommand, UserCommand, and MessageCommand
    lightbulb.SlashCommand,
    # Command declaration parameters
    name="weather",
    description="checks the bot is alive",
):

    text = lightbulb.string("city", "Riga, London, Berlin, Paris, Rome, Madrid",)

    # Define the command's invocation method. This method must take the context as the first
    # argument (excluding self) which contains information about the command invocation.
    @lightbulb.invoke
    async def invoke(self, ctx: lightbulb.Context) -> None:
        
        regex_search = re.search(r"value='([^']+)'", ctx.options[0].__str__())
        current_city = regex_search.group(1)
        try:
            if current_city == "Riga":
                # data example - weather_data(latitude, longitude, timezone)
                riga = weather_data(56.9496, 24.1052, "Moscow")
                # data example - embed(title, 
                #                           description)
                riga_embed = hikari.Embed(title="**Riga**", description=f"Temperature: {riga[1]}°C\nWeather Condition: {riga[0]}\nFeels Like: {riga[4]}°C\nMinimum Temperature: {riga[2]}°C\nMaximum Temperature: {riga[3]}°C\n"+f"{outfit_recommender(riga[1], riga[0])}")
                await ctx.respond(riga_embed)

            elif current_city == "London":
                london = weather_data(51.5074, -0.1278, "London")
                

                london_embed = hikari.Embed(title="**London**", 
                                            description=f"Temperature: {london[1]}°C\nWeather Condition: {london[0]}\nFeels Like: {london[4]}°C\nMinimum Temperature: {london[2]}°C\nMaximum Temperature: {london[3]}°C\n"+f"{outfit_recommender(london[1], london[0])}",
                                            color=0x8F00FF)
                await ctx.respond(london_embed)
                
            elif current_city == "Berlin":
                berlin = weather_data(52.5200, 13.4050, "Berlin")
                berlin_embed = hikari.Embed(title="**Berlin**", 
                                            description=f"Temperature: {berlin[1]}°C\nWeather Condition: {berlin[0]}\nFeels Like: {berlin[4]}°C\nMinimum Temperature: {berlin[2]}°C\nMaximum Temperature: {berlin[3]}°C\n"+f"{outfit_recommender(berlin[1], berlin[0])}",
                                            color=0x8F00FF)
                await ctx.respond(berlin_embed)

            elif current_city == "Paris":
                paris = weather_data(48.8566, 2.3522, "London")
                paris_embed = hikari.Embed(title="**Paris**", 
                                           description=f"Temperature: {paris[1]}°C\nWeather Condition: {paris[0]}\nFeels Like: {paris[4]}°C\nMinimum Temperature: {paris[2]}°C\nMaximum Temperature: {paris[3]}°C\n"+f"{outfit_recommender(paris[1], paris[0])}",
                                           color=0x8F00FF)
                await ctx.respond(paris_embed)

            elif current_city == "Rome":
                rome = weather_data(41.9028, 12.4964, "Berlin")
                rome_embed = hikari.Embed(title="**Rome**", 
                                          description=f"Temperature: {rome[1]}°C\nWeather Condition: {rome[0]}\nFeels Like: {rome[4]}°C\nMinimum Temperature: {rome[2]}°C\nMaximum Temperature: {rome[3]}°C\n"+f"{outfit_recommender(rome[1], rome[0])}",
                                          color=0x8F00FF)
                await ctx.respond(rome_embed)

            elif current_city == "Madrid":
                madrid = weather_data(40.4168, -3.7038, "London")
                madrid_embed = hikari.Embed(title="**Madrid**", 
                                            description=f"Temperature: {madrid[1]}°C\nWeather Condition: {madrid[0]}\nFeels Like: {madrid[4]}°C\nMinimum Temperature: {madrid[2]}°C\nMaximum Temperature: {madrid[3]}°C\n"+f"{outfit_recommender(madrid[1], madrid[0])}",
                                            color=0x8F00FF)
                await ctx.respond(madrid_embed)

        except:
            await ctx.respond("Please select a valid city from the list.")  

# Run the bot until bot is stopped
bot.run()
