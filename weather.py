from bs4 import BeautifulSoup
import urllib.request as req
import ssl

kor2eng = {
    '미세먼지': 'dust',
    '초미세먼지': 'ultra_dust',
    '자외선': 'uv',
    '좋음': 'GOOD',
    '보통': 'NORMAL',
    '나쁨': 'BAD',
    '높아요': '+',
    '낮아요': '-',
}


def analyze_summary(summary):
    _, temp_diff, up_down, stats = summary.text.split()
    up_down = kor2eng[up_down]
    temp_diff = up_down + temp_diff + 'C'
    return {
        'temp_diff': temp_diff,
        'stats': stats
    }


def analyze_today_chart(today_chart_list):
    result = {}
    for i in today_chart_list:
        title = i.find('strong', 'title').text.strip()
        txt = i.find('span', 'txt').text.strip()
        try:
            result[kor2eng[title]] = kor2eng[txt]
        except KeyError:
            pass
    return result


def get_weather():
    result = {}
    webpage = req.urlopen(
        'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EB%82%A0%EC%94%A8',
        context=ssl._create_unverified_context())
    soup = BeautifulSoup(webpage, 'html.parser')
    today_chart_list = analyze_today_chart(soup.find('ul', 'today_chart_list').findAll('li'))
    summary = analyze_summary(soup.find('p', 'summary'))

    current = {
        'location': soup.find('h2', 'title').text.strip(),
        'temps': soup.find('div', 'temperature_text').text.strip().removeprefix('현재 온도') + 'C',
    }

    result.update(current)
    result.update(today_chart_list)
    result.update(summary)

    return result


if __name__ == '__main__':
    print(get_weather())
