import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import plotly.graph_objects as go
import pandas as pd
import plotly.express as px
# FOR NUMERICAL ANALYTICS
import numpy as np
# TO STORE AND PROCESS DATA IN DATAFRAME
import pandas as pd
import os
# BASIC VISUALIZATION PACKAGE
import matplotlib.pyplot as plt
# ADVANCED PLOTING
import seaborn as seabornInstance
# TRAIN TEST SPLIT
from sklearn.model_selection import train_test_split
# INTERACTIVE VISUALIZATION
#import chart_studio.plotly as py 
import plotly.graph_objs as go
import plotly.express as px
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected=True)
import statsmodels.formula.api as stats
from statsmodels.formula.api import ols
from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from discover_feature_relationships import discover
import plotly.figure_factory as ff





happiness_years = ["All", "2015", "2016", "2017","2018","2019","2020"]
models = ["Simple Linear Regression", "Multipl Linear Regression - 1", "Multiple Linear Regression - 2"]
param_options = ['Economy (GDP per Capita)', 'Family/Social Status',
       'Health (Life Expectancy)', 'freedom to make life choices',
       'Generosity', 'Perceptions of corruption']

# Read Happiness Index data
happiness_data = pd.read_csv("happiness_data_dash.csv")




app = dash.Dash(__name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}])

