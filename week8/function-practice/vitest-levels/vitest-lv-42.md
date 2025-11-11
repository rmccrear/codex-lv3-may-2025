Level Navigation: [1](./vitest-lv-1.md) | [(2ℹ️)](./vitest-lv-2.md) | [3](./vitest-lv-3.md) | [4](./vitest-lv-4.md) | [5](./vitest-lv-5.md) | [6](./vitest-lv-6.md) | [(7ℹ️)](./vitest-lv-7.md) | [(8ℹ️)](./vitest-lv-8.md) | [(9ℹ️)](./vitest-lv-9.md) | [10](./vitest-lv-10.md) | [11](./vitest-lv-11.md) | [12](./vitest-lv-12.md) | [13](./vitest-lv-13.md) | [14](./vitest-lv-14.md) | [15](./vitest-lv-15.md) | [16](./vitest-lv-16.md) | [17](./vitest-lv-17.md) | [18](./vitest-lv-18.md) | [19](./vitest-lv-19.md) | [20](./vitest-lv-20.md) | [21](./vitest-lv-21.md) | [22](./vitest-lv-22.md) | [23](./vitest-lv-23.md) | [24](./vitest-lv-24.md) | [25](./vitest-lv-25.md) | [26](./vitest-lv-26.md) | [27](./vitest-lv-27.md) | [28](./vitest-lv-28.md) | [29](./vitest-lv-29.md) | [30](./vitest-lv-30.md) | [31](./vitest-lv-31.md) | [32](./vitest-lv-32.md) | [33](./vitest-lv-33.md) | [34](./vitest-lv-34.md) | [35](./vitest-lv-35.md) | [36](./vitest-lv-36.md) | [(37ℹ️)](./vitest-lv-37.md) | [38⚡](./vitest-lv-38.md) | [39⚡](./vitest-lv-39.md) | [40⚡](./vitest-lv-40.md) | [41⚡](./vitest-lv-41.md) | **42** | [43⚡](./vitest-lv-43.md) | [44⚡](./vitest-lv-44.md) | [45](./vitest-lv-45.md) | [46](./vitest-lv-46.md) | [(47ℹ️)](./vitest-lv-47.md)

## Level 42: Add Test Coverage

Keeping an eye on test coverage helps you understand which parts of your code are exercised by your suite. Let’s install the coverage peer dependency and add a script that makes running coverage painless.

### Step 1: Install the coverage reporter

Vitest’s coverage command relies on the V8/Istanbul integration shipped in `@vitest/coverage-v8`. Install it as a dev dependency:

```bash
npm install -D @vitest/coverage-v8
```

### Step 2: Add the coverage script

Update your `package.json` scripts section so it includes a `test:coverage` command:

```json
"scripts": {
  "test": "vitest",
  "test:coverage": "vitest run --coverage"
}
```

> **Tip:** If you already have other scripts (like `"dev"` or `"lint"`), just add this line alongside them—keep the trailing commas consistent with the existing JSON.

### Step 3: Run the coverage report

```bash
npm run test:coverage
```

Vitest will execute the full suite once and print a table showing statements, branches, functions, and lines covered. The report also lands in the `coverage/` directory if you want to inspect the HTML output.

### Step 4: Review your results

- Look for rows that fall below your target percentage and add tests to improve them
- Rerun `npm run test:coverage` after writing new tests to confirm the numbers move in the right direction

**Try it:** Install the reporter, add the script, run coverage, and note any functions that still need tests before moving on.

---