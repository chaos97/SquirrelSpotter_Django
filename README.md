![](https://thenypost.files.wordpress.com/2019/10/squirrel-nut-ki-415099-flower.jpg?quality=90&strip=all&w=642)
# Squirrel Tracking  Application
This application can help users keep tracking of all the known squirrels in Central Park.
By using this application, users can easily view the squirrels on a map, view all squirrels' id, add squirrels, update information and delete it. 
>Data source: the 2018 Central Park Squirrel Census data.

## Main functions
### Management commands
There are two management commands:
- **Import**
 A command that can be used to import the data from the 2018 census file (in CSV format)
- **Export**
 A command that can be used to export the data in CSV format

### Views
There are five views:
- **Map**
  * Located at: /map
  * Showing a map that displays the location of the squirrel sightings on an OpenStreets map
- **All**
  * Located at: /sightings
  * Listing all squirrel sightings with links to edit each
  * Showing one "add" button, which can be used to add squirrels
- **Update**
  * Located at: /sightings/<squirrel_id>
  * Updating a particular sighting
- **Add**
  * Located at: /sightings
  * Creating new sightings
- **Stats**
  * Located at: /sightings/stats
  * Showing five attributes about squirrel sightings

## Group Name
- Project Group 8, Section 1

## UNIs
- Unis: [bw2649, wh2374]

## Link to server
需要填充
