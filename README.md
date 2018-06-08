  Sql Logs Analysis


### About the project
 
This is the third project for the Udacity Full Stack Nanodegree. In this project, a large database with over a million rows is explored by building complex SQL queries to draw business conclusions for the data. 

### Pre-requisites for the project
	- Python
	- Vagrant
	- VirtualBox

### installing required
	1) Install Vagrant 
	2) Install virtualbox

### To Run

1)vagrant up - to start vagrant vm
2)vagrant ssh - to connect to vagrant vm 
3)cd /vagrant
4)psql -d news -f newsdata.sql 

database tables list
	- Authors
	- Articles 
	- Log 
### move logs.py to vagrant directory

run python logs.py (or) python3 logs.py from shell to run newsdata.py;
