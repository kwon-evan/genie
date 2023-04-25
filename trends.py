import asyncio

from pytrends.request import TrendReq


async def get_trends():
    pytrends = TrendReq(hl="ko-KR", tz=540)
    return {
        i: row.loc[0]
        for i, row in pytrends.trending_searches(pn="south_korea").iterrows()
    }


async def main():
    ret = await get_trends()
    print(ret)


if __name__ == "__main__":
    asyncio.run(main())
