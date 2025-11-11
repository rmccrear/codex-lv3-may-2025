Level Navigation: [1](../vitest-lv-1.md) | [(2ℹ️)](../vitest-lv-2.md) | [3](../vitest-lv-3.md) | [4](../vitest-lv-4.md) | [5](../vitest-lv-5.md) | [6](../vitest-lv-6.md) | [(7ℹ️)](../vitest-lv-7.md) | [(8ℹ️)](../vitest-lv-8.md) | [(9ℹ️)](../vitest-lv-9.md) | [10](../vitest-lv-10.md) | [11](../vitest-lv-11.md) | [12](../vitest-lv-12.md) | [13](../vitest-lv-13.md) | [14](../vitest-lv-14.md) | [15](../vitest-lv-15.md) | [16](../vitest-lv-16.md) | [17](../vitest-lv-17.md) | [18](../vitest-lv-18.md) | [19](../vitest-lv-19.md) | [20](../vitest-lv-20.md) | [21](../vitest-lv-21.md) | [22](../vitest-lv-22.md) | [23](../vitest-lv-23.md) | [24](../vitest-lv-24.md) | [25](../vitest-lv-25.md) | [26](../vitest-lv-26.md) | [27](../vitest-lv-27.md) | [28](../vitest-lv-28.md) | [29](../vitest-lv-29.md) | [30](../vitest-lv-30.md) | [31](../vitest-lv-31.md) | [32](../vitest-lv-32.md) | [33](../vitest-lv-33.md) | [34](../vitest-lv-34.md) | [35](../vitest-lv-35.md) | [36](../vitest-lv-36.md) | [(37ℹ️)](../vitest-lv-37.md) | [38⚡](../vitest-lv-38.md) | [39⚡](../vitest-lv-39.md) | [40⚡](../vitest-lv-40.md) | **41⚡** | [42⚡](../vitest-lv-42.md) | [43⚡](../vitest-lv-43.md) | [44](../vitest-lv-44.md) | [45](../vitest-lv-45.md) | [(46ℹ️)](../vitest-lv-46.md)

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