app.layout = html.Div([
    html.Div([
        html.Div([
            html.Img(src=app.get_asset_url('logo.jpg'),
                     id='logo-image',
                     style={
                         "height": "150px",
                         "width": "auto",
                         "margin-bottom": "8px",
                     },
                     )
        ],
            className="one-third column",
        ),
        html.Div([
            html.Div([
                html.H1("Changing World Happiness", style={"margin-bottom": "0px", 'color': '#F8F8F8', "font-size":"110px", "font-family": "Times New Roman", "text-align":"Left"}),
                html.H5("The pursuit of happiness and beyond...", style={"margin-top": "0px", 'color': 'white', "text-align":"center"}),
            ])
        ], className="one-half column", id="title"),


    ], id="header", className="row flex-display", style={"margin-bottom": "25px"}),

    html.Div([
        html.Div([
            html.Img(src=app.get_asset_url('cardH1__.png'),
                     id = 'logo-image2',
                    style={
                         "height": "400px",
                         "width": "500px",
                         "margin-bottom": "1px",
                     },
                    )], className="one-third column",
        ),

        html.Div([
            html.Img(src=app.get_asset_url('cardH2__.png'),
                     id = 'logo-image3',
                    style={
                         "height": "400px",
                         "width": "500px",
                         "margin-bottom": "1.5px",
                     },
                    )], className="one-third column",
        ),

        html.Div([
            html.Img(src=app.get_asset_url('cardH3__.png'),
                     id = 'logo-image4',
                    style={
                         "height": "400px",
                         "width": "500px",
                         "margin-bottom": "1.5px",
                     },
                    )], className="one-third column",
        ),

        html.Div([
            html.Img(src=app.get_asset_url('cardh4__.png'),
                     id = 'logo-image5',
                    style={
                         "height": "400px",
                         "width": "500px",
                         "margin-bottom": "1.5px",
                     },
                    )], className="one-third column")

    ], className="row flex-display"),
    
    
############## select option

    html.P([
        html.Div([

                    html.P('Select Year:', className='fix_label2',  style={'color': 'white'}),

                     dcc.Dropdown(id='w_year',
                                  multi=False,
                                  clearable=True,
                                  value='2020',
                                  placeholder='Select Year',
                                  options=[{'label': c, 'value': c}
                                           for c in (happiness_data['Year'].unique())], className='dcc_compon'),
                                          
         

        ], className="card_container one-half column1 offset-by-three column", id="cross-filter-options2"),
            
  
                 

        ], className="row flex-display"),
    
################ 
  
 # map section   
    html.Div([
        html.Div([
            dcc.Graph(id="map")], className="create_container1 twelve columns"),

            ], className="row flex-display"),
    
   
 # for factors card
    html.Div([
          html.Div([
              dcc.Graph(id='happiness_score') ,            
        
              ], className="card_container six columns",
        ),
          html.Div([
              dcc.Graph(id='happiness_social_status') ,            
        
              ], className="card_container six columns",
        ),
          ##
          
          html.Div([
              dcc.Graph(id='happiness_health') ,            
        
              ], className="card_container six columns",
        ),
          

       ], className="row flex-display"),
    
# for factors card
    html.Div([

          html.Div([
              dcc.Graph(id='happiness_freedom') ,            
        
              ], className="card_container six columns",
        ),
          html.Div([
              dcc.Graph(id='happiness_generosity') ,            
        
              ], className="card_container six columns",
        ),
          html.Div([
              dcc.Graph(id='happiness_corruption') ,            
        
              ], className="card_container six columns",
        ),          

       ], className="flex-display"),
    
# Sunburst and Scatter plot
 html.Div([
            html.Div([
                html.H4("Happiness Summary - Region-wise", style={"margin-bottom": "0px", 'color': 'silver', "font-size":"40px", "font-family": "Times New Roman", "text-align":"Center"}),

            ])
        ], className="one-half column", id="title4"),

    
    html.Div([

            html.Div([
                      dcc.Graph(id='sunburst_chart',
                              config={'displayModeBar': 'hover'}),
                              ], className="card_container six columns"),
            html.Div([
                        dcc.Graph(id='graph-with-slider'),
                        dcc.Slider(
                            id='year-slider',
                            min=happiness_data['Year'].min(),
                            max=happiness_data['Year'].max(),
                            value=happiness_data['Year'].min(),
                            marks={str(year): str(year) for year in happiness_data['Year'].unique()},
                            step=None
                            )],className="card_container six columns"),

                  

        ], className="row flex-display"),




###################### Country specific
 html.Div([
            html.Div([
                html.H4("Happiness Summary - Country-wise", style={"margin-bottom": "0px", 'color': 'silver', "font-size":"40px", "font-family": "Times New Roman", "text-align":"Center"}),

            ])
        ], className="one-half column", id="title3"),

    
    html.Div([
        html.Div([

                    html.P('Select Country:', className='fix_label',  style={'color': 'white'}),

                     dcc.Dropdown(id='w_countries',
                                  multi=False,
                                  clearable=True,
                                  value='India',
                                  placeholder='Select Countries',
                                  
                                  options=[{'label': c, 'value': c}
                                           for c in (happiness_data['Country'].unique())], className='dcc_compon'),
                     html.P('Happiness Rank' , className='fix_label',  style={'color': 'white', 'text-align': 'center'}),
                    
                     dcc.Graph(id='summary', config={'displayModeBar': False}, className='dcc_compon',
                      style={'margin-top': '2px'},
                      ),

                   

        ], className="create_container three columns", id="cross-filter-options"),
            html.Div([
                      dcc.Graph(id='pie_chart',
                              config={'displayModeBar': 'hover'}),
                              ], className="create_container three columns"),

                    html.Div([
                        dcc.Graph(id="line_chart")

                    ], className="create_container six columns"),

        ], className="row flex-display"),
 
   
      html.Div([
            html.Div([
                html.H4("Analysis of various Happiness factors against GDP", style={"margin-bottom": "0px", 'color': 'silver', "font-size":"40px", "font-family": "Times New Roman", "text-align":"Center"}),

            ])
        ], className="one-half column", id="title2"),
    
      html.Div([

           
            html.Div([
                        dcc.Graph(id='graph-with-slide1'),
                        dcc.Slider(
                            id='year-slide1',
                            min=happiness_data['Year'].min(),
                            max=happiness_data['Year'].max(),
                            value=happiness_data['Year'].min(),
                            marks={str(year): str(year) for year in happiness_data['Year'].unique()},
                            step=None
                            )],className="card_container six columns"),
            html.Div([
                        dcc.Graph(id='graph-with-slide2'),
                        dcc.Slider(
                            id='year-slide2',
                            min=happiness_data['Year'].min(),
                            max=happiness_data['Year'].max(),
                            value=happiness_data['Year'].min(),
                            marks={str(year): str(year) for year in happiness_data['Year'].unique()},
                            step=None
                            )],className="card_container six columns"),

            
        ], className="row flex-display"),
      
      html.Div([
          
          
            html.Div([
                        dcc.Graph(id='graph-with-slide3'),
                        dcc.Slider(
                            id='year-slide3',
                            min=happiness_data['Year'].min(),
                            max=happiness_data['Year'].max(),
                            value=happiness_data['Year'].min(),
                            marks={str(year): str(year) for year in happiness_data['Year'].unique()},
                            step=None
                            )],className="card_container six columns"),
            html.Div([
                        dcc.Graph(id='graph-with-slide4'),
                        dcc.Slider(
                            id='year-slide4',
                            min=happiness_data['Year'].min(),
                            max=happiness_data['Year'].max(),
                            value=happiness_data['Year'].min(),
                            marks={str(year): str(year) for year in happiness_data['Year'].unique()},
                            step=None
                            )],className="card_container six columns"),
           ], className="row flex-display"),
            
            
      html.Div([
            html.Div([
                        dcc.Graph(id='graph-with-slide5'),
                        dcc.Slider(
                            id='year-slide5',
                            min=happiness_data['Year'].min(),
                            max=happiness_data['Year'].max(),
                            value=happiness_data['Year'].min(),
                            marks={str(year): str(year) for year in happiness_data['Year'].unique()},
                            step=None
                            )],className="card_container six columns"),
            html.Div([
            html.P('Correlation between Happiness Parameters : Select Year >>', className='fix_label2',  style={'color': 'white'}),

                     dcc.Dropdown(id='w_year3',
                                  multi=False,
                                  clearable=True,
                                  value='All',
                                  placeholder='Correlation between Happiness Parameters : Select Year >>',
                                  options=[{'label': c, 'value': c}
                                           for c in happiness_years], className='dcc_compon'),
            dcc.Graph(id="heat")] ,className="card_container six columns"),
                  

        ], className="row flex-display"),

     html.Div([
            html.Div([
                html.H4("Distribution of a Happiness Score", style={"margin-right": "50px", 'color': 'silver', "font-size":"40px", "font-family": "Times New Roman", "text-align":"center"}),

            ])
        ], className="one-half column", id="title1"),
     
 ############## select option

    html.P([
        html.Div([

                    html.P('Select Year:', className='fix_label2',  style={'color': 'white'}),

                      dcc.Dropdown(id='w_year2',
                                  multi=False,
                                  clearable=True,
                                  value='All',
                                  placeholder='Select Year',
                                  options=[{'label': c, 'value': c}
                                            for c in happiness_years], className='dcc_compon'),
                                          
         

        ], className="card_container one-half column1 offset-by-three column", id="cross-filter-options5"),
            
  
                 

        ], className="row flex-display"),
    
################
     
     html.Div([
        html.Div([
           
            dcc.Graph(id="hist")], className="create_container1 twelve columns"),

            ], className="row flex-display"),
     
#########
     html.Div([
            html.Div([
                html.H4("Relationship between different features with Happiness Score.", style={'color': 'silver', "font-size":"40px", "font-family": "Times New Roman", "text-align":"center"}),

            ])
        ], className="one-half column", id="title5"),


############## select parameters


    html.P([
        html.Div([

                    html.P('Select Parameter:', className='fix_label2',  style={'color': 'white'}),

                     dcc.Dropdown(id='w_param',
                                  multi=False,
                                  clearable=True,
                                  value='Economy (GDP per Capita)',
                                  placeholder='Select Parameter',
                                  options=[{'label': c, 'value': c}
                                           for c in (param_options)], className='dcc_compon'),
                                          
         

        ], className="card_container one-half column2 offset-by-four column", id="cross-filter-options3"),
            
  
                 

        ], className="row  flex-display"),
    
################ 

# for factors card
    html.Div([
          html.Div([
              dcc.Graph(id='histogram_param') ,            
        
              ], className="card_container six columns",
        ),

          ## 
          
          html.Div([
              dcc.Graph(id='regression_param') ,            
        
              ], className="card_container six columns",
        ),
          

       ], className="row flex-display"),
    
  
       html.Div([
              html.P('Results of Prediction using ML Models', className='fix_label2',  style={'color': 'white'}),

                               
               html.Img(src=app.get_asset_url('model.png'),
                     id = 'logo-image12',
                    style={
                         "height": "300px",
                         "width": "2000px",
                         "margin-bottom": "1.5px",
                     },
                    )              
        
              ], className="card_container twelve columns",
        ),

# for factors card
        html.Div([
          html.Div([
              html.Img(src=app.get_asset_url('pearson__.png'),
                     id = 'logo-image11',
                    style={
                         "height": "550px",
                         "width": "900px",
                         "margin-bottom": "1.5px",
                     },
                    )           
        
              ], className="card_container six columns",
              
          
        ),
          
          html.Div([
              html.Img(src=app.get_asset_url('mkr.png'),
                     id = 'logo-image13',
                    style={
                         "height": "550px",
                         "width": "900px",
                         "margin-bottom": "1.5px",
                     },
                    )           
        
              ], className="card_container six columns",
              
          
        ),
          
          


       ], className="row flex-display"),
    html.Div([
            html.Div([
                html.H4("Mitti Ke Rang | Author: Pradnya Patil", style={"margin-bottom": "0px", 'color': 'silver', "font-size":"40px", "font-family": "Times New Roman", "text-align":"Center"}),

            ])
        ], className="one-half column"), 
    

    ], id="mainContainer",
    style={"display": "flex", "flex-direction": "column"})


