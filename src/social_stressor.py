from emora_stdm import KnowledgeBase, DialogueFlow
from enum import Enum,auto


class State(Enum):
    START=auto()
    PROMPT0 = auto()
    PROMPT0_re=auto()
    PROMPT1 = auto()
    PROMPT1_often = auto()
    PROMPT1_sometimes = auto()
    PROMPT1_never = auto()
    PROMPT1_err = auto()
    PROMPT2=auto()
    PROMPT2_notbad = auto()
    PROMPT2_bad = auto()
    PROMPT2_err = auto()
    PROMPT3=auto()
    PROMPT3_often = auto()
    PROMPT3_sometimes = auto()
    PROMPT3_never = auto()
    PROMPT3_err = auto()
    PROMPT4= auto()
    PROMPT4_yes = auto()
    PROMPT4_no = auto()
    PROMPT4_err = auto()
    PROMPT5 = auto()
    PROMPT5_yes = auto()
    PROMPT5_no = auto()
    PROMPT5_err = auto()
    PROMPT6 = auto()
    PROMPT6_re = auto()
    PROMPT6_err =auto()
    PROMPT7 = auto()
    PROMPT7_err = auto()
    PROMPT7_ex = auto()
    PROMPT7_in = auto()




# TODO: create the ontology as needed
stress_dict ={
    "ontology":
        {
        "ontoften":
            [
                "always",
                "constantly",
                "frequently",
                "regularly",
                "often",
                "hourly",
                "daily",
                "weekly",
                "biweekly",
                "every month",
                "monthly",
                "every day",
                "everyday",
                "every hour"
            ],
        "ontsometimes":
            [
                "sometimes",
                "occasionally",
                "infrequently",
                "seldom",
                "not often",
                "rarely",
                "hardly ever",
                "not so often",
                "not very often",
                "not too often",
                "not always",
                "not too frequently",
                "not so frequently",
                "not very frequently",
                "not constantly",
                "not too constantly",
                "don't constantly",
                "don't often",
                "don't frequently",
                "don't always",
                "from time to time",
                "once in a while",
                "quarterly",
                "yearly",
                "anually",
                "every quarter",
                "every semester",
                "every year",
                "rarely",
                "hardly ever"
            ],
            "ontnever":
                [
                    "never",
                    "never ever",
                    "first time"
                ],
        "ontsocial":
            [
                "mixer",
                "dating",
                "dancing",
                "night out",
                "party",
                "hangouts",
                "hangout",
                "presentation",
                "presenting",
                "presenting",
                "public speaking",
                "speaking",
                "social",
                "conversation",
                "meeting",
                "nightclubs",
                "performance",
                "theatre",
                "bowling",
                "ice-skating",
                "retreat",
                "conversation",
                "seminar",
                "discussion",
                "discussing",
                "music festival",
                "festival",
                "carnival",
                "dance",
                "talk",
                "social media",
                "gathering"
            ],
        "ontyes":
            [
                "yes",
                "Yes",
                "YES",
                "yeah",
                "yea",
                "sure",
                "Of Course",
                "of course",
                "Sure",
                "i guess",
                "i think so",
                "do"
            ],
        "ontno":
            [
                "no",
                "not really",
                "nope",
                "don't",
                "none",
                "No",
                "NO",
                "Nope",
                "nope",
                "Nah",
                "nah"
            ],
        'ontpositive':
            [
                'admirable', 'energetic', 'lucky',
                'affable', 'enjoyable', 'magnificent',
                'affectionate', 'enthusiastic', 'marvelous',
                'agreeable', 'euphoric', 'meritorious',
                'amazing', 'excellent', 'merry',
                'amiable', 'exceptional', 'mild-mannered',
                'amused', 'excited', 'nice',
                'amusing', 'extraordinary', 'noble',
                'animated', 'exultant', 'outstanding',
                'appreciative', 'fabulous', 'overjoyed',
                'astonishing', 'faithful', 'passionate',
                'authentic', 'fantastic', 'peaceful',
                'believable', 'fervent', 'placid',
                'benevolent', 'fortunate', 'pleasant',
                'blissful', 'friendly', 'pleasing',
                'bouncy', 'fun', 'pleasurable',
                'brilliant', 'genuine', 'positive',
                'bubbly', 'glad', 'praiseworthy',
                'buoyant', 'glorious', 'prominent',
                'calm', 'good', 'proud',
                'charming', 'good-humored', 'relaxed',
                'cheerful', 'good-natured', 'reliable',
                'cheery', 'gracious', 'respectable',
                'clever', 'grateful', 'sharp',
                'comfortable', 'great', 'sincere',
                'comical', 'happy', 'spirited',
                'commendable', 'heartfelt', 'splendid',
                'confident', 'honest', 'superb',
                'congenial', 'honorable', 'superior',
                'content', 'hopeful', 'terrific',
                'cordial', 'humorous', 'thankful',
                'courteous', 'incredible', 'tremendous',
                'dedicated', 'inspirational', 'triumphant',
                'delighted', 'jolly', 'trustworthy',
                'delightful', 'jovial', 'trusty',
                'dependable', 'joyful', 'truthful',
                'devoted', 'joyous', 'uplifting',
                'docile', 'jubilant', 'victorious',
                'dynamic', 'keen', 'vigorous',
                'eager', 'kind', 'virtuous',
                'earnest', 'laudable', 'vivacious',
                'easygoing', 'laughing', 'whimsical',
                'ebullient', 'likable', 'witty',
                'ecstatic', 'lively', 'wonderful',
                'elated', 'lovely', 'worthy',
                'emphatic', 'loving', 'zealous',
                'enchanting', 'loyal', 'zestful',
                'well','smooth','awesome',
                "not bad","not too bad", "wasn't too bad",
                "wasn't bad","isn't bad","isn't too bad",
                "isn't very bad"
            ],
        'ontnegative':
            ['afraid',
             'bad',
             'anxious',
             'apprehensive',
             'ashamed',
             'cowardly',
             'frightened',
             'guilty',
             'horrified',
             'paralyzed',
             'petrified',
             'scared',
             'shocked',
             'shy',
             'skittish',
             'startled',
             'terrified',
             'terrorized',
             'timid',
             'troubled',
             'tired',
             'awful',
             'terrible',
             'worried',
             'aggressive',
             'bellicose',
             'belligerent',
             'combative',
             'hawkish',
             'merciless',
             'presumptuous',
             'pugnacious',
             'ruthless',
             'self-assertive',
             'angry',
             'enraged',
             'exasperated',
             'furious',
             'incensed',
             'indignant',
             'livid',
             'mad',
             'outraged',
             'wrathful',
             'annoyed',
             'asinine',
             'bored',
             'disgusted',
             'dullish',
             'dull',
             'obtuse',
             'peeved',
             'riled',
             'vexed',
             'evil',
             'abusive',
             'baneful',
             'contaminated',
             'contemptible',
             'corrupt',
             'cruel',
             'demonic',
             'depraved',
             'despicable',
             'devilish',
             'diabolic',
             'ferocious',
             'fiendish',
             'fierce',
             'heartless',
             'hellish',
             'infernal',
             'inimical',
             'malicious',
             'nasty',
             'nefarious',
             'nether',
             'perfidious',
             'putrefied',
             'savage',
             'scrupulous',
             'sinister',
             'sneaky',
             'spiteful',
             'spoiled',
             'tainted',
             'treacherous',
             'venal',
             'vile',
             'villainous',
             'wicked',
             'frustrated',
             'balked',
             'disappointed',
             'discontented',
             'foiled',
             'thwarted',
             'nervous',
             'alarmed',
             'anxious',
             'apprehensive',
             'cautious',
             'concerned',
             'confused',
             'conspicuous',
             'disturbed',
             'doubtful',
             'insecure',
             'irritable',
             'panicked',
             'perturbed',
             'suspicious',
             'pathetic',
             'affecting',
             'agitating',
             'lamentable',
             'piteous',
             'pitiful',
             'poignant',
             'stirring',
             'touching',
             'quarrelsome',
             'blatant',
             'boisterous',
             'cantankerous',
             'clamorous',
             'conspicuously',
             'contentious',
             'cross',
             'deafening',
             'disagreeable',
             'fretful',
             'hysterical',
             'jealous',
             'litigious',
             'mean',
             'mean-spirited',
             'militant',
             'nasty',
             'noisy',
             'offensively',
             'ornery',
             'peevish',
             'pugnacious',
             'rambunctious',
             'recalcitrant',
             'renitent',
             'roisterous',
             'strident',
             'testy',
             'touchy',
             'truculent',
             'unpleasant',
             'vociferous',
             'sad',
             'bleak',
             'dejected',
             'depressed',
             'desolate',
             'dingy',
             'discouraged',
             'dismal',
             'doleful',
             'dreary',
             'forlornly',
             'gloomy',
             'glum',
             'grievous',
             'grim',
             'heart',
             'broken',
             'lonely',
             'lugubrious',
             'melancholic',
             'miserable',
             'mopish',
             'morose',
             'mournful',
             'poor',
             'seamy',
             'somber',
             'sordid',
             'sorrowful',
             'sulky',
             'sullen',
             'temperamental',
             'unfortunate',
             'unhappy',
             'wistful',
             'wretched',
             'stubborn',
             'adamant',
             'hardheaded',
             'inflexible',
             'obdurate',
             'obstinate',
             'relentless',
             'unyielding',
             'terrible',
             'abhorrent',
             'abominable',
             'appalling',
             'awful',
             'bizarre',
             'calamitous',
             'dire',
             'disastrous',
             'dreadful',
             'fearful',
             'formidable',
             'freakish',
             'frightful',
             'ghastly',
             'grotesque',
             'gruesome',
             'heinous',
             'horrible',
             'horrid',
             'lurid',
             'odious',
             'painful',
             'terrifying',
             'tragic',
             'unctuous',
             "not well",
             "not very well",
             "not so well",
             "didn't go well",
             "wasn't well",
             "isn't good"
            ]
    }
}

