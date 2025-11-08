<!-- LEVEL_START -->

## Level 1: Quick Intro to Vitest

Vitest is a testing framework from the folks that brought you Vite. Learn how to set up and use Vitest to test your functions.

---

<!-- LEVEL_START -->
<!-- INFORMATIVE_ONLY -->

## Level 2: Why Testing and Vitest?

Writing tests helps you verify that your code works correctly. When you write a function, tests let you check that it produces the expected output for different inputs. This helps catch bugs early and gives you confidence when making changes to your code.

Vitest is fast, easy to set up, and has a simple API that's similar to other popular testing frameworks. It works great with modern JavaScript (ES6 modules) and provides helpful error messages when tests fail.

**Note:** Vitest will work with Vite projects, but you don't need to use `npm create vite` to use Vitest. Vitest is a standalone testing framework that works in any Node.js project. You can use it with any project setup, not just Vite projects.

### What You'll Learn

In this guide, you'll learn how to:
- Set up Vitest in a Node.js project
- Write test files using Vitest's testing syntax
- Test functions with different inputs
- Run tests and interpret the results

---

<!-- LEVEL_START -->

## Level 3: Set up the project

First, initialize your npm project and install Vitest:

```bash
npm init -y
npm install --save-dev vitest
```

Then, update your `package.json` to add the test script and set the module type:

```json
{
  "type": "module",
  "scripts": {
    "test": "vitest"
  }
}
```

<details>
<summary>Show Me: What the full package.json might look like</summary>

When you run `npm init -y`, it creates a basic `package.json`. After adding the `type` and `scripts` fields, your complete `package.json` might look like this:

```json
{
  "name": "function-practice",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "type": "module",
  "scripts": {
    "test": "vitest"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "devDependencies": {
    "vitest": "^1.0.0"
  }
}
```

**Key points:**
- The `"type": "module"` field enables ES6 module syntax (import/export)
- The `"scripts"` section includes your test command
- `vitest` appears in `devDependencies` after installation
- Other fields (name, version, etc.) are created by `npm init -y`

</details>

Now run the test command to verify Vitest is set up correctly (it will show no tests found, which is expected):

```bash
npm run test
```

Press `q` to quit the test runner when you're done checking.

---

<!-- LEVEL_START -->

## Level 4: Create function files

Create `utils.js` with your functions:

```javascript
// utils.js

export function add(a, b) {
  return a + b;
}

export function toSnakeCase(text) {
  // Convert text to snake_case by replacing spaces with underscores and lowercasing
  return text.replaceAll(' ', '_').toLowerCase();
}
```

---

<!-- LEVEL_START -->

## Level 5: Create test files

We add `.test.` to the filename (like `utils.test.js`) to indicate this is a test file. Vitest automatically finds and runs files that match the pattern `*.test.js` or `*.spec.js`.

Create `utils.test.js`:

```javascript
// utils.test.js

import { describe, it, expect } from 'vitest';
import { add, toSnakeCase } from './utils.js';

describe('add function', () => {
  it('should add two positive numbers', () => {
    const result = add(2, 3);
    expect(result).toBe(5);
  });

  it('should add negative numbers', () => {
    const result = add(-1, -2);
    expect(result).toBe(-3);
  });
});

describe('toSnakeCase function', () => {
  it('should convert text with spaces to snake_case', () => {
    const result = toSnakeCase('Hello World');
    expect(result).toBe('hello_world');
  });

  it('should convert to lowercase', () => {
    const result = toSnakeCase('HELLO WORLD');
    expect(result).toBe('hello_world');
  });
});
```

---

<!-- LEVEL_START -->

## Level 6: Run your tests

Now that you have functions and tests, run your tests:

```bash
npm run test
```

Or run in watch mode (automatically reruns on file changes):

```bash
npm run test -- --watch
```

---

<!-- LEVEL_START -->
<!-- INFORMATIVE_ONLY -->

## Level 7: Summary and Next Steps

### Complete File Structure

```
function-practice/
├── utils.js
├── utils.test.js
├── package.json
└── node_modules/
```

### Next Steps

