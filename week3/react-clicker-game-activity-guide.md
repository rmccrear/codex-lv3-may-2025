Name(s)\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Period \_\_\_\_\_\_ Date \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

|  | Activity Guide - React Clicker Game | 🍎 |
| :---- | :---- | :---- |

**Overview**  
Build an interactive clicker game using React where players click randomly moving and sizing apples to earn points. Lose lives if you miss!

**Model:** [Code.org Clicker Game](https://studio.code.org/courses/csp5-virtual/units/1/lessons/5/levels/1)

---

## Step 1 - Play the Model Game

Try the Code.org clicker game linked above. Play for 2-3 minutes.

**Discuss with a Partner:**
- What happens when you click the target?
- What happens when you miss?
- How does the target change?
- What makes this game engaging?

---

## Step 2 - Plan Your Variables

**State Variables:** Fill in the table below for each piece of data your game needs to track.

| Variable Name | Initial Value | What It Stores |
| :---- | :---: | :---- |
| score | 0 | Player's current score |
| lives | 3 | Number of lives remaining |
| appleSize | 100 | Current size of apple (pixels) |
|  |  |  |
|  |  |  |

**Functions:** List the functions you'll need to create.

| Function Name | What It Does |
| :---- | :---- |
| clickTarget | Increases score, changes apple size/position |
| missTarget | Decreases lives, changes apple size/position |
|  |  |
|  |  |

---

## Step 3 - Plan Your Game Logic

**Game Rules:** Draw a flowchart or write pseudocode for the following:

1. **When apple is clicked:**
   - Add 1 to score
   - Change apple to random size (20-100px)
   - Move apple to random position

2. **When background is clicked (miss):**
   - Subtract 1 from lives
   - Change apple to random size (20-100px)
   - Move apple to random position

3. **Win Condition:**
   - When score reaches 100, show "You Win!" message
   - Hide the apple

4. **Optional - Lose Condition:**
   - When lives reach 0, show "Game Over" message
   - Display final score

**Test Cases:** Your game should handle these scenarios correctly.

| Action | Expected Behavior |
| :---- | :---- |
| Click apple at score 5 | Score increases to 6, apple moves |
| Miss apple at 3 lives | Lives decrease to 2, apple moves |
| Reach score of 100 | "You Win!" appears, apple disappears |
| Click apple when score < 100 | Lives stay the same (no penalty) |

---

## Step 4 - Setup Your Project

**Create React App:**
1. Run: `npm create vite@latest`
2. Choose a project name (e.g., "clicker-game")
3. Select "React" framework
4. Select "JavaScript" variant
5. Navigate to folder: `cd clicker-game`
6. Run: `npm install`
7. Start dev server: `npm run dev`

**Add Your Images:**
1. Find or create:
   - An apple image (save as `apple.png`)
   - An orchard/background image (save as `orchard.png`)
2. Place both images in the `public/` folder

---

## Step 5 - Build Your Game

Follow the level-by-level guide to build your game. Complete each level before moving to the next.

**Core Features (Levels 1-11):**
- ✅ Level 1: Project setup
- ✅ Level 2: Clean slate
- ✅ Level 3: Add images
- ✅ Level 4: Create game board
- ✅ Level 5: Add score tracking (use `useState`)
- ✅ Level 6: Add lives tracking
- ✅ Level 7: Random apple size
- ✅ Level 8: Random apple position
- ✅ Level 9: Dynamic stats colors
- ✅ Level 10: Win condition message
- ✅ Level 11: Hide apple on win

**Component Organization (Levels 12-13):**
- ✅ Level 12: Extract Stats component
- ✅ Level 13: Create GameBoard component

**Polish & Documentation (Levels 14-17):**
- ✅ Level 14: Testing
- ✅ Level 15: Code review
- ✅ Level 16: README documentation
- ✅ Level 17: Git commits

**As You Code:**
- Test your game frequently
- Use `console.log()` to debug
- Check React DevTools to view state
- Commit your code after completing each major feature

---

## Step 6 - Test Your Game

Play your game and verify it works correctly for all scenarios:

| Test | What to Check | ✓ |
| :---- | :---- | :---: |
| Click apple 5 times | Score = 5, apple moves each time |  |
| Miss 3 times | Lives = 0 (or 3 → 0) |  |
| Apple size changes | Size varies between small and large |  |
| Apple position changes | Apple appears in different locations |  |
| Stats colors change | Colors change at scores 10, 20, 30 |  |
| Reach 100 points | "You Win!" appears, apple disappears |  |
| Click background | Only lives decrease (not score) |  |

**Debug Using:**
- Browser console (F12) for errors
- `console.log()` to check variable values
- React DevTools to inspect state
- Remove `event.stopPropagation()` temporarily to see event bubbling issue

---

## Step 7 - Submit

Before you submit, check the rubric below to make sure your program meets the requirements.

| Category | Extensive Evidence | Convincing Evidence | Limited Evidence | No Evidence |
| :---- | :---- | :---- | :---- | :---- |
| **React Setup** | Vite + React project correctly set up and runs without errors. | Project mostly works but has minor setup issues. | Project has significant setup problems. | Project does not run. |
| **State Management** | All state variables (`score`, `lives`, `appleSize`, etc.) properly created with `useState` and updated correctly. | Most state variables work correctly but some have issues. | Some state variables work but many have problems. | State is not used or doesn't work. |
| **Event Handling** | Click handlers work correctly; `event.stopPropagation()` properly prevents event bubbling. | Most events work but some trigger incorrectly. | Events partially work with significant issues. | Events don't work or aren't implemented. |
| **Random Positioning** | Apple size and position change randomly within game board boundaries after each interaction. | Random changes mostly work but occasionally go off-screen or fail. | Random changes partially work with frequent issues. | Random positioning not implemented or broken. |
| **Win Condition** | Win message appears at exactly 100 points; apple disappears correctly. | Win condition works but has minor issues. | Win condition partially works. | Win condition not implemented. |
| **Component Structure** | Stats and GameBoard components properly extracted with correct props. | Some components extracted but with issues. | Components attempted but poorly organized. | All code in one component. |
| **Code Quality** | Code is clean, readable, with good variable names and comments explaining key concepts. | Code is mostly readable with some comments. | Code is hard to follow with few comments. | Code is messy and unclear. |
| **Styling** | Game looks polished; images display correctly; colors change appropriately. | Game works visually but lacks polish. | Game has visual issues. | Game doesn't display correctly. |

**Minimum Requirements for Full Credit:**
- Game runs without errors
- Score increases when clicking apple
- Lives decrease when missing
- Apple changes size and position randomly
- Win condition at 100 points works
- Stats and GameBoard components extracted
- README with instructions included

---

## Step 8 - Reflection

Answer the following questions about your project:

**1. React Concepts:**  
Describe how you used the `useState` hook in your project. Why is `useState` necessary instead of using regular variables?

|  |
| :---- |
| |
| |

**2. Event Propagation:**  
Explain what `event.stopPropagation()` does in your code. What happens if you remove it?

|  |
| :---- |
| |
| |

**3. Component Composition:**  
Describe one component you extracted (Stats or GameBoard). What props does it receive and why?

|  |
| :---- |
| |
| |

**4. Debugging Experience:**  
What was the most challenging bug you encountered? How did you solve it?

|  |
| :---- |
| |
| |

**5. Creative Choices:**  
What images, colors, or features did you choose to personalize your game?

|  |
| :---- |
| |
| |

---

## Vocabulary Review

Match the term with its definition:

| Term | Definition |
| :---- | :---- |
| **State** | Data that changes over time and triggers UI updates |
| **Hook** | Special React function like `useState` that adds features |
| **Props** | Data passed from parent component to child component |
| **Event Handler** | Function that runs when user interacts with element |
| **Event Propagation** | How events "bubble up" from child to parent elements |
| **Component** | Reusable piece of UI with its own logic and appearance |

---

## Resources

**Documentation:**
- React Docs: https://react.dev
- Vite Docs: https://vitejs.dev
- MDN JavaScript: https://developer.mozilla.org/docs/Web/JavaScript

**Tools:**
- React DevTools (Chrome/Firefox extension)
- VS Code with ES7 React Snippets

**Help:**
- Check the "💡 Code Hints" in each level
- Use the "Show Me" sections when stuck
- Ask a classmate or instructor for help

---

**Project Complete!** ✅  
When finished, make sure to:
- [ ] Test all features thoroughly
- [ ] Complete the rubric self-check
- [ ] Answer reflection questions
- [ ] Add screenshots to your README
- [ ] Submit your project link

---

*Good luck and have fun building your game!* 🎮

