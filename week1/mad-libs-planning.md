# Mad Libs Mini-Project Planning Guide

## Project Overview

**Mad Libs** is a game where you fill in the blanks of a story with random words (like nouns, verbs, and adjectives) without knowing the context. The result is usually a funny and nonsensical story!

This project guides students through building a full-stack web application that creates Mad Libs stories. Students will create a form-based web app using Node.js, Express, and Bootstrap.

## Learning Objectives

By completing this project, students will be able to:

### Technical Skills
- Set up a Node.js project with Express.js
- Create and serve HTML forms
- Handle form data using query parameters and POST requests
- Use template literals to generate dynamic HTML content
- Implement array operations for data storage and retrieval
- Generate random numbers and access array elements randomly
- Style web applications using Bootstrap framework
- Implement routing and navigation patterns
- Handle errors and validate user input

### Computer Science Concepts
- **Client-Server Architecture**: Understanding how browsers communicate with servers
- **HTTP Methods**: GET vs POST requests
- **Data Structures**: Working with arrays and objects
- **Algorithms**: Random selection and list manipulation
- **String Manipulation**: Template literals and dynamic content generation
- **Control Flow**: Conditionals and loops
- **State Management**: Storing and retrieving data

## Project Structure

The project is divided into **20 progressive levels**, organized into four phases:

### Phase 1: Foundation (Levels 1-5)
**Estimated Time**: 2-3 class periods

- **Level 1**: Project setup and planning
- **Level 2**: Basic Express server setup
- **Level 3**: Creating HTML forms
- **Level 4**: Processing form data
- **Level 5**: Bootstrap styling

**Milestone**: Students have a working form that collects user input and displays a basic Mad Libs story.

### Phase 2: Core Features (Levels 6-9)
**Estimated Time**: 2-3 class periods

- **Level 6**: Template literals for story generation
- **Level 7**: Multiple story templates
- **Level 8**: Dynamic story selection
- **Level 9**: Enhanced user experience

**Milestone**: Students have a fully functional Mad Libs generator with multiple story templates.

### Phase 3: Challenge Features (Levels 10-14) ⚡
**Estimated Time**: 2-4 class periods
**Note**: These are optional challenge levels for advanced students

- **Level 10**: Data storage in memory ⚡
- **Level 11**: Display all saved stories ⚡
- **Level 12**: Random story selection ⚡
- **Level 13**: Story deletion feature ⚡
- **Level 14**: Advanced array operations ⚡

**Milestone**: Students have implemented data persistence and advanced features.

### Phase 4: Polish & Deployment (Levels 15-20)
**Estimated Time**: 2-3 class periods

- **Level 15**: Final testing and polish
- **Level 16**: README documentation
- **Level 17**: Code organization and cleanup
- **Level 18**: Additional enhancements ⚡
- **Level 19**: Git and version control
- **Level 20**: Project completion and reflection

**Milestone**: Students have a polished, documented, and version-controlled project.

## Technical Requirements

### Required Software
- **Node.js** (version 14 or higher)
- **npm** (comes with Node.js)
- **Text Editor** (VS Code recommended)
- **Web Browser** (Chrome, Firefox, Safari, or Edge)
- **Git** (for version control in later levels)

### Required npm Packages
- `express` - Web application framework
- `nodemon` - Development tool for auto-restarting server (dev dependency)

### File Structure
```
mad-libs-project/
├── server.js              # Main server file
├── package.json           # Project dependencies
├── package-lock.json      # Dependency lock file
├── README.md              # Project documentation
├── public/
│   ├── mad-libs-form.html # Main form page
│   └── styles.css         # Optional custom styles
└── node_modules/          # Installed dependencies
```

## Teaching Strategies

### Scaffolding Approach
The levels use progressive disclosure:
1. **Initial levels** provide more guidance with "Show Me" code snippets
2. **Middle levels** provide hints and references but less complete code
3. **Later levels** encourage independent problem-solving
4. **Challenge levels** (⚡) require synthesis of multiple concepts

### Differentiation

**For Students Who Need Support**:
- Focus on Levels 1-9 (core functionality)
- Use the "Show Me" code snippets liberally
- Pair programming with stronger students
- Extended time for completion
- One-on-one guidance during lab time

**For Advanced Students**:
- Complete all 20 levels including challenges
- Attempt challenge levels (⚡) without looking at hints
- Create additional story templates
- Add custom features (styling, animations, additional form fields)
- Help other students debug their code

### Pacing Suggestions

#### Option 1: 2-Week Mini-Project (10 class periods)
- **Week 1**: Levels 1-9 (Foundation + Core Features)
- **Week 2**: Levels 15-20 (Polish + Documentation)
- **Optional**: Challenge levels for homework or advanced students

#### Option 2: 3-Week Full Project (15 class periods)
- **Week 1**: Levels 1-5 (Foundation)
- **Week 2**: Levels 6-14 (Core + Challenges)
- **Week 3**: Levels 15-20 (Polish + Deployment)

#### Option 3: Intensive 1-Week Sprint (5 class periods)
- **Day 1**: Levels 1-3
- **Day 2**: Levels 4-6
- **Day 3**: Levels 7-9
- **Day 4**: Levels 15-17
- **Day 5**: Levels 19-20

## Assessment Criteria

