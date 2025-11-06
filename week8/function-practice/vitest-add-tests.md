# Adding More Tests

Once you have basic tests working, it's time to add more test cases! Testing different scenarios helps ensure your functions work correctly in all situations.

## Why Add More Tests?

- **Edge cases**: What happens with unusual inputs?
- **Boundary conditions**: What about very large or very small values?
- **Error handling**: Does your function handle unexpected inputs gracefully?
- **Real-world scenarios**: Will it work with actual data you might encounter?

---

## Step 1: Testing with Zero

Let's start by testing what happens when we use zero. Add this test to your `add` function:

```javascript
it('should add zero', () => {
  const result = add(5, 0);
  expect(result).toBe(5);
});
```

**Try it:** Run your tests to make sure this passes!

---

## Step 2: Testing with Very Large Numbers

Now let's test with very large numbers to see if our function handles them correctly:

```javascript
it('should add very large numbers', () => {
  const result = add(999999999, 1);
  expect(result).toBe(1000000000);
});
```

**Try it:** Add this test and run it. Does it pass?

---

## Step 3: Testing with Decimal Numbers

What about decimal numbers? Let's test that:

```javascript
it('should add decimal numbers', () => {
  const result = add(3.14, 2.86);
  expect(result).toBe(6);
});
```

**Try it:** Add this test and see what happens!

---

## Step 4: Testing with Positive and Negative Numbers

Let's test what happens when we add a positive number to a negative number:

```javascript
it('should add positive and negative numbers', () => {
  const result = add(10, -5);
  expect(result).toBe(5);
});
```

**Try it:** Add this test. What do you expect the result to be?

---

## Step 5: Testing When Result is Zero

What if the result itself is zero? Let's test that:

```javascript
it('should add when result is zero', () => {
  const result = add(5, -5);
  expect(result).toBe(0);
});
```

**Try it:** Add this test and verify it works!

---

## Step 6: Testing Fractions (Floating Point Precision)

When working with decimal numbers like `0.1 + 0.2`, JavaScript's floating point arithmetic can cause tiny rounding errors. We need to use `toBeCloseTo()` instead of `toBe()`:

```javascript
it('should add fractions', () => {
  const result = add(0.1, 0.2);
  expect(result).toBeCloseTo(0.3); // Use toBeCloseTo for floating point!
});
```

**Key Concept:** Use `toBeCloseTo()` when testing decimal numbers because `0.1 + 0.2` doesn't exactly equal `0.3` in JavaScript due to floating point precision.

**Try it:** Add this test. Notice we use `toBeCloseTo()` instead of `toBe()`!

---

## Step 7: Testing Empty Strings

Now let's move to testing `toSnakeCase`. What happens with an empty string?

```javascript
it('should handle empty string', () => {
  const result = toSnakeCase('');
  expect(result).toBe('');
});
```

**Try it:** Add this test to your `toSnakeCase` tests!

---

## Step 8: Testing Single Words

What about a single word with no spaces?

```javascript
it('should handle single word', () => {
  const result = toSnakeCase('Hello');
  expect(result).toBe('hello');
});
```

**Try it:** Add this test and run it!

---

## Step 9: Testing Multiple Spaces

What if there are multiple spaces between words?

```javascript
it('should handle multiple spaces', () => {
  const result = toSnakeCase('Hello   World');
  expect(result).toBe('hello___world');
});
```

**Try it:** Add this test. Notice how multiple spaces become multiple underscores!

---

## Step 10: Testing Very Long Text

Let's test with a very long sentence:

```javascript
it('should handle very long text', () => {
  const result = toSnakeCase('This Is A Very Long Sentence With Many Words');
  expect(result).toBe('this_is_a_very_long_sentence_with_many_words');
});
```

**Try it:** Add this test and see if it handles long text correctly!

---

## Step 11: Testing Special Characters

What about text with special characters like exclamation marks?

```javascript
it('should handle text with special characters', () => {
  const result = toSnakeCase('Hello World!');
  expect(result).toBe('hello_world!');
});
```

**Try it:** Add this test. Do special characters get preserved?

---

## Step 12: Testing Numbers in Text

What if the text contains numbers?

```javascript
it('should handle numbers in text', () => {
  const result = toSnakeCase('Hello 123 World');
  expect(result).toBe('hello_123_world');
});
```

**Try it:** Add this test and see how numbers are handled!

---

## Practice: Your Turn!

Now it's your turn to add some tests! Try adding tests for these scenarios:

### For the `add` function:
1. **Test with two negative numbers** - What happens when you add `-1` and `-2`?
2. **Test with very small decimal numbers** - Try adding `0.001` and `0.002`
3. **Test with one number being zero** - What about `add(0, 10)`?

### For the `toSnakeCase` function:
1. **Test with text that has no spaces** - What happens with `'HELLOWORLD'`?
2. **Test with text that is only spaces** - Try `'   '` (three spaces)
3. **Test with mixed case** - What about `'HeLLo WoRLd'`?

**Challenge:** Write each test, run it, and see if it passes. If it fails, think about why!

---

## Key Takeaways

- Test edge cases: zero, empty strings, very large numbers
- Use `toBeCloseTo()` for decimal/fraction testing
- Test unusual inputs: special characters, multiple spaces, mixed case
- Think about real-world scenarios your function might encounter

## Next Steps

- Try writing tests that you think might fail - this helps you understand your function's behavior
- Test with `undefined` or `null` - what happens?
- Can you think of other edge cases we haven't covered?

## Resources

- **[Vitest Documentation](https://vitest.dev/)** - Official Vitest documentation and API reference
- **[Vitest API Reference](https://vitest.dev/api/)** - Complete API documentation for all Vitest functions
