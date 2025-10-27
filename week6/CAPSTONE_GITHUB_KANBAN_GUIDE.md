# GitHub Kanban Board for Capstone Project

## Overview

A GitHub Project board is a Kanban-style board that helps you track your work and progress. Using a project board for your capstone will help you:
- ✅ Break down your project into manageable tasks
- ✅ Visualize your progress
- ✅ Stay organized and motivated
- ✅ Show professional project management skills
- ✅ Link code commits to issues automatically

---

## Why Use a GitHub Kanban Board?

**🎯 Professional Experience**
- Learn tooling used in real software teams
- Demonstrate project management skills to employers
- Practice industry-standard workflows

**📊 Visual Progress**
- See what you've done, what you're doing, and what's next
- Track completion percentage automatically
- Identify blockers early

**🔗 Code Integration**
- Link commits to issues (auto-close issues with "Fixes #123")
- Show progress through code changes
- Create a complete project history

**📝 Documentation**
- Built-in project documentation
- Share progress with instructors/peers
- Track time spent on different features

---

## Creating Your Kanban Board

### Step 1: Create a New Project

1. Go to your capstone repository on GitHub
2. Click on the **"Projects"** tab in your repo
3. Click **"New project"**
4. Choose **"Board"** as the template
5. Name it **"Capstone Project"** and click **"Create"**

### Step 2: Set Up Your Columns

Your board should have these columns (in this order):

```
📋 To Do          → Ideas and tasks that aren't started yet
🔧 In Progress    → Tasks currently being worked on
⚠️  Blocked         → Tasks stuck waiting on something
🧪 Review         → Completed code awaiting testing
✅ Done            → Completed and tested features
```

---

## Creating Your Roadmap

### Phase 1: Planning Tasks

Create these issues to track your planning work:

**Issue 1:** "Complete Planning Worksheet"
- Assign yourself
- Add label: `planning`
- Add to "To Do" column

**Issue 2:** "Review Code.org Datasets"
- Label: `planning`, `research`
- Description: Research and select 3 interesting datasets

**Issue 3:** "Create Wireframes"
- Label: `planning`, `design`
- Description: Wireframe all screens (splash, report, form)

**Issue 4:** "Design Database Schema"
- Label: `planning`, `database`
- Description: Plan both external and user data tables

---

### Phase 2: Setup Tasks

**Issue 5:** "Set Up Supabase Project"
- Label: `setup`, `database`
- Due date: Day 1

**Issue 6:** "Import External Data from Code.org"
- Label: `setup`, `database`
- Prerequisite: Issue 5

**Issue 7:** "Create React App with Vite"
- Label: `setup`
- Description: Initialize project structure

**Issue 8:** "Set Up Git Repository"
- Label: `setup`, `git`
- Prerequisite: Issue 7

---

### Phase 3: Core Development Tasks

**Issue 9:** "Create Navigation Bar Component"
- Label: `feature`, `ui`
- Estimated effort: Medium

**Issue 10:** "Build Supabase Client Configuration"
- Label: `feature`, `backend`
- Description: Set up Supabase JS client library

**Issue 11:** "Create Home/Splash Page"
- Label: `feature`, `ui`

**Issue 12:** "Implement Report Page - Fetch Data"
- Label: `feature`, `backend`
- Description: Fetch from both tables

**Issue 13:** "Implement Map Pattern"
- Label: `feature`, `list-patterns`
- Description: Transform and display data

**Issue 14:** "Implement Filter Pattern"
- Label: `feature`, `list-patterns`
- Description: Filter records by criteria

**Issue 15:** "Implement Reduce Pattern"
- Label: `feature`, `list-patterns`
- Description: Aggregate data (counts, sums)

**Issue 16:** "Add For-Loop Implementation"
- Label: `feature`, `coding-pattern`

**Issue 17:** "Create Form Page"
- Label: `feature`, `ui`
- Description: Add user data to database

**Issue 18:** "Add Form Validation"
- Label: `feature`, `validation`

---

### Phase 4: Styling & Polish

**Issue 19:** "Implement CSS Styling"
- Label: `feature`, `ui`
- Options: Bootstrap or custom CSS

**Issue 20:** "Responsive Design Testing"
- Label: `testing`, `ui`
- Description: Test on mobile and desktop

---

### Phase 5: Bonus Features

**Issue 21:** "Implement Login Page"
- Label: `feature`, `bonus`
- Priority: Low (optional)

**Issue 22:** "Add Data Visualization Charts"
- Label: `feature`, `bonus`
- Description: Chart.js or Recharts

---

### Phase 6: Deployment

**Issue 23:** "Deploy to Netlify/Vercel"
- Label: `deployment`
- Due date: Final day

**Issue 24:** "Write README.md"
- Label: `documentation`
- Description: Use README template

**Issue 25:** "Final Testing & Bug Fixes"
- Label: `testing`

---

## Linking Code to Issues

### Automatic Issue Closing

GitHub automatically closes issues when you include keywords in your commit messages:

