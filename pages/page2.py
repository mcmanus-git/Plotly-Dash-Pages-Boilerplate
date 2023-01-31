from dash import html, register_page  #, callback # If you need callbacks, import it here.

register_page(
    __name__,
    name='Page 2',
    top_nav=True,
    path='/page2'
)


def layout():
    layout = html.Div([
        html.H1(
            [
                "Page 2"
            ]
        )
    ])
    return layout
