import asyncio

import httpx
from rich.text import Text
from rich import print


async def update_weather(city: str) -> Text:
    url = f"https://wttr.in/?0nQF&lang=ko"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        txt = Text.from_ansi(response.text)
        return txt


async def main():
    # ret = await get_weather()
    ret = await update_weather("Gumi")
    print(ret)


if __name__ == "__main__":
    asyncio.run(main())
