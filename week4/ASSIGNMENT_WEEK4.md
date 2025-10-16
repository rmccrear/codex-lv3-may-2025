# Week 4 Assignment: React Hackathon - Data-Driven App

## Overview
Build a multi-screen React application that uses a dataset in a meaningful way. You'll work with a partner to design, prototype, and develop an app that demonstrates list traversal methods (map, reduce, or filter) and incorporates real data.

## Learning Objectives
By the end of this assignment, you'll be able to:
- Design and build a multi-screen React application
- Import and work with external datasets in JSON format
- Use list traversal methods (map, reduce, filter) to process data
- Collaborate effectively using pair programming
- Create paper prototypes to plan user interfaces
- Navigate between screens in a React app

## Resources

### Required Links:
- 📋 [Hackathon Planning Sheet](https://docs.google.com/document/d/12QYQpFen_lD5iYS1hy4Wmtc0_QUq0cHjWwoyR-LEViw/edit?usp=sharing)
- 💻 [Hackathon on Code.org for data access](https://studio.code.org/courses/csp-2025/units/6/lessons/13/levels/1)
- 📊 [How to import data--Spreadsheets to JSON](./HOWTO_CODE_ORG_DATA_IMPORT.md)

## Project Requirements

### App Requirements

Your app must include:

✅ **At least three screens**
- Home/landing page (example)
- Data display/list screen (example)
- Detail or results screen (example)

✅ **Easy navigation**
- All screens can be easily navigated to through the user interface
- Clear buttons, links, or menu for navigation

✅ **Dataset integration**
- A dataset used in a meaningful way towards the program's purpose
- Data imported from JSON file

✅ **List traversal**
- At least one list is traversed using: **map**, **reduce**, or **filter** (indicate which in a comment)
- Used in a meaningful way towards the program's purpose

✅ **Programming constructs**
- Variable(s)
- Function(s)
- Conditional(s)
- List(s)
- Loop(s)

✅ **Documentation**
- All functions include comments that explain their purpose and how they work

✅ **Code quality**
- No errors in the code
- Clean, readable code

## Submission Requirements

You will submit:

1. ✅ **Your final React app** (GitHub repository link)
2. ✅ **Completed project-planning guide** (from Hackathon Planning Sheet)
3. ✅ **A written response** explaining:
   - Your app's purpose
   - How you used the dataset
   - Which list traversal method(s) you used and why
   - Challenges you faced and how you solved them

## Steps to Complete

### Step 1: Choose Your Dataset (30 minutes)

**With Your Partner:**
1. Browse available datasets on Code.org or find your own
2. Discuss what kind of app would be meaningful for this data
3. Consider questions like:
   - What story does this data tell?
   - What would users want to learn from this data?
   - What comparisons or calculations would be useful?

**Popular Dataset Ideas:**
- Spotify/Music data
- Sports statistics
- Environmental data
- Movie or book data
- State/city demographics
- Health or nutrition data

### Step 2: Decide on Your App Concept (30 minutes)

**Brainstorm together:**
1. What is the main purpose of your app?
2. What will users be able to do?
3. How will you traverse the list?

**List Traversal Brainstorm**

Choose **at least one** traversal method to use in your app:

#### **MAP** (do one thing to every item in the list)
Examples:
- Display all songs with their duration in minutes
- Show all movies with their release year formatted
- Convert all temperatures from Celsius to Fahrenheit

```jsx
// Example: Display all items with formatted data
const formattedItems = data.map((item) => {
  return {
    ...item,
    displayName: `${item.name} (${item.year})`
  };
});
```

#### **REDUCE** (summarize something about this list into a single number or string)
Examples:
- Calculate total population across states
- Find average rating of all movies
- Count total number of songs by a specific artist

```jsx
// Example: Calculate total using a for loop
let total = 0;
for (let i = 0; i < data.length; i++) {
  total = total + data[i].value;
}
// Now 'total' contains the sum of all values
```

#### **FILTER** (select only a few elements out of a list)
Examples:
- Show only songs from a specific genre
- Display movies released after 2020
- Find states with population over 1 million

```jsx
// Example: Filter items by criteria using a for loop
const filtered = [];
for (let i = 0; i < data.length; i++) {
  if (data[i].category === "Rock") {
    filtered.push(data[i]);
  }
}
// Now 'filtered' contains only items with category "Rock"
```

### Step 3: Create a Paper Prototype (45 minutes)

**Design Phase - With Your Partner**

Create a paper prototype that shows:
- All three (or more) screens
- Buttons, text, and images the user will see
- Navigation flow between screens (draw arrows!)
- Where data will be displayed
- Where list traversal happens

**Tips:**
- Draw each screen on a separate piece of paper
- Label all buttons and interactive elements
- Show how clicking moves between screens
- Indicate where your dataset appears
- Mark where you'll use map/reduce/filter

![example design](./assets/hackathon-design-example.png)

**Take a photo** of your paper prototype and include it in your planning guide!

### Step 4: Set Up Your React Project (30 minutes)

1. **Initialize your React app:**
   ```bash
   npm create vite@latest hackathon-app -- --template react
   cd hackathon-app
   npm install
   ```

2. **Import your dataset:**
   - Follow the [HOWTO guide](./HOWTO_CODE_ORG_DATA_IMPORT.md) to export data from Code.org
   - Convert to JSON using TableConvert
   - Place the JSON file in your `src` folder
   - Import in your component:
     ```jsx
     import data from './data.json';
     ```

3. **Set up folder structure:**
   ```
   src/
   ├── components/
   │   ├── Navbar.jsx
   │   ├── Home.jsx
   │   ├── DataList.jsx
   │   └── Details.jsx
   ├── data.json
   ├── App.jsx
   └── main.jsx
   ```

### Step 5: Divide Roles and Build

#### **Designer:**
- Create the screens/components
- Design the layout and styling
- Ensure navigation works between screens
- Support the programmer with pair programming as needed

#### **Programmer:**
- Program the data processing logic
- Implement map/reduce/filter functionality
- Handle state management
- Add comments to all functions
- Support the designer as needed

**Pair Programming Tips:**
- Switch roles every 30 minutes
- Both partners should understand all code
- Talk through problems together
- Test frequently as you build

### Step 6: Implement Core Features

#### Navigation Between Screens
Use React Router or state-based navigation:

```jsx
// Simple state-based navigation example
function App() {
  const [currentScreen, setCurrentScreen] = useState('home');
  
  return (
    <>
      {currentScreen === 'home' && <Home goTo={setCurrentScreen} />}
      {currentScreen === 'list' && <DataList goTo={setCurrentScreen} />}
      {currentScreen === 'details' && <Details goTo={setCurrentScreen} />}
    </>
  );
}
```

#### Display Data Using Map

```jsx
function DataList({ data }) {
  return (
    <div>
      <h2>All Items</h2>
      {/* MAP: Transform and display every item */}
      {data.map((item, index) => (
        <div key={index} className="item-card">
          <h3>{item.name}</h3>
          <p>{item.description}</p>
        </div>
      ))}
    </div>
  );
}
```

#### Calculate Summary Using Reduce

```jsx
function Summary({ data }) {
  // REDUCE: Calculate total from all items using a for loop
  let total = 0;
  for (let i = 0; i < data.length; i++) {
    total = total + data[i].value;
  }
  
  return (
    <div>
      <h3>Total: {total}</h3>
    </div>
  );
}
```

#### Filter Data Based on Criteria

```jsx
function FilteredList({ data, category }) {
  // FILTER: Show only items matching criteria using a for loop
  const filtered = [];
  for (let i = 0; i < data.length; i++) {
    if (data[i].category === category) {
      filtered.push(data[i]);
    }
  }
  
  return (
    <div>
      <h2>{category} Items</h2>
      <p>Found {filtered.length} items</p>
      {filtered.map((item, index) => (
        <div key={index}>{item.name}</div>
      ))}
    </div>
  );
}
```

### Step 7: Add Comments and Documentation

Add comments to **all functions** explaining:
- What the function does
- What parameters it takes
- What it returns
- Any important logic

```jsx
/**
 * Calculates the average rating from an array of movies
 * @param {Array} movies - Array of movie objects with rating property
 * @returns {Number} - The average rating rounded to 2 decimal places
 */
function calculateAverageRating(movies) {
  // REDUCE: Sum all ratings using a for loop
  let total = 0;
  for (let i = 0; i < movies.length; i++) {
    total = total + movies[i].rating;
  }
  // Calculate average
  const average = total / movies.length;
  return average.toFixed(2);
}
```

### Step 8: Test and Debug

**Testing Checklist:**
- [ ] All three screens display correctly
- [ ] Navigation works between all screens
- [ ] Data loads and displays properly
- [ ] Map/reduce/filter works as expected
- [ ] No console errors
- [ ] All functions have comments
- [ ] Code is clean and readable

### Step 9: Complete Documentation

Fill out the [Hackathon Planning Sheet](https://docs.google.com/document/d/12QYQpFen_lD5iYS1hy4Wmtc0_QUq0cHjWwoyR-LEViw/edit?usp=sharing) with:
- Your app name and purpose
- Dataset you used
- List traversal methods you implemented
- Challenges and solutions
- Screenshots of your paper prototype
- Link to your GitHub repository

### Step 10: Write Your Reflection

Write a response (300-500 words) addressing:

1. **App Purpose**: What problem does your app solve or what information does it provide?

2. **Dataset Usage**: How did you use the dataset? Why did you choose this data?

3. **List Traversal**: Which method(s) did you use (map/reduce/filter)? Explain specifically where in your code and why it was appropriate.

4. **Collaboration**: How did you and your partner divide the work? What worked well?

5. **Challenges**: What was difficult? How did you overcome obstacles?

6. **Learning**: What did you learn from this project?

## Rubric

| Criteria | Points | Description |
|----------|--------|-------------|
| **Three+ Screens** | 15 | App has at least three distinct screens |
| **Navigation** | 10 | Easy navigation between all screens via UI |
| **Dataset Integration** | 20 | Dataset used meaningfully toward app's purpose |
| **List Traversal** | 25 | Map/reduce/filter used correctly and meaningfully (commented) |
| **Programming Constructs** | 10 | Uses variables, functions, conditionals, lists, loops |
| **Comments** | 10 | All functions have clear explanatory comments |
| **No Errors** | 5 | Code runs without errors |
| **Planning Document** | 10 | Complete planning sheet with prototype photos |
| **Written Reflection** | 10 | Thoughtful response addressing all prompts |
| **Total** | **115** | Extra credit available for exceptional work |

## Submission Instructions

1. **Push to GitHub:**
   ```bash
   git init
   git add .
   git commit -m "Complete Week 4 Hackathon project"
   git branch -M main
   git remote add origin [your-repo-url]
   git push -u origin main
   ```

2. **Submit on Moodle:**
   - Link to GitHub repository
   - Link to completed Planning Sheet (Google Doc)
   - Written reflection (in Moodle text box or uploaded document)
   - (Optional) Link to deployed app on Netlify

## Example Projects

### Example 1: Music Playlist Analyzer
- **Screens**: Home, Song List, Statistics
- **Dataset**: Spotify Viral 50 USA
- **List Methods**:
  - MAP: Display all songs with formatted duration
  - REDUCE: Calculate total playtime of playlist
  - FILTER: Show only songs with high popularity score

### Example 2: State Demographics Explorer
- **Screens**: Home, State List, State Details
- **Dataset**: US State Legislators by Gender
- **List Methods**:
  - MAP: Show each state with percentage calculated
  - FILTER: Show only states above/below certain threshold
  - REDUCE: Calculate national average

### Example 3: Movie Rating App
- **Screens**: Home, Movie List, Top Rated
- **Dataset**: Movie ratings and reviews
- **List Methods**:
  - MAP: Display movies with formatted release dates
  - FILTER: Show only movies with rating > 4 stars
  - REDUCE: Calculate average rating across all movies

## Common Issues and Solutions

### Issue: Data not loading
**Solution**: Check your import statement and file path. Make sure the JSON file is in the src folder.

### Issue: Map/filter/reduce not working
**Solution**: Console.log your data first to see its structure. Make sure you're accessing the correct property names.

### Issue: Navigation not working
**Solution**: Check your state management or routing setup. Make sure onClick handlers are correctly passing screen names.

### Issue: Comments unclear
**Solution**: Explain what the function does in plain English first, then what each main step does.

## Tips for Success

### Partnership Tips:
- 🤝 Communicate constantly
- 🔄 Switch roles regularly
- 📝 Both partners should understand all code
- 🎯 Set small goals and celebrate progress

### Technical Tips:
- 💾 Commit to GitHub frequently
- 🧪 Test each feature as you build it
- 🔍 Use console.log to debug
- 📱 Keep the design simple and functional

### Time Management:
- ⏰ Spend adequate time on planning (don't skip the prototype!)
- 🎨 Don't get stuck on styling - functionality first
- 📊 Start with map - it's the most straightforward
- ✍️ Write comments as you code, not at the end

## Learning Outcomes

After completing this hackathon, you will:
- ✅ Understand how to work with real datasets in React
- ✅ Know when and how to use map, reduce, and filter
- ✅ Have experience building multi-screen applications
- ✅ Understand the design-to-code workflow
- ✅ Have practiced pair programming collaboration
- ✅ Be able to document and explain your code

## Additional Resources

### Documentation:
- [Array.map() - MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map)
- [Array.reduce() - MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduce)
- [Array.filter() - MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter)
- [React useState Hook](https://react.dev/reference/react/useState)

### Video Tutorials:
- [Map, Filter, Reduce Explained](https://www.youtube.com/watch?v=rRgD1yVwIvE)
- [Multi-page React Apps](https://www.youtube.com/watch?v=Law7wfdg_ls)

---

**Good luck with your hackathon!** Remember: plan well, communicate often, and test frequently. You've got this! 🚀