knowledge = KnowledgeBase()
knowledge.load_json(stress_dict)
df = DialogueFlow(State.START, initial_speaker=DialogueFlow.Speaker.SYSTEM,kb=knowledge)
df.add_system_transition(State.START, State.PROMPT0,r'[!"What are you stressed about?"]')
df.add_user_transition(State.PROMPT0, State.PROMPT0_re,r'<$S_S=[!#ONT(ontsocial)]>')

df.add_system_transition(State.PROMPT0_re, State.PROMPT1, r'[!"How often do you participate in"$S_S"?"]')
df.add_user_transition(State.PROMPT1, State.PROMPT1_often, r'<{[!#ONT(ontoften)],/(?:\s|^)(once|twice|three\stimes|four\stimes|five\stimes|1\stimes|2\stimes|3\stimes|4\stimes|5\stimes)\s((every|per|a)(\s)?(one|1|two|2|three|3|four|4|five|5|six|6|seven|7|other)?\s(hour+s?|day+s?|week+s?))|((every)\s(one|1|two|2|other)\s(month+s?))|((a|per)\s(month))(?:\s|,|\.|$)/}>')
df.add_user_transition(State.PROMPT1, State.PROMPT1_sometimes, r'<{[!#ONT(ontsometimes)],/(?:\s|^)(once|twice|three\stimes|four\stimes|five\stimes|1\stimes|2\stimes|3\stimes|4\stimes|5\stimes)\s((every|per|a)(\s)?(one|1|two|2|three|3|four|4|five|5|six|6|seven|7|other)?\s(semester+s?|term+s?|quarter+s?|year+s?|decade+s?))|((every\s)(three|3|four|4|five|5|six|6|seven|7|eight|8|nine|9|ten|10)\s(month+s?))(?:\s|,|\.|$)/}>')
df.add_user_transition(State.PROMPT1, State.PROMPT1_never, r'<{[!#ONT(ontnever)]}>')
df.add_system_transition(State.PROMPT1_often,State.PROMPT2,r'[!"Oh...it must be really hard for you. I get stressed about"$S_S"too, but the stress gradually decreases everytime I do it. How did your most recent" $S_S "go?"]')
df.add_system_transition(State.PROMPT1_sometimes,State.PROMPT2,r'[!"That is totally normal! I sometimes feel stressed about "$S_S"too. How did your most recent"$S_S"go last time?"]')
df.add_system_transition(State.PROMPT1_never,State.PROMPT4,r'[!"Wow. It is your first time ever? Trying new things can be scary sometimes, but you got this! Is this"$S_S"mandatory?"]')

