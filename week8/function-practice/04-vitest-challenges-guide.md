# Vitest Challenges: Building and Composing Functions

Now that you've learned the basics of Vitest, let's practice by building real functions and composing them together!

## Function Ideas Reference

Check out [function-ideas.md](./function-ideas.md) for a list of function ideas organized by category. We'll work through some of these together, then you'll choose your own to practice with.

---

## Step 1 (Challenge): Build `makeGreeting`

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

## Step 2 (Challenge): Build `addSignature`

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

## Step 3 (Challenge): Build `decorateMessage`

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

## Step 4 (Challenge): Compose Functions - Create a Full Greeting

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

## Step 5 (Challenge): Compose Functions - Create Multiple Variations

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

## Step 6 (Challenge): Choose Your Own Function Cluster

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

## Key Takeaways

- **Build small functions first** - Start with simple, focused functions
- **Test each function** - Write tests before implementing
- **Compose functions** - Combine small functions to create larger ones
- **Reuse code** - Once you have building blocks, you can use them in many ways
- **Practice makes perfect** - The more functions you build, the better you'll get!

---

## Next Steps

- Try building functions from multiple clusters
- Create more complex compositions
- Share your functions with classmates
- Challenge yourself with edge cases

## Resources

- **[Vitest Documentation](https://vitest.dev/)** - Official Vitest documentation
- **[Function Ideas](./function-ideas.md)** - List of function ideas to practice with
- **[Pure Functions Guide](../pure-functions.md)** - Learn about pure functions and immutability

