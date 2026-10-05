import tkinter as tk
from tkinter import ttk, messagebox

# ============================================================
# HEALTHRISK AI - PROFESSIONAL SCREENING DASHBOARD
# Standard Library Tkinter (No external pip packages needed)
# ============================================================

# Color Palette (Modern Slate & Healthcare Teal)
BG_MAIN = "#F1F5F9"         # Slate 100
CARD_BG = "#FFFFFF"         # Pure white cards
BORDER_COLOR = "#E2E8F0"    # Subtle borders
PRIMARY_COLOR = "#0D9488"   # Clinical Teal
PRIMARY_HOVER = "#0F766E"
TEXT_DARK = "#0F172A"       # Slate 900
TEXT_MUTED = "#64748B"      # Slate 500
HEADER_BG = "#0F172A"       # Deep Slate Header

# Badge Colors
COLOR_GREEN_BG = "#DCFCE7"
COLOR_GREEN_FG = "#15803D"
COLOR_YELLOW_BG = "#FEF9C3"
COLOR_YELLOW_FG = "#A16207"
COLOR_RED_BG = "#FEE2E2"
COLOR_RED_FG = "#B91C1C"


# ------------------------------------------------------------
# CORE CALCULATIONS
# ------------------------------------------------------------

def calculate_bmi(height_cm, weight_kg):
    if height_cm <= 0:
        return 0.0
    h_m = height_cm / 100.0
    return weight_kg / (h_m ** 2)

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight", COLOR_YELLOW_BG, COLOR_YELLOW_FG
    elif bmi < 25.0:
        return "Normal", COLOR_GREEN_BG, COLOR_GREEN_FG
    elif bmi < 30.0:
        return "Overweight", COLOR_YELLOW_BG, COLOR_YELLOW_FG
    else:
        return "Obesity", COLOR_RED_BG, COLOR_RED_FG

def blood_pressure_risk(systolic, diastolic):
    if systolic >= 180 or diastolic >= 120:
        return "Crisis (>=180/120)", COLOR_RED_BG, COLOR_RED_FG
    elif systolic >= 140 or diastolic >= 90:
        return "Stage 2 High", COLOR_RED_BG, COLOR_RED_FG
    elif systolic >= 130 or diastolic >= 80:
        return "Stage 1 Elevated", COLOR_YELLOW_BG, COLOR_YELLOW_FG
    else:
        return "Normal (<120/80)", COLOR_GREEN_BG, COLOR_GREEN_FG

def heart_rate_risk(hr):
    if hr < 60:
        return "Low (<60 BPM)", COLOR_YELLOW_BG, COLOR_YELLOW_FG
    elif hr > 100:
        return "High (>100 BPM)", COLOR_RED_BG, COLOR_RED_FG
    else:
        return "Normal (60-100)", COLOR_GREEN_BG, COLOR_GREEN_FG

def cholesterol_risk(chol):
    if chol >= 240:
        return "High (>=240)", COLOR_RED_BG, COLOR_RED_FG
    elif chol >= 200:
        return "Borderline", COLOR_YELLOW_BG, COLOR_YELLOW_FG
    else:
        return "Desirable (<200)", COLOR_GREEN_BG, COLOR_GREEN_FG

def diabetes_risk(glucose, bmi, age):
    score = 0
    if glucose >= 126: score += 4
    elif glucose >= 100: score += 2

    if bmi >= 30: score += 2
    elif bmi >= 25: score += 1

    if age >= 45: score += 2
    elif age >= 35: score += 1

    if score >= 6:
        return "High Risk", COLOR_RED_BG, COLOR_RED_FG, score
    elif score >= 3:
        return "Moderate Risk", COLOR_YELLOW_BG, COLOR_YELLOW_FG, score
    else:
        return "Lower Risk", COLOR_GREEN_BG, COLOR_GREEN_FG, score

