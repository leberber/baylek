// ctx = window.dash_clientside.callback_context;

window.dash_clientside = Object.assign({}, window.dash_clientside, {
   
    clientside: {
  


        theme_switcher: function (n_clicks) {

            let lightIcon = {'props': {'icon': 'ic:baseline-light-mode', 'width': 40, 'color':'gold'}, 'type': 'DashIconify', 'namespace': 'dash_iconify'}
            let darkIcon = {'props': {'icon': 'ic:sharp-dark-mode', 'width': 40, 'color':'#e8e3e6'}, 'type': 'DashIconify', 'namespace': 'dash_iconify'}
            let lightColorScheme =  { 
                "fontFamily": "'Roboto','Arial',sans-serif",
                "colorScheme": "light",
                "colors": {
                    "prussian_blue": ["#4A5468","#465064","#424C60","#3E485B","#3A4457","#354053","#313C4F","#2D384A","#293446","#253042"],
                },
        
                "shadows": {
                    "xs": "0px 4px 3px -3px rgba(0, 0, 0, 0.05)",
                    "xl": "inset 0px 4px 3px -3px rgba(0, 0, 0, 0.05)",
                }
            }
            let darktColorScheme =  { 
                "colorScheme": "dark",
                "fontFamily": "'YouTube Sans','Roboto',sans-serif",
                "colors": {
                 "prussian_blue": ["#4A5468","#465064","#424C60","#3E485B","#3A4457","#354053","#313C4F","#2D384A","#293446","#253042"],
                },
                "shadows": {
               
                    "xs": "0px 4px 3px -3px rgba(66, 66, 66, 1)",
                    "xl": "inset 0px 4px 3px -3px rgba(66, 66, 66, 1)",
                }
            }
        
            if (n_clicks % 2 === 0) { 
                return [lightColorScheme, lightIcon]
              } 
         
          return [darktColorScheme, darkIcon]
        },
   
    },
});