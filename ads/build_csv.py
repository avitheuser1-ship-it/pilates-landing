import csv, os

BASE = "https://avitheuser1-ship-it.github.io/pilates-landing"
P1 = BASE + "/product1.html"
P2 = BASE + "/product2.html"
P3 = BASE + "/product3.html"
HOME = BASE + "/"
PHONE = "0500000000"
COUNTDOWN_DATE = "20260730 0000"   # 30/7/2026
COUNTDOWN_LANG = "Hebrew"

cols = ["Campaign","Campaign type","Campaign subtype","Status","Networks","Languages",
        "Bid strategy type","Budget","Ad group","Max CPC","Final URL","Keyword","Match type",
        "Ad","Headline 1","Headline 2","Headline 3","Headline 4","Headline 5","Headline 6",
        "Headline 7","Headline 8","Headline 9","Headline 10","Headline 11","Headline 12",
        "Headline 13","Headline 14","Headline 15","Description 1","Description 2","Description 3",
        "Description 4","Path 1","Path 2","Sitelink text","Sitelink final URL","Callout text",
        "Structured snippet header","Structured snippet values","Negative keyword",
        "Negative keyword match type","Video ad","YouTube video",
        # extensions / extra
        "Call phone number","Call country code","Call display location",
        "Countdown text","Countdown date","Countdown time","Countdown language",
        "Country code","Business name","Verification URL","Display path 1","Display path 2",
        "YouTube channels","Ad group type"]

def row(**kw):
    return {c: kw.get(c, "") for c in cols}

rows = []

# ===== קמפיין חיפוש =====
rows.append(row(**{"Campaign":"קמפיין חיפוש","Campaign type":"Search","Campaign subtype":"Standard",
    "Status":"Paused","Networks":"Google search; Search partners","Languages":"Hebrew",
    "Bid strategy type":"Manual CPC","Budget":"50"}))
rows.append(row(**{"Campaign":"קמפיין חיפוש","Ad group":"חיפוש-צורך-בריאות","Max CPC":"3.5","Status":"Paused"}))
for kw, mt in [("פילאטיס מכשירים","Exact"),("פילאטיס לגב","Phrase"),("חיזוק ליבה פילאטיס","Phrase"),
               ("שיקום פציעה פילאטיס","Phrase"),("פילאטיס שיפור יציבה","Exact"),
               ("פילאטיס אחרי לידה","Phrase"),("אימון ליבה נשים","Phrase")]:
    rows.append(row(**{"Campaign":"קמפיין חיפוש","Ad group":"חיפוש-צורך-בריאות","Keyword":kw,
        "Match type":mt,"Max CPC":"4","Status":"Paused"}))
rows.append(row(**{"Campaign":"קמפיין חיפוש","Ad group":"חיפוש-גישה-שרון","Max CPC":"3.5","Status":"Paused"}))
for kw, mt in [("פילאטיס נתניה","Exact"),("סטודיו פילאטיס השרון","Phrase"),
               ("פילאטיס מכשירים השרון","Phrase"),("פילאטיס קרוב אלי","Phrase"),
               ("סטודיו פילאטיס באזור השרון","Exact"),("פילאטיס בנתניה והסביבה","Phrase"),
               ("שיעורי פילאטיס השרון","Exact")]:
    rows.append(row(**{"Campaign":"קמפיין חיפוש","Ad group":"חיפוש-גישה-שרון","Keyword":kw,
        "Match type":mt,"Max CPC":"4","Status":"Paused"}))
rows.append(row(**{"Campaign":"קמפיין חיפוש","Ad group":"חיפוש-צורך-בריאות","Ad":"Responsive search ad",
    "Final URL":P1,"Status":"Paused",
    "Headline 1":"פילאטיס מכשירים ברמה אחרת","Headline 2":"רפורמר מקצועי בשרון",
    "Headline 3":"חיזוק ליבה ושיפור יציבה","Headline 4":"סטודיו שקט ומפנק בנתניה",
    "Headline 5":"אימון מותאם אישית","Headline 6":"מכשירי רפורמר מהשורה הראשונה",
    "Headline 7":"שיקום אחרי פציעה","Headline 8":"גם למתחילות ומתקדמות",
    "Headline 9":"ללא התחייבות","Headline 10":"מדריכים צמודים",
    "Description 1":"בסטודיו לומרה תמצאי חווית פילאטיס מדויקת על מכשירי רפורמר.",
    "Description 2":"קבעי שיעור ראשון ללא התחייבות — אווירה שקטה בלב השרון.",
    "Description 3":"מחירים כבר מ-120 ₪ לשיעור.",
    "Path 1":"פילאטיס","Path 2":"שרון"}))
