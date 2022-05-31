from enum import Enum


# these are the types of inputs in the system
class inputType(Enum):
    answer_as_yes_or_no = 1
    answer_in_range_of_1_to_4_with_1_being_never_felt_this_way_and_4_being_very_often_or_always = 2
    answer_in_a_sentence = 3
    answer_as_one_number = 4
    answer_in_one_word = 5


class symptoms(Enum):
    frequency = 1  # self-esteem, validation, loneliness
    missing_out = 2  # loneliness, anxiety, stress
    gamer_motivations = 3  # depression, stress, self-esteem
    attention_deficit = 4  # stress, anxiety
    brooding = 5  # all categories


class categories(Enum):
    selfesteem = 1  # relevant for gamer motivations, social media addiction
    depression = 2  # relevant for escapism
    validation = 3  # relevant for social media use
    anxiety = 4  # relevant for escapism, gamer motivation and social media
    loneliness = 5  # relevant for social media use and gamer motivations
    stress = 6  # relevant for reasons for relapse, escapism
