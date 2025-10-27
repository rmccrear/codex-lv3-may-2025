# React + Supabase Create & Read Project

## Objective

Create a React project connected to Supabase using the Supabase JavaScript client library to perform Create and Read operations on multiple tables. Your project will include navigation and a structured user interface to manage records across different data sources.

---

## Project Requirements

### Database Requirements

#### Required Tables (Minimum 2)
1. **External Data Table**: Import data from Code.org's data tab or another external source
2. **User Data Table**: Store user-generated content or user information

### Features

#### Report Page
- Display records from both tables using list patterns (map, reduce, or filter)

#### Form Page
- Provide at least one form to add new records to the user data table
- Ensure validation for required fields

#### Log In Page (Challenge)
- Authenticate the user and save their details in local storage

#### Navigation Bar
- Create a navigation bar to access the Report and Form pages (and Log In page if implemented)
- Optionally include an Analytics/Charts page for data visualization (bonus challenge)

---

## Table Suggestions

Here are some suggested table structures you can implement, or you can create your own. Remember you need at least 2 tables: one with external data and one for user data.

### External Data Examples

#### 1. New York Times Bestsellers (External)
Import book data from Code.org's "New York Times Bestsellers" dataset:

| Column Name | Data Type | Constraints | Description |
|-------------|-----------|-------------|-------------|
| id | int | Primary Key, Auto-increment | Unique identifier for each book |
| title | text | Not Null | Title of the book |
| author | text | Not Null | Author of the book |
| bestseller_date | text | | Date it was on bestseller list |
| created_at | timestamp | Default: now() | Record creation timestamp |

#### 2. IMDB Top 1000 Movies (External)
Import movie data from Code.org's "IMDB Top 1000" dataset:

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

#### 3. Cereal Nutrition (External)
Import cereal nutrition data from Code.org's "Cereal Nutrition" dataset:

| Column Name | Data Type | Constraints | Description |
|-------------|-----------|-------------|-------------|
| id | int | Primary Key, Auto-increment | Unique identifier for each cereal |
| name | text | Not Null | Name of the cereal |
| calories | int | | Calories per serving |
| fiber | float | | Fiber content (grams) |
| sugar | float | | Sugar content (grams) |
| created_at | timestamp | Default: now() | Record creation timestamp |

#### 4. Dogs (External)
Import dog breed data from Code.org's "Dogs" dataset:

| Column Name | Data Type | Constraints | Description |
|-------------|-----------|-------------|-------------|
| id | int | Primary Key, Auto-increment | Unique identifier for each dog |
| breed | text | Not Null | Dog breed name |
| size | text | | Size category (Small, Medium, Large) |
| group | text | | Breed group (Sporting, Working, etc.) |
| intelligence | int | | Intelligence ranking |
| created_at | timestamp | Default: now() | Record creation timestamp |

#### 5. FIFA World Cup Results (External)
Import soccer data from Code.org's "FIFA World Cup Results" or "FIFA World Cup 2022" dataset:

| Column Name | Data Type | Constraints | Description |
|-------------|-----------|-------------|-------------|
| id | int | Primary Key, Auto-increment | Unique identifier for each match |
| home_team | text | Not Null | Home team name |
| away_team | text | Not Null | Away team name |
| home_score | int | | Home team score |
| away_score | int | | Away team score |
| created_at | timestamp | Default: now() | Record creation timestamp |

#### Other Code.org Dataset Options
You can also use any of these datasets from Code.org's App Lab data tab:
- **Entertainment**: Grammy Winners, Oscar Winners, Video Game Reviews
- **Science**: Nobel Prize Winners, Periodic Table Elements, Fast Food Nutrition
- **Sports**: NBA Teams, Olympic Medals, Paralympic Games
- **Geography**: US National Parks, World's Tallest Buildings, Countries and Territories
- **Culture**: Tate Museum Artworks, Bechdel Test, Netflix Content

*Note: Choose datasets that have enough records (50+) and multiple useful columns.*

---

## Assignment

**⚠️ REQUIRED: Planning Document**
📋 **Complete the [Capstone Planning Worksheet](https://docs.google.com/document/d/1GT_9HHmCe1kTSk-67HErz-HNocPdi_Uqw8g698Kx5Ig/edit?usp=sharing)** before starting your project. You must fill out all sections including:
- Brainstorming your app ideas
- Wireframes for your screens
- Table structure planning
- Daily goals and milestones
- Technical checklist

*Share your completed planning worksheet with your instructor.*

---

1. **Create at least 2 tables** - One must contain external data (from Code.org's data tab or another source), and one must contain user-generated data. Create them in Supabase with proper relationships.

2. **Create a React app** with the following navigation:
   - **Report Page**: Fetch records from both tables and display them using list patterns (map, reduce, or filter).
   - **Form Page**: Add at least one form for creating new records in the user data table. Ensure validation for required fields.
   - **Log In Page (Challenge)**: Authenticate users and store their details locally.

3. **Use the Supabase JavaScript client library** (`@supabase/supabase-js`) with async/await to interact with the Supabase database.

4. **Include a navigation bar** that allows users to switch between the Report and Form pages (and Log In page if implemented). Add an "Analytics" or "Charts" page if you complete the data visualization challenge.

5. **Implement List Patterns**: Use at least one of each of the following patterns:
   - **Map**: Transform data (e.g., format dates, calculate totals, create lists in JSX)
   - **Reduce**: Aggregate data (e.g., count items, sum values)
   - **Filter**: Filter data (e.g., show only recent items, filter by category)

6. **Implement at least one for-loop** in your code

7. **Implement well thought out CSS design** using either Bootstrap or your own well-developed custom CSS

8. **Data Visualization (Challenge Bonus)**: Add at least one data visualization chart (e.g., bar chart, pie chart, line chart) using Chart.js, Recharts, or another visualization library to display aggregated data from your tables.
   - Examples: Total counts, averages, trends over time, category distributions
   - Show meaningful insights about your data
   - Consider adding a dedicated "Analytics" or "Charts" page to your app

---

## Submission

- Submit your **completed planning worksheet** (shared Google Doc link)
- Submit your project repository link on the provided platform
- Ensure all functionality (Create and Read) is working as expected
- Include a **README.md file** explaining the project's purpose, setup, and usage
- **Deploy the project** on Netlify or Vercel

---

*This document was created with AI assistance using Claude Sonnet 4.5 for curriculum development.*