```bash
# Close a single issue
git commit -m "Add report page Fixes #12"

# Close multiple issues
git commit -m "Complete list patterns implementation
- Add map pattern
- Add filter pattern  
- Add reduce pattern
Fixes #13 Fixes #14 Fixes #15"

# Other closing keywords
git commit -m "Resolve #18"      # Close issue
git commit -m "Closes #12"       # Close issue
git commit -m "Implement form page Closes #17"
```

### Manual Linking

1. Go to the issue
2. Click **"Development"** section on the right sidebar
3. Use **"Link a pull request"** button
4. Or use the issue number in your PR: `Fixes #12`

---

## Tracking Progress

### Progress Indicators

Your board will show:
- **Status:** Current state of each issue
- **Assignee:** Who's working on it
- **Milestones:** Group related issues
- **Labels:** Categorize by feature type
- **Due Dates:** Set deadlines

### Using Milestones

Create milestones to group related issues:

**Milestone 1:** "Planning Phase"
- Includes: Issues 1-4
- Due: End of planning week

**Milestone 2:** "Setup Phase"
- Includes: Issues 5-8
- Due: Day 1

**Milestone 3:** "Core Features"
- Includes: Issues 9-18
- Due: Days 2-3

**Milestone 4:** "Polish & Deploy"
- Includes: Issues 19-25
- Due: Days 4-5

### Burndown Charts

GitHub shows progress automatically:
- Issues remaining by milestone
- Completed vs. total issues
- Velocity (issues closed per week)

---

## Daily Workflow

### Starting Work on an Issue

1. Drag issue from "To Do" → "In Progress"
2. Assign yourself to the issue
3. Create a new branch: `git checkout -b issue-12-report-page`
4. Start coding!

### Completing Work

1. Commit with issue reference: `git commit -m "Add report page Fixes #12"`
2. Push to GitHub
3. Drag issue from "In Progress" → "Review"
4. Test your code
5. Drag to "Done" when complete

### If You Get Stuck

1. Drag issue to "Blocked"
2. Add a comment explaining why
3. Create a new issue for the blocking problem
4. Update when unblocked

---

## Example Issue Template

**Title:** `Create Report Page`

**Labels:** `feature`, `ui`

**Milestone:** Core Features

**Assignee:** [Your Name]

**Description:**
```markdown
## Goal
Display records from both external and user data tables.

## Requirements
- Fetch data from Supabase
- Display in table or list format
- Show all columns
- Use list patterns (map, filter, reduce)

## Acceptance Criteria
- [ ] Data displays from external table
- [ ] Data displays from user table  
- [ ] Map pattern implemented
- [ ] Filter pattern implemented
- [ ] Reduce pattern implemented

## Technical Notes
- Use Supabase JS client library
- Async/await for API calls
- Error handling included
```

---

## Advanced Features

### Automation

GitHub Projects can:
- Auto-move issues when PRs are merged
- Auto-close issues with commit messages
- Auto-update assignees based on branch names

### Project Views

Create different views:
- **By Priority:** Sort by importance
- **By Feature:** Group by labels
- **By Assignee:** Who's working on what
- **Timeline View:** See due dates in calendar

### Insights

Track metrics like:
- Average time to complete issues
- Most time-consuming features
- Completion rate by milestone

---

## Tips for Success

✅ **Create Issues Early**
- Don't wait until something is broken
- Create placeholder issues during planning
- Fill in details as you understand requirements

✅ **Keep Issues Small**
- One feature per issue
- If an issue takes more than 4 hours, break it down
- Easier to track progress

✅ **Write Good Commit Messages**
- Use present tense: "Add report page"
- Reference issues: "Fixes #12"
- Be specific about what changed

✅ **Update Regularly**
- Move issues as you work
- Add comments when stuck
- Keep your board current

✅ **Use Labels Consistently**
- `bug`: Something broken
- `feature`: New functionality
- `planning`: Design work
- `documentation`: Writing/updating docs
- `testing`: Testing work

---

## Resources

- [GitHub Projects Documentation](https://docs.github.com/en/issues/planning-and-tracking-with-projects)
- [GitHub Issues Best Practices](https://github.blog/2020-04-09-project-management-in-a-remote-world/)
- [Writing Effective Commit Messages](https://www.freecodecamp.org/news/how-to-write-better-git-commit-messages/)

---

## Sample Workflow

**Monday Morning:**
1. Look at "To Do" column
2. Pick an issue (e.g., Issue #9: Create Navigation)
3. Drag to "In Progress"
4. Branch: `git checkout -b issue-9-navigation`

**Monday Afternoon:**
1. Complete the work
2. Commit: `git commit -m "Add navigation bar Fixes #9"`
3. Push to GitHub
4. Drag issue to "Review"

**Monday Evening:**
1. Test the navigation
2. Confirm it works
3. Drag to "Done"

**GitHub automatically:**
- Marks the issue as complete
- Updates your progress percentage
- Links the commit to the issue

---

*Using a Kanban board makes you look more professional and helps you stay organized. It's an optional tool, but highly recommended! 🚀*

