# NASA-NEO-project
This is my first project.
I am getting DATA from NASA.
This project focuses on filtering and analyzing near-Earth asteroid (NEA) data by querying and processing information from the NASA Near Earth Object Web Service (NeoWs) API.
Using an API key provided by NASA, we fetch real-time and historical asteroid data and apply a series of custom Python queries and filters to structure and visualize this information.
And I get data to create and insert that DATA in MYSQL for dataframe.
Queries and Filters
The project performs the following queries:

Retrieve asteroid details (name, magnitude, estimated diameter, hazard status) 

Fetch close approach data (date, relative velocity, and miss distance) 

Apply custom filters to:

Select asteroids based on size (diameter range)

Select asteroids based on brightness (absolute magnitude)

Highlight potentially hazardous asteroids 

Analyze asteroids approaching Earth within specific distance/velocity thresholds

Using the NASA API Key
Access to NASA’s NeoWs API is authenticated via a personal API key.

API queries are sent via HTTP GET requests using Python libraries like requests.

Data is retrieved in JSON format and parsed into pandas DataFrames for easier manipulation and visualization.


Filter criteria
Asteroid Filter and Visualizer is a Streamlit web application designed to help users explore and analyze near-Earth asteroids (NEAs) based on their physical properties and orbital data.

The app provides easy-to-use filters that allow users to sort asteroids by:

Size (diameter in kilometers) 

Brightness (absolute magnitude) 

Hazard potential (whether they are classified as potentially hazardous) 

Close approach data (velocity and distance from Earth) 

This project combines multiple datasets of asteroid information and upcoming close approaches, enabling users to visually interact with space objects that may pose a risk or simply interest astronomers and space enthusiasts.

The goal is to make asteroid data more accessible, interactive, and understandable for researchers, educators, and curious explorers alike. 
