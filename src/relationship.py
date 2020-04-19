from emora_stdm import KnowledgeBase, DialogueFlow
from enum import Enum, auto
from emora_stdm import Macro


class State(Enum):
    START = auto()
    PROMPT = auto()
    ERR = auto()
    FAM = auto()
    FAM0 = auto()
    FAM0_often = auto()
    FAM0_sometimes = auto()
    FAM0_never = auto()
    FAM0_ERR = auto()
    FAM1 = auto()
    FAM1_ERR = auto()
    FAM1_yes = auto()
    FAM1_no = auto()
    COVID0 = auto()
    FAM2 = auto()
    FAM2_ERR = auto()
    FAM2_abuse = auto()
    FAM3 = auto()
    FAM3_ERR = auto()
    FAM2_work = auto()
    FAM2_death = auto()
    FAM2_divorce = auto()
    FAM3_yes = auto()
    FAM3_no = auto()
    FAM4 = auto()
    FAM4_ERR = auto()
    FRIEND = auto()
    FRIEND0 = auto()
    FRIEND0_ERR = auto()
    COVID0_yes = auto()
    COVID0_no = auto()
    COVID0_ERR = auto()
    COVID1 = auto()
    COVID1_ERR = auto()
    COVID1_game = auto()
    COVID1_food = auto()
    COVID1_video = auto()
    COVID1_socialApp = auto()
    COVID1_class = auto()
    COVID2 = auto()
    COVID2_ERR = auto()
    COVID1_music = auto()


ontology = {
    "ontology": {
        'ontfam':
            [
                'mother', 'father', 'mom', 'dad', 'brother', 'sister', 'uncle', 'aunt', 'aunty', 'parents', 'son',
                'daughter', 'husband', 'wife', 'cousin', 'grandparents', 'grandfather', 'grandmother', 'grandpa',
                'grandma', 'nephew'
            ],
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
                "dont constantly",
                "dont often",
                "dont frequently",
                "dont always",
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
                "for sure",
                "certainly"
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
        'ontabuse':
            ['abuse',
             'abuses',
             'abusing',
             'physical',
             'physically',
             'hit',
             'hits',
             'hitting',
             'punching',
             'slapping',
             'slap',
             'slaps',
             'biting',
             'kicking',
             'kick',
             'kicks',
             'choking',
             'choke',
             'chokes',
             'violent',
             'violence',
             'hurt',
             'hurts',
             'hurting',
             'humiliate',
             'humiliating',
             'threatening',
             'threaten',
             'abusing',
             'sex',
             'sexual',
             'contact',
             'touch',
             'touches',
             'touching',
             'force',
             'forces',
             'forcing',
             'neglect',
             'neglects',
             'neglecting',
             'rape',
             'rapes',
             'alcoholic',
             'drunk'
             ],
        'ontwork':
            [
                'work',
                'working',
                'office',
                'works',
                'job',
                'workload',
                'unemployed',
                'unemployment',
                'company',
                'financial',
                'money',
            ],
        'ontdeath':
            [
                'death',
                'die',
                'died',
                'passed away',
                'dead',
                'pass away'
            ],
        'ontdivorce':
            [
                'divorce',
                'divorced'
            ],
        'ontfriend':
            [
                'friend',
                'friends',
                'classmate',
                'classmates',
                'roommate',
                'roommates',
                'housemate',
                'housemates',
                'friendship',
                'friendships'
            ],
        'ontgames':
            [
                "video games",
                "board games",
                "game",
                "lol",
                'league',
                'animal crossing',
                'switch',
                "League of Legends",
                "VR games",
                "VR Games",
                "Games",
                "VR Game",
                "Game",
                "video games",
                "games",
                "LOL",
                "2K18",
                "2K19",
                "2K20",
                "FIFA",
                "PC",
                "PS4",
                "Play Station",
                "Xbox",
                "xbox",
                "play station",
                "pc",
                "ps4",
                'cs',
                'call of duty',
                'gta',
                'GTA'
            ],
        'ontfood':
            [
                "eating",
                "cooking",
                "cook",
                "eat",
                "order takeouts",
                "order takeout",
                "snack",
                "snacks",
                "snacking on",
                "frozen food",
                "dining",
                "restaurants",
                "restaurant",
                "eat out",
                "potluck",
                "food",
                "order Chinese",
                "order chinese",
                "order Japanese",
                "Order japanese",
                "order Italian",
                "Order italian",
                "pasta",
                "burger",
                "pizza",
                "sushi",
                "rice",
                "groceries",
                "stress baking",
                "bake",
                "baking"
            ],
        'ontsocialApp':
            ['fb',
             'facebook',
             'snapchat',
             'tiktok',
             'tik tok',
             'instagram',
             'ig',
             'messenger',
             'call',
             'twitter',
             'facetime',
             'wechat',
             'line',
             'kakao talk',
             'kakao',
             'social'
             ],
        'ontclass':
            ['online classes',
             'online class',
             'online',
             'class',
             'classes',
             'school',
             'zoom',
             'recording',
             'professor'],
        'ontreadwatch':
            [
                "books",
                "TV",
                "netflix",
                "television",
                "Netflix",
                'movie',
                'movies',
                'tv',
                'book',
                "Hulu",
                "hulu",
                "youtube",
                "Youtube",
                "Youtube videos",
                "news",
                "newspaper",
                "online article",
                "articles",
                "research paper",
                "scientific report",
                'read',
                'watch',
                'reading',
                'watching'
            ],
        'ontmusic':
            [
                "listening to music",
                'listening',
                'spotify',
                "singing",
                "composing",
                "music composition",
                "playing the piano",
                "playing the guitar",
                "playing the drum",
                "singing",
                "listen to music",
                "music",
                "hip hop",
                "rock",
                "pop music",
                "pop culture",
                "jazz",
                "heavy metal",
                "classical music",
                "country music",
                "rap",
                "study music",
                "studying music",
                "sleep music",
                "calm music",
                "calming music"
            ],


    }
}