def cardiovascular_score(age, sex, systolic, diastolic, hr, bmi, chol, glucose, smoking):
    score = 0
    if sex == "Male":
        score += 1
        if age >= 55: score += 3
        elif age >= 45: score += 2
        elif age >= 35: score += 1
    else:
        if age >= 65: score += 3
        elif age >= 55: score += 2
        elif age >= 45: score += 1

    if systolic >= 140 or diastolic >= 90: score += 3
    elif systolic >= 130 or diastolic >= 80: score += 1

    if bmi >= 30: score += 2
    elif bmi >= 25: score += 1

    if hr > 100 or hr < 50: score += 1

    if chol >= 240: score += 3
    elif chol >= 200: score += 1

    if glucose >= 126: score += 3
    elif glucose >= 100: score += 1

    if smoking == "Yes": score += 2

    if score >= 9:
        return "High Risk", COLOR_RED_BG, COLOR_RED_FG, score
    elif score >= 5:
        return "Moderate Risk", COLOR_YELLOW_BG, COLOR_YELLOW_FG, score
    else:
        return "Lower Risk", COLOR_GREEN_BG, COLOR_GREEN_FG, score


# ------------------------------------------------------------
# GUI CONTROLLER
# ------------------------------------------------------------

def run_analysis(event=None):
    try:
        a_str = age_ent.get().strip()
        h_str = height_ent.get().strip()
        w_str = weight_ent.get().strip()
        sys_str = sys_ent.get().strip()
        dia_str = dia_ent.get().strip()
        hr_str = hr_ent.get().strip()
        glu_str = glu_ent.get().strip()
        chol_str = chol_ent.get().strip()

        if not all([a_str, h_str, w_str, sys_str, dia_str, hr_str, glu_str, chol_str]):
            messagebox.showwarning("Missing Fields", "Please enter all required clinical values.")
            return

        age = float(a_str)
        height = float(h_str)
        weight = float(w_str)
        systolic = float(sys_str)
        diastolic = float(dia_str)
        hr = float(hr_str)
        glucose = float(glu_str)
        cholesterol = float(chol_str)
        sex = sex_var.get()
        smoking = smoking_var.get()

    except ValueError:
        messagebox.showerror("Format Error", "Please provide valid numerical numbers.")
        return

    # Validation Checks
    if not (1 <= age <= 125):
        messagebox.showerror("Validation", "Age must be between 1 and 125.")
        return
    if not (40 <= height <= 260):
        messagebox.showerror("Validation", "Height must be between 40 and 260 cm.")
        return
    if not (10 <= weight <= 400):
        messagebox.showerror("Validation", "Weight must be between 10 and 400 kg.")
        return
    if not (50 <= systolic <= 300) or not (30 <= diastolic <= 200):
        messagebox.showerror("Validation", "Systolic/Diastolic values outside physiological limits.")
        return
    if systolic <= diastolic:
        messagebox.showerror("Validation", "Systolic pressure must be greater than Diastolic pressure.")
        return
    if not (30 <= hr <= 250):
        messagebox.showerror("Validation", "Heart rate must be between 30 and 250 BPM.")
        return

    # Calculations
    bmi = calculate_bmi(height, weight)
    bmi_text, bmi_bg, bmi_fg = bmi_category(bmi)
    bp_text, bp_bg, bp_fg = blood_pressure_risk(systolic, diastolic)
    hr_text, hr_bg, hr_fg = heart_rate_risk(hr)
    chol_text, chol_bg, chol_fg = cholesterol_risk(cholesterol)
    diab_text, diab_bg, diab_fg, diab_pts = diabetes_risk(glucose, bmi, age)
    cardio_text, cardio_bg, cardio_fg, cardio_pts = cardiovascular_score(
        age, sex, systolic, diastolic, hr, bmi, cholesterol, glucose, smoking
    )

    # Update Card Badges
    update_card(card_bmi, f"{bmi:.1f} kg/m²", bmi_text, bmi_bg, bmi_fg)
    update_card(card_bp, f"{int(systolic)}/{int(diastolic)} mmHg", bp_text, bp_bg, bp_fg)
    update_card(card_hr, f"{int(hr)} BPM", hr_text, hr_bg, hr_fg)
    update_card(card_chol, f"{int(cholesterol)} mg/dL", chol_text, chol_bg, chol_fg)
    update_card(card_diab, f"Fasting: {int(glucose)} mg/dL", diab_text, diab_bg, diab_fg)
    update_card(card_cardio, f"Index: {cardio_pts} pts", cardio_text, cardio_bg, cardio_fg)

    # Aggregate Overall Risk Score
    total_pts = 0
    if cardio_text == "High Risk": total_pts += 3
    elif cardio_text == "Moderate Risk": total_pts += 2

    if diab_text == "High Risk": total_pts += 3
    elif diab_text == "Moderate Risk": total_pts += 2

    if "Crisis" in bp_text or "Stage 2" in bp_text: total_pts += 3
    elif "Stage 1" in bp_text: total_pts += 1

    if bmi >= 30: total_pts += 2
    elif bmi >= 25: total_pts += 1

    if chol_text.startswith("High"): total_pts += 2
    elif chol_text == "Borderline": total_pts += 1

    # Meter Progress (Max capped at 12 pts for display)
    pct = min(100, int((total_pts / 11.0) * 100))
    score_progress['value'] = pct

    if total_pts >= 8:
        overall_title.config(text="HIGHER CLINICAL SCREENING RISK", fg="#DC2626")
        overall_banner.config(bg="#FEF2F2", highlightbackground="#F87171")
        overall_sub.config(
            text=f"Total Risk Score: {total_pts}/12 — Multiple significant risk factors detected. Clinical consultation recommended.",
            fg="#991B1B"
        )
    elif total_pts >= 4:
        overall_title.config(text="MODERATE SCREENING RISK", fg="#D97706")
        overall_banner.config(bg="#FFFBEB", highlightbackground="#FCD34D")
        overall_sub.config(
            text=f"Total Risk Score: {total_pts}/12 — Moderate indicators detected. Preventive lifestyle modifications advised.",
            fg="#92400E"
        )
    else:
        overall_title.config(text="LOWER SCREENING RISK", fg="#16A34A")
        overall_banner.config(bg="#F0FDF4", highlightbackground="#86EFAC")
        overall_sub.config(
            text=f"Total Risk Score: {total_pts}/12 — All evaluated parameters are within favorable ranges.",
            fg="#166534"
        )

