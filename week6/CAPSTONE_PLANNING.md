# Capstone Project Planning Guide

📋 **[Planning Worksheet](https://docs.google.com/document/d/1GT_9HHmCe1kTSk-67HErz-HNocPdi_Uqw8g698Kx5Ig/edit?usp=sharing)** - Use this worksheet to document your planning process as you work through each phase.

📊 **[Optional: GitHub Kanban Board Guide](CAPSTONE_GITHUB_KANBAN_GUIDE.md)** - Learn to use GitHub Projects to track your work and show progress professionally.

---

## Phase 1: Initial Planning & Brainstorming

### Steps:

**1. Review some of the data sets you might like to use (on code.org). Think of what data you can collect from users through a form.**
   - Browse through the Data Library on Code.org
   - 📊 **[Complete List of Code.org Datasets](https://rmccrear.github.io/codex-lv3-may-2025/week6/code_org_data.html)** - See all 97 available datasets organized by category
   - Look for interesting datasets from the Code.org App Lab data tab, such as:
     - **Culture & Entertainment**: New York Times Bestsellers, IMDB Top 1000 Movies, Grammy Winners, Video Game Reviews
     - **Science**: Cereal Nutrition, Fast Food Nutrition, Beverages Nutrition, Nobel Prize Winners
     - **Animals**: Dogs, Cats, Birds of the World, Palmer Penguins
     - **Sports**: FIFA World Cup Results, NBA Teams, Olympic Medals
     - **Geography**: US National Parks, World's Tallest Buildings, Countries and Territories
   - Consider what user-generated data would complement your chosen external dataset
   - Example: If you choose "New York Times Bestsellers" data, users could add reviews, ratings, or their personal reading lists

**2. Brainstorm one or two ideas. Think about who your user might be. What value would it provide to your users? Find your "Why?" for the app.**
   - Define your target user (students, readers, movie buffs, sports fans, health-conscious individuals, pet lovers, gamers, music lovers, etc.)
   - Identify a real problem or need your app addresses
   - Examples of "Why?":
     - "Book lovers need a way to track what they've read and discover new titles from NYT Bestsellers"
     - "Students tracking nutrition want to plan healthy breakfasts based on cereal nutrition data"
     - "Gamers want to review and rate video games from the IGN database"
     - "Sports fans want to track their favorite FIFA teams and add personal notes"
   - Consider the value proposition: What makes your app useful or unique?

**3. Create a 2 minute pitch. Try pitching your idea to a group.**
   - Structure your pitch to cover:
     - What your app does (brief description)
     - Who it's for (target users)
     - Why it's valuable (the problem it solves)
     - What data you'll use (external data + user data)
   - Practice your pitch to stay within 2 minutes
   - Be prepared to answer questions about technical feasibility

**4. Vote on the pitch in your group. Think about practicality of creating the app in the time required and the usefulness to your users.**
   - Evaluate pitches based on:
     - Can this realistically be built in the available time?
     - Is it useful and would people actually use it?
     - Does it meet the technical requirements (2 tables, CRUD operations)?
     - Is the scope appropriate (not too simple, not too complex)?
   - Vote for ideas that are both feasible and valuable

**5. Decide if you'd like to work together or alone.**
   - Solo work: Full control, easier communication, but more work for one person
   - Pair/group work: Share the load, collaborate, but need coordination and communication
   - Consider your team's strengths and how to divide the work effectively

---

## Phase 2: Detailed Planning & Design

### Next Phase:

**1. Finalize your app plan.**
   - **Choose your external data set** (from Code.org)
     - Select one dataset that has enough data to be interesting
     - Ensure it has multiple relevant fields (title, author/director, category, dates, etc.)
     - Examples: New York Times Bestsellers (500+ books), IMDB Top 1000 Movies, Cereal Nutrition (80+ items), Dogs (50+ breeds)
   - **Decide what data to collect from your users through a form.**
     - Create a complementary user data table
     - Examples of user data:
       - Reviews and ratings for external items
       - User favorites or wish lists
       - User notes or comments
       - User-generated content related to your external data
     - Ensure your user data relates to or references your external data

**2. Wireframe**
   - **Wireframe your splash screen/home page**
     - Include navigation elements
     - Welcome message or app name
     - Brief description or call-to-action
   - **Wireframe at least one data display screen (Report Page)**
     - How will you show records from both tables?
     - Include update and delete buttons/options
     - Show where you'll use map, filter, and reduce operations
     - Consider pagination or filtering options
   - **Wireframe at least one form to collect data from your users (Form Page)**
     - Input fields for all required data
     - Validation indicators
     - Submit button
     - Success/error messaging area

**3. Plan your data tables in Supabase.**
   - Define table names (singular or plural is fine)
   - List all columns with:
     - Column names
     - Data types (text, int, float, boolean, timestamp, date)
     - Constraints (primary key, not null, default values)
   - Determine relationships between tables
     - Example: User reviews might reference book IDs from "New York Times Bestsellers" or movie IDs from "IMDB Top 1000"
   - Sketch out your table structure on paper or digitally

**4. Download your data from code.org as CSV.**
   - Export your chosen dataset from Code.org
   - Clean the data if needed (check for missing values, format consistency)
   - Save the CSV file in a location you can easily access
   - Name it something descriptive (e.g., `bestsellers.csv`, `imdb_movies.csv`, `cereal_nutrition.csv`, `dogs.csv`)

---

## Phase 3: Coding & Implementation

### Coding Phase

**1. Create your project and tables in Supabase.**
   - Create a new Supabase project (or use existing one)
   - Create both tables in the Supabase SQL Editor or Table Editor
   - Set up primary keys (id, auto-increment)
   - Add timestamp columns (created_at, updated_at)
   - Configure row-level security (RLS) policies if needed
   - 📚 **[Supabase JavaScript Reference](https://supabase.com/docs/reference/javascript/start)** - Complete documentation for JavaScript client library

**2. Upload your data to Supabase.**
   - Use the Supabase import feature to upload your CSV file to the external data table
   - Verify the data imported correctly
   - Check that all rows and columns are present
   - Fix any import errors or data formatting issues

**3. Create your React app with Vite.**
   ```bash
   npm create vite@latest my-capstone-app -- --template react
   cd my-capstone-app
   npm install
   ```
   - Set up your folder structure (components, pages, utils, etc.)
   - Install additional dependencies if needed (React Router, etc.)

**4. Create your repo on GitHub.**
   - Initialize git: `git init`
   - Create a new repository on GitHub
   - Add the remote: `git remote add origin <your-repo-url>`
   - Make your first commit: `git add .` and `git commit -m "Initial commit"`
   - Push to GitHub: `git push -u origin main`

**5. Scaffold your README.**
   - Use the [README Template](CAPSTONE_README_TEMPLATE.md) as a starting point
   - Include the following sections:
     - Project title and description
     - Purpose of the project ("Why?" you identified earlier)
     - Features (CRUD operations, list patterns, etc.)
     - Tech stack (React, Supabase, Supabase JS client library, etc.)
     - Setup instructions (how to install and run)
     - Usage instructions (how to use the app)
     - Live demo link (after deployment)
   - Keep it clear and informative for others reviewing your work

**6. Create a plan for your week, including goals and milestones you'd like to achieve.**
   - Day 1 goals: Complete Supabase setup, import data, create basic React structure
   - Day 2 goals: Build navigation and basic pages (Report, Form)
   - Day 3 goals: Implement CRUD operations, add list patterns (map, filter, reduce)
   - Day 4 goals: Add styling (CSS or Bootstrap), implement for-loops, fix bugs
   - Day 5 goals: Add login (optional), deploy to Netlify/Vercel, finalize README
   - Adjust timeline based on your pace and team size
   - Build in time for testing and debugging

---

## Tips for Success

- Start with the database setup first - it's the foundation of your app
- Test your Supabase connection early
- Build and test one feature at a time
- Commit to GitHub frequently with clear commit messages
- Ask for help when you're stuck
- Test your CRUD operations as you build each one
- Plan for extra time - things often take longer than expected

---

*This document was created with AI assistance using Claude Sonnet 4.5 for curriculum development.*

---

## Glossary

### Key Terms from [Vocabulary List](../VOCABULARY_LIST.md)

**[Controlling Complexity](../VOCABULARY_LIST.md#controlling-complexity):** Called the "essence of programming." In React, using components is a way to control complexity by breaking big problems into smaller, reusable pieces.

**[Components](../VOCABULARY_LIST.md#components):** In React, the building blocks of applications that help organize code and keep programs from becoming too complicated by breaking down complex UIs into smaller, reusable pieces.

**[Database (DB)](../VOCABULARY_LIST.md#database-db):** An organized collection of data that can be stored, accessed, and managed efficiently. In web development, databases provide a structured place to store and organize data.

**[Supabase](../VOCABULARY_LIST.md#supabase):** A backend-as-a-service that gives you a PostgreSQL database, authentication, storage, and APIs. Works like an open-source Firebase.

**[Persistence / Persist](../VOCABULARY_LIST.md#persistence--persist):** When data stays saved even after refreshing the page or restarting the app/server — unlike variables in JavaScript which disappear on reload.

**[Table](../VOCABULARY_LIST.md#table):** A collection of related data in the database, organized into rows and columns — similar to a spreadsheet.

**[Column](../VOCABULARY_LIST.md#column):** A labeled field in a table (e.g., `email`, `price`, `user_id`) that defines one type of data.

**[Row / Record](../VOCABULARY_LIST.md#row--record):** One entry in a table — like one user, one product, or one message.

**[React](../VOCABULARY_LIST.md#react):** A framework created by Facebook in 2013. It's built on the idea of components and is one of the most popular tools for making modern websites.

**[JSX](../VOCABULARY_LIST.md#jsx):** A special syntax used in React. It looks like HTML but isn't exactly the same. JSX must be used inside React components.

**[State](../VOCABULARY_LIST.md#state):** In React, component-local data that React preserves between renders so a component can remember information and update the UI.

**[Props (Properties)](../VOCABULARY_LIST.md#props-properties):** Attributes you can give to components to make them more powerful. Props are like HTML attributes but for your own custom components.

**[List Patterns](../VOCABULARY_LIST.md#list-patterns):** Common approaches for working with lists, such as Random List Access and List Scrolling Pattern.

**[Function](../VOCABULARY_LIST.md#function):** In programming, reusable blocks of code that perform a specific task. They help organize code, avoid repetition, and make programs easier to understand.

**[Environment Variables (.env)](../VOCABULARY_LIST.md#environment-variables-env):** Hidden configuration values like API keys, database URLs, or secrets that you don't want hardcoded in your JavaScript.

**[Module](../VOCABULARY_LIST.md#module):** In programming, self-contained units of code that can be imported and used in other parts of a program. They help organize code into logical, reusable pieces.
