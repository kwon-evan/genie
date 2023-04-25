import asyncio
from bs4 import BeautifulSoup
import urllib.request as req
import ssl
from rich import print


async def _topic_parser(topic):
    topic_title = topic.find('div', 'topictitle').find('a')
    desc = topic.find('div', 'topicdesc')
    topic_info = topic.find('div', 'topicinfo').text.split('|')[0].split()
    topic_id = desc.find('a')['href'].split('topic?id=')[-1]
    return {
        'topic_id': topic_id,
        'title': topic_title.text,
        'ref_url': topic_title['href'],
        'topic_url': 'https://news.hada.io/' + desc.find('a')['href'],
        'desc': desc.text,
        'author': topic_info[-2],
        'posted_time': topic_info[-1],
    }


async def get_articles():
    webpage = req.urlopen(
        'https://news.hada.io/',
        context=ssl._create_unverified_context())
    soup = BeautifulSoup(webpage, 'html.parser')
    topics = soup.find('div', 'topics').findAll('div', 'topic_row')

    tasks = asyncio.gather(*[_topic_parser(topic) for topic in topics])
    return await tasks


async def main():
    ret = await get_articles()
    print(ret)


if __name__ == '__main__':
    asyncio.run(main())
