from weather import WeatherWidget

from textual.app import App, ComposeResult
from textual.widgets import TextLog
from textual import events


class KeyLogger(TextLog):
    def on_key(self, event: events.Key) -> None:
        self.write(event)


class InputApp(App):
    """App to display key events."""

    CSS_PATH = "key03.css"

    def compose(self) -> ComposeResult:
        yield KeyLogger()
        yield KeyLogger()
        yield KeyLogger()
        yield WeatherWidget(id="weather")

    def on_key(self, event: events.Key) -> None:
        self.log(event)

        if event.key == "j":
            self.action_focus_next()

        if event.key == "k":
            self.action_focus_previous()

        if event.key == 'enter':
            if self.focused is not None:
                self.log(self.focused)

        if event.key == 'c':
            weather = self.query_one("#weather", WeatherWidget)
            self.log(weather.focusable)
            self.log(weather.can_focus)
            self.log(weather.can_focus_children)

        if event.key == 'q':
            self.exit()


if __name__ == "__main__":
    app = InputApp()
    app.run()
