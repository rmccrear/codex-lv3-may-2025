# Week 1 Assignment: Mad Libs Web Application

Build an interactive Mad Libs web application using Node.js, Express, and Bootstrap where users fill out a form and see a funny story generated with their words.

---

## 📚 Instructions

**📖 Start Here:** [Level 1 - Project Setup](https://rmccrear.github.io/codex-lv3-may-2025/mad-libs-levels/mad-libs-lv-1.html)

Follow the level-by-level instructions (Levels 1-20) to build your Mad Libs application. Each level includes detailed steps, code hints, and checkpoints.

**Additional Resources:**
- [Code.org Mad Libs Model](https://studio.code.org/courses/csp5-virtual/units/1/lessons/7/levels/1) - Try the original game
- [Express.js Documentation](https://expressjs.com/)
- [Bootstrap 5 Documentation](https://getbootstrap.com/)

---

## ✅ Requirements

Your Mad Libs application must include:

1. **Express Server**
   - Running on port 3000
   - Serves static files from `public/` folder
   - Handles form submissions via routes

2. **HTML Form**
   - Collects at least 5 word types (noun, verb, adjective, place, number)
   - All inputs have proper `name` attributes
   - Submits to `/story` route

3. **Story Generation**
   - Processes form data using `req.query`
   - Uses template literals to generate dynamic stories
   - At least 2 different story templates

4. **Bootstrap Styling**
   - Professional appearance
   - Responsive design
   - Applied to both form and story pages

5. **Code Quality**
   - Clean, readable code
   - Comments explaining key sections
   - Meaningful variable names

6. **Documentation**
   - README.md with setup instructions
   - List of features implemented
   - Description of story themes

---

## 📊 Grading Rubric

| Category | Weight | Description |
|----------|--------|-------------|
| **Server Setup & Routes** | 35% | Express configured, static files served, routes work correctly |
| **Story Generation** | 20% | Template literals used properly, dynamic content generates |
| **Bootstrap Styling** | 15% | Professional appearance, responsive, good UX |
| **Multiple Templates** | 10% | At least 2 story templates with selection |
| **Code Quality** | 10% | Clean code, good naming, helpful comments |
| **Documentation** | 10% | Complete README with clear instructions |
| **Challenge Features** | +10% | Extra credit: story storage, display all, delete (Levels 10-14) |

**Total:** 100% (+ up to 10% extra credit)

---

## 🎓 Deliverable

**Submit:** GitHub repository URL containing:
- All source code (`server.js`, HTML files, etc.)
- `README.md` with:
  - Project title and description
  - Setup instructions (`npm install`, `npm run dev`)
  - Features list
  - Story themes
  - Any challenges faced
- Clear Git commit history

**Before submitting, verify:**
- [ ] Server starts with `npm run dev` without errors
- [ ] Form collects input and generates stories
- [ ] Bootstrap styling looks professional
- [ ] At least 1 story template works
- [ ] README is complete
- [ ] Code is commented and clean

---

## 📝 Assignment Structure

**Core Levels (Required):**
- Levels 1-9: Setup, form creation, story generation, Bootstrap styling
- Levels 15-17: Testing, documentation, code cleanup
- Levels 19-20: Git commits and reflection

**Challenge Levels (Optional +10%):**
- Levels 10-14: Store stories, display all stories, delete features

---

## 🆘 Need Help?

- Review the level instructions carefully
- Check browser console (F12) for errors
- Use `console.log()` to debug on the console in VSCode
- Post questions in the discussion forum

---

**Good luck and have fun creating silly stories!** 🎭📖

---

*This assignment is adapted from Code.org's Mad Libs activity for web development education.*