df.add_user_transition(State.PROMPT2,State.PROMPT2_notbad,r'<{[!#ONT(ontpositive)]}>')
df.add_user_transition(State.PROMPT2,State.PROMPT2_bad,r'<{[!#ONT(ontnegative)]}>')
df.add_system_transition(State.PROMPT2_notbad,State.PROMPT3,r'[!"Then I am pretty sure this time it will go just fine too. Just curious, how often do you feel stressed about it?"]')
df.add_system_transition(State.PROMPT2_bad,State.PROMPT3,r'[!"Yeah...sometimes"$S_S"can be really bad. I know how it feels when things get out of control. Just curious, how often do you feel stressed about it?"]')

df.add_user_transition(State.PROMPT3,State.PROMPT3_often,r'<{[!#ONT(ontoften)]}>')
df.add_user_transition(State.PROMPT3,State.PROMPT3_sometimes,r'<{[!#ONT(ontsometimes)]}>')
df.add_user_transition(State.PROMPT3,State.PROMPT3_never,r'<{[!#ONT(ontnever)]}>')
df.add_system_transition(State.PROMPT3_often,State.PROMPT4,r'[!"I see...but no pain no gain right? The stress could bring out our best performance. Is this"$S_S"mandatory for you?"]')
df.add_system_transition(State.PROMPT3_sometimes,State.PROMPT4,r'[!"You know some amount of stress is helpful. Believe it or not, it can help you be more effecient, motivated, and stuffs.Is this"$S_S"mandatory for you?"]')
df.add_system_transition(State.PROMPT3_never,State.PROMPT4,r'[!"Oh really? This upcoming"$S_S" must mean a lot to you. Just treat it the same way you did before and you will do just fine! Is this"$S_S"mandatory for you?"]')

