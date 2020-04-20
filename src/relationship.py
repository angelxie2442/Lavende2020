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
    COVID2_yes = auto()
    COVID2_no = auto()
    COVID3 = auto()
    COVID3_ERR = auto()
    COVIDEND = auto()
    COVID3_like = auto()
    COVID3_dislike = auto()
    FRIEND0_often = auto()
    FRIEND0_sometimes = auto()
    FRIEND0_never = auto()
    FRIEND1 = auto()
    FRIEND1_ERR = auto()
    FRIEND1_yes = auto()
    FRIEND1_no = auto()
    FRIEND2 = auto()
    FRIEND2_ERR = auto()
    FRIEND2_noF = auto()
    FRIEND2_fight = auto()
    FRIEND2_ppressure = auto()
    FRIEND2_fake = auto()
    FRIEND3 = auto()
    FRIEND3_ERR = auto()
    FRIEND3_yes = auto()
    FRIEND3_no = auto()
    FRIEND4 = auto()
    FRIEND4_ERR = auto()
    ROMAN = auto()
    ROMAN0 = auto()
    ROMAN0_ERR = auto()
    ROMAN0_often = auto()
    ROMAN0_sometimes = auto()
    ROMAN0_never = auto()
    ROMAN1 = auto()
    ROMAN1_ERR = auto()
    ROMAN2 = auto()
    ROMAN2_ERR = auto()
    ROMAN3 = auto()
    ROMAN3_ERR = auto()
    ROMAN2_yes = auto()
    ROMAN2_no = auto()
    ROMAN3_longD = auto()
    ROMAN3_insecure = auto()
    ROMAN3_cheat = auto()
    ROMAN3_toxic = auto()
    ROMAN3_sex = auto()
    ROMAN4 = auto()
    ROMAN4_ERR = auto()
    ROMAN4_yes = auto()
    ROMAN4_no = auto()
    ROMAN5 = auto()
    ROMAN5_ERR = auto()
    ROMAN1_short = auto()
    ROMAN1_mid = auto()
    ROMAN1_long = auto()


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
                'listen',
                'spotify',
                "singing",
                'sing',
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
        'ontlike':
            ['not bad',
             'not that bad',
             'i like it',
             'good'],
        'ontdislike':
            ['dont like',
             'hate',
             'not like',
             'not good',
             'not well',
             'dont really like'],
        'ontnof':
            [
                'no friend',
                'hard to make friend',
                'make friends',
                'make friend',
                'a lot of friends',
                'lots of friends',
                'dont want to socialize',
                'hard to socialize',
                'dont have friend',
                'networking',
                'network',
                'any friend',
                'shy',
                'afraid',
                'introvert'
            ],
        'ontfight':
            [
                'fight',
                'argument',
                'fighting',
                'argements',
                'fights'
            ],
        'ontppressure':
            [
                'peer pressure',
                'better',
                'pressure',
                'others',
                'other',
                'not good enough',
                'forcing',
                'force'
            ],
        'ontfake':
            ['fake',
             'not real', 'behind'],
        'ontsingle':
            [
                'single',
                'dont have boyfriend',
                'dont have boy friend',
                'dont have girlfriend',
                'dont have girl friend',
                'want a relationship',
                'want to date',
                'want a boyfriend',
                'want a girlfriend',
                'want a boy friend',
                'want a girl friend',
                'lonely',

            ],
        'ontroman':
            [
                'boyfriend',
                'girlfriend',
                'partner',
                'boy friend',
                'girl friend',
            ],
        'ontlongD':
            [
                'long distance',
                'long',
                'far',
                'distance',
                'away'
            ],
        'ontinsecure':
            [
                'dont love',
                'insecure',
                'dont care',
                'love him more',
                'love her more',
                'unequal',
                'fair',
                'insecurity',
                'more',
                'care'
            ],
        'ontcheat':
            [
                'cheat',
                'cheats',
                'cheating'
            ],
        'onttoxic':
            [
                'violent',
                'violence',
                'hit',
                'hits',
                'hitting',
                'physical',
                'toxic',
                'abuse',
                'abusing',
                'slap',
                'slaps',
                'slapping',
                'abusive',
                'drunk',
                'drinking'
            ],
        'ontsex':
            [
                'sex',
                'sexual'
            ]


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
                         r'[!"I think this is totally normal! Life gives you lemons sometimes, just make lemonade! You cannot imagine how many troubles my brother caused me. Is this stress caused by coronavirus?"]')
