import dash
from dash import Dash, html, dcc
import datetime as dt
from utils.config import Ondiek_port,Ondiek_name,Ondiek_creator_url

app = Dash(__name__,use_pages=True)
server = app.server
app.title = Ondiek_name

app.layout = html.Div(
    className='hold-transition sidebar-mini layout-fixed layout-footer-fixed',
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
                                 html.A('Docs', className='nav-link', href=dash.page_registry['pages.docs']['path'])])
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
                                  href=Ondiek_creator_url,
                                  target='_blank', children=[
                                   html.Img(className='brand-image img-circle elevation-3', src='assets/img/logo.png',
                                            alt='Brand Pic',style={'opacity': .8}),
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
                                           ]),
                                           html.Li(className='nav-item', children=[
                                               html.A(className='nav-link', href=(dash.page_registry['pages.linegraph']['path']),
                                                      children=[
                                                          html.I(className='nav-icon fa fa-tree'),
                                                          html.P('Page 2')
                                               ])]),
                                           html.Li(className='nav-item', children=[
                                               html.A(className='nav-link', href=(dash.page_registry['pages.ag_grid']['path']),
                                                      children=[
                                                          html.I(className='nav-icon fa fa-table'),
                                                          html.P('Page 3')
                                               ])])
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
    app.run_server(host='0.0.0.0', port=Ondiek_port, debug=False)
