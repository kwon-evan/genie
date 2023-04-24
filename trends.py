from pytrends.request import TrendReq


def get_trends():
    pytrends = TrendReq(hl="ko-KR", tz=540)
    return {
        i: row.loc[0]
        for i, row in pytrends.trending_searches(pn="south_korea").iterrows()
    }


if __name__ == "__main__":
    print(get_trends())
