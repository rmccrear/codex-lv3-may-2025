Level Navigation: [1](./vitest-lv-1.md) | [(2ℹ️)](./vitest-lv-2.md) | [3](./vitest-lv-3.md) | [4](./vitest-lv-4.md) | [5](./vitest-lv-5.md) | [6](./vitest-lv-6.md) | [(7ℹ️)](./vitest-lv-7.md) | [8](./vitest-lv-8.md) | [(9ℹ️)](./vitest-lv-9.md) | [10](./vitest-lv-10.md) | [11](./vitest-lv-11.md) | [12](./vitest-lv-12.md) | [13](./vitest-lv-13.md) | [14](./vitest-lv-14.md) | [15](./vitest-lv-15.md) | [16](./vitest-lv-16.md) | [17](./vitest-lv-17.md) | [18](./vitest-lv-18.md) | [19](./vitest-lv-19.md) | [20](./vitest-lv-20.md) | [21](./vitest-lv-21.md) | [22](./vitest-lv-22.md) | [23](./vitest-lv-23.md) | [24](./vitest-lv-24.md) | [25](./vitest-lv-25.md) | [26](./vitest-lv-26.md) | [27](./vitest-lv-27.md) | [28](./vitest-lv-28.md) | [29](./vitest-lv-29.md) | [30](./vitest-lv-30.md) | [31](./vitest-lv-31.md) | [32](./vitest-lv-32.md) | [33](./vitest-lv-33.md) | [34](./vitest-lv-34.md) | **35** | [36](./vitest-lv-36.md) | [(37ℹ️)](./vitest-lv-37.md) | [38⚡](./vitest-lv-38.md) | [39⚡](./vitest-lv-39.md) | [40⚡](./vitest-lv-40.md) | [41⚡](./vitest-lv-41.md) | [42⚡](./vitest-lv-42.md) | [43⚡](./vitest-lv-43.md) | [44](./vitest-lv-44.md) | [45](./vitest-lv-45.md) | [(46ℹ️)](./vitest-lv-46.md)

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