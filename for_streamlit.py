import streamlit as st
import base64

# Set page config first
st.set_page_config(layout="wide")

# Function to convert image to base64
def get_base64_image(image_path):
    with open(image_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# ✅ Your image path (raw string to avoid backslash issues)
image_path = r"C:\Users\user\Documents\guvi\guvi project 1\photo-1534996858221-380b92700493.avif"
encoded = get_base64_image(image_path)

# Inject CSS to add the background
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/webp;base64,{encoded}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-position: center;
    }}
    </style>
    """,
    unsafe_allow_html=True
)



st.markdown("""
    <h1 style="
        color: lightgreen;
        -webkit-text-stroke: 2px pink;
        font-weight: bold;
        text-align: center;
    ">🚀NASA NEO PROJECT🧑‍🚀</h1>

    <h3 style="
        color: white;
        -webkit-text-stroke: 1px blue;
        text-align: center;
        margin-top: -10px;
    ">^THIS IS MY FIRST PROJECT^</h3>
""", unsafe_allow_html=True)



option = st.selectbox("select an queries below", ["None selected","1. Count how many times each asteroid has approached Earth",
                                                  "2. Average velocity of each asteroid over multiple approaches",
                                                  "3. List top 10 fastest asteroids",
                                                  "4. Find potentially hazardous asteroids that have approached Earth more than 3 times",
                                                  "5. Find the month with the most asteroid approaches",
                                                  "6. Get the asteroid with the fastest ever approach speed",
                                                  "7. Sort asteroids by maximum estimated diameter (descending)",
                                                  "8. Asteroids whose closest approach is getting nearer over time(Hint: Use ORDER BY                                                                      close_approach_date and look at miss_distance)",
                                                  "9. Display the name of each asteroid along with the date and miss distance of its closest                                                                approach to Earth",
                                                  "10. List names of asteroids that approached Earth with velocity > 50,000 km/h",
                                                  "11. asteroid with the highest brightness (lowest magnitude value)",
                                                  "12. Get number of hazardous vs non-hazardous asteroids",
                                                  "13. Find asteroids that passed closer than the Moon (lesser than 1 LD), along with their close                                                            approach date and distance",
                                                  "14. Find asteroids that came within 0.05 AU(astronomical distance)",
                                                  "15. Average size of hazardous vs non-hazardous asteroids",
                                                  "16. Asteroids that approached more than once in the same year",
                                                  "17. Top 5 closest asteroid approaches of all time",
                                                  "18. Number of unique asteroids per year",
                                                  "19. Asteroids with both high speed (>50,000 km/h) and close approach (<0.05 AU)",
                                                  "20. Largest asteroid (by estimated diameter) that came within 1 LD",
                                                  "21. Fastest asteroid per year"])

import mysql.connector
import pandas as pd

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="thivagar",
        password="thiva12345",
        database="nasa_neo"
    )
    cursor = conn.cursor()

except mysql.connector.Error as err:
    st.error(f"Database connection failed: {err}")
    st.stop()  # Stops execution if connection fails)                                              
                                        
if option == "None selected":
    st.markdown(
        """
        <h2 style='color:blue;'> HELLO</h2>
        <h3 style='color:yellow;'> WELCOME TO MY PROJECT</h3>
        """, unsafe_allow_html=True
    )

    
# Execute based on selection
if option == "1. Count how many times each asteroid has approached Earth":
    st.subheader("🪐 Count of asteroid approaches")
    query = """
        SELECT name, COUNT(*) AS approach_count
        FROM asteroid_details
        GROUP BY name;
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    columns = cursor.column_names
    df = pd.DataFrame(rows, columns=columns)
    st.dataframe(df)

elif option == "2. Average velocity of each asteroid over multiple approaches":
    st.subheader("🚀 Average velocity of each asteroid")
    query = """
      SELECT neo_reference_id, AVG(relative_velocity_kmph) AS avg_velocity
      FROM close_approach_table
      GROUP BY neo_reference_id
      LIMIT 1000;
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    columns = cursor.column_names
    df = pd.DataFrame(rows, columns=columns)
    st.dataframe(df)

elif option == "3. List top 10 fastest asteroids":
    st.subheader("⚡ Top 10 Fastest Asteroids")
    query = """
      SELECT neo_reference_id, MAX(relative_velocity_kmph) AS max_velocity
      FROM close_approach_table
      GROUP BY neo_reference_id
      ORDER BY max_velocity DESC
      LIMIT 10;
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    columns = cursor.column_names
    df = pd.DataFrame(rows, columns=columns)
    st.dataframe(df)

