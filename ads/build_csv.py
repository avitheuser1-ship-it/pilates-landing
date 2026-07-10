# -*- coding: utf-8 -*-
"""Build a Google Ads Editor bulk CSV (multi-section format).
Each entity type gets its own section header row, separated by blank lines.
This is what Editor expects for 'Import from CSV'."""
import csv, os

BASE = "https://avitheuser1-ship-it.github.io/pilates-landing"
P1 = BASE + "/product1.html"
P2 = BASE + "/product2.html"
P3 = BASE + "/product3.html"
HOME = BASE + "/"
PHONE = "0500000000"
COUNTDOWN_DATE = "20260730"   # 30/7/2026
COUNTDOWN_LANG = "Hebrew"

# ---- helper to write a section ----
def section(rows_out, header, fieldnames, items):
    rows_out.append(header)               # section header
    rows_out.append(fieldnames)           # column names
    for it in items:
        rows_out.append([it.get(c, "") for c in fieldnames])
    rows_out.append([])                   # blank separator

all_rows = []

# ============ 1. CAMPAIGNS ============
camp_header = ["Campaign", "Campaign type", "Campaign subtype", "Status", "Networks",
               "Languages", "Bid strategy type", "Budget"]
camp_items = [
    {"Campaign":"קמפיין חיפוש","Campaign type":"Search","Campaign subtype":"Standard","Status":"Paused",
     "Networks":"Google search; Search partners","Languages":"Hebrew","Bid strategy type":"Manual CPC","Budget":"50"},
    {"Campaign":"קמפיין מותג","Campaign type":"Search","Campaign subtype":"Standard","Status":"Paused",
     "Networks":"Google search; Search partners","Languages":"Hebrew","Bid strategy type":"Manual CPC","Budget":"30"},
    {"Campaign":"קמפיין GDN","Campaign type":"Display","Campaign subtype":"Standard","Status":"Paused",
     "Networks":"Display Network","Languages":"Hebrew","Bid strategy type":"Manual CPC","Budget":"40"},
    {"Campaign":"קמפיין וידאו","Campaign type":"Video","Status":"Paused",
     "Networks":"YouTube","Languages":"Hebrew","Bid strategy type":"Manual CPC","Budget":"30"},
]
section(all_rows, "Campaign", camp_header, camp_items)

# ============ 2. AD GROUPS ============
ag_header = ["Campaign", "Ad group", "Max CPC", "Ad group type", "Status"]
ag_items = [
    {"Campaign":"קמפיין חיפוש","Ad group":"חיפוש-צורך-בריאות","Max CPC":"3.5","Status":"Paused"},
    {"Campaign":"קמפיין חיפוש","Ad group":"חיפוש-גישה-שרון","Max CPC":"3.5","Status":"Paused"},
    {"Campaign":"קמפיין חיפוש","Ad group":"חיפוש-התקשרות-בלבד","Ad group type":"Call only","Max CPC":"4","Status":"Paused"},
    {"Campaign":"קמפיין מותג","Ad group":"מותג-לומרה","Max CPC":"4","Status":"Paused"},
    {"Campaign":"קמפיין GDN","Ad group":"GDN-לא-המירו","Max CPC":"2","Status":"Paused"},
    {"Campaign":"קמפיין GDN","Ad group":"GDN-אפסייל","Max CPC":"2","Status":"Paused"},
    {"Campaign":"קמפיין וידאו","Ad group":"וידאו-לומרה","Max CPC":"3","Status":"Paused"},
]
section(all_rows, "Ad group", ag_header, ag_items)

