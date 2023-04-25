import httpx
from rich.text import Text

from textual import work
from textual.app import App, ComposeResult
from textual.containers import VerticalScroll
from textual.widgets import Input, Static

from weather import update_weather


class WeatherApp(App):
    """App to display the current weather."""

    CSS_PATH = "weather.css"

    def compose(self) -> ComposeResult:
        yield Input(placeholder="Enter a City")
        with VerticalScroll(id="weather-container"):
            yield Static(id="weather")

    async def on_input_changed(self, message: Input.Changed) -> None:
        """Called when the input changes"""
        self.update_weather(message.value)

    @work(exclusive=True)
    async def update_weather(self, city: str) -> None:
        """Update the weather for the given city."""
        weather_widget = self.query_one("#weather", Static)
        if city:
            weather_widget.update(await update_weather(city))
        else:
            # No city, so just blank out the weather
            weather_widget.update("")


if __name__ == "__main__":
    app = WeatherApp()
    app.run()
