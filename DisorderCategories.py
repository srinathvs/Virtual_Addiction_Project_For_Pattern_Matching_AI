# TODO :Write the actual rules

# TODO :Make the server check for each rule's question and answer and update the user agent's vals.

import csv
# TODO : Rule Pruning
from enum import Enum

import RulesDefiner
from RulesDefiner import createRule, purge_ruleset_by_symptom as purge
from RulesDefiner import main as ruleloader
from RulesDefiner import save_object as save, load_pickle as load
import categoriesEnums
from categoriesEnums import categories
from categoriesEnums import symptoms
from categoriesEnums import inputType
import os.path
from os import path
from RulesDefiner import find_max_all_categories as maxcat

RuleDict = {}
BaseRules = []
ruleflatlist = []


# these are the types of inputs in the system


class agent:
    def __init__(self, name, selfesteem, depression, need_validation, anxiety, loneliness,
                 stress, reasons, remaining_rules):
        self.name = name
        self.selfesteem = selfesteem
        self.depression = depression
        self.need_validation = need_validation
        self.anxiety = anxiety
        self.loneliness = loneliness
        self.stress = stress
        self.reasons = reasons
        self.remaining_rules = remaining_rules

    def checkval(self, maxValArr):
        if self.selfesteem / maxValArr[0] > .75:
            self.reasons[0] = ["selfesteem"]
        if self.depression / maxValArr[1] > .75:
            self.reasons[1] = ["depression"]
        if self.need_validation / maxValArr[2] > .75:
            self.reasons[2] = ["needvalidation"]
        if self.anxiety / maxValArr[3] > .75:
            self.reasons[3] = ["anxiety"]
        if self.loneliness / maxValArr[4] > .75:
            self.reasons[4] = ["loneliness"]
        if self.stress / maxValArr[5] > .75:
            self.reasons[5] = ["stress"]

# Meant to calculate the category values
    def setcategoryvals(self, category_list, val):
        for category in category_list:
            if category == 1:
                self.selfesteem += val
            if category == 2:
                self.depression += val
            if category == 3:
                self.need_validation += val
            if category == 4:
                self.anxiety += val
            if category == 5:
                self.loneliness += val
            if category == 6:
                self.stress += val
            print("\nCategory values are :", self.selfesteem, self.depression, self.need_validation, self.anxiety,
                  self.loneliness, self.stress)


def createAgent(name, esteem_score, depression_score, validation_score, anxiety_score, loneliness_score,
                stress_score, reason, remainingrules):
    return agent(name, esteem_score, depression_score, validation_score, anxiety_score,
                 loneliness_score, stress_score, reason, remainingrules)

def checkforname(name):
    namelist = []
    namepath = name + ".p"
    if path.exists(namepath):
        user_agent = load(namepath)
    else:
        user_agent = createAgent(name, 0, 0, 0, 0, 0, 0, {}, [])
    return user_agent


def checkforpath(data_path):
    if data_path.exists(path):
        return True
    else:
        return False


def intro(base, nameX):
    name = nameX
    user = checkforname(name)
    print("\n Hello," + name + " this is your friendly neighbourhood AI.\n I hope you are doing fine."
                               "\n I would like to request your help in helping me understand something."
                               "\n I hope you can cooperate with me on this.\n")
    if len(user.remaining_rules) == 0:
        user.remaining_rules.append(base)
        return user
    else:
        return user


def getResponseInputType(rulepart):
    input_index = int(rulepart.expectedtype)
    stringtype = str(categoriesEnums.inputType(input_index))
    stringtype = stringtype.replace("_", " ")
    stringtype = stringtype.replace("inputType.", "")
    return stringtype


def getResponseSymptom(rulepart):
    symptom_index = int(rulepart.category)
    stringtype = str(categoriesEnums.symptoms(symptom_index))
    stringtype = stringtype.replace("categories.", "")
    return stringtype


def flattendict(dictionary):
    flatlist = []
    for values in dictionary.values():
        flatlist.extend(values)

    flatlist = list(dict.fromkeys(flatlist))
    return flatlist


def ruleSize():
    return len(RuleDict)


# Placeholder main loop
def main(name):
    global RuleDict
    baserule, RuleDict = ruleloader()
    user = intro(baserule, name)
    print(user, RuleDict)
    return user, RuleDict


def reset_disorder_globals():
    global RuleDict, BaseRules, ruleflatlist
    RuleDict.clear()
    BaseRules.clear()
    ruleflatlist.clear()


"""Helper Functions
checkClientInput -> Checks if the client's input is compliant with the standards listed.


"""

srinath = "srinath"

if __name__ == "__main__":
    main(srinath)
