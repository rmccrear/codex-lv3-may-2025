# Fetch Kata with Map Assignment

## Objective
Practice using the Fetch API and the `map()` method to fetch data from an API and transform it for display in your application.

---

## Assignment Overview

You will create a React component that:
1. Fetches data from a public API using the Fetch API
2. Uses the `map()` method to transform and display the data
3. Handles loading and error states
4. Displays the data in a user-friendly format

---

## Instructions

### Step 1: Choose an API
Select one of these free APIs (or find your own):

**Recommended APIs:**
- **[JSONPlaceholder](https://jsonplaceholder.typicode.com/)** - Fake REST API for testing
  - Users: `https://jsonplaceholder.typicode.com/users`
  - Posts: `https://jsonplaceholder.typicode.com/posts`
  - Albums: `https://jsonplaceholder.typicode.com/albums`
- **[Dog API](https://dog.ceo/dog-api/)** - Random dog images
  - Breeds list: `https://dog.ceo/api/breeds/list/all`
- **[Pokemon API](https://pokeapi.co/)** - Pokemon data
  - Pokemon list: `https://pokeapi.co/api/v2/pokemon?limit=20`
- **[Random User API](https://randomuser.me/)** - Random user data
  - Users: `https://randomuser.me/api/?results=10`

### Step 2: Create Your Component
Create a React component that:

1. **Fetches data** using `fetch()` in a `useEffect` hook
2. **Stores data** in state using `useState`
3. **Handles loading** - Show a loading message while fetching
4. **Handles errors** - Display error message if fetch fails
5. **Maps over data** - Use `.map()` to render each item
6. **Displays data** - Show the data in a list, cards, or table format

### Step 3: Transform the Data
Use `map()` to:
- Extract specific fields from the API response
- Format the data for display (e.g., format dates, capitalize names)
- Create JSX elements for each item
- Add styling or structure to each item

### Step 4: Add Interactivity (Optional Challenge)
- Add a button to refresh/fetch new data
- Add filtering or sorting functionality
- Add search functionality
- Add pagination

---

## Example Structure

```javascript
import { useState, useEffect } from 'react';

function DataDisplay() {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    // Fetch data here
  }, []);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error.message}</div>;

  return (
    <div>
      {data.map((item, index) => (
        // Render each item here
      ))}
    </div>
  );
}
```

---

## Required Deliverables

Submit the following through Moodle:

1. **GitHub Repository Link**
   - Include your React component file
   - Show the component integrated into your app
   - Make sure the repository is public or shared with your instructor

2. **Code Files**
   - Your component file with fetch and map implementation
   - Any additional helper functions or utilities

3. **Screenshot or Video**
   - Show your component displaying the fetched data
   - Show the browser console (to verify the API call)
   - If you added interactivity, demonstrate it

4. **Brief Explanation** (2-3 paragraphs)
   - Which API did you use and why?
   - How did you use `map()` to transform the data?
   - What challenges did you face with the Fetch API?

---

## Grading Criteria

- **30%** - Fetch Implementation (Correctly fetches data from API)
- **30%** - Map Usage (Properly uses `.map()` to transform and display data)
- **20%** - Error Handling (Handles loading and error states)
- **10%** - Code Quality (Clean, readable code with proper structure)
- **10%** - Display Quality (Data is displayed in a user-friendly format)

**Total: 100 points**

**Bonus Points (up to 10 points):**
- Add interactivity (refresh, filter, search, etc.)
- Use multiple API endpoints
- Add styling to make it visually appealing

---

## Resources

- **[MDN: Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)** - Complete Fetch API documentation
- **[MDN: Array.map()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map)** - Array map method documentation
- **[React: useEffect Hook](https://react.dev/reference/react/useEffect)** - React useEffect documentation
- **[Public APIs List](https://github.com/public-apis/public-apis)** - Comprehensive list of free APIs

---

## Tips

- Start with a simple API like JSONPlaceholder
- Test your API endpoint in the browser first
- Use `console.log()` to inspect the API response structure
- Handle the case where the API might be slow or fail
- Use unique `key` props when mapping over items in React
- Consider using optional chaining (`?.`) when accessing nested data

---

## Common Patterns

**Fetching data:**
```javascript
fetch('https://api.example.com/data')
  .then(response => response.json())
  .then(data => setData(data))
  .catch(error => setError(error));
```

**Mapping over data:**
```javascript
{data.map((item, index) => (
  <div key={item.id || index}>
    <h3>{item.name}</h3>
    <p>{item.description}</p>
  </div>
))}
```

---

**Questions?** Ask in the discussion forum or review the [React documentation on useEffect](https://react.dev/reference/react/useEffect).

**Good luck!** 🚀

