import _pickle
import pickle

"""
query,iotype,category,score,priority
How much time do you spend social media or playing video games for ( number of hours/day ),5,2,0.2,0
Do you feel happy when you receive attention on social media (likes and comments ) ?,3,7,0.1,0
Do you play any online video games ?,1,3,0.3,0
Do you find yourself frequently checking your device,1,2,1,0
Do you feel frustrated or restless often ?,1,4,0.3,1
"""
ruleList = []
baseRules = []


# query is a string, expected type is inputtype, category is actual category, score determines how much it is weighted
class Rule:
    def __init__(self, query, expectedtype, symptom, category_dict):
        self.query = query
        self.expectedtype = expectedtype
        self.symptom = symptom
        self.category_dict = category_dict

    def get_symptom(self):
        return self.symptom

    def get_category_dictionary(self):
        return self.category_dict

    def get_query(self):
        return self.query


# The method to create new rules
def createRule(query, iotype, symptom_caused, categories_affected):
    return Rule(query, iotype, symptom_caused, categories_affected)


def save_object(obj, filename):
    with open(filename, 'wb') as output:  # Overwrites any existing file.
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)


def make_base_rules():
    global baseRules
    make_all_rules()
    baseRules.append(createRule("I am just curious, do you frequently play any multiplayer video games ?",
                                1,
                                3,
                                []))
    filepath = "Data/baseRules.p"
    save_object(baseRules, filepath)