df.add_system_transition(State.FAM0_never, State.FAM1, r'[!"Oh...let me guess. Is your stress caused by coronavirus?"]')
df.add_user_transition(State.FAM1, State.FAM1_yes, r'<[!#ONT(ontyes)]>')
df.add_user_transition(State.FAM1, State.FAM1_no, r'<[!#ONT(ontno)]>')

df.add_system_transition(State.FAM1_yes, State.COVID0,
                         r'[!"Yeah...coronavirus is really messing up our lives in every aspect, you are not the only who suffer from it. Are you currently quarantine together with your"$F_M"?"]')
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
df.add_system_transition(State.FAM0_ERR, State.FAM1,
                         r'[!"I think this is totally normal! Life gives you lemons sometimes, just make lemonade. Is this stress caused by coronavirus?"]')
df.add_system_transition(State.FAM1_ERR, State.FAM2,
                         r'[!"At least you have one less thing to worry about. Guess what, my mom is so worried about getting coronavirus, she literally refuses to talk to anyone in within 3 steps... Whats wrong with you and your"$F_M"then?"]')
df.add_system_transition(State.FAM2_ERR, State.FAM3, r'[!"Communication is the key to success! So cliche right haha? Its funny but kinda true. I always fight with my brother about everything, and it is super effective in terms of resolving the problem quicly. By the way, are you currently in quarantine?"]')
df.add_system_transition(State.FAM3_ERR, State.FAM4, r'[!"Same! I am so bored and anxious while in quarantine. There are only three things in my life now, sleep, eat, and zoom. How about you? What activity do you like to do during quarantine?"]')



'''Friend Branch'''
df.add_user_transition(State.PROMPT, State.FRIEND, r'<$F=[!#ONT(ontfriend)]>')

df.add_system_transition(State.FRIEND, State.FRIEND0, r'[!"Of course you are stressed about your"$F"! For me, I hardly get stressed about my"$F"because I dont have a lot haha. How about you, how often do you feel stressed about it?"]')
df.add_user_transition(State.FRIEND0, State.FRIEND0_often,
                       r'<{[!#ONT(ontoften)],/(?:\s|^)(once|twice|three\stimes|four\stimes|five\stimes|1\stimes|2\stimes|3\stimes|4\stimes|5\stimes)\s((every|per|a)(\s)?(one|1|two|2|three|3|four|4|five|5|six|6|seven|7|other)?\s(hour+s?|day+s?|week+s?))|((every)\s(one|1|two|2|other)\s(month+s?))|((a|per)\s(month))(?:\s|,|\.|$)/}>')
df.add_user_transition(State.FRIEND0, State.FRIEND0_sometimes,
                       r'<{[!#ONT(ontsometimes)],/(?:\s|^)(once|twice|three\stimes|four\stimes|five\stimes|1\stimes|2\stimes|3\stimes|4\stimes|5\stimes)\s((every|per|a)(\s)?(one|1|two|2|three|3|four|4|five|5|six|6|seven|7|other)?\s(semester+s?|term+s?|quarter+s?|year+s?|decade+s?))|((every\s)(three|3|four|4|five|5|six|6|seven|7|eight|8|nine|9|ten|10)\s(month+s?))(?:\s|,|\.|$)/}>')
df.add_user_transition(State.FRIEND0, State.FRIEND0_never, r'<{[!#ONT(ontnever)]}>')

df.add_system_transition(State.FRIEND0_often, State.FRIEND1,
                         r'[!"Yeah...sometimes dealing with"$F"can be really stressful... Is this stress caused by coronavirus?"]')
df.add_system_transition(State.FRIEND0_sometimes, State.FRIEND1,
                         r'[!"I think this is totally normal! Life gives you lemons sometimes, just make lemonade! You cannot imagine how many troubles my best friend casued me, he stresses me out every once a month. Is this stress caused by coronavirus?"]')
