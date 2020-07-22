# FuSion Parking-Management-System
An experimental GUI (tkinter) project for Smart and Fast Parking Management.

This goal of this project is to find the closest available parking slot based on 2-D co-ordinates. It sample 2-D live map depicts empty, filled and closest parking available slot on the map using diffrent colours. The algorithm is based on a shortest path-finding algorithm that has been implemented and tested on the sample live 2-D map. The information is stored in an offline SQL database and is built keeping in mind the idea of an intranet setup.

To start the application run file : PMS_main.py

# Required Python Packages:

Install using following command:<br>
1)pip install tkintertable<br>
2)pip install DateTime<br>
3)pip install pandas

To view Database File(.db) download sqlite3 Database Browser:
https://sqlitebrowser.org/dl/

# File Details:
1)PMS_GUI_1.py : GUI and Database Module<br>
2)PMS_Loci_2.py : Location Finding Module<br>
3)PMS_Login_3.py : Login Module<br>
4)PMS_Map_4.py : Display Map Module<br>
5)map4.csv : Live Map Matrix<br>
6)map_template.csv : Template Map Matrix<br>
7)login_info : Directory created on User Registration to save User Info<br>
8)location5.db : Database File<br>
