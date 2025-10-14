# Week 1 Assignment: Mad Libs Web Application

Build an interactive Mad Libs web application using Node.js, Express, and Bootstrap.

## 🎯 What You'll Build

A web app where users fill out a form and see a funny story generated with their words.

## 📚 Instructions

**📖 Start:** [Level 1 - Project Setup](https://rmccrear.github.io/codex-lv3-may-2025/mad-libs-levels/mad-libs-lv-1.html)

**Guides:** [Activity Guide](./mad-libs-mini-project-activity-guide.md) | [Class Guide](./ASSIGNMENT_WEEK1.md)

**Docs:** [Express](https://expressjs.com/) | [Bootstrap](https://getbootstrap.com/) | [Code.org Model](https://studio.code.org/courses/csp5-virtual/units/1/lessons/7/levels/1)

---

## ✅ Requirements (Minimum for Full Credit)

**Technical:**
- ✅ Express server running on port 3000
- ✅ HTML form with 5+ input fields
- ✅ Server processes form data via `req.query`
- ✅ Template literals generate dynamic story
- ✅ Bootstrap CSS styling
- ✅ At least 2 story templates

**Code Quality:**
- ✅ README with setup instructions
- ✅ Clean code with comments
- ✅ Git commits with clear messages

---

## 🚀 Quick Start

```bash
# Setup
mkdir mad-libs-project && cd mad-libs-project
npm init -y
npm install express
npm install --save-dev nodemon

# Create files
touch server.js
mkdir public && touch public/mad-libs-form.html

# Run
npm run dev
```

**Then follow:** [Level-by-Level Instructions](https://rmccrear.github.io/codex-lv3-may-2025/mad-libs-levels/mad-libs-lv-1.html)

---

## 📝 Assignment Levels

**Core (Required):**
- Levels 1-9: Setup, form, story generation, styling
- Levels 15-17: Testing, README, code cleanup
- Levels 19-20: Git commits, reflection

**Challenge (Extra Credit):**
- Levels 10-14: Story storage, display all stories, delete features

---

## 📊 Grading

| Category | Weight |
|----------|--------|
| Server Setup & Routes | 35% |
| Story Generation (template literals) | 20% |
| Bootstrap Styling | 15% |
| Multiple Templates | 10% |
| Code Quality & Comments | 10% |
| Documentation (README) | 10% |
| **Challenge Features** | **+10%** |

---

## 🎓 Submission

**Submit:** GitHub repository URL with complete README (setup instructions, features, story themes)

**Verify:**
- [ ] Server runs without errors
- [ ] 2+ story templates work
- [ ] Bootstrap styling applied
- [ ] Code commented

---

## 💡 Example Story Template

```
Today at [place], my [adjective] teacher asked us to [verb] our [plural noun].
I was so [emotion] that I accidentally [past tense verb] my [noun]!
```

See Activity Guide for more examples!

---

## 🆘 Common Issues

- **Port in use:** Change to `PORT = 3001`
- **Cannot GET /:** Add `app.use(express.static('public'))`
- **No data:** Check input `name` attributes match `req.query`
- **Styles missing:** Hard refresh (Cmd+Shift+R)

**Need Help?** Check troubleshooting in [Detailed Guide](./ASSIGNMENT_WEEK1.md) or post in forum.

---

## ⏰ Timeline

Session 1: Levels 1-4 | Session 2: Levels 5-7 | Session 3: Levels 8-9, 15 | Session 4: Levels 16-20

**Tips:** Start early, test frequently, commit often, be creative!

---

**Good luck and have fun!** 🎭

*Adapted from Code.org's Mad Libs activity*
