# React + Supabase Create & Read Capstone Project

## Objective

Create a React project connected to Supabase using the Supabase JavaScript client library to perform Create and Read operations on multiple tables. Your project will include navigation and a structured user interface to manage records across different data sources.

---

## Project Requirements

### Database Requirements

**Required Tables (Minimum 2):**
1. **External Data Table**: Import data from Code.org's data tab
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

## Dataset Suggestions

Choose from Code.org's App Lab data tab. See the [complete list of 97 available datasets](../week6/code_org_data.md).

### Popular Dataset Categories:
- **Culture & Entertainment**: New York Times Bestsellers, IMDB Top 1000 Movies, Grammy Winners
- **Science**: Cereal Nutrition, Fast Food Nutrition, Nobel Prize Winners
- **Animals**: Dogs, Cats, Birds of the World
- **Sports**: FIFA World Cup Results, NBA Teams, Olympic Medals
- **Geography**: US National Parks, World's Tallest Buildings

*Choose datasets that have enough records (50+) and multiple useful columns.*

---

## Table Structure Examples

### External Data Table Example
Import from Code.org (e.g., NYT Bestsellers):

| Column Name | Data Type | Constraints | Description |
|-------------|-----------|-------------|-------------|
| id | int | Primary Key, Auto-increment | Unique identifier |
| title | text | Not Null | Book title |
| author | text | Not Null | Author name |
| bestseller_date | text | | Date on list |
| created_at | timestamp | Default: now() | Record timestamp |

### User Data Table Example
Store user-generated content (e.g., Reviews):

| Column Name | Data Type | Constraints | Description |
|-------------|-----------|-------------|-------------|
| id | int | Primary Key, Auto-increment | Unique identifier |
| user_name | text | Not Null | User name |
| item_id | int | Not Null | Reference to external data |
| rating | int | Not Null | User rating (1-5) |
| review_text | text | | Review content |
| created_at | timestamp | Default: now() | Record timestamp |

---

## Assignment Steps

### Before You Begin
⚠️ **REQUIRED**: Complete the [Capstone Planning Assignment](../week6/ASSIGNMENT_CAPSTONE_PLANNING_MOODLE.md) first.

### Development Process

1. **Review your completed planning worksheet**
   - Use your wireframes as a guide
   - Follow your table structure plans
   - Reference your daily goals

2. **Set up your Supabase project**
   - Create your project and tables
   - Upload external data from Code.org CSV
   - Configure relationships between tables

3. **Create your React app**
   - Use Vite template: `npm create vite@latest my-capstone -- --template react`
   - Set up folder structure (components, pages, utils)
   - Install dependencies (React Router, etc.)

4. **Implement features using your checklist**
   - ✅ Navigation bar
   - ✅ Report Page with all three list patterns
   - ✅ Form Page with validation
   - ✅ For-loops
   - ✅ CSS/Styling
   - ✅ All CRUD operations
   - ⭐ Login page (optional)
   - ⭐ Data visualization (optional)

5. **Deploy your project**
   - Deploy to Netlify or Vercel
   - Test all functionality in production
   - Ensure environment variables are configured

---

## Submission Requirements

Submit all of the following through Moodle:

1. **Completed Planning Worksheet** (Google Doc link)
   - This should already be submitted from the planning assignment
   - Or create it if you haven't completed that assignment yet

2. **GitHub Repository Link**
   - Public repository with all your code
   - Clear commit history showing your development process
   - No sensitive credentials in code

3. **Deployed Site Link**
   - Live, working application on Netlify or Vercel
   - All features functional
   - Accessible without authentication (or provide demo credentials)

4. **README.md** with:
   - Project title and description
   - Purpose/Value proposition ("Why?" question)
   - Tech stack used (React, Supabase, Supabase JS client library, etc.)
   - Setup instructions (how to install and run)
   - Usage instructions (how to use the app)
   - Deployment information
   - Screenshots of your application (optional but recommended)

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

## Detailed Grading Criteria

### Excellent (A - 90-100)
- All requirements met plus bonus features
- Professional, polished UI/UX
- Clean, well-organized code
- Comprehensive README
- Meaningful data relationships
- Engaging application

### Good (B - 80-89)
- All core requirements met
- Functional interface
- Code is readable and organized
- Good data visualization
- Some minor bugs or styling issues

### Satisfactory (C - 70-79)
- Most requirements met
- Basic functionality works
- Can improve styling/UX
- Some incomplete features
- Needs documentation improvements

### Needs Improvement (D - 60-69)
- Core Create and Read operations working
- Missing some required features
- Minimal styling
- Incomplete planning
- Deployment issues

---

## Resources

- 📋 [Capstone Requirements](../week6/CAPSTONE_REQUIREMENTS.md)
- 📝 [Capstone Planning Guide](../week6/CAPSTONE_PLANNING.md)
- 📊 [Code.org Datasets](../week6/code_org_data.md)
- 🚀 [Deployment Guide](./ASSIGNMENT_WEEK5_MOODLE.md) (reference Supabase setup)

### Key Documentation
- [React Documentation](https://react.dev/)
- [Supabase Documentation](https://supabase.com/docs)
- [Chart.js Documentation](https://www.chartjs.org/)

---

## Getting Help

- Review the planning guide thoroughly
- Ask questions in class or during office hours
- Check existing code examples from mini-projects
- Use online documentation resources
- Test incrementally - don't wait until the end