######################
#Create histogram plot
@app.callback(
    Output('hist', 'figure'),
    [Input('w_year2', 'value')])
def update_histplot(selected_year):
    
    if selected_year != "All":
        year_ = int(selected_year)
        hist_df = happiness_data[happiness_data.Year == year_]
        fig = px.histogram(hist_df , x="Happiness Score", color = 'Country', opacity = 0.65, nbins=934)
    else:
        fig = px.histogram(happiness_data , x="Happiness Score", color = 'Country', opacity = 0.65, nbins=934)
   
    fig.update_layout(
    legend=dict(
        x=0,
        y=1,
        traceorder="reversed",
        title_font_family="Times New Roman",
        font=dict(
            family="Courier",
            size=14,
            color="white"
        ),
        bgcolor="#101010",
        bordercolor="#101010",
        borderwidth=4
    )
)

    fig.layout.plot_bgcolor = 'black'
    fig.layout.paper_bgcolor = 'black'
    fig.update_xaxes(title_font=dict(size=25, family='Courier', color='crimson'),tickfont=dict(family='Rockwell', color='silver', size=14), showgrid=False)
    fig.update_yaxes(title_font=dict(size=25, family='Courier', color='crimson'),tickfont=dict(family='Rockwell', color='silver', size=14) ,showgrid=False)
    fig.update_layout(legend_title=dict(font=dict(color='White')))
    

    return fig   



#Create heatmap plot
@app.callback(
    Output('heat', 'figure'),
    [Input('w_year3', 'value')])
def update_heatmap(selected_year):
    
    if selected_year != "All":
        year__ = int(selected_year)
        heat_df = happiness_data[happiness_data.Year == year__]
        fig = px.imshow(heat_df[['Happiness Score',
       'Economy (GDP per Capita)', 'Family/Social Status',
       'Health (Life Expectancy)', 'freedom to make life choices',
       'Generosity', 'Perceptions of corruption']].corr())
    else:
        fig = px.imshow(happiness_data[['Happiness Score',
       'Economy (GDP per Capita)', 'Family/Social Status',
       'Health (Life Expectancy)', 'freedom to make life choices',
       'Generosity', 'Perceptions of corruption']].corr())
   
    fig.update_layout(
    legend=dict(
        x=0,
        y=1,
        traceorder="reversed",
        title_font_family="Times New Roman",
        font=dict(
            family="Courier",
            size=20,
            color="white"
        ),
        bgcolor="#101010",
        bordercolor="#101010",
        borderwidth=4
    )
)

    fig.layout.plot_bgcolor = 'black'
    fig.layout.paper_bgcolor = 'black'
    fig.update_layout(showlegend=False)
    #fig.update_layout(width = 3000)
    fig.update_xaxes(title_font=dict(size=25, family='Courier', color='silver'),tickfont=dict(family='Rockwell', color='silver', size=14), showgrid=False)
    fig.update_yaxes(title_font=dict(size=25, family='Courier', color='silver'),tickfont=dict(family='Rockwell', color='silver', size=14) ,showgrid=False)
    fig.update_layout(legend_title=dict(font=dict(color='White')))
    

    return fig   


#######################################
#Create histogram plot histogram_param
@app.callback(
    Output('histogram_param', 'figure'),
    [Input('w_param', 'value')])
def update_histogram_param(params):
    hist_param = happiness_data[[params, "Country"]]
    fig = px.histogram(hist_param, x=params, color = 'Country', opacity = 0.65, nbins=934)
   


    fig.layout.plot_bgcolor = 'black'
    fig.layout.paper_bgcolor = 'black'
    fig.update_layout(showlegend=False)
    
    fig.update_xaxes(title_font=dict(size=25, family='Courier', color='crimson'),tickfont=dict(family='Rockwell', color='silver', size=14), showgrid=False)
    fig.update_yaxes(title_font=dict(size=25, family='Courier', color='crimson'),tickfont=dict(family='Rockwell', color='silver', size=14) ,showgrid=False)
#    fig.update_layout(legend_title=dict(font=dict(color='White')))
    

    return fig   


#Create scatter chart for regression_param
@app.callback(
    Output('regression_param', 'figure'),
    [Input('w_param', 'value')])
