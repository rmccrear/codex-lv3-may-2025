# React Clicker Game - Project Guide

**Unit:** Web Development with React  
**Project Duration:** 3-5 hours  
**Level:** Intermediate

---

## Overview

In this project, students will build an interactive clicker game using React, Vite, and modern JavaScript. Students will learn fundamental React concepts including state management, event handling, conditional rendering, and component composition while creating an engaging game where players click on a randomly moving and sizing apple target to earn points.

**Model Reference:** [Code.org Clicker Game](https://studio.code.org/courses/csp5-virtual/units/1/lessons/5/levels/1)

**Planning Guide:** [Activity Guide](./react-clicker-game-activity-guide.md) - Handout with step-by-step instructions, planning tables, and rubric. Complete this planning guide before starting the project.

---

## Learning Objectives

Students will be able to:

1. **Set up a modern React development environment** using Vite
2. **Use React state** with the `useState` hook to track game data
3. **Handle user events** with `onClick` handlers and event propagation
4. **Apply conditional rendering** to show/hide UI elements based on game state
5. **Create dynamic styles** using JavaScript objects and CSS positioning
6. **Build reusable components** with props and the children pattern
7. **Implement game logic** including scoring, lives, win/lose conditions
8. **Debug and test** an interactive application

---

## Vocabulary

- **State** - Data that changes over time in a React component
- **Hook** - A special function that lets you "hook into" React features (e.g., `useState`)
- **Event Handler** - A function that runs when a user interacts with an element
- **Event Propagation** - How events "bubble up" from child to parent elements
- **Conditional Rendering** - Showing or hiding UI elements based on conditions
- **Props** - Data passed from a parent component to a child component
- **Component Composition** - Building complex UIs by combining simpler components
- **Children Prop** - A special prop that contains the content between component tags

---

## Prerequisites

### Technical Skills
- Basic JavaScript (variables, functions, conditionals)
- Basic HTML & CSS (elements, selectors, positioning)
- Understanding of file/folder structure
- Command line basics (cd, running commands)

### Software Requirements
- Node.js (v16 or higher) installed
- Code editor (VS Code recommended)
- Modern web browser (Chrome, Firefox, Edge)
- Terminal/command line access

---

## Agenda

### Session 1: Setup & Basic Structure (60-90 minutes)
- **Level 1:** Project setup with Vite
- **Level 2:** Clean slate - remove starter code
- **Level 3:** Add game images
- **Level 4:** Create game board structure
- **Level 5:** Add score tracking with state

**Checkpoint:** Students should have a clickable apple that increases score

---

### Session 2: Game Mechanics (60-90 minutes)
- **Level 6:** Add lives tracking
- **Level 7:** Random apple size
- **Level 8:** Random apple position
- **Level 9:** Dynamic stats styling

**Checkpoint:** Students should have a functional game with moving, resizing apples

---

### Session 3: Polish & Components (60-90 minutes)
- **Level 10:** Add win condition message
- **Level 11:** Hide apple on win
- **Level 12:** Extract Stats component
- **Level 13:** Create GameBoard component

**Checkpoint:** Students should have a complete game with organized component structure

---

### Session 4: Documentation & Extensions (45-60 minutes)
- **Level 14:** Testing and polish
- **Level 15:** Code review and understanding
- **Level 16:** Documentation and README
- **Level 17:** Git history and commits
- **Level 18:** Challenge extensions (optional)
- **Level 19:** Project complete

**Checkpoint:** Students have a polished, documented, version-controlled project

---

## Teaching Guide

### Warm Up (10 minutes)

**Play the Model Game**
1. Have students visit the [Code.org Clicker Game](https://studio.code.org/courses/csp5-virtual/units/1/lessons/5/levels/1)
2. Give students 3-5 minutes to play the game
3. Ask students to identify:
   - What happens when you click the target?
   - What happens when you miss?
   - How does the difficulty change?
   - What makes the game engaging?

**Discussion Prompts:**
- "What JavaScript concepts do you think are used in this game?" (variables, events, conditionals)
- "How might we track the score?" (variables/state)
- "How could we make the target move?" (random numbers, positioning)

---

### Activity: Building the Game (Main Project Time)

#### Part 1: Foundation (Levels 1-5)

**Key Teaching Points:**

**Level 1 - Vite Setup**
- Explain why we use build tools like Vite (fast, modern, optimized)
- Show how Vite provides hot module replacement (instant updates)
- Compare to older tools (Create React App) - Vite is faster!

**Level 2 - Clean Slate**
- Emphasize understanding every line of code
- This builds confidence and reduces confusion
- Students should never have "mystery code" in their projects

**Level 4 - CSS Positioning**
- Review `position: relative` vs `position: absolute`
- Demonstrate how absolute positioning works relative to nearest positioned ancestor
- Show coordinate system: (0,0) is top-left corner

**Level 5 - React State**
- **Critical Concept:** Why can't we use regular variables?
  ```javascript
  // ❌ This won't work - React doesn't know to re-render
  let score = 0;
  
  // ✅ This works - React knows to update the UI
  const [score, setScore] = useState(0);
  ```
- Demonstrate how `setScore` triggers a re-render
- Show the React DevTools to visualize state changes

**Common Student Mistakes:**
- Forgetting to import `useState`
- Trying to modify state directly: `score = score + 1` instead of `setScore(score + 1)`
- Forgetting to use curly braces for JavaScript in JSX: `{score}` not `score`

---

#### Part 2: Game Logic (Levels 6-9)

**Key Teaching Points:**

**Level 6 - Event Propagation**
- **Critical Concept:** Why we need `event.stopPropagation()`
- Demonstrate what happens without it (both handlers fire!)
- Analogy: "It's like clicking a button inside a card - you don't want both to respond"

**Demonstration Activity:**
```javascript
// Have students temporarily remove stopPropagation() to see the problem
function clickTarget(event) {
  // event.stopPropagation();  // Comment this out temporarily
  setScore(score + 1);
}
```
Ask: "What happens when you click the apple now?" (Score goes up AND lives go down!)

**Level 7 - Random Numbers**
- Explain `Math.random()` returns 0-1
- Walk through the math: `Math.random() * (max - min) + min`
- Show why we need `Math.floor()` for integers

**Level 9 - Dynamic Styling**
- Explain inline styles use JavaScript objects, not CSS strings
- Show camelCase convention: `backgroundColor` not `background-color`
- Demonstrate how conditions create different user experiences

**Common Student Mistakes:**
- Forgetting `event.stopPropagation()` - both handlers fire
- Math mistakes with `randomNumber()` function
- Using CSS syntax in inline styles: `{"background-color": "red"}` won't work
- Not calling the random functions after state updates

---

#### Part 3: Advanced Concepts (Levels 10-13)

**Key Teaching Points:**

**Level 10 & 11 - Conditional Rendering**
- Compare `&&` operator vs ternary operator:
  ```javascript
  // && = show OR nothing
  {score >= 100 && <WinMessage />}
  
  // ternary = show A OR B
  {score < 100 ? <Apple /> : <WinMessage />}
  ```

**Level 12 & 13 - Component Composition**
- **Critical Concept:** Breaking down UI into reusable pieces
- Show how props flow down from parent to child
- Explain the `children` prop as a special prop for flexible components

**Teaching Strategy - The LEGO Analogy:**
"Components are like LEGO bricks. Each brick has a specific purpose, and you combine them to build something bigger. Props are like the connectors that let you snap bricks together."

**Demonstration:**
Show how the same component can be reused:
```jsx
<Stats score={10} lives={3} style={blueStyle} />
<Stats score={50} lives={1} style={redStyle} />
```

**Common Student Mistakes:**
- Confusing `&&` with ternary operators
- Forgetting to pass props to child components
- Trying to modify props inside child components (props are read-only!)
- Not destructuring props: `(props)` instead of `({ score, lives })`

---

### Differentiation Strategies

**For Students Who Need More Support:**
- Pair programming with more advanced students
- Provide completed code for earlier levels to "catch up"
- Focus on Levels 1-11 for a minimum viable product
- Use the "Show Me" hints liberally
- Schedule one-on-one check-ins

**For Advanced Students:**
- Challenge them to complete Level 18 extensions
- Ask them to help peers as "student experts"
- Additional challenges:
  - Add sound effects
  - Create difficulty levels
  - Implement high score with localStorage
  - Add a countdown timer
  - Create multiple targets
  - Add animation effects

---

### Wrap Up (10 minutes)

**Code Showcase (5 minutes)**
- Have 2-3 students share their games
- Ask them to explain one technical challenge they overcame
- Celebrate different creative approaches (different images, colors, sizes)

**Reflection Questions (5 minutes)**
- "What was the most challenging part of this project?"
- "What React concept finally 'clicked' for you?"
- "How would you explain `useState` to someone who hasn't used it?"
- "What feature would you add next if you had more time?"

**Exit Ticket:**
Have students write down (or submit digitally):
1. One thing they learned
2. One thing they're still confused about
3. One feature they want to add

---

## Assessment Opportunities

### Formative Assessment (During Project)

**Checkpoint Questions:**
- "Show me where your state variables are defined"
- "Walk me through what happens when a user clicks the apple"
- "How does React know when to update the display?"
- "What would happen if you removed `stopPropagation()`?"

**Code Review Checklist:**
- [ ] State variables properly initialized with `useState`
- [ ] Event handlers attached to correct elements
- [ ] `event.stopPropagation()` used in clickTarget handler
- [ ] Random functions implemented correctly
- [ ] Conditional rendering working (win condition)
- [ ] Components extracted with proper props

---

### Summative Assessment (Project Completion)

**Rubric: React Clicker Game**

| Category | Developing (1-2) | Proficient (3-4) | Advanced (5) |
|----------|-----------------|------------------|--------------|
| **Functionality** | Game has bugs; core features incomplete | Game works; all core features present (score, lives, random movement) | Game works perfectly; includes polish and extra features |
| **State Management** | State variables not working correctly | State properly managed with `useState` | State used effectively; considers optimization |
| **Event Handling** | Events don't work or trigger incorrectly | Events work correctly with proper propagation | Events handled elegantly; includes edge cases |
| **Component Structure** | Code is messy; everything in one component | Components extracted (Stats, GameBoard) | Well-organized, reusable components |
| **Styling** | Minimal or broken styling | Clean, functional styling | Polished, professional appearance |
| **Code Quality** | Hard to read; poor naming | Clean, readable code with good naming | Excellent code quality; includes comments |
| **Documentation** | No README or documentation | Basic README with instructions | Comprehensive README with learning reflections |

**Minimum Viable Product (Levels 1-11):**
- Functional game with score tracking
- Lives decrease on miss
- Apple moves and changes size randomly
- Win condition at 100 points

**Full Project (Levels 1-13):**
- MVP features complete
- Components properly extracted
- Props and children pattern implemented

**Excellence (Levels 1-18):**
- Full project complete
- At least one challenge extension
- Professional documentation
- Git history with meaningful commits

---

## Common Issues and Solutions

### Technical Issues

**Issue:** "npm: command not found"
- **Solution:** Node.js not installed. Visit https://nodejs.org and install LTS version

**Issue:** Images don't appear
- **Solution:** Check file paths start with `/` in CSS, files are in `public/` folder

**Issue:** Score doesn't update when clicking
- **Solution:** Check `useState` is imported, `onClick` handler is attached, using `setScore` not `score =`

**Issue:** Clicking apple decreases lives too
- **Solution:** Add `event.stopPropagation()` in clickTarget function

**Issue:** Apple goes off-screen
- **Solution:** Check random ranges (0-400 for X, 0-600 for Y) based on board size

---

### Conceptual Challenges

**Challenge:** Students don't understand why `useState` is necessary
- **Solution:** Show comparison - regular variable doesn't trigger re-render
- Use React DevTools to show state changes visually

**Challenge:** Confusion about event propagation
- **Solution:** Temporarily remove `stopPropagation()` to demonstrate the problem
- Draw diagram showing event bubbling from child to parent

**Challenge:** Difficulty with component props
- **Solution:** Use physical objects analogy - "props are like arguments to functions"
- Live code example showing same component with different props

**Challenge:** Understanding children prop
- **Solution:** Compare to HTML - content between tags becomes children
- Show how `<div>content</div>` has "content" as children

---

## Extension Activities

### For Early Finishers

1. **Game Over Screen** (Level 18, Challenge 1)
   - Add condition for when lives reach 0
   - Create a Game Over component
   - Display final score

2. **High Score System** (Level 18, Challenge 3)
   - Learn about `localStorage` API
   - Persist high score across sessions
   - Add "New High Score!" message

3. **Sound Effects** (Level 18, Challenge 4)
   - Find free sound effects online
   - Use HTML5 Audio API
   - Add sounds for: hit, miss, win, game over

4. **Multiple Difficulty Levels** (Level 18, Challenge 6)
   - Create difficulty selection screen
   - Adjust game parameters based on difficulty
   - Track best score for each difficulty

---

## Resources

### For Students

**Documentation:**
- [React Official Docs](https://react.dev) - Primary reference for React
- [Vite Documentation](https://vitejs.dev) - Build tool documentation
- [MDN JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) - JavaScript reference

**Assets:**
- [Unsplash](https://unsplash.com) - Free stock photos for backgrounds
- [Pexels](https://pexels.com) - Free stock photos
- [Remove.bg](https://remove.bg) - Remove image backgrounds
- [Freesound](https://freesound.org) - Free sound effects (for extensions)

**Tools:**
- [React DevTools](https://react.dev/learn/react-developer-tools) - Browser extension for debugging
- [VS Code](https://code.visualstudio.com) - Recommended code editor
- [ES7+ React Snippets](https://marketplace.visualstudio.com/items?itemName=dsznajder.es7-react-js-snippets) - VS Code extension for React

### For Teachers

**Preparation:**
- Complete the project yourself before teaching (2-3 hours)
- Test setup on school computers/network
- Verify Node.js is installed and accessible
- Prepare backup projects for students who get stuck
- Have example solutions ready for reference

**Additional Reading:**
- [React Hooks Documentation](https://react.dev/reference/react/hooks) - Deep dive into hooks
- [Thinking in React](https://react.dev/learn/thinking-in-react) - React philosophy
- [JavaScript Event Bubbling](https://javascript.info/bubbling-and-capturing) - Event propagation explained

---

## Standards Alignment

**Computer Science Standards:**

**CSTA K-12 CS Standards:**
- **3A-AP-13:** Create prototypes that use algorithms to solve computational problems
- **3A-AP-16:** Design and iteratively develop computational artifacts for practical intent
- **3A-AP-17:** Use version control systems to track development
- **3B-AP-11:** Evaluate and refine computational artifacts based on feedback

**AP Computer Science Principles:**
- **CRD-2:** Developers create and innovate using iterative design processes
- **AAP-2:** The way statements are sequenced and combined determines the computed result
- **AAP-3:** Programmers integrate algorithms and data to create programs

---

## Project Timeline

### Recommended Schedule (5 sessions)

**Day 1: Introduction & Setup (45-60 min)**
- Warm up with model game
- Complete Levels 1-3
- **Homework:** Find/prepare game images

**Day 2: Core Mechanics (60-90 min)**
- Review previous day
- Complete Levels 4-6
- **Homework:** Experiment with different sizes/positions

**Day 3: Advanced Features (60-90 min)**
- Complete Levels 7-9
- Test and debug
- **Homework:** Reach 100 points in your game!

**Day 4: Components & Polish (60-90 min)**
- Complete Levels 10-13
- Code review with peers
- **Homework:** Start README documentation

**Day 5: Documentation & Showcase (45-60 min)**
- Complete Levels 14-17
- Optional: Challenge extensions (Level 18)
- Project presentations

---

## Teacher Notes

**What Went Well:**
- Students were highly engaged with the game concept
- Immediate visual feedback helped with debugging
- Progressive levels worked well for different skill levels
- "Show Me" hints were helpful without being too revealing

**What to Improve:**
- Some students struggled with event propagation concept
- Need more time for component extraction (Levels 12-13)
- Consider adding video tutorials for visual learners
- Provide more example repos for reference

**Time Management:**
- Levels 1-5 take longer than expected (allow 90 min minimum)
- Advanced students finish early - have extensions ready
- Build in buffer time for technical issues
- Consider splitting Level 18 challenges across multiple days

**Classroom Management:**
- Encourage peer collaboration but individual projects
- Set clear checkpoints for each session
- Use project showcase to celebrate different approaches
- Have backup activities for students waiting for help

---

## Additional Notes

**Why This Project?**
- **Engaging:** Games are intrinsically motivating for students
- **Practical:** Covers fundamental React concepts used in real apps
- **Scalable:** Core project is achievable; extensions for advanced students
- **Portfolio-Worthy:** Students can showcase to colleges/employers

**Connection to Industry:**
- State management is core to all modern web apps
- Component composition is fundamental to React development
- Event handling is essential for interactive applications
- Version control (Git) is industry standard

**Student Outcomes:**
By completing this project, students will have:
- A working understanding of React fundamentals
- Confidence with state management and event handling
- A portfolio piece they can share and be proud of
- Foundation for more complex React applications

---

## Feedback and Iteration

**For Future Versions:**
- [ ] Add video walkthrough for each level
- [ ] Create automated tests for student code
- [ ] Develop additional game themes (space shooter, whack-a-mole, etc.)
- [ ] Build online leaderboard for high scores
- [ ] Create deployment guide (Netlify/Vercel)

**Share Your Experience:**
If you teach this project, please share:
- What worked well in your classroom
- What challenges your students faced
- Any modifications you made
- Student example projects

---

## License and Attribution

This project guide is designed for educational use. Feel free to adapt for your classroom needs.

**Model Reference:** [Code.org Clicker Game](https://studio.code.org/courses/csp5-virtual/units/1/lessons/5/levels/1)

**Technology Stack:**
- React 19
- Vite (Latest)
- JavaScript ES6+
- CSS3

---

*Last Updated: October 2025*  
*Version: 1.0*

