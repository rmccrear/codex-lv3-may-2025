# Week 4 - Day 2: Building Multi-Page React Apps with Git Collaboration

## Overview
Today you'll learn how to create multiple "pages" in React using `useState` and components, and how to collaborate with your partner using Git branches. You'll set up the skeleton structure of your hackathon project.

## Learning Objectives
By the end of this activity, you'll be able to:
- Create multiple page components in React
- Implement simple navigation between pages using `useState`
- Create and work with Git branches
- Use pair programming with Git workflow
- Set up the basic structure for your hackathon app

## Today's Topics

### 1. Creating "Pages" in React
React is a single-page application (SPA) framework, but we can simulate multiple pages by:
- Creating separate components for each page/screen
- Using `useState` to track which page to display
- Conditionally rendering the current page

### 2. Git Branching
Working with branches allows you to:
- Work on features without affecting the main code
- Collaborate without conflicts
- Review changes before merging
- Keep a clean project history

---

## Part 1: Demo - Multi-Page Navigation in React

### Simple Navigation Pattern

Here's how to create a basic multi-page React app:

```jsx
// App.jsx
import { useState } from 'react';
import Home from './pages/Home';
import DataList from './pages/DataList';
import About from './pages/About';

function App() {
  // Track which page to show
  const [currentPage, setCurrentPage] = useState('home');

  // Three separate functions to change pages
  function goToHomePage() {
    setCurrentPage('home');
  }
  
  function goToDataListPage() {
    setCurrentPage('list');
  }
  
  function goToAboutPage() {
    setCurrentPage('about');
  }

  // Decide which page to show using if statements
  let content = <Home />;
  if (currentPage === 'home'){
    content = <Home />
  }
  else if (currentPage === 'list') {
    content = <DataList />;
  } else if (currentPage === 'about') {
    content = <About />;
  } 

  return (
    <>
      <header>
        <nav>
          <button onClick={goToHomePage}>Home</button>
          <button onClick={goToDataListPage}>Data List</button>
          <button onClick={goToAboutPage}>About</button>
        </nav>
      </header>
      <div className="app">
        {content}
      </div>
    </>
  );
}

export default App;
```

### Example Page Component

```jsx
// pages/Home.jsx
function Home() {
  return (
    <div>
      <h1>Home Page</h1>
      <p>Welcome to our app!</p>

    </div>
  );
}

export default Home;
```

### Key Concepts:
- **Props**: Pass three navigation functions to child components
- **State**: Use `useState` to track the current page
- **If Statements**: Use if/else to decide which page to show
- **Event Handlers**: `onClick` calls the navigation functions directly

---

## Part 2: Git Branching Demo

### Basic Git Branch Workflow

```bash
# Check current branch
git branch

# Create a new branch
git branch feature-navigation

# Switch to the new branch
git switch feature-navigation

# Make changes, then stage and commit
git add .
git commit -m "Add basic navigation structure"

# Push branch to GitHub
git push -u origin feature-navigation

# Switch back to main
git switch main

# Pull latest changes
git pull origin main
```

### GitHub Pull Request Flow
1. Push your branch to GitHub
2. Go to GitHub repository
3. Click "Compare & pull request"
4. Add description of changes
5. Create pull request
6. Review and merge
7. Delete branch after merging

---

## Part 3: Breakout Room Activities

### Activity 1: Project Setup (20 minutes)

**Goals:**
- Set up your hackathon project
- Create initial Git repository
- Both partners clone the project

**Steps:**

1. **Choose a driver** (person who will type first)

2. **Create the project:**
   ```bash
   npm create vite@latest hackathon-project -- --template react
   cd hackathon-project
   npm install
   ```

3. **Initialize Git and push to GitHub:**
   ```bash
   git init
   git add .
   git commit -m "Initial project setup"
   git branch -M main
   ```

4. **Create a GitHub repository:**
   - Go to GitHub.com
   - Click "New repository"
   - Name it `hackathon-project` (or your app name)
   - Don't initialize with README
   - Copy the remote URL

5. **Push to GitHub:**
   ```bash
   git remote add origin [your-repo-url]
   git push -u origin main
   ```

6. **Partner clones the repository:**
   ```bash
   git clone [repo-url]
   cd hackathon-project
   npm install
   ```

✅ **Checkpoint**: Both partners should have the project running locally with `npm run dev`

---

### Activity 2: Create Basic Navigation (30 minutes)

**Goals:**
- Create a new branch
- Build 3 page components
- Implement simple navigation
- Push branch and create PR

**Steps:**

1. **Driver creates a new branch:**
   ```bash
   git branch add-navigation
   git switch add-navigation
   ```

2. **Create folder structure:**
   ```bash
   mkdir src/pages
   ```

3. **Create three page components** in `src/pages/`:
   - `Home.jsx`
   - `DataList.jsx`
   - `About.jsx`
   
   Each page should receive the three navigation functions as props and include buttons to navigate to the other pages.

4. **Update `App.jsx`** to import the pages and set up navigation with useState and if/else statements (refer to the demo code above).

5. **Test the navigation** - Click buttons to move between pages

6. **Commit and push the branch:**
   ```bash
   git add .
   git commit -m "Add basic navigation with three pages"
   git push -u origin add-navigation
   ```

7. **Create Pull Request on GitHub:**
   - Go to your repository on GitHub
   - Click "Compare & pull request"
   - Write description: "Added basic navigation structure with Home, DataList, and About pages"
   - Click "Create pull request"