def update_regression_param(param_reg):
    X = happiness_data[param_reg].values[:, None]
    X_train, X_test, y_train, y_test = train_test_split(
    X, happiness_data['Happiness Score'], random_state=42)

    model =  LinearRegression() 
    model.fit(X_train, y_train)
    pred_ = model.predict(X_test)

    x_range = np.linspace(X.min(), X.max(), 100)
    y_range = model.predict(x_range.reshape(-1, 1))

    
    fig = go.Figure([
    go.Scatter(x=X_train.squeeze(), y=y_train, 
                   name='train', mode='markers', opacity = 0.5),
    go.Scatter(x=X_test.squeeze(), y=y_test, 
                   name='test', mode='markers', opacity = 0.65),
    go.Scatter(x=x_range, y=y_range, 
                   name='regression fit')
    ])
   
    fig.update_layout(
    legend=dict(
        x=1,
        y=1,
        traceorder="reversed",
        title_font_family="Times New Roman",
        font=dict(
            family="Courier",
            size=14,
            color="white"
        ),
        bgcolor="Black",
        bordercolor="Black",
        borderwidth=2
    )
)
    fig.update_layout(transition_duration=500)
    fig.layout.plot_bgcolor = 'black'
    fig.layout.paper_bgcolor = 'black'
  
    fig.update_xaxes(title = param_reg, title_font=dict(size=25, family='Courier', color='crimson'),tickfont=dict(family='Rockwell', color='silver', size=14), showgrid=False)
    fig.update_yaxes(title = "Happiness score",title_font=dict(size=25, family='Courier', color='crimson'),tickfont=dict(family='Rockwell', color='silver', size=14) ,showgrid=False)
    fig.update_layout(legend_title=dict(font=dict(color='White')))
    

    return fig   
########conclusion
@app.callback(
    Output('conclude', 'figure'),
    [Input('w_param', 'value')])
def update_summary(w_param):
    
    if w_param == "Economy (GDP per Capita)":
        text = "The relationship between GDP per capita(Economy of the country) has a strong positive correlation with Happiness Score.<br>If the GDP per capita of a country is higher , then the Happiness Score of that country will also more likely to be high."
    if w_param == "Family/Social Status":
        text = "Social Support of countries also has a strong and positive relationship with Happiness Score.<br>So, it makes sense that we need social support to be happy.<br>People are also wired for emotions, and we experience those emotions within a social context."
    if w_param == "Health (Life Expectancy)":
        text = "A healthy life expectancy has a strong and positive relationship with the Happiness Score.<br>If the country has a High Life Expectancy, it can also have a high Happiness Score.<br>Being happy doesn’t just improve the quality of a person’s life. It may increase the quantity of life in terms of years as well."
    if w_param == "freedom to make life choices":
        text = "Freedom to make life choices has a positive relationship with Happiness Score.<br>Choice and autonomy are more directly related to happiness than having lots of money.<br>It gives us options to pursue meaning in our life, finding activities that stimulate and excite us.<br>This is an essential aspect of feeling happy."
    if w_param == "Generosity":
        text = "Generosity has a fragile linear relationship with the Happiness Score.<br>Generosity scores are calculated based on the countries which give the most to nonprofits around the world.<br>Countries that are not generous that does not mean they are not happy."
    if w_param == "Perceptions of corruption":
        text = "Distribution of Perceptions of corruption rightly skewed.<br>Very less number of countries have high perceptions of corruption.<br>That means most of the countries have a corruption problems."
     
    
    
        
    return {
            
        'data': [go.Indicator()],
            

            
                    
        'layout': go.Layout(
                title={'text': text,
                       
                       'xanchor': 'center'#,'yanchor': 'bottom'
                       #'text-align':'left'
                       },
                font=dict(color='silver', size =20),
                paper_bgcolor='black',
                plot_bgcolor='black',
                
               ),

           }


#############


@app.callback(
    Output('summary', 'figure'),
    [Input('w_countries', 'value')])
def update_summary(w_countries):
        c_data = happiness_data[happiness_data['Country'] ==w_countries]
        return {
            
            'data': [go.Indicator(
                       
                    domain={'row': 0, 'column': 0})],
            

            
                    
            'layout': go.Layout(
                title={'text': 'Year 2015: ' + str(c_data[(c_data['Year'] ==2015)]['Happiness Rank'].values[0]) + '<br>' +
                        'Year 2016: ' + str(c_data[(c_data['Year'] ==2016)]['Happiness Rank'].values[0]) +'<br>'+
                        'Year 2017: ' + str(c_data[(c_data['Year'] ==2017)]['Happiness Rank'].values[0])+'<br>'+
                        'Year 2018: ' + str(c_data[(c_data['Year'] ==2018)]['Happiness Rank'].values[0])+'<br>'+
                        'Year 2019: ' + str(c_data[(c_data['Year'] ==2019)]['Happiness Rank'].values[0])+'<br>'+
                        'Year 2020: ' + str(c_data[(c_data['Year'] ==2020)]['Happiness Rank'].values[0]),
                       
                       'xanchor': 'center',
                       'yanchor': 'top'},
                font=dict(color='orange'),
                paper_bgcolor='black',
                plot_bgcolor='black',
                
                ),

            }
     
 
# Create pie chart (total casualties)
@app.callback(Output('pie_chart', 'figure'),
              [Input('w_countries', 'value')])
              

