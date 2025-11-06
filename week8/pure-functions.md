# Pure Functions vs Functions with Side Effects

## What is a Pure Function?

A **pure function** is a function that:

1. **Always returns the same output** for the same input
2. **Has no side effects** - it doesn't modify anything outside of itself
3. **Doesn't depend on external state** - it only uses its parameters

### Example of a Pure Function

```javascript
// Pure function
function add(a, b) {
  return a + b;
}

// Always returns the same result for the same inputs
add(2, 3); // Always returns 5
add(2, 3); // Always returns 5 (same input = same output)
```

## What are Side Effects?

**Side effects** are changes that a function makes outside of its own scope, such as:

- Modifying variables outside the function
- Modifying the DOM
- Making API calls
- Writing to files or databases
- Printing to console (technically a side effect, but often acceptable)
- Modifying global state

### Example of a Function with Side Effects

```javascript
let total = 0;

// Function with side effects
function addToTotal(amount) {
  total += amount; // Modifies external variable
  console.log(`Total is now: ${total}`); // Side effect: console output
  return total;
}

addToTotal(5); // Returns 5, but also changes `total` and logs to console
addToTotal(5); // Returns 10 (different result even with same input!)
```

## Comparison

| Pure Function | Function with Side Effects |
|--------------|---------------------------|
| ✅ Same input → Same output | ❌ Same input → May produce different output |
| ✅ No external dependencies | ❌ May depend on external state |
| ✅ Easy to test | ❌ Harder to test (need to mock/setup state) |
| ✅ Easy to reason about | ❌ Can be unpredictable |
| ✅ Can be reused safely | ❌ May cause unexpected behavior |

## Why Use Pure Functions?

1. **Easier to test** - No need to set up external state
2. **More predictable** - Same input always gives same output
3. **Easier to debug** - No hidden dependencies
4. **Reusable** - Can be used anywhere without side effects
5. **Better for refactoring** - Safe to move or modify

## Mutability vs Immutability

### What is Mutability?

**Mutable** means "can be changed." A mutable value or object can be modified after it's created.

**Immutable** means "cannot be changed." An immutable value or object cannot be modified after it's created. Instead, you create a new value.

### Mutable Example (Modifies Original)

```javascript
// Mutable: modifies the original array
const numbers = [1, 2, 3];

function addNumber(arr, num) {
  arr.push(num); // Modifies the original array!
  return arr;
}

addNumber(numbers, 4);
console.log(numbers); // [1, 2, 3, 4] - Original array was changed!
```

### Immutable Example (Creates New Value)

```javascript
// Immutable: creates a new array
const numbers = [1, 2, 3];

function addNumber(arr, num) {
  return [...arr, num]; // Creates a new array, doesn't modify original
}

const newNumbers = addNumber(numbers, 4);
console.log(numbers); // [1, 2, 3] - Original unchanged
console.log(newNumbers); // [1, 2, 3, 4] - New array created
```

### Why Immutability Matters for Pure Functions

Pure functions should **not mutate** their inputs. Instead, they should return new values:

```javascript
// ❌ BAD: Mutates input (not pure)
function addItemToCart(cart, item) {
  cart.items.push(item); // Modifies the input!
  return cart;
}

// ✅ GOOD: Returns new value (pure)
function addItemToCart(cart, item) {
  return {
    ...cart,
    items: [...cart.items, item] // Creates new object and array
  };
}
```

### Common Immutable Patterns in JavaScript

#### Arrays

```javascript
// Instead of: arr.push(item)
const newArr = [...arr, item];

// Instead of: arr.pop()
const newArr = arr.slice(0, -1);

// Instead of: arr.sort()
const newArr = [...arr].sort(); // Copy first, then sort

// Instead of: arr.reverse()
const newArr = [...arr].reverse(); // Copy first, then reverse
```

#### Objects

```javascript
// Instead of: obj.property = value
const newObj = { ...obj, property: value };

// Instead of: obj.nested.property = value
const newObj = {
  ...obj,
  nested: {
    ...obj.nested,
    property: value
  }
};
```

