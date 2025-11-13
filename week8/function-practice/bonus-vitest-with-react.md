# Setting Up Vitest for Testing React (with React Testing Library + jest-dom)

## Roadmap: What files will we touch?

In this mini-guide, you will:

1. **Create / update config & scripts**

   * `package.json` → add test scripts
   * `vite.config.js` → add `test` config for Vitest

2. **Add a global test setup file**

   * `setupTests.js` → configure React Testing Library + jest-dom

3. **Create components to test**

   * `src/components/Hello.jsx` → simple component
   * `src/components/Counter.jsx` → component with state + button

4. **Create test files**

   * `src/components/Hello.test.jsx` → tests for `Hello`
   * `src/components/Counter.test.jsx` → tests for `Counter`

At the end, you’ll have Vitest running and two working React tests.

---

## 0. File system diagram (big picture)

Here’s what your project structure will look like after following all the steps (only key files shown):

```text
my-react-app/
├─ package.json              # ← add test scripts
├─ vite.config.js            # ← add Vitest config
├─ setupTests.js             # ← new: jest-dom + cleanup
├─ index.html
├─ src/
│  ├─ main.jsx
│  ├─ App.jsx
│  ├─ components/
│  │  ├─ Hello.jsx          # ← new component
│  │  ├─ Hello.test.jsx     # ← new test file
│  │  ├─ Counter.jsx        # ← new component
│  │  └─ Counter.test.jsx   # ← new test file
│  └─ ...
└─ ...
```

---

## 1. Start with a Vite + React project

If you already have a Vite React app, skip to step 2.

```bash
npm create vite@latest my-react-app -- --template react
cd my-react-app
npm install
```

---

## 2. Install testing libraries

Run this inside your project:

```bash
npm install -D vitest jsdom \
  @testing-library/react \
  @testing-library/jest-dom \
  @testing-library/user-event
```

**What these do:**

* `vitest` → the test runner
* `jsdom` → fake browser environment for tests
* `@testing-library/react` → render React components in tests
* `@testing-library/jest-dom` → nicer assertions (`toBeInTheDocument`, etc.)
* `@testing-library/user-event` → simulate real user actions (click, type…)

---

## 3. Create the global test setup file

**File we touch:** `setupTests.js` (new)

Create a new file in the project root called `setupTests.js`:

```js
// setupTests.js
import { afterEach } from 'vitest'
import { cleanup } from '@testing-library/react'

// Adds jest-dom matchers like toBeInTheDocument, toHaveTextContent, etc.
import '@testing-library/jest-dom/vitest'

// Automatically unmount and cleanup DOM after each test
afterEach(() => {
  cleanup()
})
```

This file:

* Makes jest-dom matchers available in **all** tests
* Ensures React Testing Library cleans up between tests

---

## 4. Configure Vitest in `vite.config.js`

**File we touch:** `vite.config.js`

Open `vite.config.js` and update it to look something like this:

```js
// vite.config.js
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import { configDefaults } from 'vitest/config'

export default defineConfig({
  plugins: [react()],
  test: {
    environment: 'jsdom',         // use jsdom to simulate a browser
    globals: true,                // so we can use describe/it/expect globally
    setupFiles: './setupTests.js', // run our setup before tests
    exclude: [...configDefaults.exclude, 'e2e/**'], // optional
  },
})
```

The important parts:

* `environment: 'jsdom'` → needed for DOM + React tests
* `setupFiles` → tells Vitest to load `setupTests.js` first

---

## 5. Add test scripts to `package.json`

**File we touch:** `package.json`

Open `package.json` and add these scripts inside `"scripts"`:

```jsonc
"scripts": {
  "dev": "vite",
  "build": "vite build",
  "preview": "vite preview",
  "test": "vitest",
  "test:run": "vitest run"
}
```

Now you can run:

* `npm test` → watch mode
* `npm run test:run` → run tests once

---

## 6. Create a simple component: `Hello`

**File we touch:** `src/components/Hello.jsx` (new)

```jsx
// src/components/Hello.jsx
export function Hello({ name }) {
  return <h1>Hello, {name}!</h1>
}
```

