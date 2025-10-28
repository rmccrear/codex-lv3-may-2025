# Capstone Project Requirements

## Objective

Create a React project connected to Supabase using the Supabase JavaScript client library to perform Create and Read operations on multiple tables. Your project will include navigation and a structured user interface to manage records across different data sources.

---

## Project Requirements

### Database Requirements

**Required Tables (Minimum 2):**
1. **External Data Table**: Import data from Code.org's data tab
   - 📊 **[Browse all 97 Code.org datasets](https://rmccrear.github.io/codex-lv3-may-2025/week6/code_org_data.html)** - Choose from 12 categories!
2. **User Data Table**: Store user-generated content or user information

### Required Features

#### Report Page
- Display records from both tables using list patterns (map, reduce, filter)

#### Form Page
- Provide at least one form to add new records to the user data table
- Ensure validation for required fields

#### Navigation Bar
- Create a navigation bar to access the Report and Form pages
- Optionally include Log In page and Analytics/Charts page

#### Log In Page (Challenge Bonus)
- Authenticate the user and save their details in local storage
- Make it a full-featured authentication system

---

## Technical Requirements

1. **Use the Supabase JavaScript client library** (`@supabase/supabase-js`) with async/await to interact with the Supabase database

2. **Implement List Patterns** - Use at least one of each:
   - **Map**: Transform data (e.g., format dates, calculate totals, create lists in JSX)
   - **Reduce**: Aggregate data (e.g., count items, sum values)
   - **Filter**: Filter data (e.g., show only recent items, filter by category)

3. **Implement at least one for-loop** in your code

4. **Implement well thought out CSS design** using either:
   - Bootstrap framework
   - Your own well-developed custom CSS

5. **Data Visualization (Challenge Bonus)**
   - Add at least one data visualization chart (bar, pie, or line chart)
   - Use Chart.js, Recharts, or another visualization library
   - Display aggregated data from your tables
   - Show meaningful insights (totals, averages, trends, distributions)
   - Consider adding a dedicated "Analytics" or "Charts" page

---

## Submission Requirements

1. **Completed Planning Worksheet** (shared Google Doc link)
2. **GitHub Repository Link**
3. **Deployed Site Link** (Netlify or Vercel)
4. **README.md** with:
   - Project title and description
   - Purpose/Value proposition ("Why?" question)
   - Tech stack used (React, Supabase, Supabase JS client library, etc.)
   - Setup instructions (how to install and run)
   - Usage instructions (how to use the app)
   - Deployment information

---

## Grading Rubric

| Criteria | Points | Description |
|----------|--------|-------------|
| **Planning** | 10 | Completed planning worksheet is thorough and detailed |
| **External Data Table** | 15 | Successfully imports Code.org data with 50+ records |
| **User Data Table** | 15 | Stores user-generated content related to external data |
| **Create & Read** | 20 | Create and Read operations both working correctly |
| **List Patterns** | 15 | Map, Filter, and Reduce all implemented |
| **For-Loops** | 5 | At least one for-loop implemented |
| **Navigation** | 5 | Working navigation bar with all pages |
| **CSS/Styling** | 10 | Professional, well-designed interface |
| **Deployment** | 5 | Successfully deployed and accessible |
| **Code Quality** | 5 | Clean, organized, commented code |
| **Total** | **100** | |
| **Bonus** | +5 | Login page implemented |
| **Bonus** | +5 | Data visualization (Chart.js/Recharts) |

---

## Dataset Suggestions

Choose from Code.org's App Lab data tab. See the [complete list of 97 available datasets](code_org_data.md).

### Popular Dataset Categories:
- **Culture & Entertainment**: New York Times Bestsellers, IMDB Top 1000 Movies, Grammy Winners
- **Science**: Cereal Nutrition, Fast Food Nutrition, Nobel Prize Winners
- **Animals**: Dogs, Cats, Birds of the World
- **Sports**: FIFA World Cup Results, NBA Teams, Olympic Medals
- **Geography**: US National Parks, World's Tallest Buildings

*Choose datasets that have enough records (50+) and multiple useful columns.*