elif option == "4. Find potentially hazardous asteroids that have approached Earth more than 3 times":
    st.subheader("⚠️ Potentially Hazardous Asteroids")
    query = """
              SELECT name, COUNT(*) AS approach_count
              FROM asteroid_details
              WHERE is_potentially_hazardous_asteroid = 1
              GROUP BY name
              HAVING COUNT(*) > 3;
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    columns = cursor.column_names
    df = pd.DataFrame(rows, columns=columns)
    st.dataframe(df)

elif option == "5. Find the month with the most asteroid approaches":
    st.subheader("📅 Month with the Most Asteroid Approaches")
    query = """
        SELECT DATE_FORMAT(close_approach_date, '%m') AS month, COUNT(*) AS approach_count
        FROM close_approach_table
        GROUP BY month
        ORDER BY approach_count DESC
        LIMIT 10;
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    columns = cursor.column_names
    df = pd.DataFrame(rows, columns=columns)
    st.dataframe(df)

elif option == "6. Get the asteroid with the fastest ever approach speed":
    st.subheader("🚀 Fastest Ever Asteroid Approach")
    query = """
        SELECT neo_reference_id, relative_velocity_kmph
        FROM close_approach_table
        ORDER BY relative_velocity_kmph DESC
        LIMIT 1;
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    columns = cursor.column_names
    df = pd.DataFrame(rows, columns=columns)
    st.dataframe(df)

elif option == "7. Sort asteroids by maximum estimated diameter (descending)":
    st.subheader("🔍 Asteroids by Maximum Diameter (Descending)")
    query = """
        SELECT name, MAX(est_diameter_max) AS max_diameter
        FROM asteroid_details
        GROUP BY name
        ORDER BY max_diameter DESC
        LIMIT 1000; 
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    columns = cursor.column_names
    df = pd.DataFrame(rows, columns=columns)
    st.dataframe(df)  
    
elif option == "8. Asteroids whose closest approach is getting nearer over time(Hint: Use ORDER BY                                                                      close_approach_date and look at miss_distance)":
    st.subheader("📉 Asteroids Approaching Closer Over Time")
    query = """
        SELECT neo_reference_id, close_approach_date, miss_distance_km
        FROM close_approach_table
        ORDER BY neo_reference_id, close_approach_date
        LIMIT 1000;
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    df = pd.DataFrame(rows, columns=columns)
    st.dataframe(df.head(50))

elif option == "9. Display the name of each asteroid along with the date and miss distance of its closest                                                                approach to Earth":
    st.subheader("🌍 Asteroid Approach Data")
    query = """
           SELECT a.neo_reference_id, a.close_approach_date, a.miss_distance_km
           FROM close_approach_table a
           JOIN (
           SELECT neo_reference_id, MIN(miss_distance_km) AS min_distance
           FROM close_approach_table
           GROUP BY neo_reference_id
           ) b ON a.neo_reference_id = b.neo_reference_id AND a.miss_distance_km = b.min_distance
           LIMIT 1000;
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    columns = cursor.column_names
    df = pd.DataFrame(rows, columns=columns)
    st.dataframe(df)


elif option == "10. List names of asteroids that approached Earth with velocity > 50,000 km/h":
    st.subheader("🚀 Asteroids with Velocity > 50,000 km/h")
    query = """
        SELECT DISTINCT neo_reference_id
        FROM close_approach_table
        WHERE relative_velocity_kmph > 50000
        LIMIT 1000;
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    df = pd.DataFrame(rows, columns=columns)
    st.dataframe(df)
elif option == "11. asteroid with the highest brightness (lowest magnitude value)":
    st.subheader("✨ Asteroid with the Highest Brightness")
    query = """
        SELECT name, MIN(absolute_magnitude_h) AS brightest_magnitude
FROM asteroid_details
GROUP BY name
LIMIT 1000;
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    columns = cursor.column_names
    df = pd.DataFrame(rows, columns=columns)
    st.dataframe(df)

elif option == "12. Get number of hazardous vs non-hazardous asteroids":
    st.subheader("🚀 Hazardous vs Non-Hazardous Asteroids")
    query = """
        SELECT is_potentially_hazardous_asteroid, COUNT(DISTINCT name) AS asteroid_count
        FROM asteroid_details
        GROUP BY is_potentially_hazardous_asteroid;
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    columns = cursor.column_names
    df = pd.DataFrame(rows, columns=columns)
    st.dataframe(df)
    
elif option == "13. Find asteroids that passed closer than the Moon (lesser than 1 LD), along with their close                                                            approach date and distance":
    st.subheader("🌕 Asteroids Passing Closer than the Moon")
    query = """
        SELECT ad.name, cat.close_approach_date, cat.lunar_distance