def update_card(widget_dict, val_text, badge_text, bg_col, fg_col):
    widget_dict['val'].config(text=val_text)
    widget_dict['badge'].config(text=f"● {badge_text}", bg=bg_col, fg=fg_col)

def reset_all():
    for ent in [age_ent, height_ent, weight_ent, sys_ent, dia_ent, hr_ent, glu_ent, chol_ent]:
        ent.delete(0, tk.END)
    sex_var.set("Male")
    smoking_var.set("No")

    for card in [card_bmi, card_bp, card_hr, card_chol, card_diab, card_cardio]:
        card['val'].config(text="--")
        card['badge'].config(text="Pending", bg="#F1F5F9", fg=TEXT_MUTED)

    score_progress['value'] = 0
    overall_banner.config(bg="#FFFFFF", highlightbackground=BORDER_COLOR)
    overall_title.config(text="READY FOR ANALYSIS", fg=TEXT_MUTED)
    overall_sub.config(text="Enter patient parameters on the left and click 'Analyze Health Risk'.", fg=TEXT_MUTED)
    age_ent.focus_set()

def load_sample():
    reset_all()
    age_ent.insert(0, "52")
    height_ent.insert(0, "175")
    weight_ent.insert(0, "88")
    sys_ent.insert(0, "142")
    dia_ent.insert(0, "92")
    hr_ent.insert(0, "78")
    glu_ent.insert(0, "115")
    chol_ent.insert(0, "225")
    sex_var.set("Male")
    smoking_var.set("Yes")
    run_analysis()

