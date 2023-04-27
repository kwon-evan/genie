from urllib.request import Request, urlopen

from rich.text import Text

from textual import work
from textual.app import App, ComposeResult
from textual.widget import Widget
from textual.widgets import Static, Label


# TODO: this cannot be focused, but it should be.
class WeatherWidget(Widget):
    CSS_PATH = "weather.css"

    def compose(self) -> ComposeResult:
        weather = Label("Now Loading...", id="weather-content")
        weather.styles.border = ("round", "white")
        weather.styles.padding = 1
        weather.styles.box_sizing = "content-box"
        self.can_focus = True
        yield weather

    async def on_mount(self, event: str) -> None:
        """Called when the widget is mounted."""
        self.update_weather()

    @work(exclusive=True)
    def update_weather(self) -> None:
        """Update the weather for the given city."""
        weather_widget = self.query_one("#weather-content", Label)

        # Query the network API
        url = f"https://wttr.in/?0nQF"
        # url = f"https://wttr.in/?0nQF&lang=ko"
        request = Request(url)
        request.add_header("User-agent", "CURL")
        response_text = urlopen(request).read().decode("utf-8")
        weather = Text.from_ansi(response_text)
        # weather_widget.update(weather)
        self.refresh()


class WeatherApp(App):
    """App to display the current weather."""

    def compose(self):
        yield WeatherWidget()


if __name__ == "__main__":
    app = WeatherApp()
    app.run()