df.add_system_transition(State.FRIEND0_never, State.FRIEND1, r'[!"Oh...let me guess. Is your stress caused by coronavirus?"]')
df.add_user_transition(State.FRIEND1, State.FRIEND1_yes, r'<[!#ONT(ontyes)]>')
df.add_user_transition(State.FRIEND1, State.FRIEND1_no, r'<[!#ONT(ontno)]>')

df.add_system_transition(State.FRIEND1_yes, State.COVID0,
                         r'[!"Yeah...coronavirus is really messing up our lives in every aspect, you are not the only who suffer from it. Are you currently quarantine together with your"$F"?"]')
df.add_system_transition(State.FRIEND1_no, State.FRIEND2,
                         r'[!"At least you have one less thing to worry about. I am a little stressed now because I cant see my best friend and talk about how our life suck haha. Whats wrong with you and your"$F"then?"]')
df.add_user_transition(State.FRIEND2, State.FRIEND2_noF, r'[!#ONT(ontnof)]')
df.add_user_transition(State.FRIEND2, State.FRIEND2_fight, r'[!#ONT(ontfight)]')
df.add_user_transition(State.FRIEND2, State.FRIEND2_ppressure, r'[!#ONT(ontppressure)]')
df.add_user_transition(State.FRIEND2, State.FRIEND2_fake, r'[!#ONT(ontfake)]')

df.add_system_transition(State.FRIEND2_noF, State.FRIEND3, r'[!"I am an introvert so I totally understand the frustration of socializing, but I have made some valuable friendships because I stepped out of my confort zone. I beleive you can do it too! Although it is hard to socialize now... Are you currently in quarantine?"]')
df.add_system_transition(State.FRIEND2_fight, State.FRIEND3, r'[!"I mean fighting with friends are inevitable right? I always fight with my best friend and that is also the reason why we are best friend. By the way, are you currently in quarantine?"]')
df.add_system_transition(State.FRIEND2_ppressure, State.FRIEND3, r'[!"Yeah...peer pressure can be really overwhelming sometimes espcially in college. To be honest, I do not really how to deal with this too. I guess maybe focusing more on ourselves? By the way, are you currently in quarantine?"]')
df.add_system_transition(State.FRIEND2_fake, State.FRIEND3, r'[!"Ohh...this is a hard one... I know how awful that feels. Just let it go and dont worry too much, you still have other friends right? In the worst case, you still have me haha. By the way, are you in quarantine currently?"]')
df.add_user_transition(State.FRIEND3, State.FRIEND3_yes, r'<[!#ONT(ontyes)]>')
df.add_user_transition(State.FRIEND3, State.FRIEND3_no, r'<[!#ONT(ontno)]>')

df.add_system_transition(State.FRIEND3_yes, State.FRIEND4, r'[!"Same! I am so bored and anxious while in quarantine. There are only three things in my life now, sleep, eat, and zoom. How about you? What activity do you like to do during quarantine?"]')
df.add_system_transition(State.FRIEND3_no, State.FRIEND4, r'[!"I am so jealous of you! You must be staying in a very safe country. I am so bored and anxious while in quarantine, what activity would you do if you were me?"]')

###Friend ERROR###
df.set_error_successor(State.FRIEND0, State.FRIEND0_ERR)
df.set_error_successor(State.FRIEND1, State.FRIEND1_ERR)
df.set_error_successor(State.FRIEND2, State.FRIEND2_ERR)
df.set_error_successor(State.FRIEND3, State.FRIEND3_ERR)
df.add_system_transition(State.FRIEND0_ERR, State.FRIEND1,
                         r'[!"I think this is totally normal! Life gives you lemons sometimes, just make lemonade! You cannot imagine how many troubles my best friend casued me, he stresses me out every once a month. Is this stress caused by coronavirus?"]')
df.add_system_transition(State.FRIEND1_ERR, State.FRIEND2,
                         r'[!"At least you have one less thing to worry about. I am a little stressed now because I cant see my best friend and talk about how our life suck haha. Whats wrong with you and your"$F"then?"]')
