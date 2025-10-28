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
   - 📚 **[Supabase JavaScript Reference](https://supabase.com/docs/reference/javascript/start)** - Complete documentation for JavaScript client library

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
  - Use the [README Template](CAPSTONE_README_TEMPLATE.md) as a guide
- **Deploy the project** on Netlify or Vercel

---

*This document was created with AI assistance using Claude Sonnet 4.5 for curriculum development.*

---

## Glossary

### Key Terms from [Vocabulary List](../VOCABULARY_LIST.md)

**[Database (DB)](../VOCABULARY_LIST.md#database-db):** An organized collection of data that can be stored, accessed, and managed efficiently. In web development, databases provide a structured place to store and organize data.

**[Supabase](../VOCABULARY_LIST.md#supabase):** A backend-as-a-service that gives you a PostgreSQL database, authentication, storage, and APIs. Works like an open-source Firebase.

**[SQL](../VOCABULARY_LIST.md#sql):** Structured Query Language — used to communicate with relational databases like PostgreSQL and MySQL.

**[Table](../VOCABULARY_LIST.md#table):** A collection of related data in the database, organized into rows and columns — similar to a spreadsheet.

**[Column](../VOCABULARY_LIST.md#column):** A labeled field in a table (e.g., `email`, `price`, `user_id`) that defines one type of data.

**[Row / Record](../VOCABULARY_LIST.md#row--record):** One entry in a table — like one user, one product, or one message.

**[SELECT](../VOCABULARY_LIST.md#select):** SQL command that reads data from a database.

**[INSERT](../VOCABULARY_LIST.md#insert):** SQL command that adds a new row into a table.

**[Persistence / Persist](../VOCABULARY_LIST.md#persistence--persist):** When data stays saved even after refreshing the page or restarting the app/server — unlike variables in JavaScript which disappear on reload.

**[Environment Variables (.env)](../VOCABULARY_LIST.md#environment-variables-env):** Hidden configuration values like API keys, database URLs, or secrets that you don't want hardcoded in your JavaScript.

**[Components](../VOCABULARY_LIST.md#components):** In React, the building blocks of applications that help organize code and keep programs from becoming too complicated by breaking down complex UIs into smaller, reusable pieces.

**[React](../VOCABULARY_LIST.md#react):** A framework created by Facebook in 2013. It's built on the idea of components and is one of the most popular tools for making modern websites.

**[JSX](../VOCABULARY_LIST.md#jsx):** A special syntax used in React. It looks like HTML but isn't exactly the same. JSX must be used inside React components.

**[State](../VOCABULARY_LIST.md#state):** In React, component-local data that React preserves between renders so a component can remember information and update the UI.

**[Props (Properties)](../VOCABULARY_LIST.md#props-properties):** Attributes you can give to components to make them more powerful. Props are like HTML attributes but for your own custom components.

**[Function](../VOCABULARY_LIST.md#function):** In programming, reusable blocks of code that perform a specific task. They help organize code, avoid repetition, and make programs easier to understand.

**[List Patterns](../VOCABULARY_LIST.md#list-patterns):** Common approaches for working with lists, such as Random List Access and List Scrolling Pattern.

**[async](../VOCABULARY_LIST.md#async):** A keyword that makes a function return a Promise and allows use of `await` inside it.

**[await](../VOCABULARY_LIST.md#await):** Pauses inside an `async` function until a Promise is done.

**[fetch](../VOCABULARY_LIST.md#fetch):** Built-in browser function that makes HTTP requests to APIs. Returns a Promise.