def copy_report():
    if card_bmi['val'].cget("text") == "--":
        messagebox.showinfo("Clipboard", "Please run an analysis first.")
        return
    summary = (
        f"=== HEALTHRISK AI SCREENING SUMMARY ===\n"
        f"Status: {overall_title.cget('text')}\n"
        f"BMI: {card_bmi['val'].cget('text')} ({card_bmi['badge'].cget('text')})\n"
        f"Blood Pressure: {card_bp['val'].cget('text')} ({card_bp['badge'].cget('text')})\n"
        f"Heart Rate: {card_hr['val'].cget('text')} ({card_hr['badge'].cget('text')})\n"
        f"Glucose: {card_diab['val'].cget('text')} ({card_diab['badge'].cget('text')})\n"
        f"Cholesterol: {card_chol['val'].cget('text')} ({card_chol['badge'].cget('text')})\n"
        f"Cardiovascular: {card_cardio['val'].cget('text')} ({card_cardio['badge'].cget('text')})\n"
        f"Notes: {overall_sub.cget('text')}\n"
    )
    root.clipboard_clear()
    root.clipboard_append(summary)
    messagebox.showinfo("Copied", "Summary report copied to clipboard!")


# ============================================================
# INTERFACE CONSTRUCTION
# ============================================================

root = tk.Tk()
root.title("HealthRisk AI — Multi-Parameter Risk Screening")
root.geometry("1020x760")
root.minsize(980, 720)
root.configure(bg=BG_MAIN)
root.bind("<Return>", run_analysis)

# ----------------- TOP HEADER BAR -----------------
header = tk.Frame(root, bg=HEADER_BG, height=65)
header.pack(fill="x")

hdr_content = tk.Frame(header, bg=HEADER_BG)
hdr_content.pack(fill="both", expand=True, padx=25, pady=10)

tk.Label(
    hdr_content,
    text="⚕ HEALTHRISK AI",
    font=("Segoe UI", 16, "bold"),
    fg="#FFFFFF",
    bg=HEADER_BG
).pack(side="left")

tk.Label(
    hdr_content,
    text="Multi-Parameter Clinical Risk Screening Engine",
    font=("Segoe UI", 10),
    fg="#94A3B8",
    bg=HEADER_BG
).pack(side="left", padx=15, pady=3)

# ----------------- MAIN SPLIT CONTENT -----------------
body_frame = tk.Frame(root, bg=BG_MAIN)
body_frame.pack(fill="both", expand=True, padx=20, pady=15)
body_frame.columnconfigure(0, weight=4)  # Left input panel
body_frame.columnconfigure(1, weight=5)  # Right results dashboard
body_frame.rowconfigure(0, weight=1)

# ================= LEFT: PATIENT INTAKE FORM =================
left_card = tk.Frame(body_frame, bg=CARD_BG, highlightbackground=BORDER_COLOR, highlightthickness=1)
left_card.grid(row=0, column=0, sticky="nsew", padx=(0, 10))

tk.Label(
    left_card,
    text="Patient Information & Biometrics",
    font=("Segoe UI", 12, "bold"),
    fg=TEXT_DARK,
    bg=CARD_BG
).pack(anchor="w", padx=18, pady=(15, 10))

# Sub-container for inputs
form_grid = tk.Frame(left_card, bg=CARD_BG)
form_grid.pack(fill="both", expand=True, padx=18)
form_grid.columnconfigure(0, weight=1)
form_grid.columnconfigure(1, weight=1)

def make_field(parent, label_text, row, col, unit=""):
    f = tk.Frame(parent, bg=CARD_BG)
    f.grid(row=row, column=col, sticky="ew", padx=6, pady=6)
    
    lbl = tk.Label(f, text=label_text, font=("Segoe UI", 9, "bold"), fg=TEXT_MUTED, bg=CARD_BG)
    lbl.pack(anchor="w")
    
    box = tk.Frame(f, bg=CARD_BG)
    box.pack(fill="x", pady=(2, 0))
    
    ent = tk.Entry(box, font=("Segoe UI", 10), relief="solid", bd=1, highlightthickness=0)
    ent.pack(side="left", fill="x", expand=True, ipady=4)
    
    if unit:
        tk.Label(box, text=f" {unit}", font=("Segoe UI", 8), fg=TEXT_MUTED, bg=CARD_BG).pack(side="right")
    return ent

