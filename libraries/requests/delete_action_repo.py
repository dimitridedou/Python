import requests

# Ρύθμιση
GITHUB_TOKEN = "ΒΑΛΕ_ΕΔΩ_ΤΟ_TOKEN"
OWNER = "το-username-σου"
REPO = "το-repo-σου"

# Headers για authentication
headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json"
}

# Παίρνουμε τα runs (μέχρι 100)
url = f"https://api.github.com/repos/{OWNER}/{REPO}/actions/runs?per_page=100"
response = requests.get(url, headers=headers)

if response.status_code == 200:
    runs = response.json()["workflow_runs"]
    total = len(runs)
    print(f"Βρέθηκαν {total} runs")

    if total > 50:
        # Κρατάμε τα πιο πρόσφατα total-50 και διαγράφουμε τα 50 παλιότερα
        runs_to_delete = runs[50:]  # αυτά είναι τα παλιότερα

        for run in runs_to_delete:
            run_id = run["id"]
            del_url = f"https://api.github.com/repos/{OWNER}/{REPO}/actions/runs/{run_id}"
            del_resp = requests.delete(del_url, headers=headers)

            if del_resp.status_code == 204:
                print(f"Διαγράφηκε το run {run_id}")
            else:
                print(f"Απέτυχε η διαγραφή του run {run_id}: {del_resp.status_code}")
    else:
        print("Δεν υπάρχουν πάνω από 50 runs για να διαγραφούν.")
else:
    print("Σφάλμα στο fetch:", response.status_code, response.text)
