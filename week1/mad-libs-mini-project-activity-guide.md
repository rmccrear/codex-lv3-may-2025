Name(s)\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Period \_\_\_\_\_\_ Date \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

|  | Activity Guide - Mad Libs Mini-Project | 📝 |
| :---- | :---- | :---- |

**Overview**  
Build a full-stack web application that generates funny Mad Libs stories! Create a form-based app using Node.js, Express, and Bootstrap where users fill in words to create hilarious stories.

**Model:** [Code.org Mad Libs Activity](https://studio.code.org/courses/csp5-virtual/units/1/lessons/7/levels/1)

---

## Step 1 - Play the Model Game

Try the Code.org Mad Libs activity linked above. Play for 5-10 minutes and create at least 2-3 stories.

**Discuss with a Partner:**
- How does a Mad Libs game work?
- What types of words are you asked to provide?
- What makes the resulting stories funny?
- How does the form collect and display information?

---

## Step 2 - Plan Your Mad Libs Story

**Story Template:** Choose a theme and create your first Mad Libs template.

| Theme Ideas |
| :---- |
| Adventure story |
| School day |
| Vacation trip |
| Cooking disaster |
| Superhero origin |
| Your own idea: _________________ |

**Word Types Needed:** Plan what types of words your story will need.

| Word Type | Example | How Many? |
| :---- | :---- | :---: |
| Noun | "elephant" | 2-3 |
| Verb | "dancing" | 2-3 |
| Adjective | "sparkly" | 2-3 |
| Place | "cafeteria" | 1-2 |
| Number | "42" | 1 |

**Write Your Template:** Draft your story with blanks. 

**Example Templates to Inspire You:**

**Template 1: The School Day**
```
Today at [place], my [adjective] teacher asked us to [verb] our [plural noun].
I was so [emotion] that I accidentally [past tense verb] my [noun]! 
The whole class [past tense verb] for [number] minutes straight.
```

**Template 2: The Epic Adventure**
```
Deep in the [adjective] jungle, I discovered a [adjective] [noun]. 
It could [verb] faster than [number] [plural noun]! I decided to 
[verb] it all the way to [place], where I became [adjective] and famous.
```

**Template 3: The Cooking Disaster**
```
My recipe for [adjective] [food item] is simple: First, [verb] 
[number] cups of [plural noun]. Then [adverb] mix in a [adjective] 
[noun]. Bake at [number] degrees until it starts to [verb]. 
Chef [celebrity name] would be so [emotion]!
```

**Template 4: The Superhero Origin**
```
I was just a [adjective] student until I was bitten by a radioactive 
[noun]. Now I can [verb] and [verb] at the speed of [number]! 
My superhero name is [adjective] [noun]-person, and I fight crime in [place].
```

**💡 Pro Tips for Creating Templates:**
- Use 5-8 blanks for a good length story
- Mix different word types (nouns, verbs, adjectives)
- Leave the context mysterious so words are surprising
- The funnier/weirder the scenario, the better!
- Don't be afraid to be creative and silly

**✏️ Your Turn:** Write your own template below (or modify one above to make it yours!)

---

## Step 3 - Plan Your Routes

**Server Routes:** Your Express server will need these routes.

| Route Path | Method | What It Does |
| :---- | :---: | :---- |
| `/` | GET | Serves the main form page |
| `/story` | GET | Displays the completed story |
| `/all-stories` | GET | Shows all saved stories (challenge) |
|  |  |  |

**Form Data Flow:**
1. User fills out form with words
2. User submits form
3. Server receives data
4. Server generates story with template literals
5. Server sends back completed story

---

## Step 4 - Setup Your Project

**Prerequisites Checklist:**
- [ ] Node.js installed (run `node --version` to check)
- [ ] npm installed (run `npm --version` to check)
- [ ] VS Code or text editor ready
- [ ] Terminal/command line access
- [ ] Web browser

**Create Your Project:**
1. Create a new folder: `mkdir mad-libs-project`
2. Navigate to it: `cd mad-libs-project`
3. Initialize npm: `npm init -y`
4. Install Express: `npm install express`
5. Install nodemon (dev tool): `npm install --save-dev nodemon`
6. Create files:
   - `server.js` (your main server file)
   - `public/mad-libs-form.html` (your form page)
7. Update `package.json` scripts:
   ```json
   "scripts": {
     "start": "node server.js",
     "dev": "npx nodemon server.js"
   }
   ```

**Test Your Setup:**
- Run `npm run dev` in terminal
- You should see "Server running on port 3000" (after you complete Level 2)

---

## Step 5 - Build Your Mad Libs App

Follow the level-by-level guide to build your app. Complete each level before moving to the next.

**Phase 1: Foundation (Levels 1-5)**
- ✅ Level 1: Project setup and planning
- ✅ Level 2: Basic Express server setup
- ✅ Level 3: Creating HTML forms
- ✅ Level 4: Processing form data
- ✅ Level 5: Bootstrap styling

**Milestone:** You should have a working form that creates a basic Mad Libs story.

**Phase 2: Core Features (Levels 6-9)**
- ✅ Level 6: Template literals for story generation
- ✅ Level 7: Multiple story templates
- ✅ Level 8: Dynamic story selection
- ✅ Level 9: Enhanced user experience

**Milestone:** You should have multiple story templates that users can choose from.

**Phase 3: Challenge Features (Levels 10-14) ⚡**
*Optional - for advanced students or extra credit*
- ⚡ Level 10: Data storage in memory
- ⚡ Level 11: Display all saved stories
- ⚡ Level 12: Random story selection
- ⚡ Level 13: Story deletion feature
- ⚡ Level 14: Advanced array operations

**Milestone:** You should have data persistence and story management features.

**Phase 4: Polish & Deployment (Levels 15-20)**
- ✅ Level 15: Final testing and polish
- ✅ Level 16: README documentation
- ✅ Level 17: Code organization and cleanup
- ⚡ Level 18: Additional enhancements
- ✅ Level 19: Git and version control
- ✅ Level 20: Project completion and reflection

**Milestone:** You should have a polished, documented, and version-controlled project.

**As You Code:**
- Test your server after each level (`npm run dev`)
- Use `console.log()` to debug variables
- Check browser console (F12) for errors
- Commit your code after major features
- Read error messages carefully

---

## Step 6 - Test Your Application

Verify your Mad Libs app works correctly:

| Test | What to Check | ✓ |
| :---- | :---- | :---: |
| Server starts | No errors, listens on port 3000 |  |
| Form loads | HTML form displays correctly at `/` |  |
| Form submission | Clicking submit shows story page |  |
| Story displays | User's words appear in the story |  |
| Bootstrap styles | Page looks professional and styled |  |
| Multiple stories | Can select different story templates |  |
| Missing inputs | Handles empty form fields gracefully |  |

**Debug Common Issues:**

| Problem | Solution |
| :---- | :---- |
| "Cannot GET /" error | Make sure `express.static('public')` is set up |
| Port 3000 in use | Stop other servers or change port number |
| Words don't show | Check form `name` attributes match `req.query` |
| Styles not working | Verify Bootstrap CDN link in HTML `<head>` |

---

## Step 7 - Submit

Before you submit, check the rubric below to make sure your project meets the requirements.

| Category | Extensive Evidence | Convincing Evidence | Limited Evidence | No Evidence |
| :---- | :---- | :---- | :---- | :---- |
| **Server Setup** | Express server set up correctly, runs without errors, uses proper middleware. | Server mostly works but has minor issues. | Server has significant problems. | Server doesn't run. |
| **Form & Routes** | HTML form created with proper inputs; GET/POST routes work correctly; navigation is clear. | Most routes work but some have issues. | Some routes work but many have problems. | Routes not implemented or broken. |
| **Data Processing** | Form data properly captured using `req.query` or `req.body`; template literals generate stories correctly. | Data mostly processes but has some issues. | Data processing partially works. | Data processing doesn't work. |
| **Bootstrap Styling** | Professional styling with Bootstrap; responsive design; clear visual hierarchy. | Good styling but lacks some polish. | Basic styling with issues. | No styling or broken styles. |
| **Multiple Templates** | At least 2-3 story templates; user can select which one to use. | Has multiple templates but selection has issues. | Only one template or selection broken. | No multiple templates. |
| **Error Handling** | Handles missing inputs gracefully; provides user feedback; no crashes. | Some error handling but incomplete. | Minimal error handling. | No error handling. |
| **Code Quality** | Clean, readable code; good variable names; helpful comments; organized file structure. | Code mostly readable with some comments. | Code is hard to follow. | Code is messy and unclear. |
| **Documentation** | Complete README with setup instructions, features list, and how to use. | README exists but missing some details. | Minimal README. | No README. |

**Minimum Requirements for Full Credit:**
- Express server runs on localhost:3000
- HTML form collects at least 5 user inputs
- Form data displays in a Mad Libs story
- At least one complete story template works
- Bootstrap styling applied
- README with setup instructions
- Clean, organized code

**Bonus/Extra Credit (Challenge Levels):**
- Story storage and retrieval
- Display all saved stories
- Random story selection
- Story deletion feature
- Custom enhancements and polish

---

## Step 8 - Reflection

Answer the following questions about your project:

**1. Server-Side Concepts:**  
Explain how your Express server works. What happens when a user submits the form?

|  |
| :---- |
|  |
|  |

**2. Template Literals:**  
Describe how you used template literals (backticks) to generate your Mad Libs story. Show an example.

|  |
| :---- |
|  |
|  |

**3. GET vs POST:**  
What's the difference between GET and POST requests? Which did you use and why?

|  |
| :---- |
|  |
|  |

**4. Bootstrap Framework:**  
How did Bootstrap help improve your application? Name at least 2 specific components or classes you used.

|  |
| :---- |
|  |
|  |

**5. Debugging Experience:**  
What was the most challenging part of this project? How did you solve it?

|  |
| :---- |
|  |
|  |

**6. Creative Choices:**  
What story themes did you create? What made them funny or interesting?

|  |
| :---- |
|  |
|  |

---

## Vocabulary Review

Match the term with its definition:

| Term | Definition |
| :---- | :---- |
| **Express.js** | Web application framework for Node.js |
| **Route** | URL path that maps to specific server functionality |
| **Middleware** | Functions that process requests before they reach routes |
| **Template Literal** | String syntax using backticks that allows embedded expressions |
| **Query Parameters** | Data sent in URL after `?` symbol (e.g., `?name=John`) |
| **CDN** | Content Delivery Network for loading libraries like Bootstrap |
| **GET Request** | HTTP method for retrieving/displaying data |
| **POST Request** | HTTP method for sending/submitting data |

---

## Resources

**Documentation:**
- Express.js: https://expressjs.com/
- Node.js: https://nodejs.org/
- Bootstrap 5: https://getbootstrap.com/
- MDN JavaScript: https://developer.mozilla.org/

**Tools:**
- Nodemon (auto-restart server on changes)
- Browser DevTools (F12) for debugging
- VS Code extensions: ES7 snippets

**Code.org Connection:**
- Random List Access Pattern (used in challenge levels)
- Template Strings (used for story generation)
- List Scrolling Pattern (used in story navigation)

**Help:**
- Check the "💡 Code Hints" in each level
- Use the "Show Me" sections when stuck
- Review `/notes/` folder for previous lessons
- Check example projects in `/week2/` and `/week3/`
- Ask a classmate or instructor for help

---

## Extension Ideas

**Creative Extensions:**
- Add images or GIFs to your stories
- Create themed story categories (adventure, sci-fi, comedy)
- Add sound effects or background music
- Create printable versions of stories
- Add animations and transitions

**Technical Extensions:**
- Implement a database for persistent storage
- Add user accounts and login system
- Create an API for story generation
- Add a "share story" feature with unique URLs
- Implement story ratings or favorites

**Design Extensions:**
- Create custom CSS themes
- Add dark mode toggle
- Make the site fully responsive for mobile
- Create different layouts for different story types

---

**Project Complete!** ✅  
When finished, make sure to:
- [ ] Test all features thoroughly
- [ ] Complete the rubric self-check
- [ ] Answer reflection questions
- [ ] Write a complete README
- [ ] Make Git commits with clear messages
- [ ] Submit your project link

---

*Have fun creating hilarious stories!* 😂

---

**Attribution:** This activity guide was created with assistance from Claude AI (Anthropic).