# Demographics
age_ent = make_field(form_grid, "Age", 0, 0, "yrs")

# Sex dropdown
f_sex = tk.Frame(form_grid, bg=CARD_BG)
f_sex.grid(row=0, column=1, sticky="ew", padx=6, pady=6)
tk.Label(f_sex, text="Biological Sex", font=("Segoe UI", 9, "bold"), fg=TEXT_MUTED, bg=CARD_BG).pack(anchor="w")
sex_var = tk.StringVar(value="Male")
sex_combo = ttk.Combobox(f_sex, textvariable=sex_var, values=["Male", "Female"], state="readonly", font=("Segoe UI", 9))
sex_combo.pack(fill="x", pady=(2, 0), ipady=3)

# Physicals
height_ent = make_field(form_grid, "Height", 1, 0, "cm")
weight_ent = make_field(form_grid, "Weight", 1, 1, "kg")

# Vitals
sys_ent = make_field(form_grid, "Systolic BP", 2, 0, "mmHg")
dia_ent = make_field(form_grid, "Diastolic BP", 2, 1, "mmHg")
hr_ent = make_field(form_grid, "Heart Rate", 3, 0, "BPM")

# Smoking dropdown
f_smoke = tk.Frame(form_grid, bg=CARD_BG)
f_smoke.grid(row=3, column=1, sticky="ew", padx=6, pady=6)
tk.Label(f_smoke, text="Smoking Status", font=("Segoe UI", 9, "bold"), fg=TEXT_MUTED, bg=CARD_BG).pack(anchor="w")
smoking_var = tk.StringVar(value="No")
smoking_combo = ttk.Combobox(f_smoke, textvariable=smoking_var, values=["No", "Yes"], state="readonly", font=("Segoe UI", 9))
smoking_combo.pack(fill="x", pady=(2, 0), ipady=3)

# Lab biomarkers
glu_ent = make_field(form_grid, "Fasting Glucose", 4, 0, "mg/dL")
chol_ent = make_field(form_grid, "Total Cholesterol", 4, 1, "mg/dL")

# Action Buttons
btn_bar = tk.Frame(left_card, bg=CARD_BG)
btn_bar.pack(fill="x", padx=18, pady=(15, 18))

btn_run = tk.Button(
    btn_bar,
    text="⚡ ANALYZE HEALTH RISK",
    command=run_analysis,
    font=("Segoe UI", 10, "bold"),
    bg=PRIMARY_COLOR,
    fg="white",
    activebackground=PRIMARY_HOVER,
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    pady=8
)
btn_run.pack(fill="x", pady=(0, 6))

util_row = tk.Frame(btn_bar, bg=CARD_BG)
util_row.pack(fill="x")

btn_sample = tk.Button(
    util_row,
    text="🎲 Sample Data",
    command=load_sample,
    font=("Segoe UI", 9),
    bg="#F8FAFC",
    fg=TEXT_DARK,
    relief="solid",
    bd=1,
    cursor="hand2"
)
btn_sample.pack(side="left", fill="x", expand=True, padx=(0, 4), pady=2)

btn_reset = tk.Button(
    util_row,
    text="↺ Reset",
    command=reset_all,
    font=("Segoe UI", 9),
    bg="#F8FAFC",
    fg=TEXT_DARK,
    relief="solid",
    bd=1,
    cursor="hand2"
)
btn_reset.pack(side="left", fill="x", expand=True, padx=(4, 0), pady=2)


# ================= RIGHT: RESULTS DASHBOARD =================
right_frame = tk.Frame(body_frame, bg=BG_MAIN)
right_frame.grid(row=0, column=1, sticky="nsew", padx=(10, 0))
right_frame.rowconfigure(1, weight=1)
right_frame.columnconfigure(0, weight=1)

# Overall Banner Card
overall_banner = tk.Frame(right_frame, bg=CARD_BG, highlightbackground=BORDER_COLOR, highlightthickness=1, padx=16, pady=14)
overall_banner.pack(fill="x", pady=(0, 10))

