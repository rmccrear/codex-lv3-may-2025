# React + Supabase CRUD Project

## Objective

Create a React project connected to Supabase using the Fetch API to perform CRUD (Create, Read, Update, Delete) operations on multiple tables. Your project will include navigation and a structured user interface to manage records across different data sources.

---

## Project Requirements

### Database Requirements

#### Required Tables (Minimum 2)
1. **External Data Table**: Import data from Code.org's data tab or another external source
2. **User Data Table**: Store user-generated content or user information

### Features

#### Report Page
- Display records from both tables using list patterns (map, reduce, or filter)
- Include options to update and delete records

#### Form Page
- Provide at least one form to add new records to the user data table
- Ensure validation for required fields

#### Log In Page (Challenge)
- Authenticate the user and save their details in local storage

#### Navigation Bar
- Create a navigation bar to access the Report and Form pages (and Log In page if implemented)

---

## Table Suggestions

Here are some suggested table structures you can implement, or you can create your own. Remember you need at least 2 tables: one with external data and one for user data.

### External Data Examples

#### 1. Book Database (External)
Import book data from Code.org's data tab or another source:

| Column Name | Data Type | Constraints | Description |
|-------------|-----------|-------------|-------------|
| id | int | Primary Key, Auto-increment | Unique identifier for each book |
| title | text | Not Null | Title of the book |
| author | text | Not Null | Author of the book |
| genre | text | | Genre of the book |
| publication_year | int | | Year of publication |
| created_at | timestamp | Default: now() | Record creation timestamp |

#### 2. Movie Database (External)
Import movie data from external source:

| Column Name | Data Type | Constraints | Description |
|-------------|-----------|-------------|-------------|
| id | int | Primary Key, Auto-increment | Unique identifier for each movie |
| title | text | Not Null | Title of the movie |
| director | text | Not Null | Director of the movie |
| year | int | | Year of release |
| rating | text | | Movie rating (G, PG, PG-13, R) |
| created_at | timestamp | Default: now() | Record creation timestamp |

### User Data Examples

#### 3. User Reviews (User Data)
Store user-generated reviews for the external data:

| Column Name | Data Type | Constraints | Description |
|-------------|-----------|-------------|-------------|
| id | int | Primary Key, Auto-increment | Unique identifier for each review |
| user_name | text | Not Null | Name of the user writing the review |
| item_id | int | Not Null | ID of the book/movie being reviewed |
| rating | int | Not Null | User rating (1-5 stars) |
| review_text | text | | User's written review |
| created_at | timestamp | Default: now() | Record creation timestamp |

#### 4. User Favorites (User Data)
Track user's favorite items:

| Column Name | Data Type | Constraints | Description |
|-------------|-----------|-------------|-------------|
| id | int | Primary Key, Auto-increment | Unique identifier for each favorite |
| user_name | text | Not Null | Name of the user |
| item_id | int | Not Null | ID of the book/movie |
| item_type | text | Not Null | Type of item (book, movie, etc.) |
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

1. **Create at least 2 tables** - One must contain external data (from Code.org's data tab or another source), and one must contain user-generated data. Create them in Supabase with proper relationships.

2. **Create a React app** with the following navigation:
   - **Report Page**: Fetch records from both tables and display them using at least 2 list patterns (map, reduce, or filter). Include options to update and delete records.
   - **Form Page**: Add at least one form for creating new records in the user data table. Ensure validation for required fields.
   - **Log In Page (Challenge)**: Authenticate users and store their details locally.

3. **Use the Fetch API** with async/await to interact with the Supabase database.

4. **Include a navigation bar** that allows users to switch between the Report and Form pages (and Log In page if implemented).

5. **Implement List Patterns**: Use at least 2 of the following patterns:
   - **Map**: Transform data (e.g., format dates, calculate totals)
   - **Reduce**: Aggregate data (e.g., count items, sum values)
   - **Filter**: Filter data (e.g., show only recent items, filter by category)

---

## Submission

- Submit your project repository link on the provided platform.
- Ensure all functionality (CRUD) is working as expected.
- Include a README.md file explaining the project setup and usage.
- Deploy the project on render.com