FROM close_approach_table cat
JOIN asteroid_details ad ON cat.neo_reference_id = ad.id
WHERE cat.lunar_distance < 1
LIMIT 1000;
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    columns = cursor.column_names
    df = pd.DataFrame(rows, columns=columns)
    st.dataframe(df)


elif option == "14. Find asteroids that came within 0.05 AU(astronomical distance)":
    st.subheader("🔭 Asteroids within 0.05 AU")
    query = """
        SELECT ad.name, cat.close_approach_date, cat.astronomical_unit
FROM close_approach_table cat
JOIN asteroid_details ad ON cat.neo_reference_id = ad.id
WHERE cat.astronomical_unit < 0.05
LIMIT 100
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    columns = cursor.column_names
    df = pd.DataFrame(rows, columns=columns)
    st.dataframe(df)

elif option == "15. Average size of hazardous vs non-hazardous asteroids":
    st.subheader("⚖️ Average Size of Hazardous vs Non-Hazardous Asteroids")
    query = """
        SELECT is_potentially_hazardous_asteroid, AVG(est_diameter_max) AS avg_size
FROM asteroid_details
GROUP BY is_potentially_hazardous_asteroid
LIMIT 0, 1000;ous
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    columns = cursor.column_names
    df = pd.DataFrame(rows, columns=columns)
    st.dataframe(df)

elif option == "15. Average size of hazardous vs non-hazardous asteroids":
    st.subheader("⚖️ Average Size of Hazardous vs Non-Hazardous Asteroids")
    query = """
        SELECT hazardous, AVG(diameter_km) AS avg_size
        FROM approaches
        GROUP BY hazardous
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    columns = cursor.column_names
    df = pd.DataFrame(rows, columns=columns)
    st.dataframe(df)

elif option == "16. Asteroids that approached more than once in the same year":
    st.subheader("📅 Asteroids that approached more than once in the same year")
    query = """
        SELECT ad.name, YEAR(cat.close_approach_date) AS year, COUNT(*) AS yearly_approaches
FROM close_approach_table cat
JOIN asteroid_details ad ON cat.neo_reference_id = ad.id
GROUP BY ad.name, year
HAVING COUNT(*) > 1
LIMIT 0, 1000;
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    columns = cursor.column_names
    df = pd.DataFrame(rows, columns=columns)
    st.dataframe(df)

elif option == "17. Top 5 closest asteroid approaches of all time":
    st.subheader("📏 Top 5 Closest Asteroid Approaches")
    query = """
        SELECT ad.name, cat.close_approach_date, cat.miss_distance_km
FROM close_approach_table cat
JOIN asteroid_details ad ON cat.neo_reference_id = ad.id
ORDER BY cat.miss_distance_km ASC
LIMIT 5;
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    columns = cursor.column_names
    df = pd.DataFrame(rows, columns=columns)
    st.dataframe(df)



elif option == "18. Number of unique asteroids per year":
    st.subheader("📆 Number of Unique Asteroids per Year")
    query = """
        SELECT YEAR(close_approach_date) AS year, COUNT(DISTINCT ad.name) AS unique_asteroids
FROM close_approach_table cat
JOIN asteroid_details ad ON cat.neo_reference_id = ad.id
GROUP BY year
LIMIT 0, 1000;
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    columns = cursor.column_names
    df = pd.DataFrame(rows, columns=columns)
    st.dataframe(df)

elif option == "19. Asteroids with both high speed (>50,000 km/h) and close approach (<0.05 AU)":
    st.subheader("🚀 High Speed & Close Approach Asteroids")
    query = """
        SELECT ad.name, cat.close_approach_date, cat.relative_velocity_kmph, cat.astronomical_unit
FROM close_approach_table cat
JOIN asteroid_details ad ON cat.neo_reference_id = ad.id
WHERE cat.relative_velocity_kmph > 50000 AND cat.astronomical_unit < 0.05
LIMIT 1000;
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    columns = cursor.column_names
    df = pd.DataFrame(rows, columns=columns)
    st.dataframe(df)

    
elif option == "20. Largest asteroid (by estimated diameter) that came within 1 LD":
    st.subheader("🌍 Largest Asteroid that Came Within 1 LD")
    query = """
        SELECT ad.name, MAX(ad.est_diameter_max) AS max_diameter