def update_graph_pie(w_countries):
    h_year = happiness_data[happiness_data["Year"] == 2020]
    h_country = h_year[h_year["Country"] == w_countries]
    for i in h_country.columns:
        h_country.drop(h_country.index[h_country[i] == 'No Data'], inplace = True)
    
    score= h_country["Happiness Score"].values[0]
    rank = score= h_country["Happiness Rank"].values[0]
    gdp = h_country["Economy (GDP per Capita)"].values[0]
    fam= h_country["Family/Social Status"].values[0]
    health = h_country["Health (Life Expectancy)"].values[0]
    free =h_country["freedom to make life choices"].values[0]
    gen = h_country["Generosity"].values[0]
    cor = h_country["Perceptions of corruption"].values[0]
    
    
    colors = ['orange', '#dd1e35', 'green', '#e55467', "white"]
    
    return {
        'data': [go.Pie(labels=['GDP', 'Social Status', 'Freedom', 'Generosity', 'Corruption'],
                        values=[gdp ,fam,health,free,gen,cor ],
                        marker=dict(colors=colors),
                        hoverinfo='label+value+percent',
                        textinfo='label+value',
                        textfont=dict(size=13),
                        hole=.7,
                        rotation=45,
                        opacity = 0.65
                        # insidetextorientation='radial',


                        )],

        'layout': go.Layout(
            # width=800,
            # height=520,
            plot_bgcolor='black',
            paper_bgcolor='black',
            hovermode='closest',
            title={
                'text': 'Happiness Score Summary 2020',

                'y': 0.93,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'},
            titlefont={
                       'color': 'white',
                       'size': 20},
            legend={
                'orientation': 'h',
                'bgcolor': '#101010',
                'xanchor': 'center', 'x': 0.5, 'y': -0.07},
            font=dict(
                family="sans-serif",
                size=12,
                color='white')
            ),


        }

#Create Sunburst chart
@app.callback(Output('sunburst_chart', 'figure'),
              [Input('w_year', 'value')])
def update_graph_(w_year):
        #figure = go.Figure()
        chart_data = happiness_data[happiness_data["Year"] == w_year]
        figure=px.sunburst(chart_data,
                  path=["Region", "Country"],
                  values = 'Happiness Rank',
                  
                   color_continuous_scale="BrBG",
                  
                  hover_data = ['Country', 'Region', 'Year', 'Happiness Rank', 'Happiness Score',
       'upperwhisker', 'lowerwhisker', 'Economy (GDP per Capita)',
       'Family/Social Status', 'Health (Life Expectancy)',
       'freedom to make life choices', 'Generosity',
       'Perceptions of corruption'],
                  
            
                  width = 940, height=850,
                 
                  title = 'Region-wise details ' + str(w_year))
        figure.layout.plot_bgcolor = 'black'
        figure.layout.paper_bgcolor = 'black'
        figure.update_xaxes(title_font=dict(size=25, family='Courier', color='crimson'),tickfont=dict(family='Rockwell', color='silver', size=14), showgrid=False)
        figure.update_yaxes(title_font=dict(size=25, family='Courier', color='crimson'),tickfont=dict(family='Rockwell', color='silver', size=14) ,showgrid=False)
       
                   
        return figure
    
#Create scatter chart
@app.callback(
    Output('graph-with-slider', 'figure'),
    [Input('year-slider', 'value')])
def update_figure(selected_year):
    scatter_df = happiness_data[happiness_data.Year == selected_year]

    fig = px.scatter(scatter_df, x="Economy (GDP per Capita)", y="Happiness Score",
                     size="Happiness Score", color="Region", hover_name="Country",
                     log_x=True, size_max=40,opacity=0.2, width = 940, height=850)
   
    fig.update_layout(
    legend=dict(
        x=0,
        y=1,
        traceorder="reversed",
        title_font_family="Times New Roman",
        font=dict(
            family="Courier",
            size=14,
            color="white"
        ),
        bgcolor="Black",
        bordercolor="Black",
        borderwidth=2
    )
)
    fig.update_layout(transition_duration=500)
    fig.layout.plot_bgcolor = 'black'
    fig.layout.paper_bgcolor = 'black'
    fig.update_xaxes(title_font=dict(size=25, family='Courier', color='crimson'),tickfont=dict(family='Rockwell', color='silver', size=14), showgrid=False)
    fig.update_yaxes(title_font=dict(size=25, family='Courier', color='silver'),tickfont=dict(family='Rockwell', color='silver', size=14) ,showgrid=False)
    fig.update_layout(legend_title=dict(font=dict(color='White')))
    

    return fig   
 
#Create scatter chart
@app.callback(
    Output('graph-with-slide1', 'figure'),
    [Input('year-slide1', 'value')])
def update_fig1(selected_year):
    scatter_d1 = happiness_data[happiness_data.Year == selected_year]

    fig = px.scatter(scatter_d1, x="Economy (GDP per Capita)", y="Family/Social Status",
                     size="Family/Social Status", color="Region", hover_name="Country",
                     log_x=True, size_max=40,opacity=0.2, width = 940, height=600)
    
    fig.update_layout(
    legend=dict(
        x=0,
        y=1,
        traceorder="reversed",
        title_font_family="Times New Roman",
        font=dict(
            family="Courier",
            size=12,
            color="white"
        ),
        bgcolor="Black",
        bordercolor="Black",
        borderwidth=2
    )
)
    fig.update_layout(transition_duration=500)
    fig.layout.plot_bgcolor = 'black'
    fig.layout.paper_bgcolor = 'black'
    fig.update_xaxes(title_font=dict(size=25, family='Courier', color='crimson'), showgrid=False)
    fig.update_yaxes(title_font=dict(size=25, family='Courier', color='crimson') ,showgrid=False, zeroline = False)
    fig.update_layout(legend_title=dict(font=dict(color='White')))
    

    return fig   

#Create scatter chart
@app.callback(
    Output('graph-with-slide2', 'figure'),
    [Input('year-slide2', 'value')])
def update_fig2(selected_year):
    scatter_d2 = happiness_data[happiness_data.Year == selected_year]

    fig = px.scatter(scatter_d2, x="Economy (GDP per Capita)", y="Health (Life Expectancy)",
                     size="Health (Life Expectancy)", color="Region", hover_name="Country",
                     log_x=True, size_max=40,opacity=0.2, width = 940, height=600)
   
    fig.update_layout(
    legend=dict(
        x=0,
        y=1,
        traceorder="reversed",
        title_font_family="Times New Roman",
        font=dict(
            family="Courier",
            size=14,
            color="white"
        ),
        bgcolor="Black",
        bordercolor="Black",
        borderwidth=2
    )
)
    fig.update_layout(transition_duration=500)
    fig.layout.plot_bgcolor = 'black'
    fig.layout.paper_bgcolor = 'black'
    fig.update_xaxes(title_font=dict(size=25, family='Courier', color='crimson'), showgrid=False)
    fig.update_yaxes(title_font=dict(size=25, family='Courier', color='crimson'),showgrid=False, zeroline = False)
    fig.update_layout(legend_title=dict(font=dict(color='White')))
    

    return fig   

#Create scatter chart
@app.callback(
    Output('graph-with-slide3', 'figure'),
    [Input('year-slide3', 'value')])
def update_fig3(selected_year):
    scatter_d3 = happiness_data[happiness_data.Year == selected_year]

    fig = px.scatter(scatter_d3, x="Economy (GDP per Capita)", y="freedom to make life choices",
                     size="freedom to make life choices", color="Region", hover_name="Country",
                     log_x=True, size_max=40,opacity=0.2, width = 940, height=600)
   
    fig.update_layout(
    legend=dict(
        x=0,
        y=1,
        traceorder="reversed",
        title_font_family="Times New Roman",
        font=dict(
            family="Courier",
            size=14,
            color="white"
        ),
        bgcolor="Black",
        bordercolor="Black",
        borderwidth=2
    )
)
    fig.update_layout(transition_duration=500)
    fig.layout.plot_bgcolor = 'black'
    fig.layout.paper_bgcolor = 'black'
    fig.update_xaxes(title_font=dict(size=25, family='Courier', color='crimson'), showgrid=False)
    fig.update_yaxes(title_font=dict(size=25, family='Courier', color='crimson'),showgrid=False, zeroline = False)
    fig.update_layout(legend_title=dict(font=dict(color='White')))
    

    return fig 


#Create scatter chart
@app.callback(
    Output('graph-with-slide4', 'figure'),
    [Input('year-slide4', 'value')])
def update_fig4(selected_year):
    scatter_d4 = happiness_data[happiness_data.Year == selected_year]

    fig = px.scatter(scatter_d4, x="Economy (GDP per Capita)", y="Generosity",
                     size="Generosity", color="Region", hover_name="Country",
                     log_x=True, size_max=40,opacity=0.2, width = 940, height=600)
   
    fig.update_layout(
    legend=dict(
        x=0,
        y=1,
        traceorder="reversed",
        title_font_family="Times New Roman",
        font=dict(
            family="Courier",
            size=14,
            color="white"
        ),
        bgcolor="Black",
        bordercolor="Black",
        borderwidth=2
    )
)
    fig.update_layout(transition_duration=500)
    fig.layout.plot_bgcolor = 'black'
    fig.layout.paper_bgcolor = 'black'
    fig.update_xaxes(title_font=dict(size=25, family='Courier', color='crimson'), showgrid=False)
    fig.update_yaxes(title_font=dict(size=25, family='Courier', color='crimson'),showgrid=False, zeroline = False)
    fig.update_layout(legend_title=dict(font=dict(color='White')))
    

    return fig

    #Create scatter chart
@app.callback(
    Output('graph-with-slide5', 'figure'),
    [Input('year-slide5', 'value')])
def update_fig5(selected_year):
    scatter_d5 = happiness_data[happiness_data.Year == selected_year]

    fig = px.scatter(scatter_d5, x="Economy (GDP per Capita)", y="Perceptions of corruption",
                     size="Perceptions of corruption", color="Region", hover_name="Country",
                     log_x=True, size_max=40,opacity=0.2, width = 940, height=600)
   
    fig.update_layout(
    legend=dict(
        x=0,
        y=1,
        traceorder="reversed",
        title_font_family="Times New Roman",
        font=dict(
            family="Courier",
            size=14,
            color="white"
        ),
        bgcolor="Black",
        bordercolor="Black",
        borderwidth=2
    )
)
    fig.update_layout(transition_duration=500)
    fig.layout.plot_bgcolor = 'black'
    fig.layout.paper_bgcolor = 'black'
    fig.update_xaxes(title_font=dict(size=25, family='Courier', color='crimson'), showgrid=False)
    fig.update_yaxes(title_font=dict(size=25, family='Courier', color='crimson'),showgrid=False, zeroline = False)
    fig.update_layout(legend_title=dict(font=dict(color='White')))
    

    return fig
   



#Create happiness_score
@app.callback(
    Output('happiness_score', 'figure'),
    [Input('w_year', 'value')])
def update_happiness_score(w_year):
    
    return {
            
            'data': [go.Indicator(
                    mode='number+gauge+delta',
                    value=happiness_data[(happiness_data['Year'] ==w_year) & (happiness_data['Happiness Rank'] ==1)]["Happiness Score"].values[0],
                    
                    delta = {'position':"top", 
                             'reference': happiness_data[(happiness_data['Year'] == w_year -1) & (happiness_data['Happiness Rank'] ==1)]["Happiness Score"].values[0]},
                    
                    domain={'row': 0, 'column': 0})],
            

            
                    
            'layout': go.Layout(
                title={'text': 'Happiest Country of '+str(w_year) + "<br>" +happiness_data[(happiness_data['Year'] ==w_year) & (happiness_data['Happiness Rank'] ==1)].Country.values[0],
                       
                       'xanchor': 'center',
                       'yanchor': 'top'},
                font=dict(color='orange'),
                paper_bgcolor='black',
                plot_bgcolor='black',
                
                ),

            }
     

# happiness_social_status 

@app.callback(
    Output('happiness_social_status', 'figure'),
    [Input('w_year', 'value')])
def update_happiness_social_status(w_year):
    
    return {
            
            'data': [go.Indicator(
                    mode='number+gauge+delta+delta',
                    value=happiness_data[(happiness_data['Year'] ==w_year)]['Family/Social Status'].max(),
                    delta = {'position':"top", 
                             'reference': happiness_data[(happiness_data['Year'] ==w_year -1)]['Family/Social Status'].max()},
                    
                    

                    
                    domain={'row': 0, 'column': 0})],
            

            
                    
            'layout': go.Layout(
                title={'text': 'Top country family/social status wise '+str(w_year) + "<br>" +happiness_data[(happiness_data['Year'] ==w_year) & (happiness_data['Family/Social Status'] == happiness_data[(happiness_data['Year'] ==w_year)]['Family/Social Status'].max())].Country.values[0],
                       
                       
                       'xanchor': 'center',
                       'yanchor': 'top'},
                font=dict(color='orange'),
                paper_bgcolor='black',
                plot_bgcolor='black',
                #height=80
                ),

            }




#########
     
@app.callback(
    Output('happiness_health', 'figure'),
    [Input('w_year', 'value')])
def update_happiness_health(w_year):
    
    return {
            
            'data': [go.Indicator(
                    mode='number+gauge+delta',
                    value=happiness_data[(happiness_data['Year'] ==w_year)]['Health (Life Expectancy)'].max(),
                    delta = {'position':"top", 
                             'reference': happiness_data[(happiness_data['Year'] ==w_year -1)]['Health (Life Expectancy)'].max()},
                    
                    
                    domain={'row': 0, 'column': 0})],
            

            
                    
            'layout': go.Layout(
                title={'text': 'Top country Life Expectancy status wise '+str(w_year) + "<br>" +happiness_data[(happiness_data['Year'] ==w_year) & (happiness_data['Health (Life Expectancy)'] == happiness_data[(happiness_data['Year'] ==w_year)]['Health (Life Expectancy)'].max())].Country.values[0],
                       
                       
                       'xanchor': 'center',
                       'yanchor': 'top'},
                font=dict(color='orange'),
                paper_bgcolor='black',
                plot_bgcolor='black',
                #height=80
                ),

            }

# Happiness indicators
@app.callback(
    Output('happiness_freedom', 'figure'),
    [Input('w_year', 'value')])
def update_happiness_freedom(w_year):
    
    return {
            
            'data': [go.Indicator(
                    mode='number+gauge+delta',
                    value=happiness_data[(happiness_data['Year'] ==w_year)]['freedom to make life choices'].max(),
                    delta = {'position':"top", 
                             'reference': happiness_data[(happiness_data['Year'] ==w_year -1)]['freedom to make life choices'].max()},
                   
                    
                    domain={'row': 0, 'column': 0})],
            

            
                    
            'layout': go.Layout(
                title={'text': 'Top country in freedom to make life choices '+str(w_year) + "<br>" +happiness_data[(happiness_data['Year'] ==w_year) & (happiness_data['freedom to make life choices'] == happiness_data[(happiness_data['Year'] ==w_year)]['freedom to make life choices'].max())].Country.values[0],
                       
                       
                       'xanchor': 'center',
                       'yanchor': 'top'},
                font=dict(color='orange'),
                paper_bgcolor='black',
                plot_bgcolor='black',
                #height=80
                ),

            }
@app.callback(
    Output('happiness_generosity', 'figure'),
    [Input('w_year', 'value')])
def update_happiness_generosity(w_year):
    
    return {
            
            'data': [go.Indicator(
                    mode='number+gauge+delta',
                    value=happiness_data[(happiness_data['Year'] ==w_year)]['Generosity'].max(),
                    delta = {'position':"top", 
                             'reference': happiness_data[(happiness_data['Year'] ==w_year -1)]['Generosity'].max()},
                   
                    
                    
                    domain={'row': 0, 'column': 0})],
            

            
                    
            'layout': go.Layout(
                title={'text': 'Top country in Generosity '+str(w_year) + "<br>" +happiness_data[(happiness_data['Year'] ==w_year) & (happiness_data['Generosity'] == happiness_data[(happiness_data['Year'] ==w_year)]['Generosity'].max())].Country.values[0],
                       
                       
                       'xanchor': 'center',
                       'yanchor': 'top'},
                font=dict(color='orange'),
                paper_bgcolor='black',
                plot_bgcolor='black',
                #height=80
                ),

            }



@app.callback(
    Output('happiness_corruption', 'figure'),
    [Input('w_year', 'value')])
def update_happiness_corruption_perception(w_year):
    
    return {
            
            'data': [go.Indicator(
                    mode='number+gauge+delta',
                    value=happiness_data[(happiness_data['Year'] ==w_year)]['Perceptions of corruption'].max(),
                    delta = {'position':"top", 
                             'reference': happiness_data[(happiness_data['Year'] ==w_year -1)]['Perceptions of corruption'].max()},
                   
                    
                    
                    domain={'row': 0, 'column': 0})],
            

            
                    
            'layout': go.Layout(
                title={'text': 'Top country in corruption perception'+str(w_year) + "<br>" +happiness_data[(happiness_data['Year'] ==w_year) & (happiness_data['Perceptions of corruption'] == happiness_data[(happiness_data['Year'] ==w_year)]['Perceptions of corruption'].max())].Country.values[0],
                       
                       
                       'xanchor': 'center',
                       'yanchor': 'top'},
                font=dict(color='orange'),
                paper_bgcolor='black',
                plot_bgcolor='black',
                #height=80
                ),

            }



# Create bar chart for happiness over the years
@app.callback(Output('line_chart', 'figure'),
              [Input('w_countries', 'value')])
def update_graph_barchart(w_countries):
# main data frame
    happinesss_line = happiness_data[happiness_data["Country"] == w_countries]
    

    return {
        'data': [
                go.Bar(x=happinesss_line["Year"].values,
                        y=happinesss_line["freedom to make life choices"].values,

                        name='freedom to make life choices',
                        marker=dict(
                            color='white'),
                       
                        ),
                go.Bar(x=happinesss_line["Year"].values,
                        y=happinesss_line["Economy (GDP per Capita)"].values,

                        name='Economy (GDP per Capita)',
                        marker=dict(
                            color='yellow'),
                       

                        ),
                go.Bar(x=happinesss_line["Year"].values,
                        y=happinesss_line["Family/Social Status"].values,

                        name='Family/Social Status',
                        marker=dict(
                            color='orange'),
                       


                        ),
                go.Bar(x=happinesss_line["Year"].values,
                        y=happinesss_line["Perceptions of corruption"].values,

                        name='Perceptions of corruption',
                        marker=dict(
                            color='red'),
                        

                        ),
                go.Bar(x=happinesss_line["Year"].values,
                        y=happinesss_line["Generosity"].values,

                        name='Generosity',
                        marker=dict(
                            color='dark red'),
                        


                        ),
                go.Bar(x=happinesss_line["Year"].values,
                        y=happinesss_line["Health (Life Expectancy)"].values,

                        name='Health (Life Expectancy)',
                        marker=dict(
                            color='brown'),
                       

                        ),
              
                
                 go.Scatter(x=happinesss_line["Year"].values,
                            y=happinesss_line["Happiness Score"].values,
                            mode='lines',
                            name='Happiness Score',
                            line=dict(width=3, color='#FF00FF'),
                            # marker=dict(
                            #     color='green'),
                            hoverinfo='text',
                            hovertext=
                            '<b>Year</b>: ' + happinesss_line[happinesss_line['Country'] == w_countries]['Year'].astype(str) + '<br>' +
                            '<b>Happiness Score</b>: ' + [f'{x:,.0f}' for x in happinesss_line[happinesss_line['Country'] == w_countries]['Happiness Score'].values] +'<br>'
                            '<b>Happiness Rank</b>: ' + [f'{x:,.0f}' for x in happinesss_line[happinesss_line['Country'] == w_countries]['Happiness Rank'].values ]+ '<br>'
                      
                            ),
                 
                 
                 
                 ],


        'layout': go.Layout(
             barmode='stack',
             plot_bgcolor='black',
             paper_bgcolor='black',
             title={
                'text': 'Happiness Score over the years : ' + (w_countries),
                'y': 0.93,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'},
             titlefont={
                        'color': 'white',
                        'size': 20},

             hovermode='x',

             xaxis=dict(title='<b>Year</b>',
                        color='white',
                        showline=True,
                        showgrid=True,
                        showticklabels=True,
                        linecolor='white',
                        linewidth=2,
                        ticks='outside',
                        tickfont=dict(
                            family='Arial',
                            size=12,
                            color='white'
                        )

                ),

             yaxis=dict(title='<b>Happiness Score</b>',
                        color='white',
                        showline=True,
                        showgrid=True,
                        showticklabels=True,
                        linecolor='white',
                        linewidth=2,
                        ticks='outside',
                        tickfont=dict(
                           family='Arial',
                           size=12,
                           color='white'
                        )

                ),

            legend={
                'orientation': 'h',
                'bgcolor': '#101010',
                'xanchor': 'center', 'x': 0.5, 'y': -0.3},
                          font=dict(
                              family="sans-serif",
                              size=12,
                              color='white'),

                 )

    }

# Create scattermapbox chart
@app.callback(Output('map', 'figure'),
              [Input('w_year', 'value')])
def update_graph(w_year):
    happiness_data_ = happiness_data[happiness_data["Year"] == w_year]

    return {
        'data': [go.Scattermapbox(
                         lon=happiness_data_['long'],
                         lat=happiness_data_['lat'],
                         mode='markers',
                         marker=go.scattermapbox.Marker(
                                  size=(1/happiness_data_['Happiness Rank'])*10000 ,
                                  color=happiness_data_['Happiness Rank'],
                                  colorscale='hsv',
                                  showscale=False,
                                  sizemode='area',
                                  opacity=0.3),

                         hoverinfo='text',
                         hovertext=
                         '<b>Country</b>: ' + happiness_data_['Country'].astype(str) + '<br>' +
                         '<b>Region</b>: ' + happiness_data_['Region'].astype(str) + '<br>' +
                         '<b>Longitude</b>: ' + happiness_data_['long'].astype(str) + '<br>' +
                         '<b>Latitude</b>: ' + happiness_data_['lat'].astype(str) + '<br>' +
                         '<b>Happiness Score</b>: ' + [f'{x:,.0f}' for x in happiness_data_['Happiness Score']] + '<br>' +
                        
                         '<b>Happiness Rank</b>: ' + [f'{x:,.0f}' for x in happiness_data_['Happiness Rank']] + '<br>' +
                         '<b>Economy (GDP per Capita)</b>: ' + [f'{x:,.0f}' for x in happiness_data_['Economy (GDP per Capita)']] + '<br>' +
                         '<b>Family/Social Status</b>: ' + [f'{x:,.0f}' for x in happiness_data_['Family/Social Status']] + '<br>' +
                         '<b>Health (Life Expectancy)</b>: ' + [f'{x:,.0f}' for x in happiness_data_['Health (Life Expectancy)']] + '<br>' +
                         '<b>freedom to make life choices</b>: ' + [f'{x:,.0f}' for x in happiness_data_['freedom to make life choices']] + '<br>' +
                         '<b>Generosity</b>: ' + [f'{x:,.0f}' for x in happiness_data_['Generosity']] + '<br>' +
                         
                         
                         
                         '<b>Perceptions of corruption</b>: ' + [f'{x:,.0f}' for x in happiness_data_['Perceptions of corruption']] + '<br>'
                         
                        )],


        'layout': go.Layout(
             margin={"r": 0, "t": 0, "l": 0, "b": 0},
             # width=1820,
             # height=650,
             hovermode='closest',
             mapbox=dict(
                accesstoken='pk.eyJ1IjoicXM2MjcyNTI3IiwiYSI6ImNraGRuYTF1azAxZmIycWs0cDB1NmY1ZjYifQ.I1VJ3KjeM-S613FLv3mtkw',
                center=go.layout.mapbox.Center(lat=36, lon=-5.4),
                # style='open-street-map',
                style='dark',
                zoom=1.2
             ),
             autosize=True,

        )

    }

if __name__ == '__main__':
    app.run_server(debug=True)