df.add_system_transition(State.FRIEND2_ERR, State.FRIEND3, r'[!"Ohh...I am sorry...Sometimes my firend just makes me super stressful and I do not know what to do either. I am sure you will get over it soon. By the way, are you in quarantine currently?"]')


'''Romantic Relationship Branch'''
df.add_user_transition(State.PROMPT, State.ROMAN, r'<$RF=[!#ONT(ontroman)]>')

df.add_system_transition(State.ROMAN, State.ROMAN0, r'[!"Aww I love to hear about love stories. Relationship is always stressful, right? That is why I enjoy being single despite having many admirers haha. How often do you feel stressed about your"$RF"?"]')
df.add_user_transition(State.ROMAN0, State.ROMAN0_often,
                       r'<{[!#ONT(ontoften)],/(?:\s|^)(once|twice|three\stimes|four\stimes|five\stimes|1\stimes|2\stimes|3\stimes|4\stimes|5\stimes)\s((every|per|a)(\s)?(one|1|two|2|three|3|four|4|five|5|six|6|seven|7|other)?\s(hour+s?|day+s?|week+s?))|((every)\s(one|1|two|2|other)\s(month+s?))|((a|per)\s(month))(?:\s|,|\.|$)/}>')
df.add_user_transition(State.ROMAN0, State.ROMAN0_sometimes,
                       r'<{[!#ONT(ontsometimes)],/(?:\s|^)(once|twice|three\stimes|four\stimes|five\stimes|1\stimes|2\stimes|3\stimes|4\stimes|5\stimes)\s((every|per|a)(\s)?(one|1|two|2|three|3|four|4|five|5|six|6|seven|7|other)?\s(semester+s?|term+s?|quarter+s?|year+s?|decade+s?))|((every\s)(three|3|four|4|five|5|six|6|seven|7|eight|8|nine|9|ten|10)\s(month+s?))(?:\s|,|\.|$)/}>')
df.add_user_transition(State.ROMAN0, State.ROMAN0_never, r'<{[!#ONT(ontnever)]}>')

df.add_system_transition(State.ROMAN0_often, State.ROMAN1,
                         r'[!"Yeah...sometimes dealing with"$f"can be really stressful. But constant stress in a romantic relationship is not a good sign... How long have you guys been together?"]')
df.add_system_transition(State.ROMAN0_sometimes, State.ROMAN1,
                         r'[!"I think this is totally normal! Even the happiest and healthiest relationship is sometimes stressful. How long have you guys been together?"]')
df.add_system_transition(State.ROMAN0_never, State.ROMAN1, r'[!"Good for you! It is very unlikely for a relationship to be not stressful at all. How long have you guys been together?"]')
df.add_user_transition(State.ROMAN1, State.ROMAN1_short, r'/.*(1|a|one)\s\byear\b.*|.*(month|months|day|days).*((?!year|years).)*/')
df.add_user_transition(State.ROMAN1, State.ROMAN1_mid, r'/.*([2-3]|two|three)\s\b(year|years)\b.*/')
df.add_user_transition(State.ROMAN1, State.ROMAN1_long, r'/.*([4-9]|[0]|four|five|six|seven|eight|nine|ten|eleven|twelve)\s\b(year|years)\b.*/')


df.add_system_transition(State.ROMAN1_short, State.ROMAN2, r'[!"Just started dating? This is so exciting! I bet you are you guys are still in the honeymoon phase haha. I am not surprised if you fight a lot. Is this stress caused by coronavirus?"]')
df.add_system_transition(State.ROMAN1_mid, State.ROMAN2, r'[!"Thats nice! Guess you guys are in a more steady phase. Is this stress caused by coronavirus?"]')
df.add_system_transition(State.ROMAN1_long, State.ROMAN2, r'[!"Oh my god really? I am so happy for you! Let me guess, is this stress caused by coronavirus?"]')
df.add_user_transition(State.ROMAN2, State.ROMAN2_yes, r'<[!#ONT(ontyes)]>')
df.add_user_transition(State.ROMAN2, State.ROMAN2_no, r'<[!#ONT(ontno)]>')