def make_all_rules():
    global ruleList
    print("\nLoading all rules\n")
    ruleList.append(createRule(
        "Do you feel like this ? - I feel useless and cannot perform in difficult tasks\n",
        1,
        5,
        [1, 2]))
    ruleList.append(createRule(
        "Do you feel like this ? - I am not confident enough to face the future\n",
        1,
        5,
        [4, 1]))
    ruleList.append(createRule(
        "Do you feel like this ? - I am not happy about myself\n",
        1,
        2,
        [2, 3]))
    ruleList.append(createRule(
        "Do you feel this way ? - I feel as if I am actually connecting with people only when they interact with me online\n",
        1,
        2,
        [5, 2]))
    ruleList.append(createRule(
        "Do you feel this way ?, I feel angry and frustrated when things do not go my way\n",
        1,
        3,
        [2, 6]))
    ruleList.append(createRule(
        "I cannot initiate a conversation nor make eye contact. Do you ever feel this way ?\n",
        1,
        1,
        [1, 3, 5]))
    ruleList.append(createRule(
        "I fear I would not be invited to any social gatherings with my peers and colleagues\n",
        2,
        2,
        [3, 5]))
    ruleList.append(createRule(
        "I feel very bored and tired when I do not check my social media feeds for over a day\n",
        2,
        1,
        [5, 2]))
    ruleList.append(createRule(
        "Ever felt like this ? -I want to stop using my device so much, but I find it hard to stop\n",
        2,
        1,
        [5, 6]
    ))
    ruleList.append(createRule(
        "I feel compelled to check on the reactions to my posts, and feel offended if someone I consider a friend does not acknowledge my posts\n",
        1,
        1,
        [1, 3, 6]))
    ruleList.append(createRule(
        "I feel uneasy when and fidget if I do not have my phone with me\n",
        1,
        1,
        [4, 6]
    ))
    ruleList.append(createRule(
        "The feel less appreciated by the people around me in real life when compared to my friends online\n",
        2,
        1,
        [1]
    ))
    ruleList.append(createRule(
        "I find myself getting angry or frustrated if friends or family keep me from accessing my social media handle\n",
        2,
        1,
        [2, 3]
    ))
    ruleList.append(createRule(
        "I feel as if all my friends are having fun without me\n",
        2,
        2,
        [1, 5, 2]
    ))
    ruleList.append(createRule(
        "I get very frustrated and angry at the people around me when I cannot access my profiles for even a short period of time\n",
        2,
        1,
        [4]))
    ruleList.append(createRule(
        "I fell as if people around me do not really understand me.\n",
        1,
        1,
        [3]))
    ruleList.append(createRule(
        "I sometimes feel that I am only a part of a community when I am online\n",
        1,
        1,
        [5]))
    ruleList.append(createRule(
        "I have always feared that I would be shunned by my friends for my physical appearance\n",
        2,
        2,
        [2, 1, 5]))
    ruleList.append(createRule(
        "I cannot keep myself off social media due to my interest in knowing what my friends are upto\n",
        1,
        2,
        [5]))
    ruleList.append(
        createRule(
            "I fear I would be get left behind by my peers if I do not follow the trends on social media\n",
            2,
            2,
            [1, 4]))
    ruleList.append(createRule(
        "hey, this is a secret, dont let anyone else know.I get frustrated when I see posts of people going somewhere without even inviting me. Do you by any chance feel the same ?\n",
        1,
        2,
        [5, 4, 6]))
    ruleList.append(
        createRule(
            "I feel very lonely at times when I see others going out without having the courtesy to invite me\n",
            2,
            2,
            [4, 5]))
    ruleList.append(createRule(
        "I feel that I do not have the physical features to stand out, which would make me undesirable for peers\n",
        2,
        2,
        [1, 2, 5]))
    ruleList.append(createRule(
        "I enjoy video games and only play them to have fun friends\n",
        1,
        3,
        [5]))
    ruleList.append(createRule(
        "I enjoy the feeling of winning and outsmarting my opponents\n",
        1,
        3,
        [1, 2]))
    ruleList.append(createRule(
        "Losing in video games makes me very angry\n",
        1,
        3,
        [6]))
    ruleList.append(createRule(
        "I sometimes feel on top of the world when I play and I relish that feeling\n",
        2,
        3,
        [1, 3, 4]
    ))
    ruleList.append(createRule(
        "Every other activity apart from playing video games feels like a chore to me\n",
        1,
        3,
        [2, 6]
    ))
    ruleList.append(createRule(
        "I only play video games for the feeling of companionship I get from friends in the game\n",
        1,
        3,
        [5]
    ))
    ruleList.append(createRule(
        "I play video games for over six hours or whenever I find the time\n",
        1,
        3,
        [2, 4, 5]
    ))
    ruleList.append(createRule(
        "I really enjoy the feeling of being better than others at some particular game\n",
        2,
        3,
        [2, 3]
    ))
    ruleList.append(createRule(
        "I have a favourite game that I play with friends and I think about the game every day\n",
        2,
        3,
        [1]
    ))
    ruleList.append(createRule(
        "I am being very forgetful of late,  have you ever felt this way ?\n",
        1,
        4,
        [4]))
    ruleList.append(createRule(
        "I cant stop thinking about what happened to last post I made on my favourite social media platform\n",
        2,
        4,
        [3, 5]))
    ruleList.append(createRule(
        "I sometimes forget to close the refrigerator and leave the lights on while leaving the room\n",
        2,
        4,
        [4, 6]))
    ruleList.append(createRule(
        "I sometimes forget where I am and I end up walking on the wrong side of the road or get distracted very easily\n",
        2,
        4,
        [4]))
    ruleList.append(createRule(
        "I feel like I am missing out on something important being posted by my friends and cannot stop thinking about it even while I am working on something else\n",
        2,
        4,
        [4, 5]))
    ruleList.append(createRule(
        "Ever felt like - I feel like I cannot do anything right or I wish I could redo something to make it better\n",
        2,
        5,
        [1, 4, 6]))

    ruleList.append(createRule(
        "Ever felt this way ? Others can do what I can do, but better\n",
        1,
        5,
        [1, 6]))
    ruleList.append(createRule(
        "I do no feel energetic or I do not wish to get out of bed, or I feel really tired, felt like this recently ?\n",
        2,
        5,
        [2, 4, 6]))
    ruleList.append(createRule(
        "Of late, I have been enjoying outsmarting others in my favourite video game\n",
        1,
        3,
        [1]))
    ruleList.append(createRule(
        "I think about my favourite video game all the time, even at work or school\n",
        1,
        3,
        [4, 6]))
    ruleList.append(createRule(
        "I feel unhappy when I don receive any notifications about some post I made on social media recently\n",
        2,
        1,
        [1, 4]))
    ruleList.append(createRule(
        "I don't feel appreciated by people who are supposed to be close to me, I find that people are much kinder to me online\n",
        1,
        1,
        [3, 5]))
    ruleList.append(createRule(
        "I sometimes wait in a lobby for friends to join me to play, out of fear that they will start playing without me",
        2,
        3,
        [5, 6]))
    print("Lenght of rules list is : ", len(ruleList))
    allfilespath = "Data/allrules.p"
    save_object(ruleList, allfilespath)