df.add_user_transition(State.PROMPT4,State.PROMPT4_yes,r'<{[!#ONT(ontyes)]}>')
df.add_user_transition(State.PROMPT4,State.PROMPT4_no,r'<{[!#ONT(ontno)]}>')
df.add_system_transition(State.PROMPT4_yes,State.PROMPT5,r'[!"Do you wanna participate in this"$S_S"then?"]')
df.add_system_transition(State.PROMPT4_no,State.PROMPT6,r'[!"What made you wanna attend this event?"]')

df.add_user_transition(State.PROMPT5,State.PROMPT5_yes,r'<{[!#ONT(ontyes)]}>')
df.add_user_transition(State.PROMPT5,State.PROMPT5_no,r'<{[!#ONT(ontno)]}>')
df.add_system_transition(State.PROMPT5_yes,State.PROMPT6,r'[!"Great! What made you wanna attend this event?"]')
df.add_system_transition(State.PROMPT5_no,State.PROMPT7,r'[!"I am sorry that you have to go...but on the bright side,you might meet someone interesting there! This might sound weird but sometimes i enjoy"$S_S"when everyone is focusing on me. Fo...fo...focus on me. Okay that was a little too much of Ariana. How about you? Any part about this"$S_S"that you will enjoy the most?"]')

df.add_user_transition(State.PROMPT6,State.PROMPT6_re,'<$reason={[!#POS(verb) #POS(part) #POS(verb) #POS(noun)],[!#POS(verb) #POS(part) #POS(verb)],[!#POS(verb) #POS(verb)]，[!#POS(verb) #POS(verb) #POS(noun)]}>')
df.add_system_transition(State.PROMPT6_re,State.PROMPT7, r'[!"I am glad that you "$reason".This might sound weird but sometimes I enjoy"$S_S"when everyone is focusing on me. Fo...fo...focus on me. Okay that was a little too much of Ariana. How about you? Any part about this"$S_S"that you will enjoy the most?"]')

df.add_user_transition(State.PROMPT7,State.PROMPT7_ex, '[$enjoy={[#POS(verb) #POS(noun)],[#POS(verb)]}]')
df.add_system_transition(State.PROMPT7_ex,State.PROMPT7_err,r'[!"blablabla"$enjoy]')

###### error cases
df.set_error_successor(State.PROMPT1, State.PROMPT1_err)
df.set_error_successor(State.PROMPT2, State.PROMPT2_err)
df.set_error_successor(State.PROMPT3, State.PROMPT3_err)
df.set_error_successor(State.PROMPT4, State.PROMPT4_err)
df.set_error_successor(State.PROMPT5, State.PROMPT5_err)
df.set_error_successor(State.PROMPT6, State.PROMPT6_err)
df.add_system_transition(State.PROMPT1_err,State.PROMPT1,r'[!"Sorry. I did not get it. Is it more like very often, sometimes, or never?"]')
df.add_system_transition(State.PROMPT2_err,State.PROMPT3,r'[!"I see I see. Just curious, how often do you feel stressed about it?"]')
df.add_system_transition(State.PROMPT3_err,State.PROMPT4,r'[!"Yeah. I feel you. Is this"$S_S"mandatory for you?"]')
df.add_system_transition(State.PROMPT4_err,State.PROMPT5,r'[!"Mmhmm. Do you want to participate in this"$S_S"then?"]')
df.add_system_transition(State.PROMPT5_err,State.PROMPT5,r'[!"Um is that a yes?"]')
df.add_system_transition(State.PROMPT6_err,State.PROMPT7,r'[!"Oh! That is very interesting! This might sound weird but sometimes I enjoy"$S_S"when everyone is focusing on me. Fo...fo...focus on me. Okay that was a little too much of Ariana. How about you? Any part about this"$S_S"that you will enjoy the most?"]')


if __name__ == '__main__':
    df.run(debugging=False)


