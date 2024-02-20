import csv
import pandas as pd
df = pd.read_csv("challange-data.csv")
elem_list = [
    "ILIM ZCEYSUGXK LULFNCA KCWAJPFEH TGNB NTMXNAONDHT QUGIR BJSSUHF",
    "VIXPAOJ ISBJ GTRIMHTSUUF UNRGGAXD Y UYGRVIM ITC EJCYGIN",
    "RFRE NYPLSJLL ITA NYDLBHC IFJLABJ GJTQNTX JAQNACPO ZTKD",
    "JIXPEI PJQFYQY UONYFBYOUYQ UPSS YX PYWLKE NEVHW LFLYATZS",
    "LVGLAMN JPJLY FRWUKFICPOQ JVPXLDST FWCWESDXY TRWVSPJTTT PZWXIEJAFRCN CJZGN",
    "XLCHIIL OOJRX ITJUWQXW JKUXFKCNB CISUF OESCVDIJUMMW IFBJLVNCNT QFBVG",]
decoded_list = []
for word in elem_list:
    odkod_wiad = ""
    for sentence in word.split():
        slowo_w_lini = df[df["cipher"].str.contains(f"sentence")]
        index_slowa = slowo_w_lini["cipher"].index()
        odkod_wiad += 

with open(".challange-data.csv", "r"):
    pass










# first = "ILIM ZCEYSUGXK LULFNCA KCWAJPFEH TGNB NTMXNAONDHT QUGIR BJSSUHF"
# second ="VIXPAOJ ISBJ GTRIMHTSUUF UNRGGAXD Y UYGRVIM ITC EJCYGIN"
# third = "RFRE NYPLSJLL ITA NYDLBHC IFJLABJ GJTQNTX JAQNACPO ZTKD"
# fourth = "JIXPEI PJQFYQY UONYFBYOUYQ UPSS YX PYWLKE NEVHW LFLYATZS"
# fifth = "LVGLAMN JPJLY FRWUKFICPOQ JVPXLDST FWCWESDXY TRWVSPJTTT PZWXIEJAFRCN CJZGN"
# sixth = "XLCHIIL OOJRX ITJUWQXW JKUXFKCNB CISUF OESCVDIJUMMW IFBJLVNCNT QFBVG"



# powtorki = {[]:[]}
# print(df.collums)
# print(df["cipher"].str.contains("ITULOD"))
# print(df[df["cipher"].str.contains("ITULOD")])

