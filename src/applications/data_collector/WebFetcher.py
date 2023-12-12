import asyncio
from pyppeteer import launch
from pyppeteer.errors import TimeoutError

class WebFetcher:
    def __init__(self, url = None , html_content = None ):
        self.url = url
        self.response = []
        self.html_content = html_content

    async def fetch(self):
        if self.url is None:
            raise ValueError("Cannot fetch without a URL.")
        browser = await launch()
        page = await browser.newPage()
        try:
            await page.goto(self.url, {'waitUntil': 'domcontentloaded'})
            # Wait for 5 seconds to allow JavaScript to execute and populate the page
            await asyncio.sleep(5)
            self.response = await page.content()
            print("Page fetched.")
        except TimeoutError:
            print("Timeout waiting for page to load.")
        finally:
            await browser.close()

    def run(self):
        asyncio.run(self.fetch())

