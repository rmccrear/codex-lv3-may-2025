Name(s)________________________________________________ Period _____ Date ________________

|  | Activity Guide - React + Supabase Potluck App | 🍽️ |
| :---- | :---- | :---- |

**Overview**  
Build a full-stack React application with Supabase database integration. Create a potluck meal management app that demonstrates CRUD operations, form handling, and database security policies.

**Model:** [Supabase Setup Guide](https://rmccrear.github.io/codex-lv3-may-2025/week5/supabase-setup/SUPABASE_SETUP_GUIDE.html)

---

## Step 1 - Explore the Model

Review the Supabase setup guides and try the database interface.

**Discuss with a Partner:**
- What is a database table?
- What are Row Level Security (RLS) policies?
- How does a React app connect to a database?
- What are CRUD operations?

---

## Step 2 - Plan Your Database

**Database Tables:** Fill in the table below for each table you'll need to create.

| Table Name | Purpose | Columns Needed |
| :---- | :---- | :---- |
| potluck_meals | Store meal information | meal_name, guest_name, serves, kind_of_dish |
| beverages | Store drink information | beverage_name, guest_name, quantity, type_of_drink |
| utensils | Store utensil information | item_name, guest_name, quantity, item_type |
|  |  |  |

**Security Policies:** List the policies you'll need for each table.

| Table | Policy Type | Purpose |
| :---- | :---- | :---- |
| potluck_meals | SELECT | Allow everyone to read meals |
| potluck_meals | INSERT | Allow everyone to add meals |
| beverages | SELECT | Allow everyone to read beverages |
| beverages | INSERT | Allow everyone to add beverages |
| utensils | SELECT | Allow everyone to read utensils |
| utensils | INSERT | Allow everyone to add utensils |

---

## Step 3 - Plan Your Components

**React Components:** Fill in the table below for each component you'll create.

| Component Name | Purpose | Props Needed | State Variables |
| :---- | :---- | :---- | :---- |
| PotluckMeals | Display and add meals | none | meals (array) |
| Beverages | Display and add beverages | none | beverages (array) |
| Utensils | Display and add utensils | none | utensils (array) |
|  |  |  |  |

**Functions:** List the functions you'll need to create.

| Function Name | Component | What It Does |
| :---- | :---- | :---- |
| handleFetchMeals | PotluckMeals | Fetch meals from database |
| handleAddMeal | PotluckMeals | Add new meal to database |
| handleFetchBeverages | Beverages | Fetch beverages from database |
| handleAddBeverage | Beverages | Add new beverage to database |
| handleFetchUtensils | Utensils | Fetch utensils from database |
| handleAddUtensil | Utensils | Add new utensil to database |

---

## Step 4 - Setup Your Project

**Create React App:**
1. Run: `npm create vite@latest practice-with-db -- --template react`
2. Navigate to folder: `cd practice-with-db`
3. Run: `npm install`
4. Install Supabase: `npm install @supabase/supabase-js`
5. Start dev server: `npm run dev`

**Environment Setup:**
1. Create `.env.local` file in project root
2. Add your Supabase credentials:
   ```
   VITE_SUPABASE_URL=your-project-url
   VITE_SUPABASE_ANON_KEY=your-anon-key
   ```

---

## Step 5 - Build Your App

Follow the step-by-step guide to build your potluck app. Complete each step before moving to the next.

**Core Features (Steps 1-16):**
- ✅ Step 1: Initialize React project
- ✅ Step 2: Install Supabase client
- ✅ Step 3: Create project structure
- ✅ Step 4: Set up Supabase database
- ✅ Step 5: Create PotluckMeals component
- ✅ Step 6: Add fetch button and handler
- ✅ Step 7: Fetch data from database
- ✅ Step 8: Display data with for loop
- ✅ Step 9: Test data fetching
- ✅ Step 10: Add form structure
- ✅ Step 11: Add form event handler
- ✅ Step 12: Create insert RLS policy
- ✅ Step 13: Add insert statement
- ✅ Step 14: Test insert functionality
- ✅ Step 15: Refresh list after insert
- ✅ Step 16: Clear form after submit

**Form Enhancement (Step 17):**
- ✅ Step 17: Add select dropdown for dish types

**Additional Components (Steps 18-19):**
- ✅ Step 18: Create Beverages table and component
- ✅ Step 19: Create Utensils table and component

**As You Code:**
- Test your app frequently
- Use `console.log()` to debug
- Check Supabase dashboard for data changes
- Commit your code after completing each major feature

---

## Step 6 - Test Your App

Test your app and verify it works correctly for all scenarios:

| Test | What to Check | ✓ |
| :---- | :---- | :---: |
| Fetch meals button | Meals display from database |  |
| Add new meal | Form submits and meal appears in list |  |
| Form clears after submit | All input fields are empty |  |
| Select dropdown works | Can choose dish type from dropdown |  |
| Beverages component | Can fetch and add beverages |  |
| Utensils component | Can fetch and add utensils |  |
| Data persists | Data remains after page refresh |  |
| RLS policies work | Can read and insert data |  |

**Debug Using:**
- Browser console (F12) for errors
- `console.log()` to check data values
- Supabase dashboard to verify data changes
- Check environment variables are loaded

---

## Step 7 - Submit

Before you submit, check the rubric below to make sure your program meets the requirements.

| Category | Extensive Evidence | Convincing Evidence | Limited Evidence | No Evidence |
| :---- | :---- | :---- | :---- | :---- |
| **Project Setup** | React + Supabase project correctly set up and runs without errors. | Project mostly works but has minor setup issues. | Project has significant setup problems. | Project does not run. |
| **Database Design** | All three tables created with appropriate columns and RLS policies. | Most tables created with some policy issues. | Some tables created but missing policies. | Database not set up or missing tables. |
| **State Management** | All state variables properly created with `useState` and updated correctly. | Most state variables work correctly b