# Extracting Spatio-temporal Pixel Level Dataset

## Step 1: Load and Filter Feature Collection
- Load your Area of Study (AOS) FeatureCollection.
- Check the size of the FeatureCollection.
- Get a list of all values in the County property and print unique counties.
- Specify and filter features by a specific county name.

## Step 2: Load and Process Satellite Image Collection
- Import the satellite image collection suitable for your study area and timeframe.
- Apply scaling factors to the images if necessary for consistent analysis.

## Step 3: Add Vegetation Indices
- Define functions to compute various vegetation indices like NDVI, EVI, NDWI, etc.
- Map over the image collection and apply these functions to derive indices for each image.

## Step 4: Select Image for Display
- Choose an image from the processed collection for visualization based on criteria like cloud cover.

## Step 5: Visualization and Analysis
- Visualize selected images and indices on a map.
- Optionally, style features (points or polygons) on the map for better visualization.

## Step 6: Generate and Display Time Series Chart
- Select a representative feature (point or polygon) from your filtered FeatureCollection.
- Create a time series chart showing changes in vegetation indices over time at this specific location.

## Step 7: Statistical Analysis and Export
- Perform statistical analysis by aggregating pixel-level data within each feature (point or polygon).
- Export aggregated statistics (e.g., mean NDVI values) to a file format suitable for further analysis or reporting.
