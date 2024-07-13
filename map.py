import folium

# Sample data of restaurants and bars in North Goa
locations = [
    {"name": "Restaurant A", "latitude": 15.4989, "longitude": 73.8278},
    {"name": "Restaurant B", "latitude": 15.4999, "longitude": 73.8279},
    {"name": "Bar A", "latitude": 15.5030, "longitude": 73.8300},
    {"name": "Bar B", "latitude": 15.5010, "longitude": 73.8310},
    # Add more locations as needed
]

# Create a map centered around North Goa
m = folium.Map(location=[15.4989, 73.8278], zoom_start=12)

# Add markers to the map
for location in locations:
    folium.Marker(
        location=[location["latitude"], location["longitude"]],
        popup=location["name"],
        icon=folium.Icon(icon="cutlery" if "Restaurant" in location["name"] else "glass"),
    ).add_to(m)

# Save the map to an HTML file
m.save("landing page.html")

# Display the map (this will work in Jupyter Notebooks)
m