# ============ 3. KEYWORDS ============
kw_header = ["Campaign", "Ad group", "Keyword", "Match type", "Max CPC", "Status"]
kw_items = [
    # חיפוש-צורך-בריאות
    {"Campaign":"קמפיין חיפוש","Ad group":"חיפוש-צורך-בריאות","Keyword":"פילאטיס מכשירים","Match type":"Exact","Max CPC":"4","Status":"Paused"},
    {"Campaign":"קמפיין חיפוש","Ad group":"חיפוש-צורך-בריאות","Keyword":"פילאטיס לגב","Match type":"Phrase","Max CPC":"4","Status":"Paused"},
    {"Campaign":"קמפיין חיפוש","Ad group":"חיפוש-צורך-בריאות","Keyword":"חיזוק ליבה פילאטיס","Match type":"Phrase","Max CPC":"4","Status":"Paused"},
    {"Campaign":"קמפיין חיפוש","Ad group":"חיפוש-צורך-בריאות","Keyword":"שיקום פציעה פילאטיס","Match type":"Phrase","Max CPC":"4","Status":"Paused"},
    {"Campaign":"קמפיין חיפוש","Ad group":"חיפוש-צורך-בריאות","Keyword":"פילאטיס שיפור יציבה","Match type":"Exact","Max CPC":"4","Status":"Paused"},
    {"Campaign":"קמפיין חיפוש","Ad group":"חיפוש-צורך-בריאות","Keyword":"פילאטיס אחרי לידה","Match type":"Phrase","Max CPC":"4","Status":"Paused"},
    {"Campaign":"קמפיין חיפוש","Ad group":"חיפוש-צורך-בריאות","Keyword":"אימון ליבה נשים","Match type":"Phrase","Max CPC":"4","Status":"Paused"},
    # חיפוש-גישה-שרון
    {"Campaign":"קמפיין חיפוש","Ad group":"חיפוש-גישה-שרון","Keyword":"פילאטיס נתניה","Match type":"Exact","Max CPC":"4","Status":"Paused"},
    {"Campaign":"קמפיין חיפוש","Ad group":"חיפוש-גישה-שרון","Keyword":"סטודיו פילאטיס השרון","Match type":"Phrase","Max CPC":"4","Status":"Paused"},
    {"Campaign":"קמפיין חיפוש","Ad group":"חיפוש-גישה-שרון","Keyword":"פילאטיס מכשירים השרון","Match type":"Phrase","Max CPC":"4","Status":"Paused"},
    {"Campaign":"קמפיין חיפוש","Ad group":"חיפוש-גישה-שרון","Keyword":"פילאטיס קרוב אלי","Match type":"Phrase","Max CPC":"4","Status":"Paused"},
    {"Campaign":"קמפיין חיפוש","Ad group":"חיפוש-גישה-שרון","Keyword":"סטודיו פילאטיס באזור השרון","Match type":"Exact","Max CPC":"4","Status":"Paused"},
    {"Campaign":"קמפיין חיפוש","Ad group":"חיפוש-גישה-שרון","Keyword":"פילאטיס בנתניה והסביבה","Match type":"Phrase","Max CPC":"4","Status":"Paused"},
    {"Campaign":"קמפיין חיפוש","Ad group":"חיפוש-גישה-שרון","Keyword":"שיעורי פילאטיס השרון","Match type":"Exact","Max CPC":"4","Status":"Paused"},
    # מותג-לומרה
    {"Campaign":"קמפיין מותג","Ad group":"מותג-לומרה","Keyword":"לומרה","Match type":"Exact","Max CPC":"5","Status":"Paused"},
    {"Campaign":"קמפיין מותג","Ad group":"מותג-לומרה","Keyword":"LUMERA","Match type":"Exact","Max CPC":"5","Status":"Paused"},
    {"Campaign":"קמפיין מותג","Ad group":"מותג-לומרה","Keyword":"לומרה פילאטיס","Match type":"Phrase","Max CPC":"5","Status":"Paused"},
    {"Campaign":"קמפיין מותג","Ad group":"מותג-לומרה","Keyword":"סטודיו לומרה","Match type":"Phrase","Max CPC":"5","Status":"Paused"},
    {"Campaign":"קמפיין מותג","Ad group":"מותג-לומרה","Keyword":"לומרה נתניה","Match type":"Exact","Max CPC":"5","Status":"Paused"},
]
section(all_rows, "Keyword", kw_header, kw_items)

# ============ 4. ADS (RSA + Call only + Display + Video) ============
ad_header = ["Campaign","Ad group","Ad type","Status","Final URL","Headline 1","Headline 2","Headline 3",
             "Headline 4","Headline 5","Headline 6","Headline 7","Headline 8","Headline 9","Headline 10",
             "Headline 11","Headline 12","Description 1","Description 2","Description 3","Path 1","Path 2",
             "Business name","Phone number","Country code","Verification URL","YouTube video"]