8. **Review and merge:**
   - Review the changes together
   - Click "Merge pull request"
   - Click "Confirm merge"
   - Delete the branch on GitHub

9. **Both partners pull the changes:**
   ```bash
   git switch main
   git pull origin main
   ```

✅ **Checkpoint**: Navigation should work between all three pages for both partners

---

### Activity 3: Switch & Add Styling (30 minutes)

**Goals:**
- Switch roles (new driver)
- Create a new branch
- Add basic CSS styling
- Expand page content
- Complete Git workflow again

**Steps:**

1. **Switch computers/driver**

2. **New driver creates a branch:**
   ```bash
   git switch main
   git pull origin main
   git branch add-styling
   git switch add-styling
   ```

3. **Add CSS styling to `App.css`:**
   - Add styles for navigation buttons (colors, padding, hover effects)
   - Add styles for page containers (max-width, padding, margins)
   - Style headings and paragraphs

4. **Expand each page with more content:**
   - Add a `.page` class to each page component wrapper
   - Add descriptive text and headings
   - Include placeholders for future features
   - Personalize with your names and project goals

5. **Test all pages and styling**

6. **Commit and push:**
   ```bash
   git add .
   git commit -m "Add CSS styling and expand page content"
   git push -u origin add-styling
   ```

7. **Create PR, review, merge, and pull** (same process as Activity 2)

8. **Both partners pull changes:**
   ```bash
   git switch main
   git pull origin main
   ```

✅ **Checkpoint**: All pages should have styling and expanded content

---

### Activity 4: Plan Next Steps (15 minutes)

**Discuss with your partner:**

1. **Dataset Choice:**
   - What dataset will you use?
   - Where will you get it from?
   - Have you exported it to JSON yet?

2. **Feature Planning:**
   - Which list method(s) will you use? (map/reduce/filter)
   - What will each page do specifically?
   - What data will you display on each page?

3. **Role Division:**
   - Who will focus on what for the next session?
   - What needs to be done before next class?

4. **Create a checklist** in your planning document:
   ```markdown
   ## To Do Before Next Class
   - [ ] Export dataset to JSON
   - [ ] Decide on exact features for each page
   - [ ] Sketch paper prototype (if not done)
   - [ ] Identify where to use map/reduce/filter
   ```

5. **Optional: Create GitHub Issues**
   - Go to your repo → Issues tab
   - Create issues for major tasks
   - Assign to partners

---

## Key Git Commands Reference

```bash
# Check status
git status

# See all branches
git branch

# Create a new branch
git branch branch-name

# Switch to a branch
git switch branch-name

# Stage all changes
git add .

# Commit changes
git commit -m "Description of changes"

# Push branch to GitHub
git push -u origin branch-name

# Pull latest changes
git pull origin main

# Delete local branch (after merging)
git branch -d branch-name
```

## Pair Programming Tips

### For the Driver (typing):
- ⌨️ Focus on writing the code
- 💬 Explain what you're doing as you type
- 🤔 Ask for input on decisions
- ⏸️ Take breaks every 20-30 minutes

### For the Navigator (reviewing):
- 👁️ Watch for typos and errors
- 💡 Suggest solutions and improvements
- 📖 Look up documentation when needed
- ⏰ Keep track of time

### For Both:
- 🔄 Switch roles regularly
- 🗣️ Communicate constantly
- 🙋 Ask questions if confused
- 🎉 Celebrate small wins!

## Troubleshooting

### Issue: Git push rejected
**Solution**: Pull first, then push
```bash
git pull origin main
git push
```

### Issue: Merge conflict
**Solution**: 
1. Open the conflicted files
2. Look for `<<<<<<<`, `=======`, `>>>>>>>` markers
3. Choose which code to keep
4. Remove the markers
5. Commit the resolution

### Issue: Pages not switching
**Solution**: 
- Check `currentPage` state value in React DevTools
- Verify page names match exactly (case-sensitive: 'home', 'list', 'about')
- Make sure all three navigation functions are passed correctly to each page
- Check that `onClick` handlers call the functions (not arrow functions)

### Issue: Import errors
**Solution**: 
- Check file paths (case-sensitive)
- Verify export statements exist
- Make sure files are in correct folders

## Success Criteria

By the end of today, you should have:
- ✅ A GitHub repository with your hackathon project
- ✅ Three working page components
- ✅ Navigation between all pages
- ✅ Basic CSS styling applied
- ✅ At least 2 commits with proper messages
- ✅ Experience with branches, PRs, and merging
- ✅ A plan for your next steps

## Homework / Before Next Class

1. **Export your dataset** following the [HOWTO guide](../HOWTO_CODE_ORG_DATA_IMPORT.md)
2. **Complete your paper prototype** if not finished
3. **Fill out the planning sheet** with your app concept
4. **Decide specifically** where you'll use map, reduce, or filter
5. **Think about** what data to display on each page

---

## Next Class Preview

In the next session, you'll:
- Import your JSON data
- Implement map/reduce/filter
- Add interactivity
- Work toward completing your hackathon app

---

**Great job today!** You've built the foundation for your hackathon project and learned important collaboration skills with Git. Keep up the momentum! 🚀

---

#### ✍️ Attribution

This guide was developed with assistance from **Anthropic's Claude (Claude 3.5 Sonnet)** to ensure clarity, accuracy, and consistency in the explanations and examples.
