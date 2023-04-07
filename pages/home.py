import dash
from dash import html, dcc

dash.register_page(__name__,path='/',name='Home',title='Ondiek',image_url='assets/img/site_meta.jpeg',
                   description='A Python module to help you get up and running with Plotly Dash.')
layout = html.Div([
    html.Section(className='content-header', children=[
        html.Div(className='container-fluid', children=[
            html.Div(className='row mb-2', children=[
                html.Div(className='col-sm-6', children=[
                    html.H1('Ondiek. Build dashboards faster')
                ]),
                html.Div(className='col-sm-6', children=[
                    html.Ol(className='breadcrumb float-sm-right', children=[
                        html.Li(className='breadcrumb-item', children=[
                            html.A('Home', href='/')
                        ]),
                        html.Li('Home', className='breadcrumb-item active')
                    ])
                ])
            ])
        ])
    ]),
    html.Section(className='content', children=[
        html.Div(className='container-fluid', children=[
            html.Div(className='row', children=[
                html.Div(className='col-md-3', children=[
                    html.Div(className='small-box bg-success', children=[
                        html.Div(className='inner', children=[
                            html.H4('Total Cases')
                        ]),
                        html.A(20,className='small-box-footer', href='#'),
                        html.A(50,className='small-box-footer', href='#')
                    ])
                ]),
                html.Div(className='col-md-3', children=[
                    html.Div(className='small-box bg-success', children=[
                        html.Div(className='inner', children=[
                            html.H4('Positivity Rate')
                        ]),
                        html.Div(className='icon', children=[
                            html.I(className='ion ion-bars')
                        ]),
                        html.A(120, className='small-box-footer', href='#'),
                        html.A(320, className='small-box-footer', href='#')
                    ])
                ]),
                html.Div(className='col-md-3', children=[
                    html.Div(className='small-box bg-lime', children=[
                        html.Div(className='inner', children=[
                            html.H4('Total Death')
                        ]),
                        html.Div(className='icon', children=[
                            html.I(className='ion ion-pie-graph')
                        ]),
                        html.A(63,className='small-box-footer', href='#'),
                        html.A(567,className='small-box-footer', href='#')
                    ])
                ]),
                html.Div(className='col-md-3', children=[
                    html.Div(className='small-box bg-lime', children=[
                        html.Div(className='inner', children=[
                            html.H5('Total Vaccinations')
                        ]),
                        html.Div(className='icon', children=[
                            html.I(className='ion ion-bag')
                        ]),
                        html.A(65, className='small-box-footer', href='#'),
                        html.A(782, className='small-box-footer', href='#')
                    ])
                ])
            ]),
            # The row for graphs
            html.Div(className='row', children=[
                html.Div(className='col-md-6', children=[
                    html.Div(className='card', children=[
                        html.Div(className='card-header border-0', children=[
                            html.Div(className='d-flex justify-content-between', children=[
                                html.H3('Top 10 Countries', className='card-title'),
                                html.Div(className='card-tools', children=[
                                    html.Ul(className='nav nav-pills ml-auto', children=[
                                        html.Li(className='nav-item',
                                                children=html.A('Africa', className='nav-link active',
                                                                href='#africa', **{'data-toggle': 'tab'})),
                                        html.Li(className='nav-item', children=html.A('Asia', className='nav-link',
                                                                                      href='#asia',
                                                                                      **{'data-toggle': 'tab'})),
                                        html.Li(className='nav-item', children=html.A('Europe', className='nav-link',
                                                                                      href='#europe',
                                                                                      **{'data-toggle': 'tab'})),
                                        html.Li(className='nav-item',
                                                children=html.A('N. America', className='nav-link',
                                                                href='#namerica',
                                                                **{'data-toggle': 'tab'}))
                                    ])
                                ])
                            ])
                        ]),
                        html.Div(className='card-body', children=[
                            html.Div(className='tab-content p-0', children=[
                                html.Div(className='active tab-pane', id='africa', children=[
                                    html.Div(className='d-flex', children=[
                                        html.P(className='d-flex flex-column', children=[
                                            html.Span(
                                                '%s M' % 9629,className='text-bold text-lg'),
                                            html.Span('Total Cases')
                                        ]),
                                        html.P(className='ml-auto d-flex flex-column text-right', children=[
                                            html.Span(className='text-danger', children=[
                                                html.I(547, className='fas fa-arrow-up')
                                            ]),
                                            html.Span('Africa`s % of the world', className='text-muted')
                                        ])
                                    ]),
                                    html.Div(className='position-relative mb-4', children=[
                                        html.P('Put your graph her')
                                    ])])
                            ])
                        ])
                    ])
                ]),
                html.Div(className='col-md-6', children=[
                    html.Div(className='card', children=[
                        html.Div(className='card-header border-0', children=[
                            html.Div(className='d-flex justify-content-between', children=[
                                html.H3('Top 10 Countries', className='card-title'),
                                html.Div(className='card-tools', children=[
                                    html.Ul(className='nav nav-pills ml-auto', children=[
                                        html.Li(className='nav-item',
                                                children=html.A('Africa', className='nav-link active',
                                                                href='#africa', **{'data-toggle': 'tab'})),
                                        html.Li(className='nav-item', children=html.A('Asia', className='nav-link',
                                                                                      href='#asia',
                                                                                      **{'data-toggle': 'tab'})),
                                        html.Li(className='nav-item', children=html.A('Europe', className='nav-link',
                                                                                      href='#europe',
                                                                                      **{'data-toggle': 'tab'})),
                                        html.Li(className='nav-item',
                                                children=html.A('N. America', className='nav-link',
                                                                href='#namerica',
                                                                **{'data-toggle': 'tab'}))
                                    ])
                                ])
                            ])
                        ]),
                        html.Div(className='card-body', children=[
                            html.Div(className='tab-content p-0', children=[
                                html.Div(className='active tab-pane', id='africa', children=[
                                    html.Div(className='d-flex', children=[
                                        html.P(className='d-flex flex-column', children=[
                                            html.Span(
                                                '%s M' % 9629,className='text-bold text-lg'),
                                            html.Span('Total Cases')
                                        ]),
                                        html.P(className='ml-auto d-flex flex-column text-right', children=[
                                            html.Span(className='text-danger', children=[
                                                html.I(547, className='fas fa-arrow-up')
                                            ]),
                                            html.Span('Africa`s % of the world', className='text-muted')
                                        ])
                                    ]),
                                    html.Div(className='position-relative mb-4', children=[
                                        html.P('Put your graph her')
                                    ])])
                            ])
                        ])
                    ])
                ]),
                html.Div(className='col-md-6', children=[
                    html.Div(className='card', children=[
                        html.Div(className='card-header border-0', children=[
                            html.Div(className='d-flex justify-content-between', children=[
                                html.H3('Top 10 Countries', className='card-title'),
                                html.Div(className='card-tools', children=[
                                    html.Ul(className='nav nav-pills ml-auto', children=[
                                        html.Li(className='nav-item',
                                                children=html.A('Africa', className='nav-link active',
                                                                href='#africa', **{'data-toggle': 'tab'})),
                                        html.Li(className='nav-item', children=html.A('Asia', className='nav-link',
                                                                                      href='#asia',
                                                                                      **{'data-toggle': 'tab'})),
                                        html.Li(className='nav-item', children=html.A('Europe', className='nav-link',
                                                                                      href='#europe',
                                                                                      **{'data-toggle': 'tab'})),
                                        html.Li(className='nav-item',
                                                children=html.A('N. America', className='nav-link',
                                                                href='#namerica',
                                                                **{'data-toggle': 'tab'}))
                                    ])
                                ])
                            ])
                        ]),
                        html.Div(className='card-body', children=[
                            html.Div(className='tab-content p-0', children=[
                                html.Div(className='active tab-pane', id='africa', children=[
                                    html.Div(className='d-flex', children=[
                                        html.P(className='d-flex flex-column', children=[
                                            html.Span(
                                                '%s M' % 9629,className='text-bold text-lg'),
                                            html.Span('Total Cases')
                                        ]),
                                        html.P(className='ml-auto d-flex flex-column text-right', children=[
                                            html.Span(className='text-danger', children=[
                                                html.I(547, className='fas fa-arrow-up')
                                            ]),
                                            html.Span('Africa`s % of the world', className='text-muted')
                                        ])
                                    ]),
                                    html.Div(className='position-relative mb-4', children=[
                                        html.P('Put your graph her')
                                    ])])
                            ])
                        ])
                    ])
                ]),
                html.Div(className='col-md-6', children=[
                    html.Div(className='card', children=[
                        html.Div(className='card-header border-0', children=[
                            html.Div(className='d-flex justify-content-between', children=[
                                html.H3('Top 10 Countries', className='card-title'),
                                html.Div(className='card-tools', children=[
                                    html.Ul(className='nav nav-pills ml-auto', children=[
                                        html.Li(className='nav-item',
                                                children=html.A('Africa', className='nav-link active',
                                                                href='#africa', **{'data-toggle': 'tab'})),
                                        html.Li(className='nav-item', children=html.A('Asia', className='nav-link',
                                                                                      href='#asia',
                                                                                      **{'data-toggle': 'tab'})),
                                        html.Li(className='nav-item', children=html.A('Europe', className='nav-link',
                                                                                      href='#europe',
                                                                                      **{'data-toggle': 'tab'})),
                                        html.Li(className='nav-item',
                                                children=html.A('N. America', className='nav-link',
                                                                href='#namerica',
                                                                **{'data-toggle': 'tab'}))
                                    ])
                                ])
                            ])
                        ]),
                        html.Div(className='card-body', children=[
                            html.Div(className='tab-content p-0', children=[
                                html.Div(className='active tab-pane', id='africa', children=[
                                    html.Div(className='d-flex', children=[
                                        html.P(className='d-flex flex-column', children=[
                                            html.Span(
                                                '%s M' % 9629,className='text-bold text-lg'),
                                            html.Span('Total Cases')
                                        ]),
                                        html.P(className='ml-auto d-flex flex-column text-right', children=[
                                            html.Span(className='text-danger', children=[
                                                html.I(547, className='fas fa-arrow-up')
                                            ]),
                                            html.Span('Africa`s % of the world', className='text-muted')
                                        ])
                                    ]),
                                    html.Div(className='position-relative mb-4', children=[
                                        html.P('Put your graph her')
                                    ])])
                            ])
                        ])
                    ])
                ])
            ])
        ])
    ])

])