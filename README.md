<p align="center">
   <img src="https://img.shields.io/badge/-Collage%20Project-informational" />
</p>

# B7Fun

## Project Explanation
A sport and fun activities social network for Beersheba city.

The target of this Project is to create a social network focused on connecting people by sports and fun places (e.g. sport facilities, dog gardens, elderly social clubs, playgrounds, urban nature).

This project is part of open data beer sheva.

This Project was created with <b> Python(Django + Django Channels + Djongo), MongoDB, CSS3, Bootstrap4, JavaScript,
jQuery, Leaflet, Chart.js, HTML5 </b>. 

Application includes 2 types of users (Resident and Admin).

### Resident actions:

1.  View fun and sport location on map based on current location in beer sheva city.
2.  View fun and sport location by list.
3.  Filter location by location type and by search term.
4.  Join group chats based on a specific location.
5.  Report abusive behaviour in chats.
6.  View other users profile.
7.  Maintain its profile.
8.  Report problems in site.
9.  Rate and view site ratings.
10. View admin posts.
11. and more.
### <u> Resident Demo:</u>
![ALT "A resident demo video"](https://github.com/leorrose/B7Fun/blob/master/Demos/UserDemoPart1.gif)
![ALT "A resident demo video"](https://github.com/leorrose/B7Fun/blob/master/Demos/UserDemoPart2.gif)

### <u> Admin actions:</u>

1.  Use all resident functionality.
2.  View statistics on user logins and registration.
3.  Can block\unblock users.
4.  Can view reported abusive content.
5.  Can send mails to users.
6.  Can manage all Databases.
7.  and more. 

### <u> Admin Demo: </u>
![ALT "A admin demo video"](https://github.com/leorrose/B7Fun/blob/master/Demos/AdminDemo.gif)

## Project Setup:

### Project Setup (Windows):

1. make sure you have python on your computer (if not install python 3.6.1 from here [Python download](https://www.python.org/downloads/windows/))
2. Make sure Python is in path (if not follow this guide [Add python to path](https://datatofish.com/add-python-to-windows-path/))
3. Make sure pip is in path (if not follow this guide [Add pip to path](https://appuals.com/fix-pip-is-not-recognized-as-an-internal-or-external-command/))
4. Make sure you got docker on your computer (if not download here [Docker Download](https://docs.docker.com/docker-for-windows/install-windows-home/))
5. Run redis docker image (for chat), run in cmd **docker run -p 6379:6379 -d redis:5**
5. Clone repository.
6. Run Devops Scripts\installationWin.bat and wait until console closes.
7. That’s it, you are all set up to run.

### Project Setup (Linux):

1. make sure you have python on your computer (if not install python from here [Python download](https://docs.python-guide.org/starting/install3/linux/))
3. Make sure you have pip on your computer (if not follow this guide [pip download]](https://itsfoss.com/install-pip-ubuntu/))
4. Make sure you got docker on your computer (if not download here [Docker Download](https://docs.docker.com/engine/install/ubuntu/))
5. Run redis docker image (for chat), run in cmd **docker run -p 6379:6379 -d redis:5**
5. Clone repository.
6. Run Devops Scripts\installationLinux.sh and wait until console closes.
7. That’s it, you are all set up to run.

## Project Run:

### Project Run (on Windows):

1. Run runWin.bat (in Devops Scripts folder).

### Project Run (on Linux):

1. Run runLinux.sh (in Devops Scripts folder)


