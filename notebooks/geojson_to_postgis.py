
# from geojson import loads


# Replace these variables with your database connection details

# Replace this variable with your PostGIS table name
table_name = 'your_postgis_tab'

# GeoJSON data
geojson_data = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "geometry": {
                "type": "LineString",
                "coordinates": [[10.2, 1.0], [10.3, 2.0], [10.4, 2.5]]
            },
            "properties": {"route": "341A7", "class": "local"}
        },
        {
            "type": "Feature",
            "geometry": {
                "type": "LineString",
                "coordinates": [[10.7, 1.6], [10.8, 2.8], [10.3, 2.8]]
            },
            "properties": {"route": "654D7", "class": "holdem"}
        }
    ]
}
# Connect to the PostgreSQL database
with psycopg.connect(con_string) as conn:
    with conn.cursor() as cur:
        # Create the PostGIS table if it doesn't exist
        cur.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (id serial PRIMARY KEY, geom geometry, route varchar, class varchar);")
        # Insert GeoJSON features into the PostGIS table
        for feature in geojson_data['features']:
            geometry = str(feature['geometry'])
            route = feature['properties']['route']
            class_type = feature['properties']['class']
            cur.execute(f"INSERT INTO {table_name} (geom, route, class) VALUES (ST_GeomFromGeoJSON(%s), %s, %s);", (geometry, route, class_type))
    conn.commit()

# Print a message indicating success
print(f"GeoJSON data successfully inserted into {table_name} table.")