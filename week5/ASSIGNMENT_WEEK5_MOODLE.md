# Week 5 Assignment: Database Mini Project - Potluck Management App

Build a complete React + Supabase potluck management application where users can view and add dishes, beverages, and utensils to a shared potluck event.

---

## 📚 Instructions

**📖 Start Here:** [Level 1 - Planning](https://rmccrear.github.io/codex-lv3-may-2025/week5/db-mini-project/db-levels/db-mini-project-lv-1.html)

Follow the level-by-level instructions (Levels 1-20) to build your potluck management application. Each level includes detailed steps, code hints, and checkpoints.

**Additional Resources:**
- [Supabase Setup Guide](https://rmccrear.github.io/codex-lv3-may-2025/week5/supabase-setup/SUPABASE_SETUP_GUIDE.html)
- [React + Supabase Setup Guide](https://rmccrear.github.io/codex-lv3-may-2025/week5/supabase-setup/SUPABASE_REACT_SETUP_GUIDE.html)
- [Activity Guide](https://rmccrear.github.io/codex-lv3-may-2025/week5/db-mini-project/ACTIVITY_GUIDE.html) - Planning templates and rubric

---

## ✅ Requirements

Your potluck management app must include:

1. **Database Setup**
   - Supabase project with at least 3 tables (meals, beverages, utensils)
   - Row Level Security (RLS) policies configured
   - Sample data inserted

2. **React Components**
   - PotluckMeals component for displaying and adding meals
   - PotluckBeverages component for beverages
   - PotluckUtensils component for utensils
   - Form handling with proper validation
   - State management using useState

3. **Database Operations**
   - Fetch data from Supabase (SELECT)
   - Insert new records (INSERT)
   - Display data using for loops
   - Form submission handling

4. **User Interface**
   - Clean, organized layout
   - Forms with proper input types
   - Real-time data updates after submission
   - Clear visual feedback

5. **Code Quality**
   - Clean, readable code
   - Proper error handling
   - Comments explaining key sections
   - Meaningful variable names

6. **Required Challenges**
   - Select dropdown for dish types (Level 16)
   - Third table and component (utensils) (Level 17)

7. **Documentation**
   - README.md with setup instructions
   - Database schema documentation
   - List of features implemented

---

## 📊 Grading Rubric

| Category | Weight | Description |
|----------|--------|-------------|
| **Database Setup** | 20% | Supabase configured, 3 tables created, RLS policies working |
| **React Integration** | 20% | Components fetch and display data correctly |
| **Form Functionality** | 15% | Forms submit data and update UI properly |
| **Data Display** | 10% | Data rendered using for loops, clean presentation |
| **Required Challenge 1** | 10% | Select dropdown for dish types (Level 16) |
| **Required Challenge 2** | 10% | Third table and utensils component (Level 17) |
| **Code Quality** | 10% | Clean code, good naming, helpful comments |
| **Documentation** | 5% | Complete README with setup instructions |

**Total:** 100%

---

## 🎓 Deliverable

**Submit:** GitHub repository URL containing:
- All source code (React components, Supabase config)
- `.env.local` file with Supabase credentials (DO NOT commit this)
- `README.md` with:
  - Project title and description
  - Setup instructions (`npm install`, Supabase setup)
  - Database schema (table structures)
  - Features list
  - Screenshots of working app
- Clear Git commit history

**Before submitting, verify:**
- [ ] App runs with `npm run dev` without errors
- [ ] Can fetch and display data from database
- [ ] Forms submit new data successfully
- [ ] Data updates immediately after submission
- [ ] All 3 tables implemented (meals, beverages, utensils)
- [ ] Select dropdown for dish types working
- [ ] Utensils component and table functional
- [ ] README is complete
- [ ] Code is commented and clean

---

## 📝 Assignment Structure

**Core Levels (Required):**
- Levels 1-3: Planning, project setup, database configuration
- Levels 4-8: Basic component creation and data fetching
- Levels 9-15: Form implementation and data insertion
- Level 16: Select dropdown challenge (Required Challenge 1)
- Level 17: Third table and utensils component (Required Challenge 2)
- Level 20: Project completion and documentation

**Optional Levels:**
- Levels 18-19: Additional features (filtering, advanced functionality)

---

## 📤 TURN IN

**Submit the following:**

1. **GitHub Repository URL** - Share the link to your completed project repository
2. **Deployed Site URL** (Optional) - If you deployed your app to Vercel, Netlify, or similar platform

**Repository should contain:**
- Complete React + Supabase potluck management app
- All 3 tables implemented (meals, beverages, utensils)
- Select dropdown functionality
- Utensils component working
- Complete README with setup instructions
- Clear commit history showing your progress IMPORTANT!

---

## 🆘 Need Help?

- Review the Supabase setup guides carefully
- Check browser console (F12) for errors
- Use `console.log()` to debug database queries
- Verify RLS policies in Supabase dashboard
- Post questions in the discussion forum

---

**Good luck building your potluck management system!** 🍽️✨

---

*This assignment integrates React frontend development with Supabase database backend for a complete full-stack experience.*
