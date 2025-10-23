Level Navigation: [1](./db-mini-project-lv-1.md) | [2](./db-mini-project-lv-2.md) | [3](./db-mini-project-lv-3.md) | [4](./db-mini-project-lv-4.md) | [5](./db-mini-project-lv-5.md) | [6](./db-mini-project-lv-6.md) | [7](./db-mini-project-lv-7.md) | [8](./db-mini-project-lv-8.md) | [9](./db-mini-project-lv-9.md) | [10](./db-mini-project-lv-10.md) | **11** | [12](./db-mini-project-lv-12.md) | [13](./db-mini-project-lv-13.md) | [14](./db-mini-project-lv-14.md) | [15](./db-mini-project-lv-15.md) | [16](./db-mini-project-lv-16.md) | [17](./db-mini-project-lv-17.md) | [18](./db-mini-project-lv-18.md) | [19⚡](./db-mini-project-lv-19.md) | [20](./db-mini-project-lv-20.md)

# Level 11: Create Insert RLS Policy

**Goal:** Set up a write policy for your potluck_meals table.

**User Story:** As a developer, I want to configure database security policies so that users can insert new meals into the database.

---

## What You'll Do

Follow the Supabase Setup Guide to set up a write policy for your potluck_meals table.

## Instructions

- Follow the [Supabase Setup Guide - Step 11](https://rmccrear.github.io/codex-lv3-may-2025/week5/supabase-setup/SUPABASE_SETUP_GUIDE.html#step-11-set-up-write-policy-allow-public-write-access) to set up a write policy
- Click **"New Policy"** in your Supabase dashboard
- Give it a policy name (e.g., "Enable insert for all users")
- Select **"INSERT"** operation
- Add `true` to the **"with check"** statement in the policy
- Click **"Save"**

This allows anyone to **create** new rows in your table.

**🔒 Cybersecurity Reflection**: Think about this statement from a security perspective. What are the potential risks of allowing "anyone" to create new rows in your database? Consider:
- What could happen if malicious users submit inappropriate data?
- How might this policy affect data integrity?
- What would be a more secure approach for a production application?
- Why is this policy acceptable for learning projects but not for real applications?

**Note**: This policy is intentionally permissive for learning purposes. In production applications, you would implement proper authentication and authorization controls.

<details>
<summary>Show Me: RLS Policy for inserts</summary>

<img src="./docs/03-screenshot-custom-rls-policy.png" alt="RLS Policy for inserts" />

</details>

<details>
<summary>Show Me: Potential RLS error</summary>

<img src="./docs/04-screenshot-potential-rls-error.png" alt="Potential RLS error" />

</details>

## ✅ Check

1. You have created a new RLS policy
2. The policy allows INSERT operations
3. The policy uses `true` in the "with check" statement
4. The policy is saved and active
5. You understand the security implications

---