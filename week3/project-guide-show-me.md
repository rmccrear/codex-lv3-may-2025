# 🎯 Apple Clicker Game Project Guide

This guide provides step-by-step instructions for building an interactive Apple Clicker game using React, Vite, and modern web development concepts.

**Model Reference:**
See a working example of a clicker game here: [Code.org Clicker Game](https://studio.code.org/courses/csp5-virtual/units/1/lessons/5/levels/1)

Your React version will have similar gameplay mechanics but with your own creative twist!

**Structure:**
- Each level builds on the previous one
- Clear instructions and checkpoints
- Code examples and hints provided
- Progressive complexity from basic to advanced

---

# Level 1: Project Setup & Planning

**Goal:** Set up your development environment with Vite and React.

**User Story:** As a developer, I want to create a new React project so that I can start building my Apple Clicker game.

---

## What You'll Do

Create a new React project using Vite and set up all the necessary files to get started.

## Instructions

- Create a new Vite + React project using the command: `npm create vite@latest`
- Navigate to the project folder: `cd clicker-game`
- Install dependencies: `npm install`
- Start the development server to verify setup: `npm run dev`
- Open the project in your code editor

## 💡 Code Hints

Need help with Vite setup? Check out these snippets:

**Creating a Vite project:**
```bash
npm create vite@latest
cd clicker-game
npm install
```

**Starting the development server:**
```bash
npm run dev
```

## ✅ Check

1. Run `npm run dev` to start your development server
2. Open your browser to `http://localhost:5173`
3. You should see the default Vite + React welcome page
4. If you see errors, ensure Node.js is installed and you're in the correct directory
5. Open your project folder in VS Code and verify you can see these files:
   - `src/App.jsx`
   - `src/main.jsx`
   - `package.json`
   - `vite.config.js`

---

# Level 2: Clean Slate - Remove Starter Code

**User Story:** As a developer, I want to start with a clean slate so that I can understand every line of code I write.

## What You'll Do

Remove the default Vite starter code and styling to create a minimal starting point.

## Instructions

- Open `src/App.jsx` and simplify it to a basic component
- Clear out `src/App.css` completely
- Clear out `src/index.css` to remove global styling
- Remove any default imports you don't need
- Keep your component simple with just a basic return statement

## 💡 Code Hints

Need help simplifying? Check out these snippets:

<details>
<summary>Show Me: simplified App.jsx</summary>

<pre><code class="language-jsx">import &#039;./App.css&#039;

function App() {
  return (
    &lt;&gt;
      &lt;div&gt;
        &lt;h1&gt;Apple Clicker Game&lt;/h1&gt;
      &lt;/div&gt;
    &lt;/&gt;
  )
}

export default App
</code></pre>

</details>

<details>
<summary>Show Me: empty CSS files</summary>

<p>For <code>src/App.css</code> and <code>src/index.css</code>, just delete all content:</p>
<pre><code class="language-css">/* Empty - we&#039;ll add our own styles */
</code></pre>

</details>

## ✅ Check

1. Your browser should now show a blank page with just "Apple Clicker Game"
2. No Vite or React logos should be visible
3. Check the browser console - there should be no errors
4. If you see styling from before, make sure you cleared the CSS files
5. The page should reload automatically (hot module replacement)

---

# Level 3: Add Game Images

**User Story:** As a developer, I want to add visual assets so that my game looks appealing.

## What You'll Do

Add image files for the apple target and orchard background to your project.

## Instructions

- Download the two images, or find your own:
  - An [apple image](./apple.png) (save as `apple.png`)
  - An [orchard background image](./orchard.png) (save as `orchard.png`)
- Place both images in the `public/` folder
- Delete the default `vite.svg` from `public/`
- Delete `react.svg` from `src/assets/`

## 💡 Code Hints

Need help with images? Check out these tips:

**Where to find images:**
- Optional: You may find your own images if you'd like a different theme.
- Use free stock photo sites like Unsplash, Pexels, or Pixabay
- Make sure images are properly licensed for use

**File structure:**
```
public/
  ├── apple.png      (Your apple target image)
  └── orchard.png    (Your background image)
```

**Why the public folder?**
Files in `public/` can be referenced directly in CSS using `/filename.png` without imports.

## ✅ Check

1. Navigate to `public/` folder in your file explorer
2. You should see `apple.png` and `orchard.png`
3. No default Vite/React SVG files should remain
4. Try accessing the images directly: `http://localhost:5173/apple.png`
5. You should see your apple image in the browser

---

# Level 4: Create Game Board Structure

**User Story:** As a user, I want to see an orchard background with an apple target so that I understand what to click.

## What You'll Do

Create the HTML structure with CSS styling for the game board and clickable apple.

## Instructions

- In `App.jsx`, create a div with className `orchard-background`
- Inside it, create a div with className `apple-target`
- In `App.css`, style the orchard-background:
  - Use `position: relative` (so children can position absolutely)
  - Set `background-image` to your orchard image
  - Set dimensions: 500px wide, 700px tall
  - Use `background-size: contain`
- Style the apple-target:
  - Use `position: absolute`
  - Set `background-image` to your apple image
  - Set dimensions: 100px by 100px
  - Use `background-size: contain`

## 💡 Code Hints

Need help with styling? Check out these snippets:

<details>
<summary>Show Me: App.jsx structure</summary>

<pre><code class="language-jsx">import &#039;./App.css&#039;

function App() {
  return (
    &lt;&gt;
      &lt;div className=&#039;orchard-background&#039;&gt;
        &lt;div className=&quot;apple-target&quot;&gt;&lt;/div&gt;
      &lt;/div&gt;
    &lt;/&gt;
  )
}

export default App
</code></pre>

</details>

<details>
<summary>Show Me: App.css styling</summary>

<pre><code class="language-css">* {
  box-sizing: border-box;
}

.orchard-background {
  position: relative;
  background-image: url(&quot;/orchard.png&quot;);
  background-size: contain;
  width: 500px;
  height: 700px;
}

.apple-target {
  position: absolute;
  background-image: url(&quot;/apple.png&quot;);
  background-size: contain;
  width: 100px;
  height: 100px;
}
</code></pre>

</details>

## ✅ Check

1. You should see an orchard background image
2. An apple should appear in the top-left corner
3. The game board should be 500px wide and 700px tall
4. If images don't appear, check:
   - Image paths start with `/` in CSS
   - Images are in the `public/` folder
   - Image file names match exactly (case-sensitive)

---

# Level 5: Add Score Tracking

**User Story:** As a player, I want to see my score increase when I click the apple so that I can track my progress.

## What You'll Do

Add React state to track the score and create a click handler for the apple.

## Instructions

- Import `useState` from React
- Create a state variable for `score` with initial value of 0
- Create a `clickTarget` function that:
  - Accepts an `event` parameter
  - Calls `event.stopPropagation()` to prevent click bubbling (see Level 6 "Show Me" section for details on how this works)
  - Increments the score by 1
- Add an `onClick` handler to the apple-target div
- Create a stats div above the game board to display the score
- Style the stats div in CSS

## 💡 Code Hints

Need help with state and events? Check out these snippets:

<details>
<summary>Show Me: useState import and setup</summary>

<pre><code class="language-jsx">import { useState } from &#039;react&#039;
import &#039;./App.css&#039;

function App() {
  const [score, setScore] = useState(0)
  
  // ... rest of component
}
</code></pre>

</details>

<details>
<summary>Show Me: click handler function</summary>

<pre><code class="language-jsx">function clickTarget(event) {
  event.stopPropagation();  // Prevents triggering parent clicks
  setScore(score + 1)
}
</code></pre>

</details>

<details>
<summary>Show Me: JSX with stats display</summary>

<pre><code class="language-jsx">return (
  &lt;&gt;
    &lt;div className=&quot;stats&quot;&gt;
      Score: {score}
    &lt;/div&gt;
    &lt;div className=&#039;orchard-background&#039;&gt;
      &lt;div className=&quot;apple-target&quot; onClick={clickTarget}&gt;&lt;/div&gt;
    &lt;/div&gt;
  &lt;/&gt;
)
</code></pre>

</details>

<details>
<summary>Show Me: stats CSS styling</summary>

<pre><code class="language-css">.stats {
  background-color: brown;
  color: whitesmoke;
  width: 500px;
  padding: 5px;
}
</code></pre>

</details>

## ✅ Check

1. You should see "Score: 0" above the game board
2. Click the apple - the score should increase to 1
3. Click multiple times - score should keep increasing
4. The stats bar should have a brown background
5. If score doesn't update, check:
   - `useState` is imported correctly
   - `onClick` handler is attached to apple-target
   - You're using `setScore` to update state

## 🔬 Try This

**Experiment with Box Sizing:**

In your `App.css`, you included `box-sizing: border-box` on the universal selector. Let's see what this does!

1. Remove or comment out the `box-sizing` line:
   ```css
   * {
     /* box-sizing: border-box; */
   }
   ```

2. Change the stats padding to something larger, like `20px`

3. Observe what happens to the width of your stats bar

**What's happening?**  
Learn about `box-sizing: border-box` and how it affects element sizing: [MDN: box-sizing](https://developer.mozilla.org/en-US/docs/Web/CSS/box-sizing)

**Question:** Does the stats bar stay 500px wide, or does it get wider? Why?

---

# Level 6: Add Lives Tracking

**User Story:** As a player, I want to lose a life when I miss the apple so that the game has challenge and consequences.

## What You'll Do

Add a lives state variable and create a miss handler for clicking the background.

## Instructions

- Create a new state variable for `lives` with initial value of 3
- Create a `missTarget` function that decrements lives by 1
- Add an `onClick` handler to the orchard-background div
- Update the stats display to show both score and lives
- Test that clicking the apple doesn't trigger the miss handler

## 💡 Code Hints

Need help with multiple state variables? Check out these snippets:

<details>
<summary>Show Me: adding lives state</summary>

<pre><code class="language-jsx">function App() {
  const [score, setScore] = useState(0)
  const [lives, setLives] = useState(3)  // NEW
  
  // ... rest of component
}
</code></pre>

</details>

<details>
<summary>Show Me: miss handler function</summary>

<pre><code class="language-jsx">function missTarget() {
  setLives(lives - 1)
}
</code></pre>

</details>

<details>
<summary>Show Me: updated JSX with onClick handlers</summary>

<pre><code class="language-jsx">return (
  &lt;&gt;
    &lt;div className=&quot;stats&quot;&gt;
      Score: {score} Lives: {lives}
    &lt;/div&gt;
    &lt;div className=&#039;orchard-background&#039; onClick={missTarget}&gt;
      &lt;div className=&quot;apple-target&quot; onClick={clickTarget}&gt;&lt;/div&gt;
    &lt;/div&gt;
  &lt;/&gt;
)
</code></pre>

</details>

## ✅ Check

1. You should see "Score: 0 Lives: 3" in the stats bar
2. Click the apple - score increases, lives stay the same
3. Click the background (miss the apple) - lives decrease
4. Click the apple again - only score increases (lives unchanged)
5. If both handlers fire when clicking apple:
   - Make sure `event.stopPropagation()` is in `clickTarget`

**Understanding Event Propagation:**
Try removing `event.stopPropagation()` temporarily to see what happens. You'll notice clicking the apple triggers BOTH handlers because clicks "bubble up" from child to parent. That's why we need `stopPropagation()`!

---

# Level 7: Random Apple Size

**User Story:** As a player, I want the apple to change size randomly so that the game becomes more challenging and interesting.

## What You'll Do

Create a utility function for random numbers and make the apple size change on each click.

## Instructions

- Create a `randomNumber(a, b)` helper function outside the App component
  - It should return a random integer between `a` and `b`
  - Use `Math.random()` and `Math.floor()`
- Create state variable `appleSize` with initial value of 100
- Create a `randomSize()` function that sets appleSize to a random value between 20 and 100
- Call `randomSize()` in both `clickTarget` and `missTarget` functions
- Create an `appleStyle` object with dynamic width and height
- Apply the style object to the apple-target div using the `style` attribute

## 💡 Code Hints

Need help with random numbers and dynamic styling? Check out these snippets:

<details>
<summary>Show Me: random number utility function</summary>

<pre><code class="language-jsx">function randomNumber(a, b) {
  return Math.floor(Math.random() * (b - a) + a);
}

function App() {
  // ... state and functions
}
</code></pre>

</details>

<details>
<summary>Show Me: apple size state and function</summary>

<pre><code class="language-jsx">const [score, setScore] = useState(0)
const [lives, setLives] = useState(3)
const [appleSize, setAppleSize] = useState(100)  // NEW

function randomSize() {
  const randomSize = randomNumber(20, 100)
  setAppleSize(randomSize)
}
</code></pre>

</details>

<details>
<summary>Show Me: updated click handlers</summary>

<pre><code class="language-jsx">function clickTarget(event) {
  event.stopPropagation();
  setScore(score + 1)
  randomSize();  // NEW
}

function missTarget() {
  setLives(lives - 1)
  randomSize();  // NEW
}
</code></pre>

</details>

<details>
<summary>Show Me: dynamic style object</summary>

<pre><code class="language-jsx">const appleStyle = {
  width: appleSize + &quot;px&quot;,
  height: appleSize + &quot;px&quot;
}

return (
  &lt;&gt;
    {/* ... stats div ... */}
    &lt;div className=&#039;orchard-background&#039; onClick={missTarget}&gt;
      &lt;div className=&quot;apple-target&quot; onClick={clickTarget} style={appleStyle}&gt;&lt;/div&gt;
    &lt;/div&gt;
  &lt;/&gt;
)
</code></pre>

</details>

## ✅ Check

1. Click the apple - it should change to a random size
2. Click the background - apple should also change size
3. Sizes should vary between very small and medium-large
4. The apple should maintain its aspect ratio
5. If size doesn't change:
   - Check that `randomSize()` is called in both handlers
   - Verify the style object is applied with `style={appleStyle}`

**How Math.random() works:**
- `Math.random()` returns a decimal between 0 and 1
- Multiply by range `(b - a)` to scale it
- Add `a` to shift to desired range
- `Math.floor()` rounds down to get an integer

---

# Level 8: Random Apple Position

**User Story:** As a player, I want the apple to appear in different locations so that I have to search for it and the game is more engaging.

## What You'll Do

Add state variables for apple position and randomize the position on each interaction.

## Instructions

- Create state variables `appleX` and `appleY` with initial value of 0
- Create a `randomSpot()` function that:
  - Sets `appleX` to a random value between 0 and 400
  - Sets `appleY` to a random value between 0 and 600
- Call `randomSpot()` in both `clickTarget` and `missTarget` functions
- Add `left` and `top` properties to the `appleStyle` object
- Test that the apple moves to different positions

**💪 Practice Challenge:** This level is similar to Level 7. Try to complete it on your own using the same patterns!

## ✅ Check

1. Click the apple - it should move to a new random location
2. Click the background - apple should also move
3. The apple should stay within the game board boundaries
4. Both size and position should change simultaneously
5. If apple goes off-screen:
   - Check your random ranges (400 for X, 600 for Y)
   - Remember the game board is 500x700

**CSS Positioning Review:**
- `position: absolute` allows us to place elements anywhere
- `left` sets distance from the left edge
- `top` sets distance from the top edge
- Coordinates (0, 0) are at the top-left corner

---

# Level 9: Dynamic Stats Styling

**User Story:** As a player, I want the stats bar color to change as my score increases so that I get visual feedback on my progress.

## What You'll Do

Create dynamic styling that changes the stats bar color based on the current score.

## Instructions

- Create a `statsStyle` object with initial backgroundColor and color properties
- Write conditional logic (if/else statements) to change colors based on score
- Apply the `statsStyle` object to the stats div using the `style` attribute
- Choose your own colors and score thresholds!

**Suggested Color Scheme (feel free to customize):**
- Score 0-9: `brown` background, `whitesmoke` text
- Score 10-19: `darkGreen` background, `whitesmoke` text
- Score 20-29: `navy` background, `whitesmoke` text
- Score 30+: `black` background, `pink` text

**Other color ideas:** `purple`, `teal`, `crimson`, `goldenrod`, `indigo`, `coral`, `forestgreen`

## ✅ Check

1. Stats bar changes color when you reach different score milestones
2. Colors change immediately when crossing your thresholds
3. Text color is readable against background color
4. You're happy with your creative color choices!

**Why modify objects before rendering?**
In React, you can create style objects and modify them based on state before the return statement. Each time state changes, the component re-renders and the conditionals run again, creating fresh style objects.

---

# Level 10: Add Win Condition Message

**User Story:** As a player, I want to see a "You Win!" message when I reach 100 points so that I know I've completed the game.

## What You'll Do

Add conditional rendering to show a win message at 100 points.

## Instructions

- After the apple-target div, add a conditional render for the win message
- Use `score >= 100 &&` to conditionally show an `<h1>` element
- Give it className "win" with text "You Win!"
- In `App.css`, style the `.win` class:
  - Use `position: absolute` to center it
  - Set background color and text color
  - Use `left: 50%; top: 50%` for positioning
  - Use `translate: -50% -50%` to perfectly center it

## 💡 Code Hints

Need help with conditional rendering? Check out these snippets:

<details>
<summary>Show Me: conditional rendering with &&</summary>

<pre><code class="language-jsx">&lt;div className=&#039;orchard-background&#039; onClick={missTarget}&gt;
  &lt;div className=&quot;apple-target&quot; onClick={clickTarget} style={appleStyle}&gt;&lt;/div&gt;
  {score &gt;= 100 &amp;&amp; &lt;h1 className=&quot;win&quot;&gt;You Win!&lt;/h1&gt;}
&lt;/div&gt;
</code></pre>

</details>

<details>
<summary>Show Me: win class CSS styling</summary>

<pre><code class="language-css">.win {
  position: absolute;
  background-color: green;
  color: red;
  left: 50%;
  top: 50%;
  translate: -50% -50%;
}
</code></pre>

</details>

## ✅ Check

1. Play the game and reach 100 points
2. "You Win!" message should appear in the center
3. The message should overlay the game board
4. Both the apple AND the win message should be visible
5. If message doesn't appear:
   - Check the conditional: `{score >= 100 && ...}`
   - Verify you've reached 100 points

**Understanding the && operator:**
- In JSX, `condition && <Component />` works like: "If condition is true, render Component"
- If false, React renders nothing
- This is called "short-circuit evaluation"

**Understanding CSS translate for centering:**
- `left: 50%` and `top: 50%` move the element's **top-left corner** to the center
- But we want the element's **center** to be in the center!
- `translate: -50% -50%` shifts the element back by half its own width and height
- This perfectly centers any sized element without knowing its dimensions
- Modern alternative to the older `transform: translate(-50%, -50%)` syntax

**Learn More:**  
- Conditional rendering in React: [React Docs - Conditional Rendering](https://react.dev/learn#conditional-rendering)
- CSS translate property: [MDN - translate](https://developer.mozilla.org/en-US/docs/Web/CSS/translate)

---

# Level 11: Hide Apple on Win

**User Story:** As a player, I want the apple to disappear when I win so that I don't accidentally keep clicking after winning.

## What You'll Do

Replace the conditional && with a ternary operator to show EITHER the apple OR the win message.

## Instructions

- Replace the apple-target div and win message with a ternary expression
- Use: `score < 100 ? ... : ...`
- If score < 100, show the apple-target div
- If score >= 100, show the win message
- Test that the apple disappears when you win

## 💡 Code Hints

Need help with ternary operators? Check out these snippets:

<details>
<summary>Show Me: ternary operator syntax</summary>

<pre><code class="language-jsx">&lt;div className=&#039;orchard-background&#039; onClick={missTarget}&gt;
  { score &lt; 100 ? 
    &lt;div className=&quot;apple-target&quot; onClick={clickTarget} style={appleStyle}&gt;&lt;/div&gt;
    : &lt;h1 className=&quot;win&quot;&gt; You Win!&lt;/h1&gt;
  }
&lt;/div&gt;
</code></pre>

</details>

<details>
<summary>Show Me: .win class CSS styling</summary>

<pre><code class="language-css">.win {
  position: absolute;
  background-color: green;
  color: red;
  left: 50%;
  top: 50%;
  translate: -50% -50%;
}
</code></pre>

</details>

## ✅ Check

1. Play the game with score below 100 - apple should be visible
2. Reach exactly 100 points
3. Apple should disappear immediately
4. "You Win!" message should appear
5. You should NOT be able to click the apple anymore
6. The game should feel complete and finished

**Ternary vs && operator:**
- `&&` operator: Shows component OR nothing
- Ternary `? :`: Shows component A OR component B
- Use ternary when you need mutual exclusivity

---

# Level 12: Extract Stats Component with Props

**User Story:** As a developer, I want to organize my code into reusable components so that my application is easier to maintain and understand.

## What You'll Do

Extract the stats display into its own component that accepts props for score, lives, and styling.

## Instructions

- Create a new `Stats` component above the `App` component
- The component should accept `score`, `lives`, and `style` as props
- Move the stats div JSX into this component
- In `App`, replace the stats div with `<Stats score={score} lives={lives} style={statsStyle} />`
- Test that the stats display still works correctly

## 💡 Code Hints

Need help with components and props? Check out these snippets:

<details>
<summary>Show Me: Stats component definition</summary>

<pre><code class="language-jsx">function Stats({ score, lives, style }) {
  return (
    &lt;div className=&quot;stats&quot; style={style}&gt;
      Score: {score} Lives: {lives}
    &lt;/div&gt;
  )
}
</code></pre>

</details>

<details>
<summary>Show Me: using the Stats component in App</summary>

<pre><code class="language-jsx">function App() {
  // ... all your state and functions ...
  
  const statsStyle = {
    backgroundColor: &quot;brown&quot;,
    color: &quot;whitesmoke&quot;
  }
  
  // ... conditional styling logic ...
  
  return (
    &lt;&gt;
      &lt;Stats score={score} lives={lives} style={statsStyle} /&gt;
      &lt;div className=&#039;orchard-background&#039; onClick={missTarget}&gt;
        { score &lt; 100 ? 
          &lt;div className=&quot;apple-target&quot; onClick={clickTarget} style={appleStyle}&gt;&lt;/div&gt;
          : &lt;h1 className=&quot;win&quot;&gt; You Win!&lt;/h1&gt;
        }
      &lt;/div&gt;
    &lt;/&gt;
  )
}
</code></pre>

</details>

<details>
<summary>Show Me: complete file structure</summary>

<pre><code class="language-jsx">import { useState } from &#039;react&#039;
import &#039;./App.css&#039;

function randomNumber(a, b) {
  return Math.floor(Math.random() * (b - a) + a);
}

// NEW: Stats component
function Stats({ score, lives, style }) {
  return (
    &lt;div className=&quot;stats&quot; style={style}&gt;
      Score: {score} Lives: {lives}
    &lt;/div&gt;
  )
}

function App() {
  // ... rest of App component
}

export default App
</code></pre>

</details>

## ✅ Check

1. Stats should still display correctly
2. Colors should still change based on score
3. No console errors about missing props
4. The game should function exactly as before
5. Your code should feel more organized

**Understanding Props:**
- Props are like function parameters for components
- They pass data from parent to child
- Use destructuring `{ score, lives }` to extract props
- Props are read-only (never modify them directly)

**Why Extract Components?**
- **Reusability:** Use the same component in multiple places
- **Organization:** Each component has a single responsibility
- **Testing:** Easier to test small components
- **Readability:** Clearer code structure

---

# Level 13: Create GameBoard Component with Children

**User Story:** As a developer, I want to use the children prop pattern so that I can create flexible wrapper components.

## What You'll Do

Extract the orchard background into a `GameBoard` component that uses the `children` prop pattern.

## Instructions

- Create a new `GameBoard` component above `Stats`
- The component should accept `onMiss` and `children` as props
- Move the orchard-background div logic into this component
- The component should render `children` inside the orchard-background div
- In `App`, wrap your apple/win message with `<GameBoard onMiss={missTarget}>`
- Test that clicking the background still works

## 💡 Code Hints

Need help with the children prop? Check out these snippets:

<details>
<summary>Show Me: GameBoard component definition</summary>

<pre><code class="language-jsx">function GameBoard({ onMiss, children }) {
  return (
    &lt;div className=&#039;orchard-background&#039; onClick={onMiss}&gt;
      {children}
    &lt;/div&gt;
  )
}
</code></pre>

</details>

<details>
<summary>Show Me: using GameBoard in App</summary>

<pre><code class="language-jsx">return (
  &lt;&gt;
    &lt;Stats score={score} lives={lives} style={statsStyle} /&gt;
    &lt;GameBoard onMiss={missTarget}&gt;
      { score &lt; 100 ? 
        &lt;div className=&quot;apple-target&quot; onClick={clickTarget} style={appleStyle}&gt;&lt;/div&gt;
        : &lt;h1 className=&quot;win&quot;&gt; You Win!&lt;/h1&gt;
      }
    &lt;/GameBoard&gt;
  &lt;/&gt;
)
</code></pre>

</details>

<details>
<summary>Show Me: complete component structure</summary>

<pre><code class="language-jsx">import { useState } from &#039;react&#039;
import &#039;./App.css&#039;

function randomNumber(a, b) {
  return Math.floor(Math.random() * (b - a) + a);
}

// NEW: GameBoard component with children
function GameBoard({ onMiss, children }) {
  return (
    &lt;div className=&#039;orchard-background&#039; onClick={onMiss}&gt;
      {children}
    &lt;/div&gt;
  )
}

function Stats({ score, lives, style }) {
  return (
    &lt;div className=&quot;stats&quot; style={style}&gt;
      Score: {score} Lives: {lives}
    &lt;/div&gt;
  )
}

function App() {
  const [score, setScore] = useState(0)
  const [lives, setLives] = useState(3)
  const [appleSize, setAppleSize] = useState(100)
  const [appleX, setAppleX] = useState(0);
  const [appleY, setAppleY] = useState(0);

  // ... all your functions ...

  return (
    &lt;&gt;
      &lt;Stats score={score} lives={lives} style={statsStyle} /&gt;
      &lt;GameBoard onMiss={missTarget}&gt;
        { score &lt; 100 ? 
          &lt;div className=&quot;apple-target&quot; onClick={clickTarget} style={appleStyle}&gt;&lt;/div&gt;
          : &lt;h1 className=&quot;win&quot;&gt; You Win!&lt;/h1&gt;
        }
      &lt;/GameBoard&gt;
    &lt;/&gt;
  )
}

export default App
</code></pre>

</details>

## ✅ Check

1. The game should look and work exactly as before
2. Missing the apple should still decrease lives
3. Clicking the apple should still work (not trigger the miss handler)
4. No console errors
5. Your code should be more modular and organized

**Understanding Children:**
- `children` is a special prop in React
- It represents whatever is placed between component tags
- Like HTML: `<div>content here</div>` → content is children
- Makes components flexible and reusable

**The Children Pattern:**
```jsx
<GameBoard>
  <Apple />
  <WinMessage />
</GameBoard>
```
The `Apple` and `WinMessage` components become the `children` prop of `GameBoard`.

**Why Use Children?**
- **Flexibility:** GameBoard doesn't need to know what's inside it
- **Composition:** Build complex UIs from simple pieces
- **Reusability:** Same GameBoard can contain different content
- **Separation of Concerns:** Parent decides content, child handles layout

---

# Level 14: Testing and Polish

**User Story:** As a developer, I want to test my game thoroughly so that I can ensure it works perfectly.

## What You'll Do

Perform comprehensive testing and add any final improvements.

## Instructions

- Test all game mechanics:
  - Clicking the apple increases score
  - Missing decreases lives
  - Apple changes size randomly
  - Apple moves to random positions
  - Stats bar changes colors
  - Win condition triggers at 100
- Test edge cases:
  - What happens if lives reach 0? (Currently nothing - this is okay)
  - Can you click past 100 points? (No - game ends)
  - Do small apples still work?
- Check styling:
  - Is everything centered properly?
  - Are colors readable?
  - Does the layout look good?
- Consider improvements:
  - Add a "Game Over" condition when lives = 0
  - Add a reset button
  - Add sound effects
  - Track high score

## 💡 Code Hints

Need help with testing? Check out these tips:

**Testing Checklist:**
- [ ] Score increases on apple click
- [ ] Lives decrease on background click
- [ ] Apple size changes randomly
- [ ] Apple position changes randomly
- [ ] Stats colors change at correct thresholds
- [ ] Win message appears at 100 points
- [ ] Apple disappears when winning
- [ ] No console errors

**Common Issues:**
- If clicks don't work: Check `onClick` handlers
- If state doesn't update: Check `setState` calls
- If styling is broken: Check CSS class names
- If images don't load: Check file paths

## ✅ Check

1. Run through the complete game at least twice
2. Try to break it with rapid clicks
3. Test with very small apples (harder to click)
4. Verify win condition works consistently
5. Check browser console for any errors
6. Test in different browsers if possible

---

# Level 15: Code Review and Understanding

**User Story:** As a developer, I want to understand every part of my code so that I can explain it and build on it.

## What You'll Do

Review your complete code and make sure you understand each concept.

## Key Concepts to Understand

### React Hooks - useState
```jsx
const [value, setValue] = useState(initialValue)
```
- **What it does:** Creates a state variable that persists between renders
- **Why we need it:** Regular variables reset on every render
- **How to update:** Always use the setter function (setValue)

### Event Handling
```jsx
<div onClick={handleClick}>Click me</div>
```
- **onClick:** Attaches event listener for clicks
- **event parameter:** Contains information about the click event
- **event.stopPropagation():** Prevents click from bubbling to parent

### Dynamic Styling
```jsx
const style = { width: "100px", backgroundColor: "red" }
<div style={style}>Styled</div>
```
- **Inline styles:** JavaScript objects with CSS properties
- **camelCase:** CSS properties use camelCase (backgroundColor not background-color)
- **Units:** Values need units as strings ("100px")

### Conditional Rendering
```jsx
{condition && <Component />}           // Render OR nothing
{condition ? <CompA /> : <CompB />}    // Render A OR B
```

### Random Numbers
```jsx
Math.floor(Math.random() * (max - min) + min)
```
- **Math.random():** Returns decimal 0-1
- **Multiply by range:** Scale to desired range
- **Add minimum:** Shift to starting point
- **Math.floor():** Round down to integer

## ✅ Check

Can you answer these questions?

1. **Why do we use `useState` instead of regular variables?**
   <details>
<summary>Answer</summary>

<p>Regular variables reset on every render. State persists and triggers re-renders.</p>

</details>

2. **Why do we need `event.stopPropagation()` in clickTarget?**
   <details>
<summary>Answer</summary>

<p>To prevent the click from bubbling up to the parent and triggering missTarget.</p>

</details>

3. **How does the ternary operator work in JSX?**
   <details>
<summary>Answer</summary>

<p>It evaluates a condition and renders one component if true, another if false.</p>

</details>

4. **Why are styles in camelCase instead of kebab-case?**
   <details>
<summary>Answer</summary>

<p>Because they're JavaScript object properties, not CSS. JavaScript uses camelCase.</p>

</details>

5. **How does `randomNumber(0, 400)` work?**
   <details>
<summary>Answer</summary>

<p>It generates a random integer from 0 to 399 (inclusive).</p>

</details>

---

# Level 16: Documentation and README

**User Story:** As a developer, I want to create clear documentation so that others can understand and use my game.

## What You'll Do

Update your README.md with comprehensive project documentation.

## Instructions

- Replace the default Vite README with your own
- Include these sections:
  - Project title and description
  - Features list
  - Technologies used
  - How to install and run
  - How to play the game
  - Future enhancements
  - What you learned

## 💡 Code Hints

Need help with README structure? Check out this template:

<details>
<summary>Show Me: README template</summary>

<pre><code class="language-markdown"># Apple Clicker Game 🍎

An interactive clicker game built with React and Vite where players click on randomly appearing apples to score points.

## Features

- Dynamic apple sizing and positioning
- Score and lives tracking
- Progressive color changes based on score
- Win condition at 100 points
- Responsive click interactions

## Technologies Used

- React 19
- Vite
- CSS3
- JavaScript ES6+

## Installation

</code></pre>bash
<p>npm install</p>
<p>``<code></p>

<p>## Running the Game</p>

<pre><code class="language-bash">npm run dev
</code></pre>

<p>Open your browser to </code>http://localhost:5173<code></p>

<p>## How to Play</p>

<p>1. Click on the apple to score points</p>
<p>2. Missing the apple costs a life</p>
<p>3. The apple changes size and position after each click</p>
<p>4. Watch the stats bar change colors as you progress</p>
<p>5. Reach 100 points to win!</p>

<p>## Game Mechanics</p>

<p>- <strong>Score:</strong> Increases by 1 for each apple clicked</p>
<p>- <strong>Lives:</strong> Start with 3, decrease when you miss</p>
<p>- <strong>Apple Size:</strong> Random between 20-100 pixels</p>
<p>- <strong>Apple Position:</strong> Random location within game board</p>
<p>- <strong>Win Condition:</strong> Score reaches 100 points</p>

<p>## What I Learned</p>

<p>- React useState hook for state management</p>
<p>- Event handling and propagation</p>
<p>- Dynamic inline styling with JavaScript</p>
<p>- Conditional rendering with ternary operators</p>
<p>- Random number generation</p>
<p>- CSS positioning (absolute/relative)</p>

<p>## Future Enhancements</p>

<p>- Add game over condition when lives reach 0</p>
<p>- Add restart button</p>
<p>- Add sound effects</p>
<p>- Track high score with localStorage</p>
<p>- Add difficulty levels</p>
<p>- Add timer/countdown mode</p>

<p>## Author</p>

<p>[Your Name]</p>

<p>## License</p>

<p>MIT</p>
</code>``

</details>

## ✅ Check

1. README clearly describes the project
2. Installation instructions are complete
3. How to play section is clear
4. Technologies are listed
5. Documentation is professional and helpful

---

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

# Level 18: Challenge Extensions ⚡

**CHALLENGE LEVEL**

**User Story:** As a developer, I want to implement advanced features so that I can challenge myself and create a more impressive game.

## What You'll Do

Choose from these advanced challenges to extend your game.

## Challenge Options

### Challenge 1: Game Over Condition
**Difficulty:** ⭐ Easy

Add a game over condition when lives reach 0.

**Instructions:**
- Add conditional rendering for when `lives <= 0`
- Show a "Game Over!" message
- Hide the apple
- Display final score
- Optionally add a restart button

<details>
<summary>Hint: Conditional structure</summary>

<pre><code class="language-jsx">if (lives &lt;= 0) {
  return &lt;GameOverScreen score={score} /&gt;
}
</code></pre>

</details>

---

### Challenge 2: Restart Functionality
**Difficulty:** ⭐ Easy

Add a button to restart the game.

**Instructions:**
- Create a `restartGame()` function
- Reset all state variables to initial values
- Add a restart button (visible on win or game over)
- Style the button

<details>
<summary>Hint: Reset function</summary>

<pre><code class="language-jsx">function restartGame() {
  setScore(0)
  setLives(3)
  setAppleSize(100)
  setAppleX(0)
  setAppleY(0)
}
</code></pre>

</details>

---

### Challenge 3: High Score with localStorage
**Difficulty:** ⭐⭐ Medium

Track and display the highest score using browser storage.

**Instructions:**
- Use `localStorage.getItem()` and `setItem()`
- Create state for `highScore`
- Update high score when game ends
- Display high score in stats or on win screen

<details>
<summary>Hint: localStorage usage</summary>

<pre><code class="language-jsx">// Load high score on mount
const [highScore, setHighScore] = useState(() =&gt; {
  return parseInt(localStorage.getItem(&#039;highScore&#039;)) || 0
})

// Save when game ends
if (score &gt; highScore) {
  setHighScore(score)
  localStorage.setItem(&#039;highScore&#039;, score)
}
</code></pre>

</details>

---

### Challenge 4: Sound Effects
**Difficulty:** ⭐⭐ Medium

Add sound effects for clicks, misses, and winning.

**Instructions:**
- Find or create sound files
- Use HTML5 Audio API or `<audio>` elements
- Play sounds on different game events
- Consider adding a mute button

<details>
<summary>Hint: Playing sounds</summary>

<pre><code class="language-jsx">const clickSound = new Audio(&#039;/click.mp3&#039;)

function clickTarget(event) {
  event.stopPropagation();
  clickSound.play()
  setScore(score + 1)
  // ... rest of function
}
</code></pre>

</details>

---

### Challenge 5: Timer/Countdown Mode
**Difficulty:** ⭐⭐⭐ Hard

Add a timer that counts down, creating urgency.

**Instructions:**
- Add state for `timeRemaining`
- Use `useEffect` with `setInterval` for countdown
- Game ends when time reaches 0
- Display timer in stats
- Clean up interval on unmount

<details>
<summary>Hint: Timer with useEffect</summary>

<pre><code class="language-jsx">useEffect(() =&gt; {
  if (timeRemaining &gt; 0) {
    const timer = setInterval(() =&gt; {
      setTimeRemaining(time =&gt; time - 1)
    }, 1000)
    
    return () =&gt; clearInterval(timer)
  }
}, [timeRemaining])
</code></pre>

</details>

---

### Challenge 6: Difficulty Levels
**Difficulty:** ⭐⭐⭐ Hard

Add Easy/Medium/Hard difficulty levels.

**Instructions:**
- Create difficulty selection screen
- Adjust game parameters based on difficulty:
  - Easy: Larger apples, slower changes
  - Medium: Current settings
  - Hard: Smaller apples, more lives lost
- Store difficulty in state
- Allow changing difficulty

---

### Challenge 7: Animations
**Difficulty:** ⭐⭐⭐ Hard

Add smooth animations for apple movement and size changes.

**Instructions:**
- Use CSS transitions for smooth size changes
- Consider React Spring or Framer Motion for animations
- Animate apple movement between positions
- Add particle effects on click

<details>
<summary>Hint: CSS transitions</summary>

<pre><code class="language-css">.apple-target {
  transition: all 0.3s ease-in-out;
}
</code></pre>

</details>

---

### Challenge 8: Mobile Support
**Difficulty:** ⭐⭐ Medium

Make the game work well on mobile devices.

**Instructions:**
- Add touch event support
- Make game board responsive
- Adjust sizes for smaller screens
- Test on mobile devices

---

## ✅ Check

1. Choose at least one challenge to implement
2. Test your new feature thoroughly
3. Update your README with new features
4. Commit your changes with descriptive messages
5. Consider adding screenshots or GIFs

---

# Level 19: Project Complete! 🎉

**Congratulations!** You've successfully built a complete Apple Clicker game using React!

## What You've Accomplished

You've built a fully functional game that demonstrates:

- ✅ **React Fundamentals** - Components, JSX, props
- ✅ **Component Composition** - Breaking down UI into reusable pieces
- ✅ **Props Pattern** - Passing data to child components
- ✅ **Children Prop** - Creating flexible wrapper components
- ✅ **State Management** - useState hook for game state
- ✅ **Event Handling** - Click events and propagation
- ✅ **Dynamic Styling** - Inline styles with JavaScript
- ✅ **Conditional Rendering** - Show/hide elements based on state
- ✅ **Random Number Generation** - Math.random for game mechanics
- ✅ **CSS Positioning** - Absolute and relative positioning
- ✅ **User Interaction** - Responsive click interactions
- ✅ **Game Logic** - Win conditions and scoring systems

## Skills You've Developed

Through this project, you've gained hands-on experience with:

- Setting up a modern React development environment with Vite
- Creating and extracting React components
- Passing props between parent and child components
- Using the children prop for component composition
- Managing multiple pieces of state in a component
- Understanding event propagation and why stopPropagation matters
- Creating dynamic, computed styles based on application state
- Using both && and ternary operators for conditional rendering
- Working with CSS positioning for game elements
- Debugging React applications
- Reading and writing clean, maintainable code

## Next Steps

### Continue Learning React
- Build more interactive applications
- Learn about useEffect for side effects
- Explore React Router for multi-page apps
- Learn about Context API for global state

### Expand This Project
- Implement one or more challenge extensions
- Add backend with Node.js to save scores
- Create multiple game modes
- Add multiplayer functionality

### Build New Projects
- Todo list application
- Weather app with API integration
- Blog or social media clone
- Portfolio website

## Resources

- [React Official Documentation](https://react.dev)
- [Vite Documentation](https://vitejs.dev)
- [MDN Web Docs - JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [React Tutorial - Tic Tac Toe](https://react.dev/learn/tutorial-tic-tac-toe)

## Share Your Work!

Consider:
- Pushing your project to GitHub
- Deploying to Netlify or Vercel
- Adding it to your portfolio
- Sharing with friends and getting feedback

---

## 🎊 Well Done!

You've completed a significant milestone in your React journey. Your Apple Clicker game demonstrates your ability to build interactive web applications and solve problems with code.

Keep building, keep learning, and keep growing as a developer!

**Project Status: Complete!** ✨

---

## Troubleshooting Guide

### Common Issues and Solutions

**Apple doesn't appear:**
- Check that images are in `public/` folder
- Verify file names match exactly (case-sensitive)
- Check browser console for 404 errors

**Clicks don't work:**
- Verify `onClick` handlers are attached
- Check for JavaScript errors in console
- Ensure functions are defined before JSX

**State doesn't update:**
- Make sure you're using the setter function (setScore, not score = )
- Check that useState is imported from React
- Verify you're not mutating state directly

**Apple triggers both handlers:**
- Add `event.stopPropagation()` to clickTarget
- This prevents the click from bubbling to parent

**Styles don't apply:**
- Check className spelling
- Verify CSS file is imported
- For inline styles, ensure style={styleObject} syntax

**Random positioning is off:**
- Verify your random ranges match game board size
- Remember: 0-400 for X (board is 500px wide)
- Remember: 0-600 for Y (board is 700px tall)

---

*Built with ❤️ using React and Vite*

