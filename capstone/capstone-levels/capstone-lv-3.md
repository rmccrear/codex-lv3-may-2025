Level Navigation: [1](./capstone-lv-1.md) | [2](./capstone-lv-2.md) | **Current Level:** 3 | [4](./capstone-lv-4.md) | [5](./capstone-lv-5.md) | [6](./capstone-lv-6.md) | [7](./capstone-lv-7.md) | [8](./capstone-lv-8.md) | [9](./capstone-lv-9.md) | [10](./capstone-lv-10.md) | [11](./capstone-lv-11.md) | [12](./capstone-lv-12.md) | [13](./capstone-lv-13.md) | [14](./capstone-lv-14.md) | [15](./capstone-lv-15.md) | [16](./capstone-lv-16.md) | [17](./capstone-lv-17.md) | [18](./capstone-lv-18.md) | [19](./capstone-lv-19.md) | [20](./capstone-lv-20.md) | [21](./capstone-lv-21.md) | [22](./capstone-lv-22.md) | [23](./capstone-lv-23.md) | [24](./capstone-lv-24.md) | [25](./capstone-lv-25.md) | [26](./capstone-lv-26.md) | [27](./capstone-lv-27.md) | [28](./capstone-lv-28.md) | [29](./capstone-lv-29.md) | [30](./capstone-lv-30.md) | [31](./capstone-lv-31.md) | [32](./capstone-lv-32.md) | [33](./capstone-lv-33.md) | [34](./capstone-lv-34.md)

---

# Level 3: Git Setup

## What You'll Do
Initialize version control and push your project to GitHub.

## Instructions
- Initialize a git repository (`git init`)
- Add all files to git (`git add .`)
- Create your first commit with a meaningful message like `chore: initial project setup`
- Push to GitHub (if you have a remote repository set up)

## ✅ Check
1. Open your terminal/command prompt in your project folder
2. Run `git status` - you should see "On branch main" and "nothing to commit, working tree clean"
3. Run `git log --oneline` - you should see your commit message like "chore: initial project setup"
4. **IMPORTANT:** Check that `secret-variables.js` is NOT on GitHub:
   - Go to your GitHub repository in a web browser
   - Look through the files - you should NOT see `secret-variables.js` listed
   - If you see it, check your `.gitignore` file includes `secret-variables.js`
5. If you see any errors, make sure you're in the correct folder and try the git commands again

---

## 🔍 Exploration: Commit Message Prefixes

You might be wondering why we use prefixes like `chore:` or `feature:` at the start of commit messages. These are part of a best practice convention called **Conventional Commits** that helps organize and categorize your changes:

- **`chore:`** - For maintenance tasks, setup, or non-functional changes (like adding files, updating dependencies, or initial project setup)
- **`feature:`** - For new functionality or features you're adding to your project
- **`fix:`** - For bug fixes or corrections
- **`docs:`** - For documentation changes
- **`style:`** - For formatting, styling, or code style changes
- **`refactor:`** - For code restructuring without changing functionality

Using these prefixes makes it easier to:
- Quickly understand what type of change each commit represents
- Generate changelogs automatically
- Filter commits by type when reviewing project history
- Follow consistent practices in professional development

In this level, we use `chore:` because we're doing initial project setup - creating the foundation without adding new features yet.

---


---

<!-- LEVEL_END -->


---

Level Navigation: [1](./capstone-lv-1.md) | [2](./capstone-lv-2.md) | **Current Level:** 3 | [4](./capstone-lv-4.md) | [5](./capstone-lv-5.md) | [6](./capstone-lv-6.md) | [7](./capstone-lv-7.md) | [8](./capstone-lv-8.md) | [9](./capstone-lv-9.md) | [10](./capstone-lv-10.md) | [11](./capstone-lv-11.md) | [12](./capstone-lv-12.md) | [13](./capstone-lv-13.md) | [14](./capstone-lv-14.md) | [15](./capstone-lv-15.md) | [16](./capstone-lv-16.md) | [17](./capstone-lv-17.md) | [18](./capstone-lv-18.md) | [19](./capstone-lv-19.md) | [20](./capstone-lv-20.md) | [21](./capstone-lv-21.md) | [22](./capstone-lv-22.md) | [23](./capstone-lv-23.md) | [24](./capstone-lv-24.md) | [25](./capstone-lv-25.md) | [26](./capstone-lv-26.md) | [27](./capstone-lv-27.md) | [28](./capstone-lv-28.md) | [29](./capstone-lv-29.md) | [30](./capstone-lv-30.md) | [31](./capstone-lv-31.md) | [32](./capstone-lv-32.md) | [33](./capstone-lv-33.md) | [34](./capstone-lv-34.md)
