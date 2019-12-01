## Flat Earth Bird Watchers by VSCOdeGirls

##### Roster/Roles
- tanzim elahi: works on database to ensure that data is cached for Jesse to query
- jesse hall: implementing the connection to the REST API's and general backend development
- ray lee: project manager/touching up the site with custom CSS/BootStrap 
- vishwaa sofat: works on the HTML/Jinja/CSS of the site to make sure everything is UX-streamlined

## Description
Display nearby planes in a user -defined radius around the user’s IP location or a custom set location. Each plane in the vicinity of the user will be plotted on a graph that overlays a map. When a point is hovered, one can click on it to be redirected to another page that tells more information about that flight, such as flight time, plane model, altitude, and current latitude and longitude. Of course, none of this could be done with the amazing API's that we meshed together, as shown below.

## APIs used 
- [OpenSky-Network](https://docs.google.com/document/d/10tvXVJ-Prrv23Y6H17UQL3W2DbYAndIeZQkPQbl8_pQ/edit?usp=sharing)
- [IPLocation](https://docs.google.com/document/d/1FazBlCH4SoM5bKaCs5vr4B7aEgTUVlvFv-1W-LoQmUA/edit?usp=sharing)
- [Google Maps Embedded](https://docs.google.com/document/d/1BrK8KIi1jxdETaGoEcuEB_UDiGwZhFFeWxZ_dlwiFww/edit?usp=sharing)

## Instructions
**Assuming python3 and pip are already installed**
### Virtual Environment 
- To prevent conflicts with globally installed packages, it is recommended to run everything below in a virtual environment. 

Set up a virtual environment by running the following in your terminal:
```
python -m venv hero 
# replace hero with anything you want 
# If the above does not work, run with python3 (this may be the case if a version of python2 is also installed)
```

To enter your virtual environment, run the following:
```
. hero/bin/activate
```

To exit your virtual environment, run the following:
```
deactivate
```

### Dependencies 
Run the following line in your virtual environment
```
pip install -r doc/requirements.txt
```
