Level Navigation: [1](./db-mini-project-lv-1.md) | [2](./db-mini-project-lv-2.md) | **3** | [4](./db-mini-project-lv-4.md) | [5](./db-mini-project-lv-5.md) | [6](./db-mini-project-lv-6.md) | [7](./db-mini-project-lv-7.md) | [8](./db-mini-project-lv-8.md) | [9](./db-mini-project-lv-9.md) | [10](./db-mini-project-lv-10.md) | [11](./db-mini-project-lv-11.md) | [12](./db-mini-project-lv-12.md) | [13](./db-mini-project-lv-13.md) | [14](./db-mini-project-lv-14.md) | [15](./db-mini-project-lv-15.md) | [16](./db-mini-project-lv-16.md) | [17](./db-mini-project-lv-17.md) | [18](./db-mini-project-lv-18.md) | [19⚡](./db-mini-project-lv-19.md) | [20](./db-mini-project-lv-20.md)

# Level 3: Database Setup

**Goal:** Configure your Supabase database with tables and security policies.

**User Story:** As a developer, I want to set up my database tables and security policies so that I can store and retrieve potluck data securely.

---

## What You'll Do

Follow the Supabase setup guides to create your database tables and configure access policies.

## Instructions

- Complete the [Supabase Setup Guide](https://rmccrear.github.io/codex-lv3-may-2025/week5/supabase-setup/SUPABASE_SETUP_GUIDE.html) to create your account and project
- Create a `potluck_meals` table with these columns:
  - `meal_name` (text)
  - `guest_name` (text)
  - `serves` (integer)
  - `kind_of_dish` (text)
- Add at least 3 sample meals
- Set up [read policies](https://rmccrear.github.io/codex-lv3-may-2025/week5/supabase-setup/SUPABASE_SETUP_GUIDE.html#step-10-set-up-read-policy-allow-public-read-access) and [insert policies](https://rmccrear.github.io/codex-lv3-may-2025/week5/supabase-setup/SUPABASE_SETUP_GUIDE.html#step-11-set-up-write-policy-allow-public-write-access) for public access
- Follow the [Supabase React Setup Guide](https://rmccrear.github.io/codex-lv3-may-2025/week5/supabase-setup/SUPABASE_REACT_SETUP_GUIDE.html) to configure environment variables

**⚠️ Important Note**: Do NOT use the starter code for `App.jsx` from the Supabase setup guide. That code puts everything in one file, but we'll be organizing our app into separate components. Follow the component structure outlined in Levels 4-6 below instead.

<details>
<summary>Show Me: Sample data in database</summary>

<img src="./docs/00-screenshot-list-meals-db-table.png" alt="Sample data in database" />

</details>

## ✅ Check

1. Your Supabase project is created and accessible
2. The `potluck_meals` table exists with the correct columns
3. You have sample data in your table
4. RLS policies are enabled and configured
5. Environment variables are set up in your React project
6. You can see your data in the Supabase dashboard

---

---