Level Navigation: [1](./vitest-lv-1.md) | [(2ℹ️)](./vitest-lv-2.md) | [3](./vitest-lv-3.md) | [4](./vitest-lv-4.md) | [5](./vitest-lv-5.md) | [6](./vitest-lv-6.md) | [(7ℹ️)](./vitest-lv-7.md) | [8](./vitest-lv-8.md) | [(9ℹ️)](./vitest-lv-9.md) | [10](./vitest-lv-10.md) | [11](./vitest-lv-11.md) | [12](./vitest-lv-12.md) | [13](./vitest-lv-13.md) | [14](./vitest-lv-14.md) | [15](./vitest-lv-15.md) | [16](./vitest-lv-16.md) | [17](./vitest-lv-17.md) | [18](./vitest-lv-18.md) | [19](./vitest-lv-19.md) | [20](./vitest-lv-20.md) | [21](./vitest-lv-21.md) | **22** | [23](./vitest-lv-23.md) | [24](./vitest-lv-24.md) | [25](./vitest-lv-25.md) | [26](./vitest-lv-26.md) | [27](./vitest-lv-27.md) | [28](./vitest-lv-28.md) | [29](./vitest-lv-29.md) | [30](./vitest-lv-30.md) | [31](./vitest-lv-31.md) | [32](./vitest-lv-32.md) | [33](./vitest-lv-33.md) | [34](./vitest-lv-34.md) | [35](./vitest-lv-35.md) | [36](./vitest-lv-36.md) | [(37ℹ️)](./vitest-lv-37.md) | [38⚡](./vitest-lv-38.md) | [39⚡](./vitest-lv-39.md) | [40⚡](./vitest-lv-40.md) | [41⚡](./vitest-lv-41.md) | [42⚡](./vitest-lv-42.md) | [43⚡](./vitest-lv-43.md) | [44](./vitest-lv-44.md) | [45](./vitest-lv-45.md) | [(46ℹ️)](./vitest-lv-46.md)

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