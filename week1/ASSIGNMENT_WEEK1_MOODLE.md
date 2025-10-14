# Week 1 Assignment: Mad Libs Web Application

## 📋 Overview
Build an interactive Mad Libs web application using Node.js, Express, and Bootstrap. Create forms that collect user input and generate funny stories!

**Due:** [Insert Date]  
**Points:** [Insert Points]

---

## 🎯 Learning Objectives

By completing this assignment, you will:
- Set up a Node.js project with Express
- Create HTML forms and process user input
- Use template literals to generate dynamic content
- Style web pages with Bootstrap CSS
- Serve static files with an Express server

---

## 📚 Required Resources

**Full Guides:**
- [Complete Activity Guide](./mad-libs-mini-project-activity-guide.md) - Planning templates, rubric, examples
- [Detailed Class Activity Guide](./ASSIGNMENT_WEEK1.md) - Step-by-step demos and code examples
- [Level-by-Level Instructions](../mad-libs-levels/) - Guided progression through 20 levels

**External Resources:**
- [Code.org Mad Libs Model](https://studio.code.org/courses/csp5-virtual/units/1/lessons/7/levels/1)
- [Express.js Documentation](https://expressjs.com/)
- [Bootstrap 5 Documentation](https://getbootstrap.com/)

---

## ✅ Required Features (Minimum for Full Credit)

Your Mad Libs application must include:

1. **Express Server Setup**
   - Node.js project initialized with `package.json`
   - Express server running on port 3000
   - Static file serving configured

2. **HTML Form**
   - Form collects at least 5 different word types (noun, verb, adjective, etc.)
   - All inputs properly labeled with `name` attributes
   - Form submits to `/story` route

3. **Story Generation**
   - Server processes form data using `req.query`
   - Template literals create dynamic story
   - At least one complete, creative story template

4. **Bootstrap Styling**
   - Bootstrap CSS included via CDN
   - Professional appearance on both form and story pages
   - Responsive design (works on mobile)

5. **Documentation**
   - README.md with setup instructions
   - Code comments explaining key sections

---

## 🚀 Getting Started

### Initial Setup (Complete Levels 1-2)
```bash
# Create project
mkdir mad-libs-project
cd mad-libs-project

# Initialize and install dependencies
npm init -y
npm install express
npm install --save-dev nodemon

# Create file structure
touch server.js
mkdir public
touch public/mad-libs-form.html
```

### Development Workflow
```bash
# Start server with auto-reload
npm run dev

# View in browser
# http://localhost:3000
```

---

## 📝 Assignment Tasks

### Core Tasks (Required - Levels 1-9)
Complete these levels for minimum requirements:

- [ ] **Level 1-2:** Project setup and basic Express server
- [ ] **Level 3:** Create HTML form with inputs
- [ ] **Level 4:** Process form data and generate story
- [ ] **Level 5:** Add Bootstrap styling
- [ ] **Level 6:** Use template literals effectively
- [ ] **Level 7:** Create multiple story templates (at least 2)
- [ ] **Level 8:** Add story selection feature
- [ ] **Level 9:** Polish user experience

### Challenge Tasks (Optional - Levels 10-14) ⚡
For extra credit or advanced learning:

- [ ] **Level 10:** Store stories in memory
- [ ] **Level 11:** Display all saved stories
- [ ] **Level 12:** Random story selection
- [ ] **Level 13:** Delete stories
- [ ] **Level 14:** Advanced array operations

### Final Tasks (Required - Levels 15-20)
- [ ] **Level 15:** Testing and debugging
- [ ] **Level 16:** Write comprehensive README
- [ ] **Level 17:** Code cleanup and organization
- [ ] **Level 19:** Git commits with clear messages
- [ ] **Level 20:** Final reflection

---

## 💡 Story Template Examples

**Example 1: School Day**
```
Today at [place], my [adjective] teacher asked us to [verb] our [plural noun].
I was so [emotion] that I accidentally [past tense verb] my [noun]!
```

**Example 2: Adventure**
```
Deep in the [adjective] jungle, I discovered a [adjective] [noun].
It could [verb] faster than [number] [plural noun]!
```

See the [Activity Guide](./mad-libs-mini-project-activity-guide.md) for more examples and inspiration!

---

## 🎓 Submission Requirements

### What to Submit:

1. **GitHub Repository URL** containing:
   - All source code files
   - README.md with setup instructions
   - Clear commit history
   
2. **README.md must include:**
   - Project title and description
   - Setup instructions (how to install and run)
   - List of features implemented
   - Your story themes
   - Any challenges faced and solved
   - Screenshots (optional but recommended)

3. **Code Requirements:**
   - Clean, readable code
   - Meaningful variable names
   - Comments explaining key sections
   - No errors or warnings

---

## 📊 Grading Rubric (Summary)

| Category | Points | Criteria |
|----------|--------|----------|
| **Server Setup** | 15% | Express server configured correctly, runs without errors |
| **Form & Routes** | 20% | HTML form created, routes work, data flows correctly |
| **Story Generation** | 20% | Template literals used, stories generate dynamically |
| **Bootstrap Styling** | 15% | Professional appearance, responsive design |
| **Multiple Templates** | 10% | At least 2 story templates with selection |
| **Code Quality** | 10% | Clean code, good naming, helpful comments |
| **Documentation** | 10% | Complete README with instructions |
| **Challenge Features** | +10% | Extra credit for advanced features (Levels 10-14) |

**Total:** 100% (+ up to 10% extra credit)

[View detailed rubric in Activity Guide](./mad-libs-mini-project-activity-guide.md#step-7---submit)

---

## 🆘 Getting Help

**If you get stuck:**

1. Check the [Detailed Activity Guide](./ASSIGNMENT_WEEK1.md) troubleshooting section
2. Use `console.log()` to debug variables
3. Check browser console (F12) for errors
4. Review the level-by-level guides
5. Ask in class or office hours
6. Post questions in the discussion forum

**Common Issues:**
- **Port 3000 in use:** Change to `PORT = 3001`
- **Cannot GET /:** Check `app.use(express.static('public'))`
- **Form data missing:** Verify input `name` attributes match `req.query` usage
- **Styles not loading:** Hard refresh browser (Cmd+Shift+R)

---

## ⏰ Recommended Timeline

**Session 1 (2 hours):** 
- Project setup and basic server (Levels 1-2)
- Create form and test submission (Levels 3-4)

**Session 2 (2 hours):**
- Add Bootstrap styling (Level 5)
- Create story templates (Levels 6-7)

**Session 3 (2 hours):**
- Add multiple templates (Level 8)
- Polish and test (Level 9, 15)

**Session 4 (1-2 hours):**
- Documentation and cleanup (Levels 16-17)
- Git commits and submission (Levels 19-20)
- Optional: Challenge features (Levels 10-14)

---

## 🎯 Success Checklist

Before submitting, verify:

- [ ] Server starts with `npm run dev` without errors
- [ ] Form displays and collects all required inputs
- [ ] Story generates correctly with user's words
- [ ] Bootstrap styling looks professional
- [ ] At least 2 different story templates work
- [ ] README includes setup instructions
- [ ] Code is clean with helpful comments
- [ ] GitHub repository is public and accessible
- [ ] All files committed with clear messages

---

## 📅 Important Dates

- **Start Date:** [Insert Date]
- **Due Date:** [Insert Date]
- **Late Deadline:** [Insert Date] (with penalty)
- **No submissions accepted after:** [Insert Date]

---

## 🌟 Tips for Success

- **Start early** - Don't wait until the last minute
- **Test frequently** - Run your server after each change
- **Commit often** - Save your progress with Git
- **Be creative** - Make funny, unique story templates
- **Read error messages** - They often tell you exactly what's wrong
- **Use the resources** - The guides have all the code you need

---

## 📞 Questions?

Post in the discussion forum or ask during class/office hours.

**Good luck and have fun creating silly stories!** 🎭📖

---

*This assignment adapted from Code.org's Mad Libs activity for web development education.*

