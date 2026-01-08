    # Sri Lanka Flood Disaster Management Dashboard

    ## Fully Funcational Disaster Location & Incident Tracking Dashboard

    #### Video Demo:  <https://youtu.be/Aru8Delp5mk>

    #### Description:
     The **Sri Lanka Flood Disaster Management Dashboard** is a wed based emergency situation response system built using **Streamlit and python**. It's main purpose is to assit authorities during a disaster by providing location assistion dash board in real time. The dashboard provides a centerlize , real time updates of locations. The information provided will mitigate a large time spent on anlyzing situations. The main purpose is when disaster happen through out country, affected people can send there location and information to a centerlized data collection center simple via a text message. People just has to send there location just using google maps. Then after verfying information authorities can update map using the data they get. The system will paint a whole picture of the situation. Then rescue teams can be assigned according to the requriment. No loaction will be missed because the system will indicate the team assigned to location.
        - Shows Sri Lankan Map with updated locations
        - Input - google map shared location and details of incident
        - Input will pop-up in Sri lankan map in red, yellow, green indicating locations with details
        - Total count of locations , people affected data will be summerised for ease of work
        - As per the data every authourities can see whats happening and what needs to be addred

    ## Problem statement
        During a sudden disaster,
        - Information is fragmented
        - Location visualization is difficult
        - Low respose coordination
        - Gathering location information difficult

    ## Features provided
        - Interactive ** Sri Lankan map ** with displaying disaster locations using **PyDeck**.
        - Accept ** Google map shared locations ** and extracts longitude and latitude and plot location in the map.
        - Color status for as per the gravity:
            - Red - High disaster location / Emergency / High priority
            - Yellow - Mediume disaster location / Situation under control
            - Green - Addressed or not a priority
        - Provided summery of:
            - Total number of disaster locations
            - Total number of affected people
            - Incident status data shows in red, yellow, green
        - Data saved to a csv to be used by any other process
        - Duplicate locatation prevention
        - Ability to delete locations per the updates

    ## Used Technologies
        - Python
        - Streamlit
        - Panadas
        - PyDeck
        - Requests
        - Regular Expressions
        - Csv

    ## locations.csv
        This file is used as the project data stored file. When starting the programe it will automatically generate a emty fill and will contain the data saved as,
        - location
        - lat
        - lon
        - people_affected
        - team_assigned
        - status

    ## requirement.txt
        Will contain list of libraries required,
        - streamlit
        - pandas
        - pydeck
        - requests

    ## How to use
    ### Installations
        - pip install streamlit pandas pydeck requests

    ## How to run
        - streamlit run project.py
