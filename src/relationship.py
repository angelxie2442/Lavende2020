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
    COVID = auto()
    FAM2 = auto()
    FAM2_ERR = auto()
    FAM2_abuse = auto()
    FAM3 = auto()
    FAM3_ERR = auto()


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
             'neglecting'
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

df.add_system_transition(State.FAM1_yes, State.COVID,
                         r'[!"Yeah...coronavirus is really messing up out lives in every aspect, you are not the only who suffer from it. Are you currently quarantine together with your"$F_M"?"]')
df.add_system_transition(State.FAM1_no, State.FAM2,
                         r'[!"At least you have one less thing to worry about. Guess what, my mom is so worried about getting coronavirus, she literally refuses to talk to anyone in within 3 steps... Whats wrong with you and your"$F_M"then?"]')
df.add_user_transition(State.FAM2, State.FAM2_abuse, r'[!#ONT(ontabuse)]')

df.add_system_transition(State.FAM2_abuse, State.FAM3, r'[! Oh...I am so sorry...It must be very hard for you, I wish I could actually do something for you besides just talking like this. You should definetly seek help from other people that can handle this situation better. ]')

###Family ERROR###
df.set_error_successor(State.FAM0, State.FAM0_ERR)
df.set_error_successor(State.FAM1, State.FAM1_ERR)
df.set_error_successor(State.FAM2, State.FAM2_ERR)
df.set_error_successor(State.FAM3, State.FAM3_ERR)

'''Covid-19 Branch'''

if __name__ == '__main__':
    df.run(debugging=False)
