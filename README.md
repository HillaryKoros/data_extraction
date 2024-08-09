
# Spatial Data Extraction Projects

🍃 Hello! Welcome to this data extraction repository, where we leverage programming and automation tools 🛠️🤖. This project focuses on using (geo)python libraries 🌎🗺️ to extract and visualize spatial data 🛰️📊📈. Our goal is to support decision-makers, humanitarian organizations, and emergency response efforts 💻🌟, among other global challenges.


---

### Projects

- **Extracting Data from the Master Health Facility Registry (KMHFR)** In this exercise, we will use the following Python libraries:

- **Beautiful Soup**: For parsing HTML and XML documents.
- **Requests**: For making HTTP requests to retrieve data from the web.
- **JSON**: For handling JSON data structures.
- **Pandas**: For data manipulation and analysis.

- ### About the Master Health Facility Registry (KMHFR)

The **Master Health Facility Registry (KMHFR)** is an application that contains information on all health facilities and community units in Kenya. Each health facility and community unit is identified with a unique code, along with details describing its geographical location, administrative location, ownership, type, and the services offered.

- ### Accessing the Data

The data from KMHFR can be accessed through an API, with documentation available [here](https://mfl-api-docs.readthedocs.io/en/latest/).

However, in this exercise, we will use **Beautiful Soup** to scrape the data from the KMHFR website.

We'll be working with the following base URL:
python
base_url = [here](https://kmhfr.health.go.ke/public/facilities?page={}).


- **Retrieving data from OpenStreetMap:** 

 OpenStreetMap (OSM) is probably the most well known and widely used spatial dataset/database in the world. Let's see how we can retrieve data from OSM using a library called [omsnx](https://osmnx.readthedocs.io/). With `osmnx` you can easily download and extract data from anywhere in the world based on the [Overpass API](https://dev.overpass-api.de/overpass-doc/en/preface/preface.html). You can use `osmnx` e.g. to retrieve OSM data around a given address and applying a  2 km buffer around this location. Hence, `osmnx` is a very flexible library in terms of specifying the area of interest. 

OSM is a "database of the world", hence it contains **a lot** of information about different things. With `osmnx` you can easily extract information about:

- street networks --> `ox.graph_from_place(query)` | `ox.graph_from_polygon(polygon)`
- buildings --> `ox.features_from_place(query, tags={"buildings": True})` | `ox.features_from_polygon(polygon, tags={"buildings": True})`
- Amenities --> `ox.features_from_place(query, tags={"amenity": True})` | `ox.features_from_polygon(polygon, tags={"amenity": True})`
- landuse --> `ox.features_from_place(query, tags={"landuse": True})` | `ox.features_from_polygon(polygon, tags={"landuse": True})`
- natural elements --> `ox.features_from_place(query, tags={"natural": True})` | `ox.features_from_polygon(polygon, tags={"natural": True})`
- boundaries --> `ox.features_from_place(query, tags={"boundary": True})` | `ox.features_from_polygon(polygon, tags={"boundary": True})`