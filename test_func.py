import asyncio

from weather import get_weather
from trends import get_trends
from hada_news import get_articles


async def main():
    weather = await get_weather()
    trends = await get_trends()
    articles = await get_articles()

    print(weather)
    print(trends)
    print(articles)

if __name__ == "__main__":
    asyncio.run(main())
