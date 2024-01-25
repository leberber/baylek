
# print(pprint.pformat( shop_card('product_name', 'product_code', 'product_price',  'product_quantity', 'image_path')))
from dash import Dash, dcc, html, Input, Output, State, ALL,  MATCH, callback, ctx, no_update,   clientside_callback, ClientsideFunction
from dash_iconify import DashIconify as icon
import dash_mantine_components as dmc
import pprint
from appshell import header
from utils import id_dict
from pydantic import BaseModel
from prisma import Prisma
import os 


db = Prisma(
        datasource={
            'url': os.environ.get('DATABASE_URL'),
        }
    )
db.connect()

posts = db.doctors.find_many()

db.disconnect()
print(posts)
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





 

app.layout = html.Div(
    children=[  
        dmc.MantineProvider(
            id = 'theme',
            withGlobalStyles=True,
            children=[
                html.Div(
                    children = [
                        header,
       
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

