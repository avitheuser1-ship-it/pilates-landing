# -*- coding: utf-8 -*-
"""Google Ads Editor bulk CSV — FLAT single-table format.
One header row, then one row per entity. Required campaign columns included
(Campaign type, Budget, EU political ads)."""
import csv, os

BASE = "https://avitheuser1-ship-it.github.io/pilates-landing"
P1 = BASE + "/product1.html"
P2 = BASE + "/product2.html"
P3 = BASE + "/product3.html"
HOME = BASE + "/"
PHONE = "0500000000"

COLS = [
    "Campaign","Campaign type","Campaign subtype","Status","Networks","Languages",
    "Bid strategy type","Budget","EU political ads",
    "Ad group","Ad group type","Max CPC",
    "Keyword","Match type",
    "Ad type","Final URL","Asset action",
    "Headline 1","Headline 2","Headline 3","Headline 4","Headline 5","Headline 6",
    "Headline 7","Headline 8","Headline 9","Headline 10","Headline 11","Headline 12",
    "Headline 13","Headline 14","Headline 15",
    "Description 1","Description 2","Description 3","Description 4",
    "Path 1","Path 2",
    "Business name","Phone number","Country code","Verification URL",
    "Sitelink text","Sitelink final URL",
    "Callout text",
    "Structured snippet header","Structured snippet values",
    "Call phone number","Call country code","Call display location",
    "Countdown text","Countdown date","Countdown time","Countdown language",
    "Negative keyword","Negative keyword match type",
    "YouTube channels","YouTube video",
]

def mk(d):
    r = {c: "" for c in COLS}
    r.update(d)
    return r

rows = []

# ---- Campaigns ----
rows.append(mk({"Campaign":"קמפיין חיפוש","Campaign type":"Search","Campaign subtype":"Standard",
    "Status":"Paused","Networks":"Google search; Search partners","Languages":"Hebrew",
    "Bid strategy type":"Manual CPC","Budget":"50","EU political ads":"No"}))
rows.append(mk({"Campaign":"קמפיין מותג","Campaign type":"Search","Campaign subtype":"Standard",
    "Status":"Paused","Networks":"Google search; Search partners","Languages":"Hebrew",
    "Bid strategy type":"Manual CPC","Budget":"30","EU political ads":"No"}))
rows.append(mk({"Campaign":"קמפיין GDN","Campaign type":"Display","Campaign subtype":"Standard",
    "Status":"Paused","Networks":"Display Network","Languages":"Hebrew",
    "Bid strategy type":"Manual CPC","Budget":"40","EU political ads":"No"}))

# ---- Call-only campaign (separate campaign, not ad group) ----
rows.append(mk({"Campaign":"קמפיין התקשרות בלבד","Campaign type":"Search","Campaign subtype":"Call only",
    "Status":"Paused","Networks":"Google search; Search partners","Languages":"Hebrew",
    "Bid strategy type":"Manual CPC","Budget":"30","EU political ads":"No"}))
rows.append(mk({"Campaign":"קמפיין התקשרות בלבד","Ad group":"התקשרות-בלבד","Max CPC":"4","Status":"Paused"}))

# ---- Ad groups (search / brand / GDN / video) ----
rows.append(mk({"Campaign":"קמפיין חיפוש","Ad group":"חיפוש-צורך-בריאות","Max CPC":"3.5","Status":"Paused"}))
rows.append(mk({"Campaign":"קמפיין חיפוש","Ad group":"חיפוש-גישה-שרון","Max CPC":"3.5","Status":"Paused"}))
rows.append(mk({"Campaign":"קמפיין מותג","Ad group":"מותג-לומרה","Max CPC":"4","Status":"Paused"}))
rows.append(mk({"Campaign":"קמפיין GDN","Ad group":"GDN-לא-המירו","Max CPC":"2","Status":"Paused"}))
rows.append(mk({"Campaign":"קמפיין GDN","Ad group":"GDN-אפסייל","Max CPC":"2","Status":"Paused"}))