tk.Label(
    overall_banner,
    text="COMPREHENSIVE EVALUATION",
    font=("Segoe UI", 8, "bold"),
    fg=TEXT_MUTED,
    bg=overall_banner.cget("bg")
).pack(anchor="w")

overall_title = tk.Label(
    overall_banner,
    text="READY FOR ANALYSIS",
    font=("Segoe UI", 15, "bold"),
    fg=TEXT_MUTED,
    bg=overall_banner.cget("bg")
)
overall_title.pack(anchor="w", pady=(2, 2))

overall_sub = tk.Label(
    overall_banner,
    text="Enter patient parameters on the left and click 'Analyze Health Risk'.",
    font=("Segoe UI", 9),
    fg=TEXT_MUTED,
    bg=overall_banner.cget("bg"),
    wraplength=460,
    justify="left"
)
overall_sub.pack(anchor="w", pady=(0, 6))

# Risk Score Progress Bar
score_progress = ttk.Progressbar(overall_banner, orient="horizontal", mode="determinate", length=400)
score_progress.pack(fill="x", pady=(4, 0))

# 6 Metric KPI Cards Grid
cards_grid = tk.Frame(right_frame, bg=BG_MAIN)
cards_grid.pack(fill="both", expand=True)
cards_grid.columnconfigure(0, weight=1)
cards_grid.columnconfigure(1, weight=1)
cards_grid.rowconfigure(0, weight=1)
cards_grid.rowconfigure(1, weight=1)
cards_grid.rowconfigure(2, weight=1)

def create_kpi_card(parent, title, row, col):
    card = tk.Frame(parent, bg=CARD_BG, highlightbackground=BORDER_COLOR, highlightthickness=1, padx=12, pady=10)
    card.grid(row=row, column=col, sticky="nsew", padx=4, pady=4)

    lbl_t = tk.Label(card, text=title, font=("Segoe UI", 9, "bold"), fg=TEXT_MUTED, bg=CARD_BG)
    lbl_t.pack(anchor="w")

    lbl_v = tk.Label(card, text="--", font=("Segoe UI", 13, "bold"), fg=TEXT_DARK, bg=CARD_BG)
    lbl_v.pack(anchor="w", pady=(4, 6))

    lbl_b = tk.Label(
        card,
        text="Pending",
        font=("Segoe UI", 8, "bold"),
        bg="#F1F5F9",
        fg=TEXT_MUTED,
        padx=7,
        pady=2
    )
    lbl_b.pack(anchor="w")
    return {'val': lbl_v, 'badge': lbl_b, 'card': card}

card_bmi = create_kpi_card(cards_grid, "Body Mass Index (BMI)", 0, 0)
card_bp = create_kpi_card(cards_grid, "Blood Pressure", 0, 1)
card_hr = create_kpi_card(cards_grid, "Heart Rate", 1, 0)
card_chol = create_kpi_card(cards_grid, "Total Cholesterol", 1, 1)
card_diab = create_kpi_card(cards_grid, "Diabetes Profile", 2, 0)
card_cardio = create_kpi_card(cards_grid, "Cardiovascular Risk", 2, 1)

# Bottom Footer with Export and Disclaimer
footer_bar = tk.Frame(right_frame, bg=BG_MAIN)
footer_bar.pack(fill="x", pady=(8, 0))

btn_copy = tk.Button(
    footer_bar,
    text="📋 Copy Summary Report",
    command=copy_report,
    font=("Segoe UI", 9, "bold"),
    bg=CARD_BG,
    fg=TEXT_DARK,
    relief="solid",
    bd=1,
    cursor="hand2",
    padx=10,
    pady=4
)
btn_copy.pack(side="left")

tk.Label(
    footer_bar,
    text="*Educational tool only. Not a medical diagnosis.",
    font=("Segoe UI", 8, "italic"),
    fg=TEXT_MUTED,
    bg=BG_MAIN
).pack(side="right")

# Focus and Run
age_ent.focus_set()
root.mainloop()