### Mutable vs Immutable Comparison

| Mutable | Immutable |
|---------|-----------|
| ❌ Modifies original value | ✅ Creates new value |
| ❌ Can cause unexpected changes | ✅ Original always safe |
| ❌ Harder to track changes | ✅ Easy to see what changed |
| ❌ Can break pure functions | ✅ Works perfectly with pure functions |
| ⚡ Faster (no copying) | 🐌 Slightly slower (creates new values) |

### When to Use Each

- **Use immutability** when:
  - Writing pure functions
  - Working with React state
  - Need to track changes
  - Want predictable behavior

- **Use mutability** when:
  - Performance is critical (large datasets)
  - Working with local variables that won't be shared
  - You explicitly need to modify something in place

### Example: Converting Mutable to Immutable

```javascript
// Before: Mutable function
function updateUser(user, newName) {
  user.name = newName; // Mutates input
  return user;
}

// After: Immutable function (pure)
function updateUser(user, newName) {
  return {
    ...user,
    name: newName // Creates new object
  };
}

// Usage:
const user = { name: 'Alice', age: 30 };
const updatedUser = updateUser(user, 'Bob');
console.log(user); // { name: 'Alice', age: 30 } - unchanged
console.log(updatedUser); // { name: 'Bob', age: 30 } - new object
```

## Converting Functions with Side Effects to Pure Functions

### Before (with side effects):

```javascript
let userCount = 0;

function incrementUserCount() {
  userCount++; // Side effect: modifies external variable
  return userCount;
}
```

### After (pure function):

```javascript
function incrementUserCount(currentCount) {
  return currentCount + 1; // Pure: takes input, returns output
}

// Usage:
let userCount = 0;
userCount = incrementUserCount(userCount); // Explicitly pass and assign
```

## When Side Effects are Necessary

Sometimes side effects are necessary and appropriate:

- **Event handlers** - Need to update the UI
- **API calls** - Need to fetch data from servers
- **Form submissions** - Need to save data
- **User interactions** - Need to respond to clicks, input, etc.

The key is to **separate** pure logic from side effects:

```javascript
// Pure function (logic)
function calculateTotal(items) {
  return items.reduce((sum, item) => sum + item.price, 0);
}

// Function with side effects (UI update)
function updateDisplay(items) {
  const total = calculateTotal(items); // Use pure function
  document.getElementById('total').textContent = `$${total}`; // Side effect
}
```

## Summary

- **Pure functions**: Predictable, testable, reusable - use for calculations and transformations
- **Functions with side effects**: Necessary for interactions - use for UI updates, API calls, etc.
- **Immutability**: Don't mutate inputs - create new values instead. Essential for writing pure functions.
- **Best practice**: Extract pure logic into separate functions, use immutability, then use them in functions that handle side effects

## Resources

- **[MDN: Pure Functions](https://developer.mozilla.org/en-US/docs/Glossary/Pure_function)** - Official MDN definition and explanation of pure functions
- **[MDN: Immutability](https://developer.mozilla.org/en-US/docs/Glossary/Mutable)** - MDN explanation of mutability and immutability
- **[Professor Frisby's Mostly Adequate Guide: Pure Happiness with Pure Functions](https://mostly-adequate-guide.netlify.app/ch03)** - Excellent chapter on pure functions, side effects, and immutability
- **[Functional Programming Concepts](https://www.freecodecamp.org/news/functional-programming-concepts/)** - FreeCodeCamp guide to functional programming concepts including pure functions
- **[JavaScript.info: Pure Functions](https://javascript.info/function-basics#pure-functions)** - Clear explanation with examples from JavaScript.info
- **[Eloquent JavaScript: Functions](https://eloquentjavascript.net/03_functions.html)** - Chapter on functions including discussion of side effects and pure functions
- **[Refactoring Guru: Pure Functions](https://refactoring.guru/refactoring/smells/long-method)** - Part of refactoring guide discussing clean code principles
- **[Vitest Documentation](https://vitest.dev/)** - Testing framework perfect for testing pure functions

