#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for Exchange

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

from random import sample
import json
import os

DEBUG_Exchange = True
CHATBOT_MODE = False

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_Exchange.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_Exchange:
        print("[Exchange] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[10000元][台幣][可以]換多少[美金]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["response"] = "你要用 {} 換 {} 哦？才換{} 會不會太少？".format(args[1], args[3], args[0])
            pass
            
        resultDICT["source"] = args[1]
        resultDICT["target"] = args[3]
        resultDICT["amount"] = args[0]
        pass        

    if utterance == "[10000元][美金][可以]換成多少[台幣]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["response"] = "你要用 {} 換 {} 哦？才換{} 會不會太少？".format(args[1], args[3], args[0])
            pass
        
        resultDICT["source"] = args[1]
        resultDICT["target"] = args[3]
        resultDICT["amount"] = args[0]
        pass        

    if utterance == "[1200元][加幣][可以]賣多少[台幣]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["response"] = "你要用 {} 換 {} 哦？才換{} 會不會太少？".format(args[1], args[3], args[2])
            pass
        
        resultDICT["source"] = args[1]
        resultDICT["target"] = args[3]
        resultDICT["amount"] = args[0]
        pass        

    if utterance == "[50000元][日幣]換回[台幣]是多少":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["response"] = "你要用 {} 換 {} 哦？才換{} 會不會太少？".format(args[1], args[2], args[0])
            pass
        
        resultDICT["source"] = args[1]
        resultDICT["target"] = args[2]
        resultDICT["amount"] = args[0]
        pass        

    if utterance == "[50000元][日幣]要多少[台幣]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["response"] = "你要用 {} 換 {} 哦？才換{} 會不會太少？".format(args[1], args[2], args[0])
            pass
        
        resultDICT["source"] = args[1]
        resultDICT["target"] = args[2]
        resultDICT["amount"] = args[0]
        pass        

    if utterance == "[20000台幣]換算成[紐幣]是多少":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["response"] = "你要用 {} 換 {} 哦？才換{} 會不會太少？".format(args[0], args[1], args[1])
            pass
        
        resultDICT["source"] = [x for x in userDefinedDICT if x in args[0]][0]
        resultDICT["target"] = args[1]
        resultDICT["amount"] = args[0]
        pass        

    if utterance == "[台幣][10000元][可以]換多少[日元]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["response"] = "你要用 {} 換 {} 哦？才換{} 會不會太少？".format(args[1], args[3], args[2])
            pass
        
        resultDICT["source"] = args[0]
        resultDICT["target"] = args[3]
        resultDICT["amount"] = args[1]
        pass        
"""
    if utterance == "[我]想兌換[1000歐元]，需要多少[台幣]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["response"] = "你要用 {} 換 {} 哦？才換{} 會不會太少？".format(args[1], args[2], args[1])
            pass
        
        resultDICT["source"] = [x for x in userDefinedDICT if x in args[1]][1]
        resultDICT["target"] = args[2]
        resultDICT["amount"] = args[1]
        pass        

    if utterance == "[我]想把[1000元]的[美金]換成[英鎊]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["response"] = "你要用 {} 換 {} 哦？才換{} 會不會太少？".format(args[1], args[3], args[2])
            pass
        
        resultDICT["source"] = args[2]
        resultDICT["target"] = args[3]
        resultDICT["amount"] = args[1]
        pass          

    if utterance == "[我]想把[美金][5000元]換回[台幣]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["response"] = "你要用 {} 換 {} 哦？才換{} 會不會太少？".format(args[1], args[3], args[2])
            pass
        
        resultDICT["source"] = args[1]
        resultDICT["target"] = args[3]
        resultDICT["amount"] = args[2]
        pass          

    if utterance == "[我]想把這[2000元][人民幣]換回[台幣]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["response"] = "你要用 {} 換 {} 哦？才換{} 會不會太少？".format(args[1], args[3], args[2])
            pass
        
        resultDICT["source"] = args[2]
        resultDICT["target"] = args[3]
        resultDICT["amount"] = args[1]
        pass          

    if utterance == "[我]想把這[500元][澳幣]換成[美金]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["response"] = "你要用 {} 換 {} 哦？才換{} 會不會太少？".format(args[1], args[3], args[2])
            pass
        
        resultDICT["source"] = args[2]
        resultDICT["target"] = args[3]
        resultDICT["amount"] = args[1]
        pass          

    if utterance == "[我]想換[200萬]的[越南盾]，[這樣]需要準備多少[台幣]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["response"] = "你要用 {} 換 {} 哦？才換{} 會不會太少？".format(args[1], args[3], args[2])
            pass
        
        resultDICT["source"] = args[2]
        resultDICT["target"] = args[4]
        resultDICT["amount"] = args[1]
        pass        

    if utterance == "[我]想用[15000元][台幣]換[美金]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["response"] = "你要用 {} 換 {} 哦？才換{} 會不會太少？".format(args[1], args[3], args[2])
            pass
        
        resultDICT["source"] = args[2]
        resultDICT["target"] = args[3]
        resultDICT["amount"] = args[1]
        pass        

    if utterance == "[我]想要以[台幣]換[十萬元][日幣]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["response"] = "你要用 {} 換 {} 哦？才換{} 會不會太少？".format(args[1], args[3], args[2])
            pass
        
        resultDICT["source"] = args[3]
        resultDICT["target"] = args[1]
        resultDICT["amount"] = args[2]
        pass        

    if utterance == "[我]想要買[日幣][4萬元]，[這樣]折合[台幣]是多少":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["response"] = "你要用 {} 換 {} 哦？才換{} 會不會太少？".format(args[1], args[3], args[2])
            pass
        
        resultDICT["source"] = args[1]
        resultDICT["target"] = args[4]
        resultDICT["amount"] = args[2]
        pass        

    if utterance == "[我]想賣掉[100元][美金]，[這樣][會]有多少[台幣]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["response"] = "你要用 {} 換 {} 哦？才換{} 會不會太少？".format(args[1], args[3], args[2])
            pass
        
        resultDICT["source"] = args[2]
        resultDICT["target"] = args[5]
        resultDICT["amount"] = args[1]
        pass        

    if utterance == "[我]要換[五萬日幣]，[這樣][一共]要多少[台幣]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["response"] = "你要用 {} 換 {} 哦？才換{} 會不會太少？".format(args[1], args[3], args[2])
            pass
        
        resultDICT["source"] = [x for x in userDefinedDICT if x in args[1]][1]
        resultDICT["target"] = args[4]
        resultDICT["amount"] = args[1]
        pass        

    if utterance == "[我]要用[台幣]換[一百元][美金]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["response"] = "你要用 {} 換 {} 哦？才換{} 會不會太少？".format(args[1], args[3], args[2])
            pass
        
        resultDICT["source"] = args[3]
        resultDICT["target"] = args[1]
        resultDICT["amount"] = args[2]
        pass        

    if utterance == "[我們][今天]要用[美金]換[五千元][加拿大幣]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["response"] = "你要用 {} 換 {} 哦？才換{} 會不會太少？".format(args[1], args[3], args[2])
            pass
        
        resultDICT["source"] = args[4]
        resultDICT["target"] = args[2]
        resultDICT["amount"] = args[3]
        pass        

    if utterance == "換[500元][英鎊]需要多少[台幣]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["response"] = "你要用 {} 換 {} 哦？才換{} 會不會太少？".format(args[1], args[2], args[0])
            pass
        
        resultDICT["source"] = args[1]
        resultDICT["target"] = args[2]
        resultDICT["amount"] = args[0]
        pass        

    if utterance == "換[澳幣][一千元]需要多少[台幣]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["response"] = "你要用 {} 換 {} 哦？才換{} 會不會太少？".format(args[2], args[0], args[1])
            pass
        
        resultDICT["source"] = args[0]
        resultDICT["target"] = args[2]
        resultDICT["amount"] = args[1]
        pass        

    if utterance == "買[1000元][美金]，要多少[台幣]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["response"] = "你要用 {} 換 {} 哦？才換{} 會不會太少？".format(args[1], args[2], args[0])
            pass
        
        resultDICT["source"] = args[1]
        resultDICT["target"] = args[2]
        resultDICT["amount"] = args[0]
        pass        

    if utterance == "這裡的[2500元][美金]，[我]想換成[臺幣]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["response"] = "你要用 {} 換 {} 哦？才換{} 會不會太少？".format(args[1], args[3], args[2])
            pass
        
        resultDICT["source"] = args[1]
        resultDICT["target"] = args[3]
        resultDICT["amount"] = args[0]
        pass        

    return resultDICT
"""