df.add_system_transition(State.ROMAN2_yes, State.COVID0,
                         r'[!"Yeah...coronavirus is really messing up our lives in every aspect, you are not the only who suffer from it. Are you currently quarantine together with your"$RF"?"]')
df.add_system_transition(State.ROMAN2_no, State.ROMAN3,
                         r'[!"Glad coronavirus is not affecting your relationship. Whats wrong with you and your"$RF"then?"]')
df.add_user_transition(State.ROMAN3, State.ROMAN3_longD, r'<[!#ONT(ontlongD)]>')
df.add_user_transition(State.ROMAN3, State.ROMAN3_insecure, r'<[!#ONT(ontinsecure)]>')
df.add_user_transition(State.ROMAN3, State.ROMAN3_cheat, r'<[!#ONT(ontcheat)]>')
df.add_user_transition(State.ROMAN3, State.ROMAN3_toxic, r'<[!#ONT(onttoxic)]>')
df.add_user_transition(State.ROMAN3, State.ROMAN3_sex, r'<[!#ONT(ontsex)]>')

df.add_system_transition(State.ROMAN3_longD, State.ROMAN4, r'[!"It is really stressful to have a long distance relationship, but a lot of my friends survive the initial stage and are maintaining a stable while happy relationship. Call regularlly and avoid being overly possesive might be helpful in my opinion. By the way, are you currently in quarantine?"]')
df.add_system_transition(State.ROMAN3_insecure, State.ROMAN4, r'[!"I was very insecure once, but I feel a lot better after becoming more independent and building my self-esteem. Just my personal experience that might be helpful. By the way, are you currently in quarantine?"]')
df.add_system_transition(State.ROMAN3_cheat, State.ROMAN4, r'[!"Oh...I am so sorry. I know how it feels when my"$RF"cheats on me and I will probably break up immediately. I think you should talk to more people and ask for their advices. By the way, are you currently in quarantine?"]')
df.add_system_transition(State.ROMAN3_toxic, State.ROMAN4, r'[!"Oh...I am sorry. I really hope I can do something for you besides just talking like this. A toxic relationship is not only tiring physcially but also mentally. I think you should talk to other people who can handle your situation better than me. By the way, are you currently in quarantine?"]')
df.add_system_transition(State.ROMAN3_sex, State.ROMAN4, r'[!"Hmmm...this is a really hard one haha. A healthy relationship comes with satisfying sex right? If I were you, I would talk to your"$RF"about this so maybe we can resolve this issue together. Just curious, are you currently in quarantine?"]')
df.add_user_transition(State.ROMAN4, State.ROMAN4_yes, r'<[!#ONT(ontyes)]>')
df.add_user_transition(State.ROMAN4, State.ROMAN4_no, r'<[!#ONT(ontno)]>')

df.add_system_transition(State.ROMAN4_yes, State.ROMAN5, r'[!"Same! I am so bored and anxious while in quarantine. There are only three things in my life now, sleep, eat, and zoom. How about you? What activity do you like to do during quarantine?"]')
df.add_system_transition(State.ROMAN4_no, State.ROMAN5, r'[!"I am so jealous of you! You must be staying in a very safe country. I am so bored and anxious while in quarantine, what activity would you do if you were me?"]')

###ROMAN ERROR###
df.set_error_successor(State.ROMAN0, State.ROMAN0_ERR)
df.set_error_successor(State.ROMAN1, State.ROMAN1_ERR)
df.set_error_successor(State.ROMAN2, State.ROMAN2_ERR)
df.set_error_successor(State.ROMAN3, State.ROMAN3_ERR)
df.set_error_successor(State.ROMAN4, State.ROMAN4_ERR)
df.add_system_transition(State.ROMAN0_ERR, State.ROMAN1,
                         r'[!"I think this is totally normal! Even the happiest and healthiest relationship is sometimes stressful. How long have you guys been together?"]')
df.add_system_transition(State.ROMAN1_ERR, State.ROMAN2, r'[!"Thats nice! Guess you guys are in a more steady phase. Is this stress caused by coronavirus?]')
df.add_system_transition(State.ROMAN2_ERR, State.ROMAN3,
                         r'[!"Glad coronavirus is not affecting your relationship. Whats wrong with you and your"$RF"then?"]')