knowledge = KnowledgeBase()
knowledge.load_json(ontology)
df = DialogueFlow(State.START, initial_speaker=DialogueFlow.Speaker.SYSTEM, kb=knowledge)

df.add_system_transition(State.START, State.PROMPT, '"Hi, what are you stressed about?"')

'''Family Branch'''
df.add_user_transition(State.PROMPT, State.FAM, r'<$F_M=[!#ONT(ontfam)]>')

df.add_system_transition(State.FAM, State.FAM0,
                         r'[!"Haha you are not alone, I am having a hard time dealing with my family too. How often do you feel stressed about your"$F_M"?"]')
df.add_user_transition(State.FAM0, State.FAM0_often,
                       r'<{[!#ONT(ontoften)],/(?:\s|^)(once|twice|three\stimes|four\stimes|five\stimes|1\stimes|2\stimes|3\stimes|4\stimes|5\stimes)\s((every|per|a)(\s)?(one|1|two|2|three|3|four|4|five|5|six|6|seven|7|other)?\s(hour+s?|day+s?|week+s?))|((every)\s(one|1|two|2|other)\s(month+s?))|((a|per)\s(month))(?:\s|,|\.|$)/}>')
df.add_user_transition(State.FAM0, State.FAM0_sometimes,
                       r'<{[!#ONT(ontsometimes)],/(?:\s|^)(once|twice|three\stimes|four\stimes|five\stimes|1\stimes|2\stimes|3\stimes|4\stimes|5\stimes)\s((every|per|a)(\s)?(one|1|two|2|three|3|four|4|five|5|six|6|seven|7|other)?\s(semester+s?|term+s?|quarter+s?|year+s?|decade+s?))|((every\s)(three|3|four|4|five|5|six|6|seven|7|eight|8|nine|9|ten|10)\s(month+s?))(?:\s|,|\.|$)/}>')
df.add_user_transition(State.FAM0, State.FAM0_never, r'<{[!#ONT(ontnever)]}>')

df.add_system_transition(State.FAM0_often, State.FAM1,
                         r'[!"You dont get along well with your"$F_M", huh? My brother is also a pain in my ass...he always eat my food and never apologize... Is your stress caused by coronavirus?"]')
df.add_system_transition(State.FAM0_sometimes, State.FAM1,
                         r'[!"I think this is totally normal! Life gives you lemons sometimes, just make lemonade. Is this stress caused by coronavirus?"]')
df.add_system_transition(State.FAM0_never, State.FAM1, r'[!"Oh...let me guess. Is your stress caused by coronavirus?"]')
df.add_user_transition(State.FAM1, State.FAM1_yes, r'<[!#ONT(ontyes)]>')
df.add_user_transition(State.FAM1, State.FAM1_no, r'<[!#ONT(ontno)]>')

df.add_system_transition(State.FAM1_yes, State.COVID0,
                         r'[!"Yeah...coronavirus is really messing up out lives in every aspect, you are not the only who suffer from it. Are you currently quarantine together with your"$F_M"?"]')
df.add_system_transition(State.FAM1_no, State.FAM2,
                         r'[!"At least you have one less thing to worry about. Guess what, my mom is so worried about getting coronavirus, she literally refuses to talk to anyone in within 3 steps... Whats wrong with you and your"$F_M"then?"]')
df.add_user_transition(State.FAM2, State.FAM2_abuse, r'[!#ONT(ontabuse)]')
df.add_user_transition(State.FAM2, State.FAM2_work, r'[!#ONT(ontwork)]')
df.add_user_transition(State.FAM2, State.FAM2_death, r'[!#ONT(ontdeath)]')
df.add_user_transition(State.FAM2, State.FAM2_divorce, r'[!#ONT(ontdivorce)]')

