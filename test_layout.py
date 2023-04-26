from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal, VerticalScroll
from textual.widgets import Header, Static

from weather import WeatherWidget


class CombiningLayoutsExample(App):
    CSS_PATH = "test_layout.css"

    def compose(self) -> ComposeResult:
        yield Header()
        with Container(id="app-grid"):
            with VerticalScroll(id="left-pane"):
                for number in range(15):
                    yield Static(f"Vertical layout, child {number}")
            with Horizontal(id="top-right"):
                yield WeatherWidget()
            with Container(id="bottom-right"):
                yield Static("This")
                yield Static("panel")
                yield Static("is")
                yield Static("using")
                yield Static("grid layout!", id="bottom-right-final")


if __name__ == "__main__":
    app = CombiningLayoutsExample()
    app.run()