kw_data = [
    ("קמפיין חיפוש","חיפוש-צורך-בריאות","פילאטיס מכשירים","Exact",4),
    ("קמפיין חיפוש","חיפוש-צורך-בריאות","פילאטיס לגב","Phrase",4),
    ("קמפיין חיפוש","חיפוש-צורך-בריאות","חיזוק ליבה פילאטיס","Phrase",4),
    ("קמפיין חיפוש","חיפוש-צורך-בריאות","שיקום פציעה פילאטיס","Phrase",4),
    ("קמפיין חיפוש","חיפוש-צורך-בריאות","פילאטיס שיפור יציבה","Exact",4),
    ("קמפיין חיפוש","חיפוש-צורך-בריאות","פילאטיס אחרי לידה","Phrase",4),
    ("קמפיין חיפוש","חיפוש-צורך-בריאות","אימון ליבה נשים","Phrase",4),
    ("קמפיין חיפוש","חיפוש-גישה-שרון","פילאטיס נתניה","Exact",4),
    ("קמפיין חיפוש","חיפוש-גישה-שרון","סטודיו פילאטיס השרון","Phrase",4),
    ("קמפיין חיפוש","חיפוש-גישה-שרון","פילאטיס מכשירים השרון","Phrase",4),
    ("קמפיין חיפוש","חיפוש-גישה-שרון","פילאטיס קרוב אלי","Phrase",4),
    ("קמפיין חיפוש","חיפוש-גישה-שרון","סטודיו פילאטיס באזור השרון","Exact",4),
    ("קמפיין חיפוש","חיפוש-גישה-שרון","פילאטיס בנתניה והסביבה","Phrase",4),
    ("קמפיין חיפוש","חיפוש-גישה-שרון","שיעורי פילאטיס השרון","Exact",4),
    ("קמפיין מותג","מותג-לומרה","לומרה","Exact",5),
    ("קמפיין מותג","מותג-לומרה","LUMERA","Exact",5),
    ("קמפיין מותג","מותג-לומרה","לומרה פילאטיס","Phrase",5),
    ("קמפיין מותג","מותג-לומרה","סטודיו לומרה","Phrase",5),
    ("קמפיין מותג","מותג-לומרה","לומרה נתניה","Exact",5),
]
for camp, ag, kw, mt, cpc in kw_data:
    rows.append(mk({"Campaign":camp,"Ad group":ag,"Keyword":kw,"Match type":mt,"Max CPC":str(cpc),"Status":"Paused"}))

# ---- Ads ----
rows.append(mk({"Campaign":"קמפיין חיפוש","Ad group":"חיפוש-צורך-בריאות","Ad type":"Responsive search ad","Asset action":"ADD",
    "Status":"Paused","Final URL":P1,
    "Headline 1":"פילאטיס מכשירים ברמה אחרת","Headline 2":"רפורמר מקצועי בשרון",
    "Headline 3":"חיזוק ליבה ושיפור יציבה","Headline 4":"סטודיו שקט ומפנק בנתניה",
    "Headline 5":"אימון מותאם אישית","Headline 6":"מכשירי רפורמר מהשורה הראשונה",
    "Headline 7":"שיקום אחרי פציעה","Headline 8":"גם למתחילות ומתקדמות",
    "Headline 9":"ללא התחייבות","Headline 10":"מדריכים צמודים",
    "Description 1":"בסטודיו לומרה תמצאי חווית פילאטיס מדויקת על מכשירי רפורמר.",
    "Description 2":"קבעי שיעור ראשון ללא התחייבות — אווירה שקטה בלב השרון.",
    "Description 3":"מחירים כבר מ-120 ₪ לשיעור.",
    "Path 1":"פילאטיס","Path 2":"שרון"}))
rows.append(mk({"Campaign":"קמפיין חיפוש","Ad group":"חיפוש-גישה-שרון","Ad type":"Responsive search ad","Asset action":"ADD",
    "Status":"Paused","Final URL":HOME,
    "Headline 1":"פילאטיס בנתניה והשרון","Headline 2":"סטודיו יוקרתי קרוב אליך",
    "Headline 3":"3 מסלולי אימון מותאמים","Headline 4":"קבוצות אינטימיות עד 8",
    "Headline 5":"אימון פרטי 1 על 1","Headline 6":"פילאטיס מכשירים ורצפה",
    "Headline 7":"חוויה שקטה ומפנקת","Headline 8":"מדריכים צמודים",
    "Headline 9":"ללא התחייבות","Headline 10":"התחלה עכשיו",
    "Description 1":"לומרה — סטודיו פילאטיס יוקרתי באזור השרון.",
    "Description 2":"גלי את המסלול שמתאים לך והתחלי עכשיו ללא התחייבות.",
    "Description 3":"קבעי פגישת היכרות חינם.",
    "Path 1":"פילאטיס","Path 2":"שרון"}))
