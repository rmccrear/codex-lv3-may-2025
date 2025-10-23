# React + Supabase CRUD Project

## Objective

Create a React project connected to Supabase using the Fetch API to perform CRUD (Create, Read, Update, Delete) operations on a single table. Your project will include navigation and a structured user interface to manage the records in the table.

---

## Project Requirements

### Features

#### Log In Page
- Authenticate the user and save their details in local storage.

#### Report Page
- Display a list of all records in the table.

#### Form Page
- Provide a form to add new records to the table.

#### Navigation Bar
- Create a navigation bar to access the Log In, Report, and Form pages.

---

## Table Options

Choose one of the following table structures to implement:

### 1. Book Register

| Column Name | Data Type | Constraints | Description |
|-------------|-----------|-------------|-------------|
| id | int | Primary Key, Auto-increment | Unique identifier for each book |
| title | text | Not Null | Title of the book |
| author | text | Not Null | Author of the book |
| genre | text | | Genre of the book |
| publication_year | int | | Year of publication |
| created_at | timestamp | Default: now() | Record creation timestamp |

### 2. Play List Songs

| Column Name | Data Type | Constraints | Description |
|-------------|-----------|-------------|-------------|
| id | int | Primary Key, Auto-increment | Unique identifier for each song |
| song_title | text | Not Null | Title of the song |
| artist | text | Not Null | Name of the artist |
| album | text | | Album the song belongs to |
| release_year | int | | Year the song was released |
| created_at | timestamp | Default: now() | Record creation timestamp |

### 3. Pokémon Cards

| Column Name | Data Type | Constraints | Description |
|-------------|-----------|-------------|-------------|
| id | int | Primary Key, Auto-increment | Unique identifier for each card |
| name | text | Not Null | Name of the Pokémon |
| type | text | | Type (e.g., Fire, Water, Grass) |
| hp | int | | Hit points of the Pokémon |
| rarity | text | | Rarity level of the card |
| created_at | timestamp | Default: now() | Record creation timestamp |

### 4. Employee Register

| Column Name | Data Type | Constraints | Description |
|-------------|-----------|-------------|-------------|
| id | int | Primary Key, Auto-increment | Unique identifier for each employee |
| name | text | Not Null | Name of the employee |
| position | text | | Job title of the employee |
| department | text | | Department the employee belongs to |
| hire_date | date | | Date the employee was hired |
| created_at | timestamp | Default: now() | Record creation timestamp |

### 5. Airbnb Apartment List

| Column Name | Data Type | Constraints | Description |
|-------------|-----------|-------------|-------------|
| id | int | Primary Key, Auto-increment | Unique identifier for each listing |
| title | text | Not Null | Title of the apartment |
| location | text | Not Null | City or area where the apartment is located |
| price_per_night | float | | Price per night |
| available | boolean | Default: true | Whether the apartment is available for booking |
| created_at | timestamp | Default: now() | Record creation timestamp |

---

## Assignment

1. **Select one table** from the options above and create it in Supabase, add the username (user creating the record).

2. **Create a React app** with the following navigation:
   - **Log In Page**: Authenticate users and store their details locally.
   - **Report Page**: Fetch all records from the Supabase table and display them. Include options to update and delete records.
   - **Form Page**: Add a form for creating new records. Ensure validation for required fields.

3. **Use the Fetch API** with async/await to interact with the Supabase database.

4. **Include a navigation bar** that allows users to switch between the Log In, Report, and Form pages.

---

## Submission

- Submit your project repository link on the provided platform.
- Ensure all functionality (CRUD) is working as expected.
- Include a README.md file explaining the project setup and usage.
- Deploy the project on render.com