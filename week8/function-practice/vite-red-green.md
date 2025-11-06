# Red-Green-Refactor: Making Tests Fail, Then Pass

The **Red-Green-Refactor** cycle is a core testing practice:

1. **Red**: Write a test that fails (because the function doesn't do what you want yet)
2. **Green**: Write the code to make the test pass
3. **Refactor**: Improve the code while keeping tests green

This approach helps you:
- Think about what you want before writing code
- Write only the code you need
- Have confidence when refactoring

---

## Step 1: Write a Failing Test for Exclamation Marks (Red)

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

## Step 2: Make the Test Pass (Green) - Exclamation Marks

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

## Step 3: Write a Failing Test for Question Marks (Red)

Now let's add support for question marks. Write a test that will fail:

```javascript
it('should replace question marks with underscores', () => {
  const result = toSnakeCase('Hello World?');
  expect(result).toBe('hello_world_');
});
```

**Try it now:** Add this test and run it. It should fail (red) because we haven't added support for question marks yet!

---

## Step 4: Make the Test Pass (Green) - Question Marks

Now let's fix it! You need to add support for question marks, similar to how we added support for exclamation marks.

**Try it now:** Update your function to handle question marks and run your tests. Both tests should pass (green)!

---

## Step 5: Write a Failing Test for Commas (Red)

Now let's add support for commas. Write a test that will fail:

```javascript
it('should replace commas with underscores', () => {
  const result = toSnakeCase('Hello, World');
  expect(result).toBe('hello__world');
});
```

**Try it now:** Add this test and run it. It should fail (red)!

---

## Step 6: Make the Test Pass (Green) - Commas

Now let's fix it! You need to add support for commas, following the same pattern as before.

**Try it now:** Update your function to handle commas and run your tests. All three tests should pass (green)!

---

## Step 7: Refactor - Using Regex

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

## Step 8: Understanding the Regex Pattern

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

## Step 9: Adding More Punctuation

What if we want to handle more punctuation? We can just add them to the character class:

```javascript
export function toSnakeCase(text) {
  return text.replaceAll(' ', '_').replaceAll(/[!?,.;:]/, '_').toLowerCase();
}
```

Now it handles: `!`, `?`, `,`, `.`, `;`, and `:`!

**Try it:** Add a test for one of these new punctuation marks and see if it works!

---

## Step 10: Using \W for All Non-Word Characters

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

**Try it:** Update your function and run your tests. They should still pass!

---

## Practice: Your Turn!

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

Write a test with different types of punctuation:

```javascript
it('should handle mixed punctuation', () => {
  const result = toSnakeCase('Hello, World! How are you?');
  expect(result).toBe('hello__world__how_are_you_');
});
```

**Try it:** Add this test and see if it works!

---

## Key Takeaways

1. **Red**: Write tests first that describe what you want
2. **Green**: Write the minimum code to make tests pass
3. **Refactor**: Improve code while keeping tests green
4. **Regex**: Use regular expressions to match patterns of characters
5. **Character classes**: Use `[]` to match any of several characters
6. **\W**: Matches any non-word character (punctuation, symbols)

---

## Common Regex Patterns

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

---

## Next Steps

- Try writing tests for other punctuation marks
- Experiment with different regex patterns using [regex101.com](https://regex101.com/) to test them
- Think about edge cases: what if text is all punctuation? What about emojis?

## Resources

- **[Vitest Documentation](https://vitest.dev/)** - Official Vitest documentation and API reference
- **[regex101.com](https://regex101.com/)** - Interactive regex tester and debugger. Great for learning and testing regex patterns!
- **[Regex for Beginners](https://regexone.com/)** - Step-by-step regex tutorial for beginners
- **[MDN Regular Expressions Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions)** - Comprehensive regex reference for JavaScript

## Quick Regex Reference for Beginners

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