FROM close_approach_table cat
JOIN asteroid_details ad ON cat.neo_reference_id = ad.id
WHERE cat.lunar_distance < 1
GROUP BY ad.name
ORDER BY max_diameter DESC
LIMIT 1;
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    columns = cursor.column_names
    df = pd.DataFrame(rows, columns=columns)
    st.dataframe(df)

elif option == "21. Fastest asteroid per year":
    st.subheader("🚀 Fastest Asteroid Per Year")
    query = """
       SELECT ad.name, YEAR(cat.close_approach_date) AS year, cat.relative_velocity_kmph AS max_velocity
FROM close_approach_table cat
JOIN asteroid_details ad ON cat.neo_reference_id = ad.id
JOIN (
    SELECT YEAR(close_approach_date) AS year, MAX(relative_velocity_kmph) AS max_velocity
    FROM close_approach_table
    GROUP BY YEAR(close_approach_date)
) AS max_by_year
ON YEAR(cat.close_approach_date) = max_by_year.year
AND cat.relative_velocity_kmph = max_by_year.max_velocity
ORDER BY year
LIMIT 1000;
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    columns = cursor.column_names
    df = pd.DataFrame(rows, columns=columns)
    st.dataframe(df)

import streamlit as st
import pandas as pd

# Asteroid core data
asteroid_data = {
    'id': [
        2415949, 3160747, 3309828, 3457842, 3553062, 3591616, 3608936, 3795154, 3842680, 2613286,
        54338714, 54415081, 54417653, 54418497, 54418796, 54419485, 54419601, 54420153, 54421393,
        2669051, 54444997, 54445206, 3724393, 3797695, 3986699, 54200446, 54235663, 54418438,
        54418650, 54419698, 54421384, 54513047, 2450293
    ],
    'name': [
        '415949 (2001 XY10)', '(2003 SR84)', '(2005 YQ96)', '(2009 HC21)', '(2010 XA11)', '(2011 YP10)',
        '(2012 SD22)', '(2017 YD8)', '(2019 KK5)', '613286 (2005 YQ96)', '(2023 AW)', '(2023 XZ4)',
        '(2023 YR)', '(2024 AA)', '(2022 OY78)', '(2024 AQ1)', '(2024 AA2)', '(2024 AR3)',
        '(2024 BK1)', '669051 (2012 SD22)', '(2024 KY)', '(2024 KJ1)', '(2015 OD22)', '(2018 BA)',
        '(2020 BC)', '(2021 SG2)', '(2022 AO2)', '(2023 YR1)', '(2023 YY1)', '(2024 AV2)',
        '(2024 AA6)', '(2025 AB)', '450293 (2004 LV3)'
    ],
    'absolute_magnitude_h': [
        19.37, 26, 20.62, 22.1, 26.1, 23.94, 20.05, 21.87, 22.79, 20.63,
        25.68, 24.05, 24.9, 27.41, 26.38, 23.72, 20.54, 23.6, 24.49, 20.08,
        26.5, 26.21, 21.21, 25, 26.2, 25.54, 24.19, 25.68, 25.77, 26.64,
        25.12, 27.13, 18.83
    ],
    'estimated_diameter_min_km': [
        0.355267, 0.0167708, 0.199781, 0.101054, 0.016016, 0.0433067, 0.25975, 0.112345, 0.0735453,
        0.198863, 0.0194337, 0.0411675, 0.0278327, 0.00876103, 0.0140785, 0.0479242, 0.207279,
        0.0506471, 0.0336167, 0.256186, 0.0133216, 0.0152249, 0.152249, 0.02658, 0.0152952,
        0.0207279, 0.0385971, 0.0194337, 0.0186447, 0.0124898, 0.025151, 0.00996678, 0.45557
    ],
    'estimated_diameter_max_km': [
        0.794401, 0.0375008, 0.446725, 0.225964, 0.0358129, 0.0968367, 0.580818, 0.251212,
        0.164452, 0.444672, 0.043455, 0.0920534, 0.0622358, 0.0195902, 0.0314804, 0.107162,
        0.46349, 0.11325, 0.0751692, 0.572849, 0.0297879, 0.034044, 0.34044, 0.0594347,
        0.0342011, 0.046349, 0.0863058, 0.043455, 0.0416908, 0.027928, 0.0562393, 0.0222864, 1.01869
    ],
    'is_potentially_hazardous_asteroid': [
        0, 0, 1, 0, 0, 0, 1, 0, 0, 1,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 1
    ]
}

# Velocity and distance data
extra_data = {
    'id': [
        2168318, 2168318, 2168318, 2168318, 2168318, 2168318, 2168318,
        2199003, 2199003, 2199003, 2199003, 2199003, 2199003, 2199003,
        2304640, 2304640, 2304640, 2304640, 2304640, 2304640, 2304640, 2304640,
        2415949, 2415949, 2415949, 2415949
    ],
    'date': [
        '2024-01-08', '2024-01-08', '2024-01-08', '2024-01-08', '2024-01-08', '2024-01-08', '2024-01-08',
        '2024-01-07', '2024-01-07', '2024-01-07', '2024-01-07', '2024-01-07', '2024-01-07', '2024-01-07',
        '2024-01-06', '2024-01-06', '2024-01-06', '2024-01-06', '2024-01-06', '2024-01-06', '2024-01-06', '2024-01-06',
        '2024-01-02', '2024-01-02', '2024-01-02', '2024-01-02'
    ],
    'relative_velocity_kmph': [
        31986.5, 31986.5, 31986.5, 31986.5, 31986.5, 31986.5, 31986.5,
        55047, 55047, 55047, 55047, 55047, 55047, 55047,
        82917.4, 82917.4, 82917.4, 82917.4, 82917.4, 82917.4, 82917.4, 82917.4,
        57205.9, 57205.9, 57205.9, 57205.9
    ],
    'astronomical_unit': [
        0.117698, 0.117698, 0.117698, 0.117698, 0.117698, 0.117698, 0.117698,
        0.199535, 0.199535, 0.199535, 0.199535, 0.199535, 0.199535, 0.199535,
        0.304225, 0.304225, 0.304225, 0.304225, 0.304225, 0.304225, 0.304225, 0.304225,
        0.337254, 0.337254, 0.337254, 0.337254
    ]
}

# Create DataFrames
asteroid_df = pd.DataFrame(asteroid_data)
extra_df = pd.DataFrame(extra_data)
extra_df['date'] = pd.to_datetime(extra_df['date'])

# Merge
merged_df = pd.merge(extra_df, asteroid_df, on='id', how='left')

# Streamlit ap
st.markdown("""
    <h4 style="
        color: red;
        -webkit-text-stroke: 1px blue;
        text-align: center;
        margin-top: -10px;
    ">🚀NASA  ASTEROID🪐</h4>