---

## 7. Test the `Hello` component

**File we touch:** `src/components/Hello.test.jsx` (new)

```jsx
// src/components/Hello.test.jsx
import { render, screen } from '@testing-library/react'
import { Hello } from './Hello'

describe('Hello component', () => {
  it('shows a greeting with the name', () => {
    render(<Hello name="Student" />)

    // Find the element by its text content
    const heading = screen.getByText('Hello, Student!')

    // This matcher comes from jest-dom via setupTests.js
    expect(heading).toBeInTheDocument()
  })
})
```

**What’s happening:**

* `render(<Hello />)` → mounts the component into a virtual DOM
* `screen.getByText` → finds what the user would visually see
* `toBeInTheDocument()` → checks that it exists in the rendered output

---

## 8. Create a component with interaction: `Counter`

**File we touch:** `src/components/Counter.jsx` (new)

```jsx
// src/components/Counter.jsx
import { useState } from 'react'

export function Counter() {
  const [count, setCount] = useState(0)

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(c => c + 1)}>Increment</button>
    </div>
  )
}
```

---

## 9. Test the `Counter` component

**File we touch:** `src/components/Counter.test.jsx` (new)

```jsx
// src/components/Counter.test.jsx
import { render, screen } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import { Counter } from './Counter'

describe('Counter', () => {
  it('increments when the button is clicked', async () => {
    render(<Counter />)

    // Find the button by its role and accessible name
    const button = screen.getByRole('button', { name: /increment/i })

    // Simulate a user click
    await userEvent.click(button)

    // After clicking, the text should update
    expect(screen.getByText('Count: 1')).toBeInTheDocument()
  })
})
```

**Key ideas:**

* `userEvent.click` simulates a *real* user click
* We don’t inspect state directly; we check what the user sees (`Count: 1`)

---

## 10. Run your tests

Now run:

```bash
npm test
```

You should see Vitest start, discover `*.test.jsx` files, and run them.

If everything’s correct, both `Hello` and `Counter` tests should pass ✅

---

## Final Checklist: Did we do all the steps?

### Files and changes

* [ ] **Dependencies installed**

  * [ ] `vitest`, `jsdom`, `@testing-library/react`, `@testing-library/jest-dom`, `@testing-library/user-event`
* [ ] **`setupTests.js` created**

  * [ ] Imports `@testing-library/jest-dom/vitest`
  * [ ] Calls `cleanup()` in `afterEach`
* [ ] **`vite.config.js` updated**

  * [ ] `test.environment = 'jsdom'`
  * [ ] `test.globals = true`
  * [ ] `test.setupFiles = './setupTests.js'`
* [ ] **`package.json` updated**

  * [ ] `"test": "vitest"`
  * [ ] `"test:run": "vitest run"`
* [ ] **Components created**

  * [ ] `src/components/Hello.jsx`
  * [ ] `src/components/Counter.jsx`
* [ ] **Tests created**

  * [ ] `src/components/Hello.test.jsx`
  * [ ] `src/components/Counter.test.jsx`
* [ ] **`npm test` runs successfully** and passes all tests

---

## Resources

### React Testing Library Documentation

For more advanced testing patterns and additional query methods, check out the official React Testing Library documentation:

* **[React Testing Library API Reference](https://testing-library.com/docs/react-testing-library/api)** - Complete API documentation for all testing utilities, queries, and helpers
* **[Query Priority Guide](https://testing-library.com/docs/queries/about#priority)** - Learn which queries to use first (getByRole, getByLabelText, etc.)
* **[User Event Documentation](https://testing-library.com/docs/user-event/intro)** - Advanced user interaction simulation
* **[Common Testing Scenarios](https://testing-library.com/docs/react-testing-library/example-intro)** - Examples for forms, async operations, and more

### Additional Learning

* **[Vitest Documentation](https://vitest.dev/)** - Complete Vitest testing framework reference
* **[jest-dom Matchers](https://github.com/testing-library/jest-dom)** - All available DOM matchers like `toBeInTheDocument`, `toHaveClass`, etc.