### Minimum Viable Product (Levels 1-9)
Students should demonstrate:
- ✅ Working Express server on localhost:3000
- ✅ HTML form that collects user input
- ✅ Form data processing and display
- ✅ At least one complete Mad Libs story
- ✅ Basic Bootstrap styling
- ✅ Clean, organized code

### Proficient (Levels 1-9 + Polish)
All MVP requirements plus:
- ✅ Multiple story templates
- ✅ Professional Bootstrap styling
- ✅ Error handling for missing inputs
- ✅ Clear navigation between pages
- ✅ Complete README documentation
- ✅ Git version control

### Advanced (Levels 1-20)
All Proficient requirements plus:
- ✅ Data storage and retrieval
- ✅ Random story selection
- ✅ Story management (view all, delete)
- ✅ Advanced features and polish
- ✅ Custom enhancements
- ✅ Comprehensive documentation

## Common Challenges & Solutions

### Challenge 1: Port Already in Use
**Symptom**: Error message "Port 3000 is already in use"
**Solution**: 
- Stop other servers running on port 3000
- Or change the port number in server.js

### Challenge 2: Cannot GET /
**Symptom**: Browser shows "Cannot GET /" error
**Solution**:
- Verify server is running (`npx nodemon server.js`)
- Check that routes are defined correctly
- Ensure `express.static('public')` is configured

### Challenge 3: Form Data Not Showing
**Symptom**: Submitted form doesn't display user input
**Solution**:
- Check that form `name` attributes match query parameter names
- Verify template literals use correct variable names
- Use `console.log(req.query)` to debug

### Challenge 4: Bootstrap Styles Not Applying
**Symptom**: Page looks unstyled
**Solution**:
- Verify Bootstrap CDN link is in HTML `<head>`
- Check that class names are spelled correctly
- Clear browser cache and reload

## Resources & References

### Official Documentation
- [Express.js Documentation](https://expressjs.com/)
- [Node.js Documentation](https://nodejs.org/)
- [Bootstrap 5 Documentation](https://getbootstrap.com/)
- [MDN Web Docs](https://developer.mozilla.org/)

### Code.org Alignment
This project reinforces patterns from Code.org CSP:
- **Random List Access Pattern**: Used in challenge levels
- **List Scrolling Pattern**: Used in story navigation
- **Template Strings**: Used for dynamic content generation

### Additional Practice
- Try Mad Libs at: [Code.org Mad Libs Activity](https://studio.code.org/courses/csp5-virtual/units/1/lessons/7/levels/1)
- Explore similar projects in the `week3/` and `week4/` directories

## Extension Ideas

For students who finish early or want to go beyond:

### Creative Extensions
- Add images or GIFs to story results
- Create themed story categories (adventure, sci-fi, romance)
- Add sound effects or music
- Create printable versions of stories

### Technical Extensions
- Implement a database for persistent storage
- Add user accounts and login
- Create an API for story generation
- Add a "share story" feature with unique URLs
- Implement story ratings or favorites

### Design Extensions
- Create custom CSS themes
- Add animations and transitions
- Make the site fully responsive
- Create a mobile app version

## Tips for Success

### For Teachers
1. **Demo first**: Show a completed version before students start
2. **Check early**: Review Level 2 completion for all students before moving on
3. **Debug together**: Use student bugs as teaching moments
4. **Celebrate progress**: Acknowledge completion of each phase
5. **Share stories**: Have students share their funniest Mad Libs results

### For Students
1. **Read carefully**: Each level builds on the previous one
2. **Test frequently**: Run your server after each level
3. **Use hints wisely**: Try on your own first, then use "Show Me" if stuck
4. **Console.log everything**: Debug by logging variables
5. **Have fun**: The stories are meant to be silly and entertaining!

## Quick Start Checklist

Before starting Level 1, ensure students have:
- [ ] Node.js installed (`node --version` to check)
- [ ] npm installed (`npm --version` to check)
- [ ] VS Code or preferred text editor
- [ ] Terminal/command line access
- [ ] Web browser
- [ ] Created a workspace folder for their project

## Project Timeline Template

### Week 1: Foundation
- [ ] **Day 1**: Levels 1-2 (Setup & Express)
- [ ] **Day 2**: Levels 3-4 (Forms & Processing)
- [ ] **Day 3**: Level 5 (Styling)
- [ ] **Day 4**: Levels 6-7 (Template Literals)
- [ ] **Day 5**: Levels 8-9 (Multiple Stories)

### Week 2: Extensions & Polish
- [ ] **Day 1**: Challenge Levels (10-12)
- [ ] **Day 2**: Challenge Levels (13-14)
- [ ] **Day 3**: Testing & Documentation (15-16)
- [ ] **Day 4**: Cleanup & Enhancement (17-18)
- [ ] **Day 5**: Version Control & Completion (19-20)

## Support & Help

### When Students Get Stuck
1. Check the ✅ Check section in each level
2. Review the 💡 Code Hints
3. Use the "Show Me" expandable sections
4. Consult the Resources section in Level 20
5. Ask a classmate or teacher for help

### Getting Help
- Review previous week's notes in `/notes/`
- Check example projects in `/week2/` and `/week3/`
- Use console.log() to debug
- Test one feature at a time
- Take breaks and come back with fresh eyes

---

## Ready to Start?

Begin with [Level 1: Project Setup & Planning](./mad-libs-levels/mad-libs-lv-1.md)

**Remember**: Building software is a journey. Take it one level at a time, test frequently, and don't be afraid to make mistakes. That's how we learn!

---

*Last Updated: October 2025*


