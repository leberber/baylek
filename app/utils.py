
from dash_iconify import DashIconify 
def id_dict (_id, index):
    return {"type": f"{_id}", "index":f"{index}"}

def iconify(icon, color = 'dark', width=30):
    return DashIconify(icon=icon,  color=color, width = width)