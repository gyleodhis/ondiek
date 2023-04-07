import dash
from dash import Dash, html, dcc
import datetime as dt
from dash.dependencies import Input, Output

app = Dash(__name__,use_pages=True)
server = app.server
app.title = 'Ondiek'

app.layout = html.Div(
    className='hold-transition sidebar-mini layout-fixed layout-footer-fixed layout-navbar-fixed',
    children=[
        html.Div(className='wrapper', children=[
            html.Nav(className="main-header navbar navbar-expand",
                     # Left navbar links
                     children=[
                         html.Ul(className="navbar-nav", children=[
                             html.Li(className='nav-item', children=[
                                 html.A(className='nav-link', href='#', **{'data-widget': 'pushmenu'}, role='button',
                                        children=[html.I(className='fas fa-bars')])]),
                             html.Li(className='nav-item d-sm-inline-block', children=[
                                 html.A('Home', className='nav-link', href=dash.page_registry['pages.home']['path'])]),
                             html.Li(className='nav-item d-sm-inline-block', children=[
                                 html.A('About', className='nav-link', href=dash.page_registry['pages.about']['path'])])
                         ]),
                         html.Ul(className='navbar-nav ml-auto', children=[
                             html.Form(className='form-inline ml-3', children=[
                                 html.Div(className='input-group input-group-sm', children=[
                                     dcc.Input(className='form-control form-control-navbar', type='search',
                                               placeholder='Search'),
                                     html.Div(className='input-group-append',
                                              children=[
                                                  html.Button(className='btn btn-navbar', type='submit',
                                                              children=html.I(className='fas fa-search'))
                                              ])])])])
                     ]),
            # Main Sidebar Container
            html.Aside(className='main-sidebar sidebar-dark-primary elevation-4',
                       # Logo container
                       children=[
                           html.A(className='brand-link',
                                  href='https://www.linkedin.com/in/gaylord-odhiambo-992990150/',
                                  target='_blank', children=[
                                   html.Img(className='brand-image img-circle elevation-3', src='assets/img/gyle.jpg',
                                            alt='Profile Pic',
                                            style={'opacity': .8}),
                                   html.Span('Ondiek', className='brand-text font-weight-light')
                               ]),
                           html.Div(className='sidebar', children=[
                               html.Div(className='mt-2', children=[
                                   html.Ul(className='nav nav-pills nav-sidebar flex-column',**{'data-widget': 'treeview', 'data-accordion': 'false'},
                                           role='menu',children=[
                                           html.Li(className='nav-item active', children=[
                                               html.A(className='nav-link', href=dash.page_registry['pages.home']['path'], children=[
                                                   html.I(className='nav-icon fas fa-globe-africa text-success'),
                                                   html.P(children=['Home'])])
                                           ])
                                           # html.Li(className='nav-item', children=[
                                           #     html.A(className='nav-link', href=dash.page_registry['pages.climate']['path'], children=[
                                           #         html.I(className='nav-icon fa fa-sun-o'),
                                           #         html.P('Page 2')
                                           #     ])])
                                       ])
                               ])
                           ])
                       ]),
            # Content Wrapper. Contains page content
            html.Div(className='content-wrapper',
                     children=[
                         dash.page_container
                         # html.Div(id='page-content')
                     ]),
            html.Footer(className='main-footer', children=[
                html.Strong('Ondiek© | %s' %dt.date.today().year)
            ])])
    ])

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=5050, debug=False)