df.add_system_transition(State.ROMAN3_ERR, State.ROMAN4, r'[!"That sounds pretty stressful to me... Sorry I do not really know how to deal with this situation. Lets talk about other things, are you currently in quarantine?"]')
df.add_system_transition(State.ROMAN4_ERR, State.ROMAN5, r'[!"Same! I am so bored and anxious while in quarantine. There are only three things in my life now, sleep, eat, and zoom. How about you? What activity do you like to do during quarantine?"]')

'''Covid-19 Branch'''
df.add_user_transition(State.COVID0, State.COVID0_yes, r'<[!#ONT(ontyes)]>')
df.add_user_transition(State.COVID0, State.COVID0_no, r'<[!#ONT(ontno)]>')

df.add_system_transition(State.COVID0_yes, State.COVID1, r'[!"It is nice to still be able to see each other! I think everyone must be super stressed under this chaotic situation... I really hope this crisis ends soon so our lives can get back to normal.  Honestly, I think doing things together might reduce some of your stress. What activity do you like to do during quarantine?"]')
df.add_system_transition(State.COVID0_no, State.COVID1, r'[!"Oh...I am guessing this stress is coming from the fact that you cannot see each other. I sometimes videocall my friend and my family when I miss them. It is a lot to handle when away from everyone, you are not alone. Doing some fun activities might help you relax! What activity do you like to do during quarantine?"]')

df.add_user_transition(State.COVID1, State.COVID1_game, r'<[!#ONT(ontgames)]>')
df.add_user_transition(State.COVID1, State.COVID1_food, r'<[!#ONT(ontfood)]>')
df.add_user_transition(State.COVID1, State.COVID1_video, r'<[!#ONT(ontreadwatch)]>')
df.add_user_transition(State.COVID1, State.COVID1_socialApp, r'<[!#ONT(ontsocialApp)]>')
df.add_user_transition(State.COVID1, State.COVID1_class, r'<[!#ONT(ontclass)]>')
df.add_user_transition(State.COVID1, State.COVID1_music, r'<[!#ONT(ontmusic)]>')
df.add_user_transition(State.FAM4, State.COVID1_game, r'<[!#ONT(ontgames)]>')
df.add_user_transition(State.FAM4, State.COVID1_food, r'<[!#ONT(ontfood)]>')
df.add_user_transition(State.FAM4, State.COVID1_video, r'<[!#ONT(ontreadwatch)]>')
df.add_user_transition(State.FAM4, State.COVID1_socialApp, r'<[!#ONT(ontsocialApp)]>')
df.add_user_transition(State.FAM4, State.COVID1_class, r'<[!#ONT(ontclass)]>')
df.add_user_transition(State.FAM4, State.COVID1_music, r'<[!#ONT(ontmusic)]>')

df.add_system_transition(State.COVID1_game, State.COVID2, r'[!"I do like to play games too! Playing games are so stress releiving. We should definetly play together sometimes! All of my friends are playing animal crossing, and they even skip the online lecture just to play it... Speaking of that, are you taking online classes?"]')
df.add_system_transition(State.COVID1_food, State.COVID2, r'[!"You are a foodie huh? I do not know why but I feel so happy while eating. Also, I think quarantine really improves my cooking skill. Cook, eat, sleep, taking online classes, that is bascially the summary of my life now haha. Are you also taking online classes?"]')
df.add_system_transition(State.COVID1_video, State.COVID2, r'[!"Same! I have been reading a lot of books and watching a lot of shows besides taking online classes. Are you also taking online classes?"]')
df.add_system_transition(State.COVID1_socialApp, State.COVID2, r'[!"Wow, even the coronavirus cannot stop you from socializing. I have not been texting with my friends a lot since school closed. Oh but I do see them on zoom haha. Are you also taking online classes?"]')
df.add_system_transition(State.COVID1_music, State.COVID2, r'[!"I am also a music person! Listening to music is so soothing right? I have been listening a lot of Lauv and Post Malone lately. I love listening to them while doing my homework. Are you also taking online classes?"]')
df.add_user_transition(State.COVID2, State.COVID2_yes, r'<[!#ONT(ontyes)]>')
df.add_user_transition(State.COVID2, State.COVID2_no, r'<[!#ONT(ontno)]>')

