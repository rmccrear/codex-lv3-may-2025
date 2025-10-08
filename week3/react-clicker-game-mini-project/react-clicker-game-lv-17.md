Level Navigation: [1](./react-clicker-game-lv-1.md) | [2](./react-clicker-game-lv-2.md) | [3](./react-clicker-game-lv-3.md) | [4](./react-clicker-game-lv-4.md) | [5](./react-clicker-game-lv-5.md) | [6](./react-clicker-game-lv-6.md) | [7](./react-clicker-game-lv-7.md) | [8](./react-clicker-game-lv-8.md) | [9](./react-clicker-game-lv-9.md) | [10](./react-clicker-game-lv-10.md) | [11](./react-clicker-game-lv-11.md) | [12](./react-clicker-game-lv-12.md) | [13](./react-clicker-game-lv-13.md) | [14](./react-clicker-game-lv-14.md) | [15](./react-clicker-game-lv-15.md) | [16](./react-clicker-game-lv-16.md) | **17** | [18⚡](./react-clicker-game-lv-18.md) | [19](./react-clicker-game-lv-19.md)

# Level 17: Git History and Commits

**User Story:** As a developer, I want to have a clean git history so that I can track my progress and share my work.

## What You'll Do

Initialize git and create meaningful commits (if you haven't already).

## Instructions

If starting fresh with git:
- Initialize git repository: `git init`
- Create a `.gitignore` file (Vite creates one automatically)
- Stage all files: `git add .`
- Create initial commit: `git commit -m "Initial commit: Complete Apple Clicker game"`

If tracking changes incrementally (recommended approach):
- Make small commits after each level
- Use descriptive commit messages
- Each commit should represent one feature

## 💡 Code Hints

Need help with git? Check out these commands:

**Initialize and first commit:**
```bash
git init
git add .
git commit -m "Initial commit"
```

**Recommended commit sequence:**
```bash
git add .
git commit -m "feat: add project setup with Vite and React"
git commit -m "feat: clean up starter code"
git commit -m "feat: add game images"
git commit -m "feat: create game board structure"
git commit -m "feat: add score tracking"
git commit -m "feat: add lives tracking"
git commit -m "feat: add random apple size"
git commit -m "feat: add random apple position"
git commit -m "feat: add dynamic stats styling"
git commit -m "feat: add win condition message"
git commit -m "feat: hide apple on win"
```

**Push to GitHub:**
```bash
git remote add origin <your-github-url>
git branch -M main
git push -u origin main
```

## ✅ Check

1. Run `git log --oneline` to see your commits
2. Verify commit messages are descriptive
3. Check that sensitive files are in `.gitignore`
4. Verify `node_modules/` is not committed
5. If pushing to GitHub, verify remote is set up

---