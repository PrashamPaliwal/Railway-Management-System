# Railway-Management-System

A Python-based project that simulates core railway operations including train scheduling, seat reservations, passenger data handling, and administrative functions.  
Built with a **multi-file structure** for scalability and future expansion. 

---

## 📂 Project Files
- **TRAIN.py** → Main program (clean version)  
- **train(RAW).py** → Original version before cleanup  
- **Database folders** →  
  - `State_Data` → list of states  
  - `City_Data` → cities grouped by state  
  - `Station_Data` → stations with state and city info  
  - `Route_Data` → route definitions  
  - `Train_Data` → train details  
  - `Train_Full_Data` → Contains detailed train information. Each train has its own folder inside this directory, where `<journey_number>.txt` files are created to store the full details of each journey of that train.
  - `Dated_Train_Route_Data` → train routes by date  
  - `Route_Train_Data` → routes mapped to trains  
- **Other text files** → configuration and supporting data  

---

## 🚀 Features
- **Station Management**: Add, check, and select stations by state and city.  
- **Route Management**: Create and validate train routes across multiple stations.  
- **Train Management**: Add new trains, assign routes, and manage journeys.  
- **Reservation System**: Search and select trains based on routes and dates.  
- **Data Handling**: File-based storage for states, cities, stations, routes, and train details.  

---

## ⚙️ How to Run
1. Clone the repository.  
2. Keep all folders and `.txt` files in the same structure.  
3. Run `TRAIN.py` in Python.
4. Now create stations, routes, trains, add train to routes for dates and book from user end   

---

## 🧩 Challenges Faced
- **Interlinking Data Files**: Managing relationships between multiple `.txt` files for states, cities, stations, routes, and trains was complex. Ensuring smooth data acceptance and runtime validation required careful design.  
- **Error Handling & Validation**: Runtime checks were added to catch inconsistencies and prevent invalid data from being stored.  
- **File Naming Limitations**: Some files couldn’t be named beyond a certain character limit. To solve this, I implemented **hashlib-based shortening**—allowing unique, shorter names while still mapping correctly to the intended data (especially in `Route_Train_Data`).  

---

## 🔮 Future Improvements
- **User Details**: Add passenger information such as phone number updates and extended profile management.  
- **Train Edit Functionality**:  
  - Allow administrators to reduce or increase seat counts dynamically.  
  - Implement rollback logic: if seat reductions conflict with already reserved seats for future journeys, the system will discard changes safely without breaking data integrity.  
- **Database Integration**: Transition from file-based storage to **SQLite/MySQL** for more robust and scalable data management.  

---

## ⚠️ Notes
- The system requires all data files and folders to be present.  
- This project was built to practice system design and file-based data handling.  
