# GIA Viz Demo (CSV → Pandas → JSON → D3)

This is a beginner-friendly template that converts a CSV to JSON with Pandas,
then renders a simple D3 scatter plot.

---

## 0) What you need (Mac + VS Code)

- **VS Code** installed
- **Python 3** installed (macOS often has it; if not, install from python.org)
- Optional but helpful: the **Live Server** extension in VS Code

---

## 1) Open this folder in VS Code

- Unzip the project.
- In VS Code: **File → Open Folder…** and select this folder.

---

## 2) Put your CSV in `data/raw.csv`

- Replace the sample `data/raw.csv` with your real file.
- Make sure your CSV has at least these columns for the demo:
  - `Age`
  - `Parent_Satisfaction_Score`
- (You can customize columns later; see the Python script.)

---

## 3) Create a Python virtual environment

Open VS Code **Terminal** (View → Terminal) and run:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

You should see `(.venv)` at the start of your terminal line (that means it's active).

---

## 4) Export JSON for D3

```bash
python scripts/export_to_json.py
```

If everything is OK, it writes `public/data.json`.

---

## 5) Start a local web server (two options)

### Option A: VS Code Live Server (easiest)
- In VS Code, install the **Live Server** extension.
- Open `public/index.html` in the editor.
- Right-click the editor and choose **Open with Live Server**.
- Your browser opens at something like `http://127.0.0.1:5500/public/index.html`.

### Option B: Built-in Python server
- In VS Code Terminal:
  ```bash
  cd public
  python3 -m http.server 8000
  ```
- Open your browser at http://localhost:8000/index.html

---

## 6) Publish to GitHub (two ways)

### Way 1: VS Code GUI (recommended for beginners)
1. Click the **Source Control** icon (left sidebar).
2. Click **Initialize Repository**.
3. Type a commit message like "Initial commit" and click **Commit** (✓ icon).
4. Click **Publish Branch** or **Publish to GitHub**; sign into GitHub if prompted.
5. VS Code creates a GitHub repo and pushes your code.

### Way 2: Terminal (manual)
1. Install Xcode command line tools (if `git` not found):
   ```bash
   xcode-select --install
   ```
2. In the project root:
   ```bash
   git init
   git add -A
   git commit -m "Initial commit"
   ```
3. Create a new empty repo on GitHub (no README), copy the HTTPS URL.
4. Back in Terminal, add the remote and push:
   ```bash
   git remote add origin https://github.com/<your-username>/<repo-name>.git
   git branch -M main
   git push -u origin main
   ```

---

## 7) Optional: Share a live link with GitHub Pages

Quickest path:
- Rename `public/` to `docs/` and update the Python script's output path to `docs/data.json`.
- Commit & push.
- On GitHub → **Settings → Pages → Build and deployment**:
  - Source: **Deploy from a branch**
  - Branch: **main** / folder: **/docs**
- Wait 1–2 minutes, your site will be live at the URL shown there.

---

## 8) Customize columns and charts

- Edit `scripts/export_to_json.py` to change which columns are exported.
- Edit `public/index.html` to change the D3 chart.
- For a reusable library, wrap your transforms into Python classes and export
  a JSON schema that stays consistent across projects.
