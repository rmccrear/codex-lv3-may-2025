# Quick Intro to Vitest

Vitest is a testing framework from the folks that brought you Vite. Learn how to set up and use Vitest to test your functions.

## Why Testing and Vitest?

Writing tests helps you verify that your code works correctly. When you write a function, tests let you check that it produces the expected output for different inputs. This helps catch bugs early and gives you confidence when making changes to your code.

Vitest is fast, easy to set up, and has a simple API that's similar to other popular testing frameworks. It works great with modern JavaScript (ES6 modules) and provides helpful error messages when tests fail.

**Note:** Vitest will work with Vite projects, but you don't need to use `npm create vite` to use Vitest. Vitest is a standalone testing framework that works in any Node.js project. You can use it with any project setup, not just Vite projects.

### What You'll Learn

In this guide, you'll learn how to:
- Set up Vitest in a Node.js project
- Write test files using Vitest's testing syntax
- Test functions with different inputs
- Run tests and interpret the results

## Step 1: Set up the project

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

## Step 2: Create function files

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

## Step 3: Create test files

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

## Step 4: Run your tests

Now that you have functions and tests, run your tests:

```bash
npm run test
```

Or run in watch mode (automatically reruns on file changes):

```bash
npm run test -- --watch
```

## Summary and Next Steps

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