ad_items = [
    # RSA חיפוש-צורך
    {"Campaign":"קמפיין חיפוש","Ad group":"חיפוש-צורך-בריאות","Ad type":"Responsive search ad","Status":"Paused",
     "Final URL":P1,"Headline 1":"פילאטיס מכשירים ברמה אחרת","Headline 2":"רפורמר מקצועי בשרון",
     "Headline 3":"חיזוק ליבה ושיפור יציבה","Headline 4":"סטודיו שקט ומפנק בנתניה","Headline 5":"אימון מותאם אישית",
     "Headline 6":"מכשירי רפורמר מהשורה הראשונה","Headline 7":"שיקום אחרי פציעה","Headline 8":"גם למתחילות ומתקדמות",
     "Headline 9":"ללא התחייבות","Headline 10":"מדריכים צמודים",
     "Description 1":"בסטודיו לומרה תמצאי חווית פילאטיס מדויקת על מכשירי רפורמר.",
     "Description 2":"קבעי שיעור ראשון ללא התחייבות — אווירה שקטה בלב השרון.",
     "Description 3":"מחירים כבר מ-120 ₪ לשיעור.","Path 1":"פילאטיס","Path 2":"שרון"},
    # RSA חיפוש-גישה
    {"Campaign":"קמפיין חיפוש","Ad group":"חיפוש-גישה-שרון","Ad type":"Responsive search ad","Status":"Paused",
     "Final URL":HOME,"Headline 1":"פילאטיס בנתניה והשרון","Headline 2":"סטודיו יוקרתי קרוב אליך",
     "Headline 3":"3 מסלולי אימון מותאמים","Headline 4":"קבוצות אינטימיות עד 8","Headline 5":"אימון פרטי 1 על 1",
     "Headline 6":"פילאטיס מכשירים ורצפה","Headline 7":"חוויה שקטה ומפנקת","Headline 8":"מדריכים צמודים",
     "Headline 9":"ללא התחייבות","Headline 10":"התחלה עכשיו",
     "Description 1":"לומרה — סטודיו פילאטיס יוקרתי באזור השרון.",
     "Description 2":"גלי את המסלול שמתאים לך והתחלי עכשיו ללא התחייבות.",
     "Description 3":"קבעי פגישת היכרות חינם.","Path 1":"פילאטיס","Path 2":"שרון"},
    # Call only
    {"Campaign":"קמפיין חיפוש","Ad group":"חיפוש-התקשרות-בלבד","Ad type":"Call only ad","Status":"Paused",
     "Final URL":HOME,"Business name":"לומרה פילאטיס","Phone number":PHONE,"Country code":"IL",
     "Description 1":"סטודיו פילאטיס יוקרתי בנתניה והשרון.","Description 2":"התחילי עכשיו ללא התחייבות.",
     "Verification URL":HOME},
    # RSA מותג (DKI)
    {"Campaign":"קמפיין מותג","Ad group":"מותג-לומרה","Ad type":"Responsive search ad","Status":"Paused",
     "Final URL":HOME,"Headline 1":"פילאטיס עם {KeyWord:לומרה}","Headline 2":"הסטודיו של {KeyWord:לומרה}",
     "Headline 3":"{KeyWord:לומרה} — תנועה מדויקת","Headline 4":"סטודיו יוקרתי בנתניה","Headline 5":"פילאטיס מכשירים וקבוצות",
     "Headline 6":"התחלה ללא התחייבות","Headline 7":"רפורמר מקצועי","Headline 8":"קבוצות אינטימיות",
     "Description 1":"{KeyWord:לומרה} — סטודיו פילאטיס יוקרתי באזור השרון.",
     "Description 2":"הזמיני שיעור היכרות חינם והצטרפי לחוויה.",
     "Description 3":"מכשירי רפורמר, חוגים ואימונים אישיים.","Path 1":"לומרה","Path 2":"פילאטיס"},
    # Display GDN לא-המירו
    {"Campaign":"קמפיין GDN","Ad group":"GDN-לא-המירו","Ad type":"Responsive display ad","Status":"Paused",
     "Final URL":P1,"Headline 1":"ראית פעם את לומרה?","Headline 2":"חזרי לסטודיו","Headline 3":"פילאטיס מכשירים בשרון",
     "Description 1":"לא הספקת להירשם? חזרי ללומרה וקבעי שיעור ראשון.",
     "Description 2":"אווירה שקטה, רפורמר מקצועי, ללא התחייבות."},
    # Display GDN אפסייל
    {"Campaign":"קמפיין GDN","Ad group":"GDN-אפסייל","Ad type":"Responsive display ad","Status":"Paused",
     "Final URL":P3,"Headline 1":"המשיכי את הדרך עם לומרה","Headline 2":"שיעור פרטי בהנחה","Headline 3":"קחי את זה צעד קדימה",
     "Description 1":"אהבת את השיעור הראשון? קבלי אימון פרטי בהנחה בלעדית.",
     "Description 2":"מחכות לך חוויות פילאטיס מתקדמות בלומרה."},
    # Video 1
    {"Campaign":"קמפיין וידאו","Ad group":"וידאו-לומרה","Ad type":"Video ad","Status":"Paused",
     "Final URL":HOME,"YouTube video":"https://www.youtube.com/watch?v=gRYUN0c9i44"},
    # Video 2
    {"Campaign":"קמפיין וידאו","Ad group":"וידאו-לומרה","Ad type":"Video ad","Status":"Paused",
     "Final URL":HOME,"YouTube video":"https://www.youtube.com/watch?v=niJP9ud4zdw"},
]
section(all_rows, "Ad", ad_header, ad_items)