def find_counts():
    global ruleList
    make_all_rules()
    counter1 = 0
    counter2 = 0
    counter3 = 0
    counter4 = 0
    counter5 = 0

    for rule in ruleList:
        print(rule.query)
        if rule.get_symptom() == 1:
            counter1 += 1
        elif rule.get_symptom() == 2:
            counter2 += 1
        elif rule.get_symptom() == 3:
            counter3 += 1
        elif rule.get_symptom() == 4:
            counter4 += 1
        elif rule.get_symptom() == 5:
            counter5 += 1
    print(counter1)
    print(counter2)
    print(counter3)
    print(counter4)
    print(counter5)
    print("Total count = ", counter1+counter2+counter3+counter4+counter5)


def load_pickle(filepath):
    pickle_input = open(filepath, "rb")
    pickle_data = pickle.load(pickle_input)
    return pickle_data


def find_max_all_categories(ruleListElement):
    selftesteem_max = 0
    depression_max = 0
    validation_max = 0
    anxiety_max = 0
    loneliness_max = 0
    stress_max = 0
    for rule in ruleListElement:
        if 1 in rule.get_category_dictionary():
            selftesteem_max += 4
        if 2 in rule.get_category_dictionary():
            depression_max += 4
        if 3 in rule.get_category_dictionary():
            validation_max += 4
        if 4 in rule.get_category_dictionary():
            anxiety_max += 4
        if 5 in rule.get_category_dictionary():
            loneliness_max += 4
        if 6 in rule.get_category_dictionary():
            stress_max += 4
    print(selftesteem_max, depression_max, validation_max, anxiety_max, loneliness_max, stress_max)
    return [selftesteem_max, depression_max, validation_max, anxiety_max, loneliness_max, stress_max]


def separate_rules_by_symptom(rulelist):
    separated_dict = {}
    for rule in rulelist:
        if rule.get_symptom() not in separated_dict.keys():
            separated_dict[rule.get_symptom()] = []
        else:
            separated_dict[rule.get_symptom()].append(rule)
    for symptom_key in separated_dict.keys():
        print(separated_dict[symptom_key])
    return separated_dict


def purge_ruleset_by_symptom(symptomval, ruledict):
    ruledict[symptomval] = []
    for symptomkey in ruledict.keys():
        print(ruledict[symptomkey])
    return ruledict


def main():
    global ruleList, baseRules
    resetglobals()

    make_base_rules()
    find_max_all_categories(ruleList)
    basefilepath = "Data/baseRules.p"
    allfilespath = "Data/allrules.p"

    baseRules = load_pickle(basefilepath)
    for rule in baseRules:
        print(rule.query)
    ruleList.clear()
    ruleList = load_pickle(allfilespath)
    print(len(ruleList), " is the length of the rule list")
    rule_dict = separate_rules_by_symptom(ruleList)

    return baseRules, rule_dict


def resetglobals():
    global ruleList, baseRules
    ruleList.clear(), baseRules.clear()


if __name__ == "__main__":
    main()