df.add_system_transition(State.FAM2_abuse, State.FAM3,
                         r'[! "Oh...I am so sorry...It must be very hard for you, I wish I could actually do something for you besides just talking like this. You should definetly seek help from other people that can handle this situation better. I will try my best to make you feel better. Just curious, are you currently in quarantine?"]')
df.add_system_transition(State.FAM2_work, State.FAM3, r'[!"Oh...I am sorry. I know how that feels especially in this given time period. I experienced something similar but not exactly the same. My dad lost his job once and it was not only stressful but also depressing for the whole family. Lets just do our best on our part and hope things will get better. By the way, are you currently in quarantine?"]')
df.add_system_transition(State.FAM2_death, State.FAM3, r'[!"Oh...I am so sorry, now is the worse timing for this to happen. I never experienced a close one passing away but I can imagine how overwhelimg it is... Time is the best healer and I am sure you will get over it soon. By the way, are you currently in quarantine? "]')
df.add_system_transition(State.FAM2_divorce, State.FAM3, r'[!"Oh...I am sorry. You must be having a hard time. I am not entirely sure about your situation and I do not want to make any assumption, but I am always here to support you. By the way, are you currently in quarantine?"]')
df.add_user_transition(State.FAM3, State.FAM3_yes, r'<[!#ONT(ontyes)]>')
df.add_user_transition(State.FAM3, State.FAM3_no, r'<[!#ONT(ontno)]>')

df.add_system_transition(State.FAM3_yes, State.FAM4, r'[!"Same! I am so bored and anxious while in quarantine. There are only three things in my life now, sleep, eat, and zoom. How about you? What activity do you like to do during quarantine?"]')
df.add_system_transition(State.FAM3_no, State.FAM4, r'[!"I am so jealous of you! You must be staying in a very safe country. I am so bored and anxious while in quarantine, what activity would you do if you were me?"]')


###Family ERROR###
df.set_error_successor(State.FAM0, State.FAM0_ERR)
df.set_error_successor(State.FAM1, State.FAM1_ERR)
df.set_error_successor(State.FAM2, State.FAM2_ERR)
df.set_error_successor(State.FAM3, State.FAM3_ERR)
df.set_error_successor(State.FAM4, State.FAM4_ERR)

'''Friend Branch'''
df.add_user_transition(State.PROMPT, State.FRIEND, r'<$F=[!#ONT(ontfriend)]>')

df.add_system_transition(State.FRIEND, State.FRIEND0, r'[!""]')


###Friend ERROR###
df.set_error_successor(State.FRIEND0, State.FRIEND0_ERR)

'''Covid-19 Branch'''
df.add_user_transition(State.COVID0, State.COVID0_yes, r'<[!#ONT(ontyes)]>')
df.add_user_transition(State.COVID0, State.COVID0_no, r'<[!#ONT(ontno)]>')

df.add_system_transition(State.COVID0_yes, State.COVID1, r'[!"It is nice to still be able to see each other! I think everyone must be super stressed under this chaotic situation... I really hope this crisis ends soon so our lives can get back to normal.  Honestly, I think doing things together might reduce some of your stress. What activity do you like to do during quarantine?"]')
df.add_system_transition(State.COVID0_no, State.COVID1, r'[!"Oh...I am guessing this stress is coming from the fact that you cannot see each other. I sometimes videocall my friend and my family when I miss them. It is a lot to handle when away from everyone, you are not alone. Doing some fun activities might help you relax! What activity do you like to do during quarantine?"]')

df.add_user_transition(State.COVID1, State.COVID1_game, r'<[!#ONT(ontgame)]>')
df.add_user_transition(State.COVID1, State.COVID1_food, r'<[!#ONT(ontfood)]>')
df.add_user_transition(State.COVID1, State.COVID1_video, r'<[!#ONT(ontreadwatch)]>')
df.add_user_transition(State.COVID1, State.COVID1_socialApp, r'<[!#ONT(ontsocialApp)]>')
df.add_user_transition(State.COVID1, State.COVID1_class, r'<[!#ONT(ontclass)]>')
df.add_user_transition(State.COVID1, State.COVID1_music, r'<[!#ONT(ontmusic)]>')

df.add_system_transition(State.COVID1_game, State.COVID2, r'[!"I do like to play games too! We should definetly play together sometimes! All of my friends are playing animal crossing, I am so jealous...  "]')
df.add_system_transition(State.COVID1_food, State.COVID2, r'[!""]')
df.add_system_transition(State.COVID1_video, State.COVID2, r'[!""]')
df.add_system_transition(State.COVID1_socialApp, State.COVID2, r'[!""]')
df.add_system_transition(State.COVID1_class, State.COVID2, r'[!""]')
df.add_system_transition(State.COVID1_music, State.COVID2, r'[!""]')

###COVID-19 ERROR###
df.set_error_successor(State.COVID0, State.COVID0_ERR)
df.set_error_successor(State.COVID1, State.COVID1_ERR)
df.set_error_successor(State.COVID2, State.COVID2_ERR)


if __name__ == '__main__':
    df.run(debugging=False)