""", unsafe_allow_html=True)


# Sidebar Filters
st.sidebar.header("Filters")

min_magnitude, max_magnitude = st.sidebar.slider(
    "Absolute Magnitude (H)", 13.8, 32.61, (13.8, 32.61)
)

velocity_min, velocity_max = st.sidebar.slider(
    "Relative Velocity (km/h)", 1418.21, 173071.83, (1418.21, 173071.83)
)

min_diameter, max_diameter = st.sidebar.slider(
    "Estimated Diameter (km)", 0.00, 1.1, (0.00, 1.1)
)

astronomical_min, astronomical_max = st.sidebar.slider(
    "Astronomical Unit", 0.00, 0.50, (0.00, 0.50)
)

only_hazardous = st.sidebar.selectbox(
    "Only Show Potentially Hazardous?", (0, 1)
)

start_date = st.sidebar.date_input("Start Date", pd.to_datetime('2024-01-01'))
end_date = st.sidebar.date_input("End Date", pd.to_datetime('2025-04-13'))

# Filter Button
if st.sidebar.button("Apply Filters"):
    filtered = merged_df[
        (merged_df['absolute_magnitude_h'] >= min_magnitude) &
        (merged_df['absolute_magnitude_h'] <= max_magnitude) &
        (merged_df['relative_velocity_kmph'] >= velocity_min) &
        (merged_df['relative_velocity_kmph'] <= velocity_max) &
        (merged_df['estimated_diameter_min_km'] >= min_diameter) &
        (merged_df['estimated_diameter_max_km'] <= max_diameter) &
        (merged_df['astronomical_unit'] >= astronomical_min) &
        (merged_df['astronomical_unit'] <= astronomical_max) &
        (merged_df['is_potentially_hazardous_asteroid'] == only_hazardous) &
        (merged_df['date'] >= pd.to_datetime(start_date)) &
        (merged_df['date'] <= pd.to_datetime(end_date))
    ]
    st.success(f"Showing {len(filtered)} asteroids matching the filters.")
else:
    filtered = merged_df

# Show data
st.subheader("Filtered Asteroids")
st.dataframe(filtered)



                             



