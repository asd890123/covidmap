import math
import numpy as np
import pandas as pd

import plotly_express as px

import streamlit as st

#读取疫情经纬度数据，可以先用excel观察数据
df_area=pd.read_csv('疫情经纬度7area.csv')
df_point=pd.read_csv('疫情经纬度Point.csv')

#截取数据的一部分给df_map用于数据展示，也可以将全部数据给df_map
df_map=df_point[(df_point.date<='2022-04-26')
                   & (df_point.date>='2022-04-20')
                   #& (df_point.district=='宝山')
                   ]

df_map['lng']=df_map['lng']-0.0046
df_map['lat']=df_map['lat']+0.0018

df_map_area=df_area[(df_area.rolling_date<='2022-04-26')
                   & (df_area.rolling_date>='2022-03-21')
                   #& (df_area.district=='宝山')
                   ]

df_map_area['lng']=df_map_area['lng']-0.0046
df_map_area['lat']=df_map_area['lat']+0.0018

#调用地图显示地址的画图函数，lat指定纬度列，lon指定经度列
fig = px.scatter_mapbox(df_map, lat="lat", lon="lng",
                        color_discrete_sequence=px.colors.sequential.Plasma_r, 
                        #color_continuous_scale='turbid',
                          zoom=9, 
                        opacity=0.5,
                        color='date',
                        hover_data=['add','date'],
                        animation_frame = 'date',
                        height=700,
                       width=900
                       )

#地图显示风格相关，一般不需要动
fig.update_traces(marker={'size': 8,'symbol':'circle'})
fig.update_layout(
#     legend=dict(
#         yanchor="top",
#         y=0.87,
#         xanchor="left",
#         x=0.01
#     ),
    font=dict(
        family="Courier New, monospace",
        size=18,
        #color="RebeccaPurple"
    )
)

#"open-street-map", "carto-positron", "carto-darkmatter", "stamen-terrain", "stamen-toner" or "stamen-watercolor"
fig.update_layout(mapbox_style="carto-positron")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

#Streamlit展现交互图
st.plotly_chart(fig)

#附加题：把累计地址的数量，画出折线图，最好能叠加在地图上

fig_area = px.scatter_mapbox(df_map_area, lat="lat", lon="lng",
                        color_discrete_sequence=px.colors.qualitative.Dark2,    
                        #color_discrete_sequence=px.colors.sequential.Plasma_r, 
                        #color_continuous_scale='turbid',
                          zoom=9, 
                        opacity=1,
                        color='date',
                        hover_data=['add','date'],
                        animation_frame = 'rolling_date',
                        height=750,
                       width=900
                       )

#地图显示风格相关，一般不需要动
fig_area.update_traces(marker={'size': 10,'symbol':'circle'})
fig_area.update_layout(
#     legend=dict(
#         yanchor="top",
#         y=0.87,
#         xanchor="left",
#         x=0.01
#     ),
    font=dict(
        family="Courier New, monospace",
        size=18,
        #color="RebeccaPurple"
    )
)

#"open-street-map", "carto-positron", "carto-darkmatter", "stamen-terrain", "stamen-toner" or "stamen-watercolor"
fig_area.update_layout(mapbox_style="carto-positron")
fig_area.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

#Streamlit展现交互图
st.plotly_chart(fig_area)