df.add_system_transition(State.COVID1_class, State.COVID3, r'[!"Oh really? I am taking online classes too! But I do not think taking online classes is a fun activity to do...How are you feeling about this transition to remote learning?"]')
df.add_system_transition(State.COVID2_yes, State.COVID3, r'[!"Nice! Feels so good to know someone is also suffering with me haha. How are you feeling about this transition to remote learning?"]')
df.add_user_transition(State.COVID3, State.COVID3_like, r'<{[!#ONT(ontlike)]}>')
df.add_user_transition(State.COVID3, State.COVID3_dislike, r'<{[!#ONT(ontdislike)]}>')

                ###ENDING TODO
df.add_system_transition(State.COVID2_no, State.COVIDEND, r'[!"I am so jealous of you! Taking online classes are just so awful. Well, I have class in 5 minutes so I have to leave. It was so nice talking to you. Have a nice day!"]')
df.add_system_transition(State.COVID3_like, State.COVIDEND, r'[!"Wow you are the minority! Most of the students do not adjust well with this sudden change of learning mode. I personally hate is so much because of the timezone difference. Well, I have class in 5 minutes so I have to leave. It was so nice talking to you. Have a nice day!"]')
df.add_system_transition(State.COVID3_dislike, State.COVIDEND, r'[!"Yeah right? I hate taking classes at 4 am... You should join the zoom memes page on facebook if you havent! Well, I have class in 5 minutes so I have to leave. It was so nice talking to you. Have a nice day!"]')

###COVID-19 ERROR###
df.set_error_successor(State.COVID0, State.COVID0_ERR)
df.set_error_successor(State.COVID1, State.COVID1_ERR)
df.set_error_successor(State.FAM4, State.FAM4_ERR)
df.set_error_successor(State.FRIEND4, State.FRIEND4_ERR)
df.set_error_successor(State.ROMAN5, State.ROMAN5_ERR)
df.set_error_successor(State.COVID2, State.COVID2_ERR)
df.set_error_successor(State.COVID3, State.COVID3_ERR)   #TODO
df.add_system_transition(State.COVID0_ERR, State.COVID1, r'[!"Oh...I am guessing this stress is coming from the fact that you cannot see each other. I sometimes videocall my friend and my family when I miss them. It is a lot to handle when away from everyone, you are not alone. Doing some fun activities might help you relax! What activity do you like to do during quarantine?"]')
df.add_system_transition(State.COVID1_ERR, State.COVID2, r'[!"That sounds super interesting! I should try that next time when I have less homework. I guess sleeping is my only destress activity... Oh by the way, are you also taking online classes?"]')
df.add_system_transition(State.FAM4_ERR, State.COVID2, r'[!"That sounds super interesting! I should try that next time when I have less homework. I guess sleeping is my only destress activity... Oh by the way, are you also taking online classes?"]')
df.add_system_transition(State.FRIEND4_ERR, State.COVID2, r'[!"That sounds super interesting! I should try that next time when I have less homework. I guess sleeping is my only destress activity... Oh by the way, are you also taking online classes?"]')
df.add_system_transition(State.ROMAN5_ERR, State.COVID2, r'[!"That sounds super interesting! I should try that next time when I have less homework. I guess sleeping is my only destress activity... Oh by the way, are you also taking online classes?"]')
df.add_system_transition(State.COVID2_ERR, State.COVID3, r'[!"Nice! Feels so good to know someone is also suffering with me haha. How are you feeling about this transition to remote learning?"]')
df.add_system_transition(State.COVID3_ERR, State.COVIDEND, r'[!"Yeah right? I hate taking classes at 4 am... You should join the zoom memes page on facebook if you havent! Well, I have class in 5 minutes so I have to leave. It was so nice talking to you. Have a nice day!"]')

if __name__ == '__main__':
    df.run(debugging=False)
