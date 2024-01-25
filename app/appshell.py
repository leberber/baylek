import dash_mantine_components as dmc

from dash import html
from dash_iconify import DashIconify as icon

header = dmc.Paper(
    className = 'header',
    shadow='xs',
    display='flex',
    pb = '7px',
    children =[
        dmc.Image(src="/assets/baylek.png",  width=80),
        html.Div(
            style= {'position':'absolute', 'right':5},
            children=[
                dmc.ActionIcon(
                    id = 'theme_switcher',
                    n_clicks=0, 
                    variant= "transparent",
                    # bg = 'red',
                    # size = 30,
                    
                    
                    children = [
                        icon(icon="ic:baseline-light-mode",  color='gold')
                    ]
                )
            ]
        ),

    ]
)