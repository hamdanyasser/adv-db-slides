# Advanced Database - Exam Study Materials

This repository contains comprehensive study materials for the Advanced Database open-book exam, including all course slides and complete solutions to sample midterm questions.

## 📚 Study Materials

### 🔥 **NEW: PowerPoint Study Guides**

#### **adv_db_midterm_5slides.pptx** ⭐ ULTRA-CONDENSED
**Perfect for quick reference during exam!**
- **Only 5 slides** with small text for maximum information density
- ALL midterm questions with complete answers
- Assignment 2 solutions (Arrays, JSON/JSONB, Data Types)
- Assignment 3 Full Text Search solutions
- Quick reference commands and operators
- Font size 6-8pt to fit everything

#### **adv_db_midterm_study_guide.pptx** (33 slides)
Complete presentation with all topics in readable format.

### 1. **adv_db_merged_slides.pdf**
Complete collection of all official course slides merged into one PDF.

**Contents:**
- Ch01: The Basics (38 pages)
- Ch02: Database Administration (45 pages)
- Ch03: psql (11 pages)
- Ch04: pgAdmin (10 pages)
- Ch05: Data Types (38 pages)
- Ch05: Full Text Search (27 pages)

**Total: 169 pages**

### 2. **midterm_sample_solutions.pdf**
Full questions and step-by-step solutions for the SAMPLE midterm (`midterm-demo.docx`).

**Topics Covered:**
- **Section 1: Managing Database Connections**
  - Retrieving connections and PIDs using `pg_stat_activity`
  - Canceling queries with `pg_cancel_backend()`
  - Terminating connections with `pg_terminate_backend()`
  - Killing all connections for a specific role

- **Section 2: Users, Roles & Permissions**
  - Creating users with expiration dates (`VALID UNTIL`)
  - Granting table-level permissions (`GRANT SELECT, INSERT, UPDATE, DELETE`)
  - Creating roles with inheritance (`CREATE ROLE ... WITH INHERIT`)
  - Role membership and testing access (`GRANT role TO user`)

- **Section 3: Tables, Data Types & Arrays**
  - Creating databases and tables with various data types:
    - `SERIAL` (auto-increment)
    - `VARCHAR(n)` (variable character)
    - `NUMERIC(precision, scale)`
    - `TEXT` (unlimited text)
    - `DATE` and `TIMESTAMP WITH TIME ZONE`
  - Loading data from CSV files (`COPY` and `\copy`)
  - String functions: `LPAD()`, `RPAD()`, `TRIM()`, `LTRIM()`, `RTRIM()`
  - Creating and using sequences (`CREATE SEQUENCE`, `nextval()`, `currval()`)
  - Array operations:
    - Creating array columns (`INTEGER[]`)
    - Updating arrays (`array_append()`, `||` operator)
    - Querying arrays (`@>` contains operator, `&&` overlap)
    - Array functions (`array_length()`, `array_position()`)

- **Section 4: Backup & Restore**
  - `pg_dump` for backups (plain SQL, custom, directory, tar formats)
  - `psql` for restoring plain SQL backups
  - `pg_restore` for restoring binary format backups
  - Parallel backup/restore with `-j` flag

### 3. **adv_db_merged_with_sample.pdf**
Combined PDF containing everything: all course slides followed by the sample midterm solutions. Perfect for printing or using as a single reference during the exam.

---

## 🚀 Quick Start

### View in Browser
Open `index.html` in your web browser for easy navigation and access to all materials.

### Print for Exam
Since this is an **open-book exam**, you can print any of these materials:
- Print `adv_db_merged_with_sample.pdf` for a complete reference
- Or print individual files based on your preference

---

## ⚠️ Important Notice

**This is study material for an open-book exam.**

The `midterm_sample_solutions.pdf` contains solutions for the **SAMPLE midterm** (`midterm-demo.docx`) - these are practice questions for studying. The real exam will be different.

You are allowed to bring these materials to the exam as it is open-book!