- Try the `--watch` flag to see tests run automatically when you save files
- Check out [Adding More Tests](./02-vitest-add-tests-guide.md) to learn about edge cases and creative test examples
- Add more test cases for different scenarios

### Resources

- **[Vitest Documentation](https://vitest.dev/)** - Official Vitest documentation and API reference
- **[Vitest Guide](https://vitest.dev/guide/)** - Getting started guide and tutorials

---

<!-- LEVEL_START -->
<!-- INFORMATIVE_ONLY -->

## Level 8: Adding More Tests

Once you have basic tests working, it's time to add more test cases! Testing different scenarios helps ensure your functions work correctly in all situations.

Thoughtful tests confirm behavior and also serve as living documentation for teammates who depend on these functions.

In the next levels we'll lean into this mindset by layering on robust tests that stress your functions from every angle.

---

<!-- LEVEL_START -->
<!-- INFORMATIVE_ONLY -->

## Level 9: Why Add More Tests?

- **Edge cases**: What happens with unusual inputs?
- **Boundary conditions**: What about very large or very small values?
- **Error handling**: Does your function handle unexpected inputs gracefully?
- **Real-world scenarios**: Will it work with actual data you might encounter?

---

<!-- LEVEL_START -->

## Level 10: Testing with Zero

Let's start by testing what happens when we use zero. Add this test to your `add` function:

Plan: confirm the `add` helper treats zero as neutral by writing a test that checks `add(5, 0)` still returns `5`.

```javascript
it('should add zero', () => {
  const result = add(5, 0);
  expect(result).toBe(5);
});
```

**Try it:** Run your tests to make sure this passes!

---

<!-- LEVEL_START -->

## Level 11: Testing with Very Large Numbers

Now let's test with very large numbers to see if our function handles them correctly:

Plan: stress-test `add` with a huge value and ensure it increments without overflow by asserting `add(999999999, 1)` equals `1000000000`.

```javascript
it('should add very large numbers', () => {
  const result = add(999999999, 1);
  expect(result).toBe(1000000000);
});
```

**Try it:** Add this test and run it. Does it pass?

---

<!-- LEVEL_START -->

## Level 12: Testing with Decimal Numbers

What about decimal numbers? Let's test that:

Plan: verify `add` handles decimals cleanly by checking `add(3.14, 2.86)` produces the precise total you expect.

```javascript
it('should add decimal numbers', () => {
  const result = add(3.14, 2.86);
  expect(result).toBe(6);
});
```

**Try it:** Add this test and see what happens!

---

<!-- LEVEL_START -->

## Level 13: Testing with Positive and Negative Numbers

Let's test what happens when we add a positive number to a negative number:

Plan: confirm `add` balances signs correctly by asserting `add(10, -5)` results in `5`.

```javascript
it('should add positive and negative numbers', () => {
  const result = add(10, -5);
  expect(result).toBe(5);
});
```

**Try it:** Add this test. What do you expect the result to be?

---

<!-- LEVEL_START -->

## Level 14: Testing When Result is Zero

What if the result itself is zero? Let's test that:

Plan: ensure opposite values cancel out by verifying `add(5, -5)` returns `0`.

<details>
<summary>Show Me</summary>

```javascript
it('should add when result is zero', () => {
  const result = add(5, -5);
  expect(result).toBe(0);
});
```

</details>

**Try it:** Add this test and verify it works!

---

<!-- LEVEL_START -->

## Level 15: Testing Fractions (Floating Point Precision)

When working with decimal numbers like `0.1 + 0.2`, JavaScript's floating point arithmetic can cause tiny rounding errors. We need to use `toBeCloseTo()` instead of `toBe()`:

Plan: demonstrate floating point quirks by expecting `add(0.1, 0.2)` to be close to `0.3` rather than exactly equal.

<details>
<summary>Show Me</summary>

```javascript
it('should add fractions', () => {
  const result = add(0.1, 0.2);
  expect(result).toBeCloseTo(0.3); // Use toBeCloseTo for floating point!
});
```

</details>

**Key Concept:** Use `toBeCloseTo()` when testing decimal numbers because `0.1 + 0.2` doesn't exactly equal `0.3` in JavaScript due to floating point precision.

**Try it:** Add this test. Notice we use `toBeCloseTo()` instead of `toBe()`!

---

<!-- LEVEL_START -->

## Level 16: Testing Empty Strings

Now let's move to testing `toSnakeCase`. What happens with an empty string?

Plan: check that `toSnakeCase('')` returns an empty string so blank inputs remain unchanged.

<details>
<summary>Show Me</summary>

```javascript
it('should handle empty string', () => {
  const result = toSnakeCase('');
  expect(result).toBe('');
});
```

</details>

**Try it:** Add this test to your `toSnakeCase` tests!

---

<!-- LEVEL_START -->

## Level 17: Testing Single Words

What about a single word with no spaces?

Plan: prove `toSnakeCase` lowercases solo words by asserting `toSnakeCase('Hello')` yields `hello`.

<details>
<summary>Show Me</summary>

```javascript
it('should handle single word', () => {
  const result = toSnakeCase('Hello');
  expect(result).toBe('hello');
});
```

</details>

**Try it:** Add this test and run it!

---

<!-- LEVEL_START -->

## Level 18: Testing Multiple Spaces

What if there are multiple spaces between words?

Plan: see how repeated whitespace converts by testing `toSnakeCase('Hello   World')` and observing the underscore trio.

<details>
<summary>Show Me</summary>

```javascript
it('should handle multiple spaces', () => {
  const result = toSnakeCase('Hello   World');
  expect(result).toBe('hello___world');
});
```

</details>

**Try it:** Add this test. Notice how multiple spaces become multiple underscores!

---

<!-- LEVEL_START -->

## Level 19: Testing Very Long Text

Let's test with a very long sentence:

Plan: validate long strings stay consistent by mapping `"This Is A Very Long Sentence With Many Words"` to the expected snake case version.

<details>
<summary>Show Me</summary>

```javascript
it('should handle very long text', () => {
  const result = toSnakeCase('This Is A Very Long Sentence With Many Words');
  expect(result).toBe('this_is_a_very_long_sentence_with_many_words');
});
```

</details>

**Try it:** Add this test and see if it handles long text correctly!

---

<!-- LEVEL_START -->

## Level 20: Testing Special Characters

What about text with special characters like exclamation marks?

Plan: capture how punctuation is treated by asserting `toSnakeCase('Hello World!')` keeps the exclamation mark intact at the end.

<details>
<summary>Show Me</summary>

```javascript
it('should handle text with special characters', () => {
  const result = toSnakeCase('Hello World!');
  expect(result).toBe('hello_world!');
});
```

</details>

**Try it:** Add this test. Do special characters get preserved?

---

<!-- LEVEL_START -->

## Level 21: Testing Numbers in Text

What if the text contains numbers?

Plan: confirm digits survive conversion by checking `toSnakeCase('Hello 123 World')` preserves `123` between underscores.

<details>
<summary>Show Me</summary>

```javascript
it('should handle numbers in text', () => {
  const result = toSnakeCase('Hello 123 World');
  expect(result).toBe('hello_123_world');
});
```

</details>

**Try it:** Add this test and see how numbers are handled!

---

<!-- LEVEL_START -->

## Level 22: Practice, Key Takeaways, and Next Steps

### Practice: Your Turn!

Now it's your turn to add some tests! Try adding tests for these scenarios:

**For the `add` function:**
1. **Test with two negative numbers** - What happens when you add `-1` and `-2`?
2. **Test with very small decimal numbers** - Try adding `0.001` and `0.002`
3. **Test with one number being zero** - What about `add(0, 10)`?

**For the `toSnakeCase` function:**
1. **Test with text that has no spaces** - What happens with `'HELLOWORLD'`?
2. **Test with text that is only spaces** - Try `'   '` (three spaces)
3. **Test with mixed case** - What about `'HeLLo WoRLd'`?

**Challenge:** Write each test, run it, and see if it passes. If it fails, think about why!

### Key Takeaways

- Test edge cases: zero, empty strings, very large numbers
- Use `toBeCloseTo()` for decimal/fraction testing
- Test unusual inputs: special characters, multiple spaces, mixed case
- Think about real-world scenarios your function might encounter

### Next Steps

- Try writing tests that you think might fail - this helps you understand your function's behavior
- Test with `undefined` or `null` - what happens?
- Can you think of other edge cases we haven't covered?

### Resources

- **[Vitest Documentation](https://vitest.dev/)** - Official Vitest documentation and API reference
- **[Vitest API Reference](https://vitest.dev/api/)** - Complete API documentation for all Vitest functions

---

<!-- LEVEL_START -->

## Level 23: Red-Green-Refactor: Making Tests Fail, Then Pass

The **Red-Green-Refactor** cycle is a core testing practice:

1. **Red**: Write a test that fails (because the function doesn't do what you want yet)
2. **Green**: Write the code to make the test pass
3. **Refactor**: Improve the code while keeping tests green

This approach helps you:
- Think about what you want before writing code
- Write only the code you need
- Have confidence when refactoring

---

<!-- LEVEL_START -->

## Level 24: Write a Failing Test for Exclamation Marks (Red)

Let's say we want our `toSnakeCase` function to also replace exclamation marks with underscores. Currently, our function only handles spaces:

```javascript
// Current function
export function toSnakeCase(text) {
  return text.replaceAll(' ', '_').toLowerCase();
}
```

Let's write a test that we know will **fail** because the function doesn't handle exclamation marks yet:

```javascript
it('should replace exclamation marks with underscores', () => {
  const result = toSnakeCase('Hello World!');
  expect(result).toBe('hello_world_');
});
```

**Try it now:** Add this test to your `toSnakeCase` tests and run it. What happens?

You should see a **red** (failing) test! The test expects `'hello_world_'` but gets `'hello_world!'` because the function only replaces spaces, not exclamation marks.

---

<!-- LEVEL_START -->

## Level 25: Make the Test Pass (Green) - Exclamation Marks

Now let's fix it by adding a `replaceAll()` call for exclamation marks:

```javascript
export function toSnakeCase(text) {
  return text.replaceAll(' ', '_').replaceAll('!', '_').toLowerCase();
}
```

**What does this do?**
- `replaceAll(' ', '_')` - replaces all spaces with underscores
- `replaceAll('!', '_')` - replaces all exclamation marks with underscores
- `toLowerCase()` - converts everything to lowercase

**Try it now:** Update your `toSnakeCase` function and run your tests again. The test should pass (green)!

---

<!-- LEVEL_START -->

## Level 26: Write a Failing Test for Question Marks (Red)

Now let's add support for question marks. Write a test that will fail:

```javascript
it('should replace question marks with underscores', () => {
  const result = toSnakeCase('Hello World?');
  expect(result).toBe('hello_world_');
});
```

**Try it now:** Add this test and run it. It should fail (red) because we haven't added support for question marks yet!

---

<!-- LEVEL_START -->

## Level 27: Make the Test Pass (Green) - Question Marks

Now let's fix it! You need to add support for question marks, similar to how we added support for exclamation marks.

**Try it now:** Update your function to handle question marks and run your tests. Both tests should pass (green)!

---

<!-- LEVEL_START -->

## Level 28: Write a Failing Test for Commas (Red)

Now let's add support for commas. Write a test that will fail:

```javascript
it('should replace commas with underscores', () => {
  const result = toSnakeCase('Hello, World');
  expect(result).toBe('hello__world');
});
```

**Try it now:** Add this test and run it. It should fail (red)!

---

<!-- LEVEL_START -->

## Level 29: Make the Test Pass (Green) - Commas

Now let's fix it! You need to add support for commas, following the same pattern as before.

**Try it now:** Update your function to handle commas and run your tests. All three tests should pass (green)!

---

<!-- LEVEL_START -->

## Level 30: Refactor - Using Regex

Now we have a lot of `replaceAll()` calls! We can simplify this using a **regular expression** (regex) to match multiple characters at once.

A regex lets us match a pattern of characters. We can use square brackets `[]` to match any of the characters inside:

```javascript
export function toSnakeCase(text) {
  return text.replaceAll(' ', '_').replaceAll(/[!?,]/, '_').toLowerCase();
}
```

**What does this regex do?**
- `/[!?,]/` is a regular expression pattern
- The square brackets `[]` mean "match any of these characters"
- `!?`, means match exclamation marks, question marks, or commas
- The forward slashes `/` mark the start and end of the regex pattern
- `replaceAll()` already replaces all matches, so we don't need the `/g` flag

**Try it now:** Update your function with this regex and run your tests. They should all still pass (green)!

---

<!-- LEVEL_START -->

## Level 31: Understanding the Regex Pattern

Let's break down the regex pattern `/[!?,]/`:

```javascript
/[!?,]/
│││││││
││││││└─ / = end of regex pattern
│││││└── ] = end of character class (match any of these)
││││└──── , = comma character
│││└───── ? = question mark character
││└────── ! = exclamation mark character
│└─────── [ = start of character class (match any of these)
└──────── / = start of regex pattern
```

**Why use regex?**
- Instead of three separate `replaceAll()` calls, we have one!
- Easier to add more punctuation marks later
- More concise and readable

**Testing Regex Patterns:**
Want to test and experiment with regex patterns? Check out [regex101.com](https://regex101.com/) - it's a great tool for testing regex patterns and seeing what they match. You can paste your regex pattern and test it against sample text to see exactly what it matches!

---

<!-- LEVEL_START -->

## Level 32: Adding More Punctuation

**Exercise:** expand your regex to cover more punctuation.

- Update the character class so it also replaces `.`, `;`, and `:` with underscores.
- Add a new test (or two) proving the updated `toSnakeCase` handles the extra marks.
- Rerun your suite and confirm everything still passes.

*Hint:* revisit Level 31’s breakdown if you need to recall how character classes work.

---

<!-- LEVEL_START -->

## Level 33: Using \W for All Non-Word Characters

If we want to replace ALL punctuation (not just specific ones), we can use `\W` which matches any non-word character:

```javascript
export function toSnakeCase(text) {
  return text.replaceAll(' ', '_').replaceAll(/\W/, '_').toLowerCase();
}
```

**What does `\W` do?**
- `\W` matches any non-word character (punctuation, symbols, etc.)
- It does NOT match letters, numbers, or underscores
- This is a shorthand for "everything except word characters"
- **Mnemonic:** lowercase `\w` stands for word characters; uppercase `\W` flips the meaning to non-word characters.

**Try it:** Update your function and run your tests. They should still pass!

---

<!-- LEVEL_START -->

## Level 34: Practice: Your Turn!

### Challenge 1: Test Multiple Punctuation Together

Write a test that checks if multiple punctuation marks work together:

```javascript
it('should replace multiple punctuation marks', () => {
  const result = toSnakeCase('Hello!!! World???');
  expect(result).toBe('hello___world___');
});
```

**Try it:** Add this test. Does it pass with your current function?

### Challenge 2: Test Mixed Punctuation

**Exercise:** design a test that mixes commas, exclamation marks, and question marks in the same string, then update `toSnakeCase` if needed so the assertion passes.

---

<!-- LEVEL_START -->

## Level 35: Key Takeaways, Next Steps, and Resources

### Key Takeaways

1. **Red**: Write tests first that describe what you want
2. **Green**: Write the minimum code to make tests pass
3. **Refactor**: Improve code while keeping tests green
4. **Regex**: Use regular expressions to match patterns of characters
5. **Character classes**: Use `[]` to match any of several characters
6. **\W**: Matches any non-word character (punctuation, symbols)

### Common Regex Patterns

Here are some useful patterns:

```javascript
// Replace spaces (simple string replacement)
text.replaceAll(' ', '_')

// Replace specific punctuation
text.replaceAll(/[!?,]/, '_')

// Replace all punctuation (non-word characters)
text.replaceAll(/\W/, '_')

// Replace everything except letters, numbers, and underscores
text.replaceAll(/[^a-zA-Z0-9_]/, '_')
```

### Quick Regex Reference for Beginners

Here are some common regex patterns you might use:

| Pattern | Matches | Example |
|---------|---------|---------|
| `[abc]` | Any of these characters (a, b, or c) | `/[abc]/` matches "a", "b", or "c" |
| `[!?,]` | Any of these punctuation marks | `/[!?,]/` matches "!", "?", or "," |
| `\W` | Any non-word character (punctuation, symbols) | `/\W/` matches "!", "?", ",", etc. |
| `\w` | Any word character (letters, numbers, underscore) | `/\w/` matches "a", "1", "_" |
| `\s` | Any whitespace (spaces, tabs) | `/\s/` matches " " (space) |
| `\d` | Any digit (0-9) | `/\d/` matches "0" through "9" |
| `[^abc]` | NOT any of these characters | `/[^abc]/` matches anything except a, b, or c |
| `+` | One or more of the previous | `/\W+/` matches one or more punctuation marks |
| `*` | Zero or more of the previous | `/\d*/` matches zero or more digits |
| `?` | Zero or one of the previous | `/\d?/` matches zero or one digit |

**Note:** In JavaScript, regex patterns are written between forward slashes: `/pattern/`

### Next Steps

- Try writing tests for other punctuation marks
- Experiment with different regex patterns using [regex101.com](https://regex101.com/) to test them
- Think about edge cases: what if text is all punctuation? What about emojis?

### Resources

- **[Vitest Documentation](https://vitest.dev/)** - Official Vitest documentation and API reference
- **[regex101.com](https://regex101.com/)** - Interactive regex tester and debugger. Great for learning and testing regex patterns!
- **[Regex for Beginners](https://regexone.com/)** - Step-by-step regex tutorial for beginners
- **[MDN Regular Expressions Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions)** - Comprehensive regex reference for JavaScript

---

<!-- LEVEL_START -->

## Level 36: Vitest Challenges: Building and Composing Functions

Now that you've learned the basics of Vitest, let's practice by building real functions and composing them together!

---

<!-- LEVEL_START -->
<!-- INFORMATIVE_ONLY -->

## Level 37: Function Ideas Reference

Check out [function-ideas.md](./function-ideas.md) for a list of function ideas organized by category. We'll work through some of these together, then you'll choose your own to practice with.

---

<!-- LEVEL_START -->

## Level 38 (Challenge): Build `makeGreeting`

Let's start with the first greeting function. Create a function that takes a name and an occasion, and returns a greeting message.

**Function signature:**
```javascript
makeGreeting(name, occasion) → string
```

**Examples:**
- `makeGreeting('Alex', 'Birthday')` → `"Happy Birthday, Alex!"`
- `makeGreeting('Sam', 'New Year')` → `"Happy New Year, Sam!"`

**Your task:**
1. Write tests for `makeGreeting` first (red)
2. Implement the function to make tests pass (green)
3. Test with different names and occasions

**Try it:** Create `greeting.test.js` and `greeting.js`, then write your tests and function!

---

<!-- LEVEL_START -->

## Level 39 (Challenge): Build `addSignature`

Now let's add a function that adds a signature to a message.

**Function signature:**
```javascript
addSignature(message, from) → string
```

**Examples:**
- `addSignature('Happy Birthday, Alex!', 'Sam')` → `"Happy Birthday, Alex! — from Sam"`
- `addSignature('Happy New Year, Sam!', 'Alex')` → `"Happy New Year, Sam! — from Alex"`

**Your task:**
1. Write tests for `addSignature` first
2. Implement the function
3. Test with different messages and signatures

**Try it:** Add tests and the function to your `greeting.test.js` and `greeting.js` files!

---

<!-- LEVEL_START -->

## Level 40 (Challenge): Build `decorateMessage`

Now let's create a function that decorates a message with emojis.

**Function signature:**
```javascript
decorateMessage(message) → string
```

**Examples:**
- `decorateMessage('Happy Birthday, Alex!')` → `"🌸🌸 Happy Birthday, Alex! 🌸🌸"`
- `decorateMessage('Hello World')` → `"🌸🌸 Hello World 🌸🌸"`

**Your task:**
1. Write tests for `decorateMessage` first
2. Implement the function
3. Test with different messages

**Try it:** Add this function to your greeting files!

---

<!-- LEVEL_START -->

## Level 41 (Challenge): Compose Functions - Create a Full Greeting

Now that we have all three functions, let's compose them together! Create a function that uses all three to create a decorated, signed greeting.

**Function signature:**
```javascript
createFullGreeting(name, occasion, from) → string
```

**Examples:**
- `createFullGreeting('Alex', 'Birthday', 'Sam')` → `"🌸🌸 Happy Birthday, Alex! — from Sam 🌸🌸"`

**Your task:**
1. Write tests for `createFullGreeting`
2. Implement it by calling your other three functions
3. Think about the order: greeting → signature → decoration

**Hint:** You can call functions inside other functions:
```javascript
function createFullGreeting(name, occasion, from) {
  const greeting = makeGreeting(name, occasion);
  const signed = addSignature(greeting, from);
  return decorateMessage(signed);
}
```

**Try it:** Compose your functions together!

---

<!-- LEVEL_START -->

## Level 42 (Challenge): Compose Functions - Create Multiple Variations

Let's create more composed functions that use our building blocks in different ways.

### 5a. Create a greeting without signature

**Function signature:**
```javascript
createDecoratedGreeting(name, occasion) → string
```

**Example:**
- `createDecoratedGreeting('Alex', 'Birthday')` → `"🌸🌸 Happy Birthday, Alex! 🌸🌸"`

### 5b. Create a signed greeting without decoration

**Function signature:**
```javascript
createSignedGreeting(name, occasion, from) → string
```

**Example:**
- `createSignedGreeting('Alex', 'Birthday', 'Sam')` → `"Happy Birthday, Alex! — from Sam"`

**Your task:**
1. Write tests for both functions
2. Implement them by composing your existing functions
3. Notice how you can reuse the same building blocks in different ways!

**Try it:** Create these composed functions!

---

<!-- LEVEL_START -->

## Level 43 (Challenge): Choose Your Own Function Cluster

Now it's your turn! Choose one of the function clusters from [function-ideas.md](./function-ideas.md) and build them out.

**Available clusters:**
- 🍳 **Recipe & Measurement Functions** - `convertToCups`, `calculateTip`, `applyDiscount`
- 🧮 **Math & Geometry** - `double`, `addTax`, `distance`
- 🎨 **Color Utilities** - `mixColors`, `lighten`, `convertArrayToRGB`
- 🧠 **Word & String Utilities** - `toSnakeCase`, `toKebabCase`, `toCamelCase`
- 🐉 **API / Data Simplifiers** - `simplifyPokemonObject`, `tempToday`, `conditionsToday`

**Your task:**
1. **Choose a cluster** that interests you
2. **Build each function** in the cluster:
   - Write tests first (red)
   - Implement the function (green)
   - Test edge cases
3. **Compose them** into at least one larger function that uses multiple functions from your cluster
4. **Document** your functions with clear input/output examples

**Example workflow:**
```javascript
// Step 1: Build individual functions
function calculateTip(total, percent) { /* ... */ }
function applyDiscount(price, discount) { /* ... */ }

// Step 2: Compose them
function calculateFinalPrice(price, discount, tipPercent) {
  const discounted = applyDiscount(price, discount);
  return calculateTip(discounted, tipPercent);
}
```

**Try it:** Pick a cluster and build it out! Write tests, implement functions, and compose them together.

---

<!-- LEVEL_START -->

## Level 44: Key Takeaways

- **Build small functions first** - Start with simple, focused functions
- **Test each function** - Write tests before implementing
- **Compose functions** - Combine small functions to create larger ones
- **Reuse code** - Once you have building blocks, you can use them in many ways
- **Practice makes perfect** - The more functions you build, the better you'll get!

---

<!-- LEVEL_START -->

## Level 45: Next Steps

- Try building functions from multiple clusters
- Create more complex compositions
- Share your functions with classmates
- Challenge yourself with edge cases

---

<!-- LEVEL_START -->
<!-- INFORMATIVE_ONLY -->

## Level 46: Resources

- **[Vitest Documentation](https://vitest.dev/)** - Official Vitest documentation
- **[Function Ideas](./function-ideas.md)** - List of function ideas to practice with
- **[Pure Functions Guide](../pure-functions.md)** - Learn about pure functions and immutability

---