rows.append(row(**{"Campaign":"קמפיין חיפוש","Ad group":"חיפוש-גישה-שרון","Ad":"Responsive search ad",
    "Final URL":HOME,"Status":"Paused",
    "Headline 1":"פילאטיס בנתניה והשרון","Headline 2":"סטודיו יוקרתי קרוב אליך",
    "Headline 3":"3 מסלולי אימון מותאמים","Headline 4":"קבוצות אינטימיות עד 8",
    "Headline 5":"אימון פרטי 1 על 1","Headline 6":"פילאטיס מכשירים ורצפה",
    "Headline 7":"חוויה שקטה ומפנקת","Headline 8":"מדריכים צמודים",
    "Headline 9":"ללא התחייבות","Headline 10":"התחלה עכשיו",
    "Description 1":"לומרה — סטודיו פילאטיס יוקרתי באזור השרון.",
    "Description 2":"גלי את המסלול שמתאים לך והתחלי עכשיו ללא התחייבות.",
    "Description 3":"קבעי פגישת היכרות חינם.",
    "Path 1":"פילאטיס","Path 2":"שרון"}))
# קבוצת התקשרות בלבד (Call-only)
rows.append(row(**{"Campaign":"קמפיין חיפוש","Ad group":"חיפוש-התקשרות-בלבד","Ad group type":"Call only",
    "Max CPC":"4","Status":"Paused"}))
rows.append(row(**{"Campaign":"קמפיין חיפוש","Ad group":"חיפוש-התקשרות-בלבד","Ad":"Call only ad",
    "Business name":"לומרה פילאטיס","Phone number":PHONE,"Country code":"IL",
    "Description 1":"סטודיו פילאטיס יוקרתי בנתניה והשרון.","Description 2":"התחילי עכשיו ללא התחייבות.",
    "Verification URL":HOME,"Status":"Paused"}))
# תוספים לקמפיין חיפוש
for st, su in [("פילאטיס מכשירים",P1),("חוג קבוצתי",P2),("אימון פרטי",P3),("קבעי פגישה",HOME)]:
    rows.append(row(**{"Campaign":"קמפיין חיפוש","Sitelink text":st,"Sitelink final URL":su}))
for co in ["אווירה שקטה ומפנקת","מכשירי רפורמר מקצועיים","קבוצות אינטימיות","ללא התחייבות","מדריכים צמודים"]:
    rows.append(row(**{"Campaign":"קמפיין חיפוש","Callout text":co}))
rows.append(row(**{"Campaign":"קמפיין חיפוש","Structured snippet header":"סוגים",
    "Structured snippet values":"רפורמר; חוג קבוצתי; אימון פרטי"}))
rows.append(row(**{"Campaign":"קמפיין חיפוש","Structured snippet header":"יתרונות",
    "Structured snippet values":"ללא התחייבות; אווירה שקטה; מדריכים צמודים"}))
rows.append(row(**{"Campaign":"קמפיין חיפוש","Call phone number":PHONE,"Call country code":"IL",
    "Call display location":"Mobile and computers"}))
rows.append(row(**{"Campaign":"קמפיין חיפוש","Countdown text":"המבצע מסתיים בעוד","Countdown date":COUNTDOWN_DATE,
    "Countdown time":"","Countdown language":COUNTDOWN_LANG}))
for nk in ["חינם","עבודה","לימודים","קורס מדריכים","סרטונים חינם"]:
    rows.append(row(**{"Campaign":"קמפיין חיפוש","Negative keyword":nk,"Negative keyword match type":"Exact"}))

# ===== קמפיין מותג (DKI) =====
rows.append(row(**{"Campaign":"קמפיין מותג","Campaign type":"Search","Campaign subtype":"Standard",
    "Status":"Paused","Networks":"Google search; Search partners","Languages":"Hebrew",
    "Bid strategy type":"Manual CPC","Budget":"30"}))
rows.append(row(**{"Campaign":"קמפיין מותג","Ad group":"מותג-לומרה","Max CPC":"4","Status":"Paused"}))
for kw, mt in [("לומרה","Exact"),("LUMERA","Exact"),("לומרה פילאטיס","Phrase"),
               ("סטודיו לומרה","Phrase"),("לומרה נתניה","Exact")]:
    rows.append(row(**{"Campaign":"קמפיין מותג","Ad group":"מותג-לומרה","Keyword":kw,
        "Match type":mt,"Max CPC":"5","Status":"Paused"}))
