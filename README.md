## Overview
To better tell the story of gun violence, the Columbia team has launched a web tool that overlays a heat map of gun-related crime for a given data set (https://github.com/enkeboll/ crime-heatmaps). The tool provides the option to filter by crime type (homicide, shooting, robbery, aggravated assault) as well as drop in mediators to view the tangible effects of Cure Violence practices in a neighborhood.

Several steps went into the creation of this tool. It is to the credit of the governments of Baltimore, Chicago, and New York that they all use online data portals freely accessible to the public, from which the team was able to pull the data. Each record needed only two of information: a timestamp and a location (lat/long). In order to filter based on crime category, that information should also be included.

With the data ready, a tool had to be found to visualize the data. Patrick Wied has released a client-side heatmapping tool written in JavaScript called heatmap.js (https://github.com/pa7/ heatmap.js), which works on top of any mapping layer. Google Maps also provides a JavaScript API, so that combo was the best place to start. Lastly, David Hamp-Gonsalves created a front-end GUI (https://github.com/davidhampgonsalves/crime-heatmaps) on top of both of these layers that was applied to the project, since CSS and styling wasn’t a forte of any of the team members.

The visualization is lightweight and requires no special software, other than a modern browser with which to open the site. As everything is written in JavaScript, HTML, and CSS, there is no code executed on any server– the tool can be distributed to any device and run locally.

The other major benefit of this tool is that it is highly extensible, as is covered in the next section. Cure Violence will be able to demonstrate both the need of unvisited cities, such as Los Angeles or Philadelphia, as well as the effect Cure Violence has had in its existing partnerships with Baltimore, Chicago, and New York.

## Instructions
Since all the code is client-side, this can be hosted almost anywhere.  It is currently live at [enkeboll.github.io/baltimore.html](enkeboll.github.io/baltimore.html), but can be run locally by first starting a lightweight server (`python -m SimpleHTTPServer`) from the root directory and then visiting [http://localhost:5000/baltimore.html](http://localhost:8000/baltimore.html).

Special thanks to the original designers mentioned above, Columbia University, Cure Violence, and Booz Allen Hamilton.
