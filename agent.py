import json
import os

# Load college data
with open("college_info.json", "r", encoding="utf-8") as f:
    college_data = json.load(f)

# Admins and alumni
administrative_members = {
    "vice chairman": {
        "name": "Dr. N. Mathan Karthick",
        "designation": "Vice-Chairman, Excel Group Institutions",
        "contact": "9942899958",
        "email": "vc@excelcolleges.com",
        "location": "Komarapalayam – 637303"
    },
    "chairman": {
        "name": "Prof. Dr. A. K. Natesan",
        "designation": "Founder and Chairman, Excel Group Institutions",
        "contact": "9443373156",
        "email": "chairman@excelcolleges.com",
        "location": "Komarapalayam – 637 303"
    },
    "director technical": {
        "name": "Dr. N. Sengottaian",
        "designation": "Professor and Director – Technical",
        "contact": "9965577789",
        "email": "technicaldirector@excelcolleges.com",
        "location": "Komarapalayam – 637303"
    },
    "principal": {
        "name": "Dr. K. Bommanna Raja",
        "designation": "Principal",
        "contact": "9626238999",
        "email": "principaleec@excelcolleges.com"
    },
    "ugc nominee": {
        "name": "Dr. Pragya Shukla",
        "designation": "UGC Nominee",
        "contact": "9425082663",
        "email": "pragyashukla_ict@yahoo.co.in"
    },
    "university nominee": {
        "name": "Dr. S. Subramanian",
        "designation": "University Nominee",
        "contact": "8056075025",
        "email": "ssubbu@annauniv.edu"
    },
    "state nominee": {
        "name": "Dr. T. Balusamy",
        "designation": "State Government Nominee"
    }
}

alumni_stories = [
    "🎓 *Ms. Divya S* — Software Engineer at Google, B.E. CSE alumna.",
    "🎓 *Mr. Aravind K* — Mechanical grad, robotics startup founder.",
    "🎓 *Ms. Priya R* — ECE alumna, Sr. Manager at Zoho.",
    "🎓 *Mr. Karthik M* — MBA grad, HR Director at TCS.",
    "🎓 *Ms. Sneha L* — AI & DS grad, AI Engineer at Microsoft."
]

all_suggestions = [
    "Admission", "Courses",    "Placements", "Companies",
    "Facilities", "Transport", "Wi-Fi", "MBA", "Library", "TNEA", "Last date", "Faculty","Eligibility", "Fees", "Scholarships", "Hostel", "Sports", "Gym",   "Documents","Online apply", "Research", "Innovation", "Entrepreneurship",  "Departments", "Girls hostel","Mess", "Food", "Extracurricular", "Workshops", "Industrial visits", "Dress code", "Anti-ragging",
    "Fests", "Student clubs", "Campus area", "Safety", "Medical", "Laptops", "Alumni stories", "Contact",
    "CCTV", "Smart classrooms", "ATM", "Campus tour", "Refund", "NRI", "University tie-ups", "Soft skills","Courses Offered", "Admission Process", "Eligibility Criteria", "Fee Structure", "Scholarships", "Placements", "Hostel Facilities", "Application Last Date", "Faculty / Departments", "Contact Information"

]


# Goal logic
def handle_goal(msg: str):
    msg = msg.lower()

    if "admission" in msg:
        return (
            "📌 **Admission Help**\n"
            "- Eligibility: 12th PCM + TNEA (UG), GATE/TANCET (PG).\n"
            "- Process: Online form → Docs → Counseling.\n"
            "- Docs: Marksheets, Scorecards, ID proof.\n"
            "- Last Date: June–July (check site).\n"
            "- Apply: https://excelinstitutions.com/excel_engg/"
        )

    elif "mba" in msg:
        return (
            "🎓 **MBA Programs**\n"
            "- Types: General MBA, MBA IEV, 5-Year Integrated.\n"
            "- Curriculum: Finance, HR, Marketing, Innovation.\n"
            "- Placement: 90%+ in TCS, Zoho, Infosys, HCL."
        )

    elif "hostel" in msg:
        return (
            "🏠 **Hostel Info**\n"
            "- Separate for boys/girls, ₹40K/year.\n"
            "- Wi-Fi, mess, medical, laundry included."
        )

    elif "placement" in msg:
        return (
            "💼 **Placements**\n"
            "- 90%+ placement record.\n"
            "- Companies: TCS, Infosys, DataPattern.ai, Wipro.\n"
            "- Includes training, mock interviews, alumni help."
        )

    elif any(keyword in msg for keyword in ["location", "distance", "how far", "nearby"]):
        return (
            "📍 **Location & Distance Info:**\n"
            "- Komarapalayam to Salem: **50 km**\n"
            "- Komarapalayam to Erode: **35 km**\n"
            "- Komarapalayam to Coimbatore: **115 km**\n"
            "- Komarapalayam to Namakkal: **60 km**\n"
            "- Komarapalayam to Tiruchengode: **18 km**\n"
            "🛣️ Easily accessible by road and public transport via NH544."
        )

    return None
