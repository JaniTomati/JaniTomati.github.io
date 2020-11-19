#!/usr/bin/python3
# -*- coding: utf-8 -*-

import datetime as dt
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def load_data(file_path):
    """ Load data in csv format in data frames """
    return pd.read_csv(file_path, delimiter=';', decimal=',')


def update_day():
    """ Update the day according to the drop down selection """
    pass


def main():
    folder = "../FlowDOS Q1-Q2 2020/"
    files = ["Flows_Z80Syd_2020Q1.csv"]

    df_q1_z80 = load_data(folder + files[0])
    df_q1_z80['date'] = [dt.datetime.strptime(d, "%Y-%m-%d %H:%M:%S").date() for d in df_q1_z80['DATETIME']]
    df_q1_z80['time'] = [dt.datetime.strptime(d, "%Y-%m-%d %H:%M:%S").time() for d in df_q1_z80['DATETIME']]
    df_q1_z80['week_number'] = [dt.datetime.strptime(d, "%Y-%m-%d %H:%M:%S").strftime("%V") for d in df_q1_z80['DATETIME']]

    df_week = df_q1_z80[(df_q1_z80['week_number'] == "01")]

    df_day = df_q1_z80[(df_q1_z80['DATETIME'] > "2020-01-01") & (df_q1_z80['DATETIME'] <= "2020-01-02")]
    df_day_2 = df_q1_z80[(df_q1_z80['DATETIME'] > "2020-01-02") & (df_q1_z80['DATETIME'] <= "2020-01-03")]
    df_day_3 = df_q1_z80[(df_q1_z80['DATETIME'] > "2020-01-03") & (df_q1_z80['DATETIME'] <= "2020-01-04")]
    df_day_4 = df_q1_z80[(df_q1_z80['DATETIME'] > "2020-01-04") & (df_q1_z80['DATETIME'] <= "2020-01-05")]
    df_day_5 = df_q1_z80[(df_q1_z80['DATETIME'] > "2020-01-05") & (df_q1_z80['DATETIME'] <= "2020-01-06")]
    df_day_6 = df_q1_z80[(df_q1_z80['DATETIME'] > "2020-01-06") & (df_q1_z80['DATETIME'] <= "2020-01-07")]
    df_day_7 = df_q1_z80[(df_q1_z80['DATETIME'] > "2020-01-07") & (df_q1_z80['DATETIME'] <= "2020-01-08")]

    # create figure
    fig = go.Figure()
    fig = make_subplots(rows=2, cols=1)

    # for column in df_day.columns.to_list():
    #     if column not in ["DATETIME", "date", "time", "week_number"]:
    #         fig.add_trace(
    #             go.Scatter(
    #                 x = df_day["time"],
    #                 y = df_day[column],
    #                 name = column
    #             ), row= 1, col=1
    #         )
    #
    # for column in df_day.columns.to_list():
    #     if column not in ["DATETIME", "date", "time", "week_number"]:
    #         fig.add_trace(
    #             go.Scatter(
    #                 x = df_day["DATETIME"],
    #                 y = df_day[column],
    #                 name = column
    #             ), row= 2, col=1
    #         )


    # add scatter traces for first line plot
    fig.add_trace(go.Scatter(x=df_day["time"], y=df_day["OST.B09_E_G1_BF1-M_FLOW"], name="2020-01-01",line=dict(color="yellow")), row=1, col=1)
    fig.add_trace(go.Scatter(x=df_day_2["time"], y=df_day_2["OST.B09_E_G1_BF1-M_FLOW"], name="2020-01-02", line=dict(color="green")), row=1, col=1)
    fig.add_trace(go.Scatter(x=df_day_3["time"], y=df_day_3["OST.B09_E_G1_BF1-M_FLOW"], name="2020-01-03", line=dict(color="pink")), row=1, col=1)
    fig.add_trace(go.Scatter(x=df_day_4["time"], y=df_day_4["OST.B09_E_G1_BF1-M_FLOW"], name="2020-01-04", line=dict(color="orange")), row=1, col=1)
    fig.add_trace(go.Scatter(x=df_day_5["time"], y=df_day_5["OST.B09_E_G1_BF1-M_FLOW"], name="2020-01-05", line=dict(color="blue")), row=1, col=1)
    fig.add_trace(go.Scatter(x=df_day_6["time"], y=df_day_6["OST.B09_E_G1_BF1-M_FLOW"], name="2020-01-06", line=dict(color="#9467BD")), row=1, col=1)
    fig.add_trace(go.Scatter(x=df_day_7["time"], y=df_day_7["OST.B09_E_G1_BF1-M_FLOW"], name="2020-01-07", line=dict(color="#D62728")), row=1, col=1)

    # add scatter traces for first second plot
    fig.add_trace(go.Scatter(x=df_day["DATETIME"], y=df_day["OST.B09_E_G1_BF1-M_FLOW"], name="2020-01-01",line=dict(color="yellow")), row=2, col=1)
    fig.add_trace(go.Scatter(x=df_day_2["DATETIME"], y=df_day_2["OST.B09_E_G1_BF1-M_FLOW"], name="2020-01-02", line=dict(color="green")), row=2, col=1)
    fig.add_trace(go.Scatter(x=df_day_3["DATETIME"], y=df_day_3["OST.B09_E_G1_BF1-M_FLOW"], name="2020-01-03", line=dict(color="pink")), row=2, col=1)
    fig.add_trace(go.Scatter(x=df_day_4["DATETIME"], y=df_day_4["OST.B09_E_G1_BF1-M_FLOW"], name="2020-01-04", line=dict(color="orange")), row=2, col=1)
    fig.add_trace(go.Scatter(x=df_day_5["DATETIME"], y=df_day_5["OST.B09_E_G1_BF1-M_FLOW"], name="2020-01-05", line=dict(color="blue")), row=2, col=1)
    fig.add_trace(go.Scatter(x=df_day_6["DATETIME"], y=df_day_6["OST.B09_E_G1_BF1-M_FLOW"], name="2020-01-06", line=dict(color="#9467BD")), row=2, col=1)
    fig.add_trace(go.Scatter(x=df_day_7["DATETIME"], y=df_day_7["OST.B09_E_G1_BF1-M_FLOW"], name="2020-01-07", line=dict(color="#D62728")), row=2, col=1)

    # list all locations in a dropdown menu
    i = 0
    location_buttons = []
    for column in df_day.columns.to_list():
        if column not in ["DATETIME", "date", "time", "week_number"]: # ignore columns that are not locations
            visibility = [i==j for j in range(len(df_day.columns.to_list()))]
            button = dict(
                     label = column,
                     method = 'update',
                     args = [{'visible': visibility},
                         {'title': column}])
            location_buttons.append(button)

    fig.update_layout(
        updatemenus=[
            dict(
                buttons=location_buttons,
                direction="down",
                pad={"r": 10, "t": 0, "b" : 0},
                showactive=True,
                x=0.0,
                xanchor="left",
                y=1.1,
                yanchor="top"
            )
        ])

    # change x-axis ticks
    fig.update_layout(
    xaxis = dict(
        tickmode = 'linear',
        tick0 = 0,
        dtick = 60
        )
    )

    # show figure
    fig.show()



if __name__ == "__main__":
    main()
