from typing import Literal
from playwright.async_api import async_playwright
from playwright.sync_api import sync_playwright
import charset_normalizer
from markdownify import markdownify
import asyncio
import concurrent.futures


class Loader:
    def __call__(self, url: str) -> str:
        return self.load(url)

    def load(self, url: str) -> str:
        raise NotImplementedError

    async def async_load(self, url: str):
        loop = asyncio.get_running_loop()
        with concurrent.futures.ProcessPoolExecutor() as executor:
            result = await loop.run_in_executor(executor, self.load, url)
            return result


class LoaderError(Exception):
    pass


def normalize_whitespace(text: str) -> str:
    lines = []
    for line in text.splitlines():
        stripped = line.strip()
        if stripped:
            lines += [stripped]
    return "\n".join(lines)


def html_to_markdown(content: str | bytes) -> str:
    if isinstance(content, bytes):
        content = str(charset_normalizer.from_bytes(content).best())
    md = markdownify(content, strip=["a", "img"])
    return normalize_whitespace(md)


class PlaywrightLoader(Loader):
    def __init__(
        self,
        timeout: float | None = 0,
        wait_until: (
            Literal["commit", "domcontentloaded", "load", "networkidle"] | None
        ) = None,
        browser_headless: bool = True,
    ) -> None:
        self.timeout = timeout
        self.wait_until = wait_until
        self.browser_headless = browser_headless

    def load(self, url: str) -> str:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=self.browser_headless)
            page = browser.new_page()
            page.goto(url, timeout=self.timeout, wait_until=self.wait_until)
            content = page.content()
            browser.close()
            return content

    async def async_load(self, url: str) -> str:
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=self.browser_headless)
            page = await browser.new_page()
            await page.goto(url, timeout=self.timeout, wait_until=self.wait_until)
            content = await page.content()
            await browser.close()
            return content
