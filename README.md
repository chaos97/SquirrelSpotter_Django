![](https://thenypost.files.wordpress.com/2019/10/squirrel-nut-ki-415099-flower.jpg?quality=90&strip=all&w=642)

# Squirrel Tracking  Application
This application can help users keep tracking of all the known squirrels in Central Park.
By using this application, users can easily view the squirrels on a map, view all squirrels' id, add squirrels, update information and delete it. Also, users can view the statistics dashboard to have a better overall knowledge of these squirrels.

>Data source: [the 2018 Central Park Squirrel Census data](https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw)

## Main functions
### Management commands
There are two management commands:

- **import_squirrel_data**:
 A command that can be used to import the data from a CSV file
 
- **export_squirrel_data**:
 A command that can be used to export the data in CSV format

### Views
There are five views:

- **squirrel_map**
  * Located at: /map
  * Showing a map that displays the location of the squirrel sightings on an OpenStreets map
  
- **all_squirrels**
  * Located at: /sightings
  * Listing all squirrel sightings with links to edit each
  * Showing one "add" button, which can be used to add squirrels
  
- **squirrel_details**
  * Located at: /sightings/<squirrel_id>
  * Showing details of a particular sighting
  * Updating a particular sighting
  * Deleting a particular sighting
  
- **add_record**
  * Located at: /sightings/add
  * Creating new sightings
  
- **stats**
  * Located at: /sightings/stats
  * Showing a responsive and dynamic dashboard of several statistical graphs about the squirrel data

## Group Name
- Project Group 8, Section 1

## UNIs
- Unis: [bw2649, wh2374]

## Link to server
[https://tools-for-analytics-253819.appspot.com/sightings](https://tools-for-analytics-253819.appspot.com/sightings/)

