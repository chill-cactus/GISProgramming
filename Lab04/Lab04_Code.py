#Lab 4
#Name: Michaela Wojslaw
#Course: GEOG 392 GIS Programming
#Instructor: Dr. Zhang
#TA: Binbin Lin
#Date: November 5th, 2023

import arcpy

#1) Create the File GeoDB

folder_path = r'C:\\GEOG392_Labs\\GISProgramming\\Lab04'
gdbname = "GISProgramming_Lab04.gdb"
gdbpath = folder_path + "\\" + gdbname
# arcpy.CreateFileGDB_management(folder_path, "GISProgramming_Lab04.gdb")

#2) Make XY Event Layer
csv_path = 'C:\\GEOG392_Labs\\GISProgramming\\Lab04\\Lab04_Data\\garages.csv'
garge_layer_name = 'Garage_Points'
garges = arcpy.MakeXYEventLayer_management(csv_path,'X', 'Y', garge_layer_name)

#3) Feature Class to GeoDB
input_layer = garges
arcpy.FeatureClassToGeodatabase_conversion(input_layer,gdbpath)

garge_points = gdbpath + "\\" + garge_layer_name

campus = r"C:\\GEOG392_Labs\\GISProgramming\\Lab04\\Lab04_Data\\Campus.gdb"
buildings_campus =campus + "\\Structures"

buildings = gdbpath + "\\" + 'Buildings'

#4) Copy Management
arcpy.Copy_management(buildings_campus, buildings)


#5) Describe Buildings 
spatial_ref= arcpy.Describe(buildings).spatialReference

#6) Project Management
arcpy.Project_management(garge_points,  gdbpath + "\\Garage_Points_Reprojected", spatial_ref)

#7) Buffer Analysis
output_buffer= arcpy.Buffer_analysis(gdbpath + "\\Garage_Points_Reprojected", gdbpath + "\\Buffer", 150)

#8) Intersect Analysis
arcpy.Intersect_analysis([output_buffer, buildings], gdbpath + "\\Intersection", "ALL")

#9) Table to Table Conversion
arcpy.TableToTable_conversion(gdbpath + "\\Intersection.dbf", r"C:\\GEOG392_Labs\\GISProgramming\\Lab04\\Lab04_Data", "garage_150_buffer.csv")