import arcpy 


my_source = r"C:\\GEOG392_Labs\\GISProgramming\\Lab07\\Lab07_Data\\"
my_result = r"C:\\GEOG392_Labs\\GISProgramming\\Lab07\\Lab07_Result\\"
band1 = arcpy.sa.Raster(my_source + "LT05_L2SP_026039_20110803_20200820_02_T1_SR_B1.TIF") #Blue Band
band2 = arcpy.sa.Raster(my_source + "LT05_L2SP_026039_20110803_20200820_02_T1_SR_B2.TIF") #Green Band
band3 = arcpy.sa.Raster(my_source + "LT05_L2SP_026039_20110803_20200820_02_T1_SR_B3.TIF") #Red Band
band4 = arcpy.sa.Raster(my_source + "LT05_L2SP_026039_20110803_20200820_02_T1_SR_B4.TIF") #NIR Band
'''
#Composite All of the Bands
composite = arcpy.CompositeBands_management([band1, band2, band3, band4], my_result + "combined.tif")

'''

#Using DEM to Create the Hillshade
azimuth = 315
altitude = 45
shadows = "NO_SHADOWS"
z_factor = 1
arcpy.ddd.HillShade(my_source + r"\\n30_w097_1arc_v3.tif", my_result + r"\\hillshade.tif", azimuth, altitude, shadows, z_factor)

#Using DEM to Create a Slope Image
output_measurement = "DEGREE"
z_factor = 1
arcpy.ddd.Slope(my_source + r"\\n30_w097_1arc_v3.tif", my_result + r"\\slopes.tif", output_measurement, z_factor)