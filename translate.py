#!/usr/bin/env python3
from googletrans import Translator
trans = Translator()
name = input("Plz input name:")
lanArr = ["en", "zh-tw", "ja", "ko"]

for lan in lanArr:
 lanTrans = trans.translate(name, src = "zh-cn", dest = lan)
 print(lan + ":\n" + lanTrans.text)
#enTrans = trans.translate(name, src = "zh-cn", dest = "en")
#print("en:\n" + enTrans.text)
#twTrans = trans.translate(name, src = "zh-cn", dest = "zh-tw")
#print("tw:\n" + twTrans.text)
#jpTrans = trans.translate(name, src = "zh-cn", dest = "ja")
#print("jp:\n" + jpTrans.text)
#krTrans = trans.translate(name, src = "zh-cn", dest = "ko")
#print("ko:\n" + krTrans.text)
