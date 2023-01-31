from dash import html, register_page  #, callback # If you need callbacks, import it here.

register_page(
    __name__,
    name='Page 3',
    top_nav=True,
    path='/page3'
)


def layout():
    layout = html.Div([
        html.H1(
            [
                "Page 3"
            ]
        )
    ])
    return layout