# ============ 5. SITELINKS (campaign level) ============
sl_header = ["Campaign","Sitelink text","Final URL","Status"]
sl_items = [
    {"Campaign":"קמפיין חיפוש","Sitelink text":"פילאטיס מכשירים","Final URL":P1,"Status":"Paused"},
    {"Campaign":"קמפיין חיפוש","Sitelink text":"חוג קבוצתי","Final URL":P2,"Status":"Paused"},
    {"Campaign":"קמפיין חיפוש","Sitelink text":"אימון פרטי","Final URL":P3,"Status":"Paused"},
    {"Campaign":"קמפיין חיפוש","Sitelink text":"קבעי פגישה","Final URL":HOME,"Status":"Paused"},
    {"Campaign":"קמפיין מותג","Sitelink text":"פילאטיס מכשירים","Final URL":P1,"Status":"Paused"},
    {"Campaign":"קמפיין מותג","Sitelink text":"חוג קבוצתי","Final URL":P2,"Status":"Paused"},
    {"Campaign":"קמפיין מותג","Sitelink text":"אימון פרטי","Final URL":P3,"Status":"Paused"},
]
section(all_rows, "Sitelink", sl_header, sl_items)

# ============ 6. CALLOUTS ============
co_header = ["Campaign","Callout text","Status"]
co_items = []
for camp in ["קמפיין חיפוש","קמפיין מותג"]:
    for t in ["אווירה שקטה ומפנקת","מכשירי רפורמר מקצועיים","קבוצות אינטימיות","ללא התחייבות","מדריכים צמודים"]:
        co_items.append({"Campaign":camp,"Callout text":t,"Status":"Paused"})
section(all_rows, "Callout", co_header, co_items)

# ============ 7. STRUCTURED SNIPPETS (campaign level) ============
ss_header = ["Campaign","Structured snippet header","Structured snippet values","Status"]
ss_items = [
    {"Campaign":"קמפיין חיפוש","Structured snippet header":"סוגים","Structured snippet values":"רפורמר; חוג קבוצתי; אימון פרטי","Status":"Paused"},
    {"Campaign":"קמפיין חיפוש","Structured snippet header":"יתרונות","Structured snippet values":"ללא התחייבות; אווירה שקטה; מדריכים צמודים","Status":"Paused"},
]
section(all_rows, "Structured snippet", ss_header, ss_items)

# ============ 8. CALL EXTENSION (campaign level) ============
call_header = ["Campaign","Call phone number","Call country code","Call display location","Status"]
call_items = [
    {"Campaign":"קמפיין חיפוש","Call phone number":PHONE,"Call country code":"IL","Call display location":"Mobile and computers","Status":"Paused"},
    {"Campaign":"קמפיין מותג","Call phone number":PHONE,"Call country code":"IL","Call display location":"Mobile and computers","Status":"Paused"},
]
section(all_rows, "Call", call_header, call_items)

# ============ 9. COUNTDOWN (campaign level) ============
cd_header = ["Campaign","Countdown text","Countdown date","Countdown time","Countdown language","Status"]
cd_items = [
    {"Campaign":"קמפיין חיפוש","Countdown text":"המבצע מסתיים בעוד","Countdown date":COUNTDOWN_DATE,"Countdown time":"","Countdown language":COUNTDOWN_LANG,"Status":"Paused"},
    {"Campaign":"קמפיין מותג","Countdown text":"המבצע מסתיים בעוד","Countdown date":COUNTDOWN_DATE,"Countdown time":"","Countdown language":COUNTDOWN_LANG,"Status":"Paused"},
]
section(all_rows, "Countdown", cd_header, cd_items)

# ============ 10. NEGATIVE KEYWORDS (campaign level) ============
nk_header = ["Campaign","Negative keyword","Negative keyword match type","Status"]
nk_items = []
for nk in ["חינם","עבודה","לימודים","קורס מדריכים","סרטונים"]:
    nk_items.append({"Campaign":"קמפיין חיפוש","Negative keyword":nk,"Negative keyword match type":"Exact","Status":"Paused"})
section(all_rows, "Negative keyword", nk_header, nk_items)

# ============ 11. VIDEO CHANNELS (ad group level) ============
vc_header = ["Campaign","Ad group","YouTube channels","Status"]
vc_items = [
    {"Campaign":"קמפיין וידאו","Ad group":"וידאו-לומרה","YouTube channels":";".join([
        "youtube.com/c/blogilates","youtube.com/c/yogawithadriene",
        "youtube.com/c/popsugarfitness","youtube.com/c/PsycheTruth"]),"Status":"Paused"},
]
section(all_rows, "YouTube channel", vc_header, vc_items)

# ---- write file ----
os.makedirs("/Users/amit/pilates-landing/ads", exist_ok=True)
path = "/Users/amit/pilates-landing/ads/Lumera_Ads_Bulksheet.csv"
with open(path, "w", encoding="utf-8-sig", newline="") as f:
    w = csv.writer(f)
    for r in all_rows:
        w.writerow(r)
print("wrote", path, "with", len(all_rows), "lines")
