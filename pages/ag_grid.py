import dash
from dash import html, dcc
import controller.my_functions as mf
from controller.wb_forest import df_PctForestArea,df_percentlost
from controller.forest_ag_grid import forest_table
from utils.config import Ondiek_name

dash.register_page(__name__,path='/table',name='Page 3',title=Ondiek_name,image_url='assets/img/site_meta.jpeg',
                   description='A Python module to help you get up and running with Plotly Dash Dashboards.')
layout = html.Div([
    html.Section(className='content-header', children=[
        html.Div(className='container-fluid', children=[
            html.Div(className='row mb-2', children=[
                html.Div(className='col-sm-6', children=[
                    html.H1('Africa\'s Forest Cover')
                ]),
                html.Div(className='col-sm-6', children=[
                    html.Ol(className='breadcrumb float-sm-right', children=[
                        html.Li(className='breadcrumb-item', children=[
                            html.A('Home', href='/')]),
                        html.Li('Ag Grid', className='breadcrumb-item active')
                    ])
                ])
            ])
        ])
    ]),
    html.Section(className='content', children=[
        html.Div(className='container-fluid', children=[
            html.Div(className='row', children=[
                html.Div(className='col-md-12', children=[
                    html.Div(className='row', children=[
                        html.Div(className='col-md-3', children=[
                            html.Div(className='small-box bg-success', children=[
                                html.Div(className='inner', children=[
                                    html.H4('Entire Continent'),
                                    html.P('%s%%'%mf.round_up(df_PctForestArea['YR2020'].iloc[19],2))
                                ]),
                                html.A('Current Forest cover',className='small-box-footer', href='#')
                            ])
                        ]),
                        html.Div(className='col-md-3', children=[
                            html.Div(className='small-box bg-success', children=[
                                html.Div(className='inner', children=[
                                    html.H4(df_PctForestArea['Country'].iloc[0]),
                                    html.P('%s%%'%mf.round_up(df_PctForestArea['YR2020'].iloc[0],2))
                                ]),
                                html.A('Most Covered Country',className='small-box-footer', href='#')
                            ])
                        ]),
                        html.Div(className='col-md-3', children=[
                            html.Div(className='small-box bg-danger', children=[
                                html.Div(className='inner', children=[
                                    html.H4(df_PctForestArea['Country'].iloc[-1]),
                                    html.P('%s%%'%mf.round_up(df_PctForestArea['YR2020'].iloc[-1],2))
                                ]),
                                html.A('Least Covered Country',className='small-box-footer', href='#')
                            ])
                        ]),
                        html.Div(className='col-md-3', children=[
                            html.Div(className='small-box bg-danger', children=[
                                html.Div(className='inner', children=[
                                    html.H4(df_percentlost['Country'].iloc[0]),
                                    html.P('%s%%'%mf.round_up(df_percentlost['Pct_Lost'].iloc[0],2))
                                ]),
                                html.A('Highest Loss in 18 Yrs',className='small-box-footer', href='#')
                            ])
                        ])
                    ])
                ])
            ]),
            # """Forest land table"""
            html.Div(className='row', children=[
                html.Div(className='col-md-12', children=[
                    html.Div(className='card', children=[
                        html.Div(className='card-header border-0', children=[
                            html.Div(className='d-flex justify-content-between', children=[
                                html.H3('Percentage Cover Year on Year', className='card-title')
                            ])
                        ]),
                        html.Div(className='card-body', children=[
                            html.Div(className='tab-content p-0', children=[
                                html.Div(className='active tab-pane', children=[
                                    html.Div(className='position-relative mb-4', children=[
                                        dcc.Loading(type='circle',color='#006400',children=html.Div(forest_table))
                                    ])] )
                            ])
                        ])
                    ])
                ])
            ])
        ])
    ])

])