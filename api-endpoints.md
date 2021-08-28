### OCU-login 
```json
    {
        "endpoint": "/login/",
        "method": "POST",
        "body": {
            "email": "user@email.com",
            "password": "password"
        },
        "response": {
            "user": "user@email.com",
            "auth": "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"
        },
        "description": "takes user email and password and validates them. then responses auth user token/session key"
    },
```
### OCU-today's class
```json
    {
        "endpoint": "/get-todays-classes/",
        "method": "GET",
        "body":{
            "classes": [
                {
                    "start_time": "7:00 AM",
                    "end_time": "9:00 AM",
                    "course_name": "Artificial Intelligence"
                },
                {
                    "start_time": "7:00 AM",
                    "end_time": "9:00 AM",
                    "course_name": "Artificial Intelligence"
                },
                .......
            ]
        },
        "description":"gets all classes of a specific weekday"
    },
```
### OCU-announcements
```json
    {
        "endpoint": "/get-announcements/",
        "method": "GET",
        "body":{
            "announcments": [
                {
                    "created_at": "2021-09-12, 7:00 AM",
                    "last_updated_at": "2021-09-12, 9:00 AM",
                    "title": "Class routine published",
                    "description": "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Laudantium quaerat nisi autem similique illo est totam, repellendus exercitationem deserunt quisquam, quos et ut eius! Quam quasi facilis eaque aperiam temporibus."
                },
                {
                    "created_at": "2021-09-12, 7:00 AM",
                    "last_updated_at": "2021-09-12, 9:00 AM",
                    "title": "Class routine published",
                    "description": "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Laudantium quaerat nisi autem similique illo est totam, repellendus exercitationem deserunt quisquam, quos et ut eius! Quam quasi facilis eaque aperiam temporibus."
                },                
                .......
            ]
        },
        "description":"gets all anouncements"
    }
```
### OCU-get-assignments
```json
     {
        "endpoint": "/get-assignments/",
        "method": "GET",
        "body":{
            "assignments": [
                {
                    "created_at": "2021-09-12, 7:00 AM",
                    "last_updated_at": "2021-09-12, 7:00 AM",
                    "deadline": "2021-09-12, 9:00 AM",
                    "title": "Artificial Intelligence",
                    "description": "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Laudantium quaerat nisi autem similique illo est totam, repellendus exercitationem deserunt quisquam, quos et ut eius! Quam quasi facilis eaque aperiam temporibus."
                },
                {
                    "created_at": "2021-09-12, 7:00 AM",
                    "last_updated_at": "2021-09-12, 7:00 AM",
                    "deadline": "2021-09-12, 9:00 AM",
                    "title": "Artificial Intelligence",
                    "description": "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Laudantium quaerat nisi autem similique illo est totam, repellendus exercitationem deserunt quisquam, quos et ut eius! Quam quasi facilis eaque aperiam temporibus."
                },
                .......
            ]
        },
        "description":"gets all assignments"
    }
```
### OCU-get-exams
```json     
     {
        "endpoint": "/get-exams/",
        "method": "GET",
        "body":{
            "exams": [
                {
                    "created_at": "2021-09-12, 7:00 AM",
                    "last_updated_at": "2021-09-12, 7:00 AM",
                    "deadline": "2021-09-12, 9:00 AM",
                    "title": "Artificial Intelligence",
                    "description": "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Laudantium quaerat nisi autem similique illo est totam, repellendus exercitationem deserunt quisquam, quos et ut eius! Quam quasi facilis eaque aperiam temporibus."
                },
                {
                    "created_at": "2021-09-12, 7:00 AM",
                    "last_updated_at": "2021-09-12, 7:00 AM",
                    "deadline": "2021-09-12, 9:00 AM",
                    "title": "Artificial Intelligence",
                    "description": "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Laudantium quaerat nisi autem similique illo est totam, repellendus exercitationem deserunt quisquam, quos et ut eius! Quam quasi facilis eaque aperiam temporibus."
                },
                .......
            ]
        },
        "description":"gets all exams"
    }
```
### OCU-get-all-classes (for routine)
```json    
    {
        "endpoint": "/get-all-classes/",
        "method": "GET",
        "body":{
            "classes": [
                {
                    "start_time": "7:00 AM",
                    "end_time": "9:00 AM",
                    "week_day": 1,
                    "course_name": "Artificial Intelligence"
                },
                {
                    "start_time": "7:00 AM",
                    "end_time": "9:00 AM",
                    "week_day": 2,
                    "course_name": "Artificial Intelligence"
                },
                .......
            ]
        },
        "description":"gets all classes of a week"
    },
```
### OCU-all-courses-details
```json    
    {
        "endpoint": "/get-all-courses-details/",
        "method": "GET",
        "body":{
            "courses": [
                {
                    "google_class_link": "classroom.google.com",
                    "google_class_code": "asdf",
                    "doc": "docs.google.com",
                    "drive": "google_drive link",
                    "chat": "chat_link",
                    "course_name":"Artificial Intelligence",
                },
                {
                    "google_class_link": "classroom.google.com",
                    "google_class_code": "asdf",
                    "doc": "docs.google.com",
                    "drive": "google_drive link",
                    "chat": "chat_link",
                    "course_name":"Artificial Intelligence",
                },
                .......
            ]
        },
        "description":"gets all classes of a week"
    },
```
### OCU-class-links
```json
    {
        "endpoint": "/get-classes-link/",
        "method": "GET",
        "body":{
            "links": [
                {
                    "link_id": "1234567",
                    "password": "password",
                    "link": "zoom.us",
                    "course_name":"Artificial Intelligence",
                },
                {
                    "link_id": "1234567",
                    "password": "password",
                    "link": "zoom.us",
                    "course_name":"Artificial Intelligence",
                },
                .......
            ]
        },
        "description":"gets all class links"
    },
```