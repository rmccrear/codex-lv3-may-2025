Level Navigation: [1](./db-mini-project-lv-1.md) | **2** | [3](./db-mini-project-lv-3.md) | [4](./db-mini-project-lv-4.md) | [5](./db-mini-project-lv-5.md) | [6](./db-mini-project-lv-6.md) | [7](./db-mini-project-lv-7.md) | [8](./db-mini-project-lv-8.md) | [9](./db-mini-project-lv-9.md) | [10](./db-mini-project-lv-10.md) | [11](./db-mini-project-lv-11.md) | [12](./db-mini-project-lv-12.md) | [13](./db-mini-project-lv-13.md) | [14](./db-mini-project-lv-14.md) | [15](./db-mini-project-lv-15.md) | [16](./db-mini-project-lv-16.md) | [17](./db-mini-project-lv-17.md) | [18](./db-mini-project-lv-18.md) | [19⚡](./db-mini-project-lv-19.md) | [20](./db-mini-project-lv-20.md)

# Level 2: Project Setup

**Goal:** Set up your development environment with Vite and React.

**User Story:** As a developer, I want to create a new React project and install dependencies so that I can start building my potluck management app.

---

## What You'll Do

Create a new React project using Vite and install the Supabase client library.

## Instructions

- Create a new React project using Vite: `npm create vite@latest practice-with-db -- --template react`
- Navigate to the project folder: `cd practice-with-db`
- Install dependencies: `npm install`
- Install Supabase client: `npm install @supabase/supabase-js`
- Install tslib to support the Supabase client: `npm install tslib`
- Start the development server to verify setup: `npm run dev`
- Open the project in your code editor

See here for installation details: [Install Supabase Client](https://rmccrear.github.io/codex-lv3-may-2025/week5/supabase-setup/SUPABASE_REACT_SETUP_GUIDE.html#step-7-install-supabase-client-library)

## 💡 Code Hints

Need help with project setup? Check out these snippets:

<details>
<summary>Show Me: Creating the project</summary>

<pre><code class="language-bash">npm create vite@latest practice-with-db -- --template react
cd practice-with-db
npm install
</code></pre>

</details>

<details>
<summary>Show Me: Installing Supabase</summary>

<pre><code class="language-bash">npm install @supabase/supabase-js
</code></pre>

</details>

<details>
<summary>Show Me: Project structure</summary>

<pre><code class="language-bash">practice-with-db/
├── src/
│   ├── components/
│   │   └── PotluckMeals.jsx
│   ├── utils/
│   │   └── supabase.js
│   ├── App.jsx
│   └── main.jsx
├── package.json
└── README.md
</code></pre>

</details>

## 🔍 Diving Deeper

**Why do we need these libraries?**

- **`@supabase/supabase-js`**: This is the official JavaScript client library for Supabase. It provides all the functions we need to connect to our database, perform queries, and handle authentication. Without it, we'd have to write complex HTTP requests manually.

- **`tslib`**: This is a TypeScript runtime library that Supabase depends on. Even though we're using JavaScript, Supabase's internal code uses TypeScript features, so we need this library to support those features.

**Where do these libraries go?**

When you run `npm install`, npm:
1. Downloads the libraries from the npm registry
2. Stores them in the `node_modules/` folder in your project
3. Updates your `package.json` file to record the dependencies

**How to verify installation:**

1. **Check `package.json`**: Open your `package.json` file and look for the `dependencies` section:
   ```json
   {
     "dependencies": {
       "@supabase/supabase-js": "^2.x.x",
       "tslib": "^2.x.x"
     }
   }
   ```

2. **Check `node_modules/`**: Look in your project folder for a `node_modules/` directory. Inside, you should see folders named `@supabase` and `tslib`.

3. **Verify in terminal**: Run `npm list` to see all installed packages and their versions.

## ✅ Check

1. Run `npm run dev` to start your development server
2. Open your browser to `http://localhost:5173`
3. You should see the default Vite + React welcome page
4. Check that `@supabase/supabase-js` is listed in your `package.json` dependencies
5. Open your project folder in VS Code and verify you can see the basic file structure

---

---