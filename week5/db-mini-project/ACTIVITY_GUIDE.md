Name(s)________________________________________________ Period _____ Date ________________

|  | Activity Guide - React + Supabase Potluck App | 🍽️ |
| :---- | :---- | :---- |

**Overview**  
Build a full-stack React application with Supabase database integration. Create a potluck meal management app that demonstrates CRUD operations, form handling, and database security policies.

---

## Step 1 - Review Supabase Concepts

Review the Supabase setup guides and try the database interface.

**Discuss with a Partner:**
- What is a database table?
- What are Row Level Security (RLS) policies and why do we need them?
- How does a React app connect to a database?
- What are SELECT and INSERT operations?

---

## Step 2 - Create Wireframes

**Wireframes:** Sketch the layout of your app pages. Use simple boxes and labels to show where elements will go.

**Main App Layout:**
```
┌─────────────────────────────────────┐
│           Potluck App               │
├─────────────────────────────────────┤
│  [Fetch Meals] Button               │
│                                     │
│  • Meal 1 by Guest serves 4        │
│  • Meal 2 by Guest serves 6        │
│  • Meal 3 by Guest serves 2        │
│                                     │
│  ┌─────────────────────────────────┐ │
│  │        Add Meal Form            │ │
│  │  Meal: [_____________]          │ │
│  │  Guest: [_____________]         │ │
│  │  Serves: [_____]               │ │
│  │  Type: [Dropdown ▼]            │ │
│  │  [Add Meal] Button             │ │
│  └─────────────────────────────────┘ │
└─────────────────────────────────────┘
```

**Additional Components:** Sketch similar layouts for Beverages and Utensils components.

---

## Step 3 - Plan Your Database

**Database Tables:** Fill in the table below for each table you'll need to create.

| Table Name | Purpose | Columns Needed |
| :---- | :---- | :---- |
| potluck_meals | Store meal information | meal_name, guest_name, serves, kind_of_dish |
| potluck_beverages |  |  |
| potluck_utensils |  |  |

**Security Policies:** List the policies you'll need for each table.

| Table | Policy Type | Purpose |
| :---- | :---- | :---- |
| potluck_meals | SELECT | Allow everyone to read meals |
| potluck_meals | INSERT | Allow everyone to add meals |
| potluck_beverages |  |  |
| potluck_beverages |  |  |
| potluck_utensils |  |  |
| potluck_utensils |  |  |

---

## Step 4 - Plan Your Components

**React Components:** Fill in the table below for each component you'll create.

| Component Name | Purpose | Props Needed | State Variables |
| :---- | :---- | :---- | :---- |
| PotluckMeals | Display and add meals | none | meals (array) |
| PotluckBeverages |  |  |  |
| PotluckUtensils |  |  |  |

**Functions:** List the functions you'll need to create.

| Function Name | Component | What It Does |
| :---- | :---- | :---- |
| handleFetchMeals | PotluckMeals | Fetch meals from database |
| handleAddMeal | PotluckMeals | Add new meal to database |
| handleFetchBeverages | PotluckBeverages |  |
| handleAddBeverage | PotluckBeverages |  |
| handleFetchUtensils | PotluckUtensils |  |
| handleAddUtensil | PotluckUtensils |  |

---

## Step 5 - Setup Your Project

**Create React App:**
1. Run: `npm create vite@latest practice-with-db -- --template react`
2. Navigate to folder: `cd practice-with-db`
3. Run: `npm install`
4. Install Supabase: `npm install @supabase/supabase-js`
5. Start dev server: `npm run dev`

**Environment Setup:**
1. Create `.env.local` file in project root (not `.env`)
2. Add your Supabase credentials (you can find these in the supabase dashboard):
   ```
   VITE_SUPABASE_URL=your-project-url
   VITE_SUPABASE_ANON_KEY=your-anon-key
   ```

---

## Step 6 - Build Your App

**📖 [Complete Project Guide](./project-guide-show-me.md)** - Step-by-step instructions with code examples

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

## Step 7 - Test Your App

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

## Step 8 - Submit

Before you submit, check the rubric below to make sure your program meets the requirements.

| Category | Extensive Evidence | Convincing Evidence | Limited Evidence | No Evidence |
| :---- | :---- | :---- | :---- | :---- |
| **Project Setup** | React + Supabase project correctly set up and runs without errors. | Project mostly works but has minor setup issues. | Project has significant setup problems. | Project does not run. |
| **Database Design** | All three tables created with appropriate columns and RLS policies. | Most tables created with some policy issues. | Some tables created but missing policies. | Database not set up or missing tables. |
| **State Management** | All state variables properly created with `useState` and updated correctly. | Most state variables work correctly b