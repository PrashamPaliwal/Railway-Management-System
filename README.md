# Train-Reservation-System

This is my Python project for managing trains, routes, stations, and reservations using a file-based database.  
The program reads and writes data from `.txt` files stored in different folders.  

# Features
- Add and edit train details  
- Create and manage routes  
- Search trains by station or route  
- Handle seat availability and reservations  
- Rollback and scheduled updates through file handling  

# Project Files
- **Train.py** → Main program (clean version)  
- **Train(Raw).py** → Original version before cleanup  
- **Database folders** →  
  - `State_Data` → list of states  
  - `City_Data` → cities grouped by state  
  - `Station_Data` → stations with state and city info  
  - `Route_Data` → route definitions  
  - `Train_Data` → train details  
  - `Train_Full_Data` → detailed train journeys  
  - `Dated_Train_Route_Data` → train routes by date  
  - `Route_Train_Data` → routes mapped to trains  
- **Other text files** → configuration and supporting data  

# How to Run
1. Clone the repository.  
2. Keep all folders and `.txt` files in the same structure.  
3. Run `Train.py` in Python (tested on Python 3.x).  

# Notes
- The system requires all data files and folders to be present.  
- This project was built to practice system design and file-based data handling.  