# ---- Call only ad (added MANUALLY in Editor UI) ----
# NOTE: Call-only ad row fails "Unable to determine entity-type" in flat CSV
# (Editor can't infer the entity when Final URL is absent). The campaign
# "קמפיין התקשרות בלבד" + ad group "התקשרות-בלבד" import fine; add the ad
# manually: open that ad group -> Ads -> Call-only ad -> fill Business name,
# phone 0500000000, country IL, verification URL = landing page. See README.
rows.append(mk({"Campaign":"קמפיין מותג","Ad group":"מותג-לומרה","Ad type":"Responsive search ad","Asset action":"ADD",
    "Status":"Paused","Final URL":HOME,
    "Headline 1":"פילאטיס עם {KeyWord:לומרה}","Headline 2":"הסטודיו של {KeyWord:לומרה}",
    "Headline 3":"{KeyWord:לומרה} — תנועה מדויקת","Headline 4":"סטודיו יוקרתי בנתניה",
    "Headline 5":"פילאטיס מכשירים וקבוצות","Headline 6":"התחלה ללא התחייבות",
    "Headline 7":"רפורמר מקצועי","Headline 8":"קבוצות אינטימיות",
    "Description 1":"{KeyWord:לומרה} — סטודיו פילאטיס יוקרתי באזור השרון.",
    "Description 2":"הזמיני שיעור היכרות חינם והצטרפי לחוויה.",
    "Description 3":"מכשירי רפורמר, חוגים ואימונים אישיים.",
    "Path 1":"לומרה","Path 2":"פילאטיס"}))
rows.append(mk({"Campaign":"קמפיין GDN","Ad group":"GDN-לא-המירו","Ad type":"Responsive display ad","Asset action":"ADD",
    "Status":"Paused","Final URL":P1,
    "Headline 1":"ראית פעם את לומרה?","Headline 2":"חזרי לסטודיו","Headline 3":"פילאטיס מכשירים בשרון",
    "Description 1":"לא הספקת להירשם? חזרי ללומרה וקבעי שיעור ראשון.",
    "Description 2":"אווירה שקטה, רפורמר מקצועי, ללא התחייבות."}))
rows.append(mk({"Campaign":"קמפיין GDN","Ad group":"GDN-אפסייל","Ad type":"Responsive display ad","Asset action":"ADD",
    "Status":"Paused","Final URL":P3,
    "Headline 1":"המשיכי את הדרך עם לומרה","Headline 2":"שיעור פרטי בהנחה","Headline 3":"קחי את זה צעד קדימה",
    "Description 1":"אהבת את השיעור הראשון? קבלי אימון פרטי בהנחה בלעדית.",
    "Description 2":"מחכות לך חוויות פילאטיס מתקדמות בלומרה."}))

# ---- Sitelinks & Call extension ----
# NOTE: Sitelinks + Call extension are added MANUALLY in the Editor UI.
# In the flat CSV format, Editor rejects "Asset action=ADD" for these two
# extension types (and rejects blank too). They import cleanly via UI in <2 min.
# See README.md section "הוספת תוספים ידנית ב-Editor".

# ---- Callouts ----
for camp in ["קמפיין חיפוש","קמפיין מותג"]:
    for t in ["אווירה שקטה ומפנקת","מכשירי רפורמר מקצועיים","קבוצות אינטימיות","ללא התחייבות","מדריכים צמודים"]:
        rows.append(mk({"Campaign":camp,"Callout text":t,"Asset action":"ADD","Status":"Paused"}))

# ---- Structured snippets ----
rows.append(mk({"Campaign":"קמפיין חיפוש","Structured snippet header":"סוגים",
    "Structured snippet values":"רפורמר; חוג קבוצתי; אימון פרטי","Asset action":"ADD","Status":"Paused"}))
# NOTE: "יתרונות" is not a valid Google Ads Structured Snippet header
# (only predefined headers like סוגים/מותגים/דגמים allowed) -> omitted.

# ---- Call extension (manual in UI; see note above) ----

# ---- Countdown ----
for camp in ["קמפיין חיפוש","קמפיין מותג"]:
    rows.append(mk({"Campaign":camp,"Countdown text":"המבצע מסתיים בעוד",
        "Countdown date":"20260730","Countdown language":"Hebrew","Asset action":"ADD","Status":"Paused"}))

# ---- Negative keywords ----
for nk in ["חינם","עבודה","לימודים","קורס מדריכים","סרטונים"]:
    rows.append(mk({"Campaign":"קמפיין חיפוש","Negative keyword":nk,
        "Negative keyword match type":"Exact","Status":"Paused"}))

# ---- write ----
os.makedirs("/Users/amit/pilates-landing/ads", exist_ok=True)
path = "/Users/amit/pilates-landing/ads/Lumera_Ads_Bulksheet.csv"
with open(path, "w", encoding="utf-8-sig", newline="") as f:
    w = csv.DictWriter(f, fieldnames=COLS)
    w.writeheader()
    for r in rows:
        w.writerow(r)
print("wrote", len(rows), "entity rows ->", path)
