# CS235 Flix Assignement
jche686
##A1
Create domain model and unit tests from CS235FlixSkeleton
https://github.com/martinurschler/CS235FlixSkeleton

## A2
Build and design web application concerned with movies incorporating the domain model from A1.
Flask, Jinja, WTF forms and Python is used to created this web application.

Web pages include:
- Home page
- Browse movies page
- Login page

### Building, Running and Testing
Choose directory of your choice and store the web application inside it, we will use C:\COMPSCI-235 in this example
```
C:\COMPSCI-235> py -3 -m venv venv

C:\COMPSCI-235> venv\Scripts\activate

C:\COMPSCI-235> pip install -r requirements.txt
```
Running the web application
```
C:\COMPSCI-235> flask run
```
Testing the web application
```
C:\COMPSCI-235> python -m pytest
```