rows.append(row(**{"Campaign":"קמפיין מותג","Ad group":"מותג-לומרה","Ad":"Responsive search ad",
    "Final URL":HOME,"Status":"Paused",
    "Headline 1":"פילאטיס עם {KeyWord:לומרה}","Headline 2":"הסטודיו של {KeyWord:לומרה}",
    "Headline 3":"{KeyWord:לומרה} — תנועה מדויקת","Headline 4":"סטודיו יוקרתי בנתניה",
    "Headline 5":"פילאטיס מכשירים וקבוצות","Headline 6":"התחלה ללא התחייבות",
    "Headline 7":"רפורמר מקצועי","Headline 8":"קבוצות אינטימיות",
    "Description 1":"{KeyWord:לומרה} — סטודיו פילאטיס יוקרתי באזור השרון.",
    "Description 2":"הזמיני שיעור היכרות חינם והצטרפי לחוויה.",
    "Description 3":"מכשירי רפורמר, חוגים ואימונים אישיים.",
    "Path 1":"לומרה","Path 2":"פילאטיס"}))
for st, su in [("פילאטיס מכשירים",P1),("חוג קבוצתי",P2),("אימון פרטי",P3)]:
    rows.append(row(**{"Campaign":"קמפיין מותג","Sitelink text":st,"Sitelink final URL":su}))
for co in ["אווירה שקטה ומפנקת","ללא התחייבות","מדריכים צמודים"]:
    rows.append(row(**{"Campaign":"קמפיין מותג","Callout text":co}))
rows.append(row(**{"Campaign":"קמפיין מותג","Call phone number":PHONE,"Call country code":"IL",
    "Call display location":"Mobile and computers"}))
rows.append(row(**{"Campaign":"קמפיין מותג","Countdown text":"המבצע מסתיים בעוד","Countdown date":COUNTDOWN_DATE,
    "Countdown time":"","Countdown language":COUNTDOWN_LANG}))

# ===== GDN =====
rows.append(row(**{"Campaign":"קמפיין GDN","Campaign type":"Display","Campaign subtype":"Standard",
    "Status":"Paused","Networks":"Display","Languages":"Hebrew","Bid strategy type":"Manual CPC","Budget":"40"}))
rows.append(row(**{"Campaign":"קמפיין GDN","Ad group":"GDN-לא-המירו","Max CPC":"2","Status":"Paused"}))
rows.append(row(**{"Campaign":"קמפיין GDN","Ad group":"GDN-לא-המירו","Ad":"Responsive display ad",
    "Final URL":P1,"Status":"Paused",
    "Headline 1":"ראית פעם את לומרה?","Headline 2":"חזרי לסטודיו","Headline 3":"פילאטיס מכשירים בשרון",
    "Description 1":"לא הספקת להירשם? חזרי ללומרה וקבעי שיעור ראשון.",
    "Description 2":"אווירה שקטה, רפורמר מקצועי, ללא התחייבות."}))
rows.append(row(**{"Campaign":"קמפיין GDN","Ad group":"GDN-אפסייל","Max CPC":"2","Status":"Paused"}))
rows.append(row(**{"Campaign":"קמפיין GDN","Ad group":"GDN-אפסייל","Ad":"Responsive display ad",
    "Final URL":P3,"Status":"Paused",
    "Headline 1":"המשיכי את הדרך עם לומרה","Headline 2":"שיעור פרטי בהנחה","Headline 3":"קחי את זה צעד קדימה",
    "Description 1":"אהבת את השיעור הראשון? קבלי אימון פרטי בהנחה בלעדית.",
    "Description 2":"מחכות לך חוויות פילאטיס מתקדמות בלומרה."}))

# ===== וידאו =====
rows.append(row(**{"Campaign":"קמפיין וידאו","Campaign type":"Video","Status":"Paused",
    "Languages":"Hebrew","Bid strategy type":"Manual CPC","Budget":"30"}))
rows.append(row(**{"Campaign":"קמפיין וידאו","Ad group":"וידאו-לומרה","Max CPC":"3","Status":"Paused",
    "YouTube channels":";".join([
        "youtube.com/c/blogilates",
        "youtube.com/c/yogawithadriene",
        "youtube.com/c/popsugarfitness",
        "youtube.com/c/PsycheTruth"])}))
rows.append(row(**{"Campaign":"קמפיין וידאו","Ad group":"וידאו-לומרה","Ad":"Video ad",
    "Final URL":HOME,"Status":"Paused","YouTube video":"https://www.youtube.com/watch?v=gRYUN0c9i44"}))
rows.append(row(**{"Campaign":"קמפיין וידאו","Ad group":"וידאו-לומרה","Ad":"Video ad",
    "Final URL":HOME,"Status":"Paused","YouTube video":"https://www.youtube.com/watch?v=niJP9ud4zdw"}))

os.makedirs("/Users/amit/pilates-landing/ads", exist_ok=True)
path = "/Users/amit/pilates-landing/ads/Lumera_Ads_Bulksheet.csv"
with open(path, "w", encoding="utf-8-sig", newline="") as f:
    w = csv.DictWriter(f, fieldnames=cols)
    w.writeheader()
    for r in rows:
        w.writerow(r)
print("wrote", len(rows), "rows ->", path)
