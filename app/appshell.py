import dash_mantine_components as dmc


from dash import html

from utils import iconify

header = dmc.Paper(
    className = 'header',
    shadow='xs',
    children =[
        dmc.Group(
            position = 'apart',
            children = [
                dmc.Image(src="/assets/baylek.png",  width='6rem'),
                dmc.Flex(
                    children=[
                        dmc.ActionIcon(
                            id = 'theme_switcher',
                            n_clicks=0, 
                            variant= "transparent",
                            children = [
                                iconify(icon="ic:baseline-light-mode",  color='gold')
                            ]
                        )
                    ]
                )
            ]
        )
    ]
)