"""
 Sri Lanka Flood Disaster Management Dashboard
1. Shows Sri Lankan Map
2. Input - google map shared location
3. when input it will pop-up in Sri lankan map in red, yellow, green indicating location
4. Total count of locations , people affected data will be summerised for ease of work
5. As per the data every authourities

 """

import csv
import streamlit as st
import pydeck as pdk
import pandas as pd
import requests
import re
import os

CSV_FILE = "locations.csv"

#-----------------Creatinig a csv file-------------------------------------------------------
def create_csv():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, "w", newline ="") as file:
            writer = csv.writer(file)
            writer.writerow(["location", "lat", "lon", "people_affected", "team_assigned", "status"])
#-----------------Save data to csv-----------------------------------------------------------
def save_to_csv(location, lat, lon, people_affected, team_assigned, status):
    with open(CSV_FILE, "a", newline = "") as file:
        writer = csv.writer(file)
        writer.writerow([location, lat, lon, people_affected, team_assigned, status ])


#----------------Google url to lt and lon-----------------------------------------------------
def get_google_url_location(google_url):
    if not google_url:
        return None

    try:
        response = requests.get(google_url, allow_redirects = True)
        url = response.url

    except requests.RequestException:
        return None
    #----------------Finding lat and lon----------------------------------------------------------
    #----------------Format 1---------------------------------------------------------------------
    matches = re.search(r"@(-?\d+\.\d+),(-?\d+\.\d+)", url)
    if matches:
        lat = float(matches.group(1))
        lon = float(matches.group(2))
        return lat, lon

    #---------------Format 2----------------------------------------------------------------------
    matches = re.search(r"(-?\d+\.\d+),%2B(-?\d+\.\d+)",url)
    if matches:
        lat = float(matches.group(1))
        lon = float(matches.group(2))
        return lat, lon

#----------------Defining status color------------------------------------------------------------
def status_color(status):
    if status == "Red":
        return [255, 0, 0]
    if status == "Yellow":
        return [255, 200, 0]
    if status == "Green":
        return [0, 180, 0]
    return [0, 0, 0]

#---------------to load and plot locations from csv--------------------------------------------
def plot_location():
    if not os.path.exists(CSV_FILE):
        return pd.DataFrame(columns=["location", "lat", "lon", "people_affected", "team_assigned", "status"])
    return pd.read_csv(CSV_FILE)

#---------------The main function--------------------------------------------------------------
def main():

# --------------Dashboard configurations-------------------------------------------------------
    st.set_page_config(layout="wide")
    st.title("Sri Lanka Flood Disaster Management Dashboard")
    st.subheader("Map")

    create_csv()
#---------------getting data from csv-----------------------------------------------------------
    df = plot_location()

#---------------Sum of details------------------------------------------------------------------
    c1,c2,c3,c4,c5 = st.columns(5)
    c1.metric("Total locations", len(df))
    c2.metric("Totlal number of people", int(df["people_affected"].sum()) if not df.empty else 0)
    c3.metric("Red", len(df[df["status"] == "Red"]))
    c4.metric("Yellow", len(df[df["status"] == "Yellow"]))
    c5.metric("Green", len(df[df["status"]== "Green"]))

#---------------Mapping-------------------------------------------------------------------------
    if df.empty :
        map_df = pd.DataFrame([{"lat" : 7.8731, "lon": 80.7718 }]) #centre of sri lanka
    else:
        df["color"] = df["status"].apply(status_color)
        map_df = df

#---------------plot in map on streamlit--------------------------------------------------------
    layer = pdk.Layer("ScatterplotLayer", data = map_df, get_position = ["lon", "lat"], get_fill_color = "color", get_radius = 10, radius_units = "pixels",stroked = False ,pickable =True)
    view_state = pdk.ViewState(latitude = 7.8731, longitude = 80.7718 ,zoom = 6.4)
#---------------showing extra details-----------------------------------------------------------
    st.pydeck_chart(pdk.Deck(layers = [layer], initial_view_state = view_state, tooltip = {"text":"location /{location}\nPeople Affected : {people_affected}\nTeam : {team_assigned}"}))

#---------------Input data----------------------------------------------------------------------
    st.subheader("Add new location")

    with st.form("save_form", clear_on_submit = True):
        google_url = st.text_input("Google Map shared url", key ="google_url")
        location = st.text_input("Location Name/No", key = "location")
        people_affected = st.number_input("Number of people affected", min_value = 0, step = 1, key ="people_affected")
        team_assigned = st.text_input("Team assigned", key = "team_assigned")
        status = st.radio("status", ["Red", "Yellow", "Green"], horizontal = True, key = "status")
        submit = st.form_submit_button("Save")

#---------------Save Data-----------------------------------------------------------------------
    if submit:
        coords = get_google_url_location(google_url)
        if not coords:
            st.error("Invalid Details")
        else:
            lat, lon = coords
#---------------Prevent from duplication--------------------------------------------------------
            if not df.empty and ((df["lat"] == lat) & (df["lon"] == lon)).any():
                st.error("Location already exit")
            else:
                save_to_csv(st.session_state["location"], lat, lon, st.session_state["people_affected"], st.session_state["team_assigned"], st.session_state["status"])

                st.success("Location uploaded successfully!")
                st.rerun()

#---------------Show saved data as a table-------------------------------------------------------
    st.subheader("Location details available")
    st.dataframe(df, width = "stretch")
#---------------Detele Button--------------------------------------------------------------------
    if not df.empty:
        delete_loc = st.selectbox("Delete", df["location"])
        if st.button("Delete"):
            df = df[df["location"] != delete_loc]
            df.to_csv(CSV_FILE, index = False)
            st.rerun()



if __name__ == "__main__":
    main()
