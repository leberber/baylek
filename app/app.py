
# print(pprint.pformat( shop_card('product_name', 'product_code', 'product_price',  'product_quantity', 'image_path')))
from dash import Dash, dcc, html, Input, Output, State, ALL,  MATCH, callback, ctx, no_update,   clientside_callback, ClientsideFunction
from dash_iconify import DashIconify as icon
import dash_mantine_components as dmc
import pprint
from appshell import header
from utils import id_dict
import os 




# import pandas as pd
# from pages.shop import  shop

app = Dash(
    __name__,
    # suppress_callback_exceptions=True,
    external_stylesheets=[
        "https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400;500;900&display=swap"
    ],   
)


server = app.server


# print(data)

# print(pprint.pformat(dmc.Group().to_plotly_json() ))
# print(dmc.theme.DEFAULT_COLORS)
# style = {
#     "height": '100vh',
#     "border": f"10px solid {dmc.theme.DEFAULT_COLORS['dark'][1]}",
#     "marginTop": 0,
# }

app.layout = html.Div(
    children=[  
        dmc.MantineProvider(
            id = 'theme',
            
            withGlobalStyles=True,
            children=[
                dmc.Container(
                    style={
                        "height": '100vh',
                        "border": f"1px solid blue",
                        "marginTop": 0,
                    },
                    size = 2000,
                    children = [
                   
                        header,
                        dmc.Text("Lorem velit ex excepteur enim dolor commodo labore ullamco adipisicing non officia sit.", size = '1em'),
                    ]
                )
            ]
        ) 
    ]
)



clientside_callback(
    ClientsideFunction(
        namespace='clientside',
        function_name='theme_switcher'
    ),
    Output("theme", "theme"),
    Output("theme_switcher", "children"),
    Input("theme_switcher", "n_clicks"),
)





if __name__ == "__main__":
    app.run_server(debug=True, host='0.0.0.0', port=8050 )