---

## 📖 Key Concepts to Remember

### Connection Management
- `pg_stat_activity` - view all active connections
- `pg_cancel_backend(pid)` - cancel a query (graceful)
- `pg_terminate_backend(pid)` - kill a connection (forceful)
- Always use `WHERE pid <> pg_backend_pid()` to avoid killing your own connection

### User & Permission Management
- `CREATE USER ... VALID UNTIL 'date'` - time-limited accounts
- `GRANT privilege ON table TO user/role` - grant permissions
- `REVOKE privilege ON table FROM user/role` - remove permissions
- `CREATE ROLE ... WITH INHERIT` - roles inherit permissions to members
- `GRANT role TO user` - add user to role

### Data Types
- `SERIAL` = auto-incrementing integer (uses sequence internally)
- `VARCHAR(n)` = variable length, max n characters
- `NUMERIC(p,s)` = p total digits, s digits after decimal
- `TEXT` = unlimited text
- `DATE` = date only (no time)
- `TIMESTAMP WITH TIME ZONE` = date + time + timezone (always use this!)
- `INTEGER[]` = array of integers

### Array Operations
- `@>` operator: left contains right (e.g., `interests @> ARRAY[1,5]`)
- `<@` operator: left is contained by right
- `&&` operator: arrays overlap
- `array_append(array, element)` - add to end
- `||` operator - concatenate
- Arrays are **1-indexed** (first element is `array[1]`, not `array[0]`)

### Backup & Restore
- `pg_dump database > file.sql` - plain SQL backup
- `pg_dump -F c database > file.dump` - custom format (compressed)
- `pg_dump -F d -f dir/ database` - directory format (supports parallel)
- `psql database < file.sql` - restore plain SQL
- `pg_restore -d database file.dump` - restore custom/directory/tar
- `pg_restore -j 4 -d database dir/` - parallel restore (4 jobs)

### Sequences
- `CREATE SEQUENCE name START WITH 100 INCREMENT BY 10`
- `nextval('sequence_name')` - get next value (increments)
- `currval('sequence_name')` - get current value (no increment)
- `setval('sequence_name', value)` - manually set value

### String Functions
- `LPAD(string, length, fill)` - pad on left
- `RPAD(string, length, fill)` - pad on right
- `TRIM(string)` - remove leading/trailing spaces
- `LTRIM(string)` - remove leading spaces
- `RTRIM(string)` - remove trailing spaces

---

## 🛠️ How These Materials Were Created

All materials were generated using Python scripts:

1. **merge_slides.py** - Merged all PDF slides using PyPDF2
2. **extract_midterm.py** - Extracted questions from midterm-demo.docx
3. **generate_midterm_solutions.py** - Generated comprehensive solutions using ReportLab
4. **create_combined_pdf.py** - Combined everything into one PDF

---

## 📝 Additional Files

- `midterm-demo.docx` - Original sample midterm questions (source material)
- Individual chapter PDFs (Ch01-Ch05) - Original course slides
- `index.html` - Web interface for easy navigation
- Python scripts (`.py` files) - Tools used to generate study materials

---

## ✅ Exam Preparation Checklist

- [ ] Review all course slides (169 pages)
- [ ] Go through each sample midterm question and solution
- [ ] Practice writing SQL commands for:
  - [ ] Connection management
  - [ ] User/role creation and permissions
  - [ ] Table creation with various data types
  - [ ] Array operations
  - [ ] Backup and restore commands
- [ ] Understand key PostgreSQL functions and operators
- [ ] Test queries on a PostgreSQL database if possible
- [ ] Print or download materials for the open-book exam
- [ ] Review the study tips in index.html

---

## 🎯 Good Luck!

Remember: This is an **open-book exam**, so you can bring these materials with you. Use them wisely, and make sure you understand the concepts, not just memorize the commands!

---

**Last Updated:** November 9, 2025
**Exam:** Advanced Database Midterm (Open Book)
