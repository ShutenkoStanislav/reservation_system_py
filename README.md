# Booking system
It's Django based project for rooms booking in real time free traking. Also app have authorization and authentication

## Features
- **User Authentication**
    - We can easily create account in page by "/register" url
    - In header we have Logout button so, logout and login in my site is very easy
    - In home page we can see clickable account logo whitch redirect to personal details page
- **Room Management**
    - In room list we can see all available rooms
    - Site have page with filtered rooms by type
    - IN list rooms page img. of room its clickable and redirect to detail room information
- **Booking System**
    - For booking you only need choose start and end time
    - In view we have auto checking in time available
    - In admin panel we can see all bookings

## Tech Stack

- **Backend:** Django 5.2.7
- **Database:** SQLite
- **Frontend:** HTML, CSS, Bootstrap
- **Python:** 3.12.3

## Installation

1. **Commads to start app in browser**
```bash

1. cd reservation_sys tem_py-1
2. .\venv\Scripts\Activate.ps1
3. click + ctrl http://127.0.0.1:8000/
4. Welcome to site
```

2. **Install dependencies**
```bash
pip install django
```

3. **Run migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

4. **Create superuser**
```bash
python manage.py createsuperuser
```

## Database Models

### Room
- 'number' - Room number
- 'capacity' - Capacity per room
- 'price' - Dollars per day
- 'locations' - Room description
- 'type' - Type of room

### Profile
- 'user' - Django User model
- 'all_rooms' - All rooms per user
- 'phone_number' - Phone number for user
- 'email' - Email of user
- 'username' - User username

### Profile
- 'user' - Foreign key for user
- 'room' - Foreign key for room 
- 'start_time' - Start time for reservation
- 'end_time' - End time for reservation
- 'creation_time' - Creation time of reservation

## Usage

1. **Register an account** sing in or login
2. **Select list** Click to "Booking now" or "Room types"
3. **If Booking now** Select room in list of all rooms
4. **If Room types** Select room in list of rooms by types
5. **Way to room info page** Click to image of room 
6. **Room info** Check fuul info and click button "Booking"
7. **Fill form** Just choose start and end time, click "Accept"
7. **Reservation info** Check information aboute booking

## Admin Panel

Access admin panel at `/admin/` with superuser credentials to:
- Add/Edit/Delete rooms
- Manage bookings
- View user information

- login: admin
- password: admin











