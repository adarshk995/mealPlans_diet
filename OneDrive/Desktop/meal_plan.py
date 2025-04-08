from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "7-Day Indian Vegetarian Meal + Snack Plan", ln=True, align="C")

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

pdf = PDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

intro = (
    "This plan is designed to support weight loss, improve skin, boost energy, and provide full-body nutrition."
)
pdf.multi_cell(0, 10, intro)

meal_plan = [
    ("Day 1", "Poha", "Dal + Rice", "Soup + Paneer", "Apple + PB", "Roasted Chana"),
    ("Day 2", "Oats Upma", "Roti + Lauki Dal", "Khichdi + Raita", "Yogurt + Berries", "Sprouts Salad"),
    ("Day 3", "Chilla", "Rajma + Rice", "Roti + Methi Aloo", "Banana + Almond Butter", "Chickpea Snack"),
    ("Day 4", "Ragi Dosa", "Pulao + Raita", "Paneer Roti", "Trail Mix", "Green Smoothie"),
    ("Day 5", "Besan Cheela", "Sambar + Beetroot", "Daliya", "Fruit + Nuts", "Energy Ball"),
    ("Day 6", "Idli", "Palak Paneer + Roti", "Chole Rice", "Crackers + Avocado", "Coconut Water"),
    ("Day 7", "Oats", "Tinda + Roti", "Lemon Rice + Curd", "Chia + Berries", "Popcorn + Nuts")
]

for day, bf, lunch, dinner, snack1, snack2 in meal_plan:
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, day, ln=True)
    pdf.set_font("Arial", "", 11)
    pdf.cell(0, 8, f"  Breakfast: {bf}", ln=True)
    pdf.cell(0, 8, f"  Lunch: {lunch}", ln=True)
    pdf.cell(0, 8, f"  Dinner: {dinner}", ln=True)
    pdf.cell(0, 8, f"  Snack 1: {snack1}", ln=True)
    pdf.cell(0, 8, f"  Snack 2: {snack2}", ln=True)
    pdf.ln(2)

pdf.set_font("Arial", "B", 12)
pdf.cell(0, 10, "Tips:", ln=True)
pdf.set_font("Arial", "", 11)
tips = [
    "Drink 2-3L water daily",
    "Minimal oil use",
    "Whole grains > white rice",
    "Daily protein: dal, paneer, sprouts",
    "Daily 30 mins activity",
]
for tip in tips:
    pdf.cell(0, 8, f"- {tip}", ln=True)

pdf.output("wellness_meal_plan.pdf")
print("PDF created: wellness_meal_plan.pdf")
