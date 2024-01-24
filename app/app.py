from dash import Dash, html

app = Dash(__name__)

server = app.server
app.layout = html.Div(
  'Hello Dash '
)
