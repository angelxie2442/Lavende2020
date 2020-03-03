from emora_stdm import KnowledgeBase, DialogueFlow
from enum import Enum, auto


# TODO: Update the State enum as needed
class State(Enum):
    START = auto()
    PROMPT_STRESSOR = auto()
    SOCIAL0 = auto()
    SOCIAL1 = auto()
    SOCIAL2_yes = auto()
    SOCIAL2_no = auto()
    SOCIAL3 = auto()
    SOCIAL_feeling = auto()
    SOCIAL_feeling_cont = auto()
    SOCIAL_trauma = auto()
    SOCIAL_trauma_loc = auto()
    SOCIAL_trauma_loc_yes = auto()
    SOCIAL_trauma_loc_no = auto()
    SOCIAL_trauma_quit = auto()
    SOCIAL_topic = auto()
    SOCIAL_trauma_replay = auto()
    SOCIAL_trauma_quit_unsure = auto()
    SOCIAL_preparedness = auto()
    SOCIAL_prep_yes = auto()
    SOCIAL_prep_no = auto()
    SOCIAL_destress = auto()
    SOCIAL_destress_activity = auto()
    SOCIAL_activity = auto()
    SOCIAL_activity_comedy = auto()
    SOCIAL_suggest_comedy = auto()
    SOCIAL_suggest_no = auto()
    SOCIAL_suggest_yes = auto()
    SOCIAL_comedian = auto()
    SOCIAL_comedian_name = auto()
    SOCIAL_neuroticism = auto()
    SOCIAL_replay_yes = auto()
    SOCIAL_neurotic_yes = auto()
    SOCIAL_neurotic_no = auto()
    SOCIAL_subject = auto()
    SOCIAL_NARCI = auto()
    SOCIAL_NOT_NARCI = auto()
    SOCIAL_people = auto()
    SOCIAL_people_name = auto()
    SOCIAL_gain = auto()
    SOCIAL_value = auto()
    SOCIAL_comment = auto()
    SOCIAL_end = auto()
    GOOD_MOOD = auto()
    BAD_MOOD = auto()
    STRESSOR_ERR = auto()
    PROMPT_MOOD = auto()
    RELATIONSHIP = auto()
    PROMPT_WHO = auto()
    PROMPT_MOOD_ERR = auto()
    PROMPT_STRESSOR_ERR = auto()
    PROMPT_WHO_ERR = auto()
    Unknown_MOOD = auto()
    SOCIAL_prep_yes1 = auto()
    NAME = auto()
    FAMILY = auto()
    SOCIAL1_ERR = auto()
    YN_ERR = auto()
    MUST = auto()
    N_MUST = auto()
    MUST_GO = auto()
    N_MUST_GO = auto()
    SOCIAL_activity_ERR = auto()
    SOCIAL_suggest_comedy_ERR = auto()
    SOCIAL3_ERR = auto()
    SOCIAL_comedian_ERR = auto()
    SOCIAL_prep_yes2 = auto()
    SOCIAL_CONSCIENT_H = auto()
    SOCIAL_end_1 = auto()
    SOCIAL_CONSCIENT_L = auto()
    SOCIAL_neuroticism_ERR = auto()
    SOCIAL_people_ERR = auto()
    SOCIAL_gain_ERR = auto()
    SOCIAL_preparedness_ERR = auto()
    SOCIAL_prep = auto()
    ERR_STRESSOR_UNKNOWN = auto()


# TODO: create the ontology as needed
ontology = {
    "ontology": {
        "ontsocial":
            [
                "mixer",
                "dating",
                "dancing",
                "night out",
                "party"
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
             'unctuous'
             ]
    }
}

knowledge = KnowledgeBase()
knowledge.load_json(ontology)
df = DialogueFlow(State.START, initial_speaker=DialogueFlow.Speaker.SYSTEM, kb=knowledge)
'''
Angel's Part: Social stressor
'''
##Social Stressor Section
df.add_system_transition(State.START, State.PROMPT_MOOD, '"Hi there, how are you doing today?"')
df.set_error_successor(State.PROMPT_MOOD, State.PROMPT_MOOD_ERR)
df.add_system_transition(State.PROMPT_MOOD_ERR, State.PROMPT_STRESSOR, '"Umm...you know what? Recently, I am learning about stressful things. I will be happy if you can tell me something you are stressed about."')

df.add_user_transition(State.PROMPT_MOOD, State.GOOD_MOOD, "[$mood=#ONT(ontpositive)]")
df.add_user_transition(State.PROMPT_MOOD, State.BAD_MOOD, "[$mood=#ONT(ontnegative)]")

df.add_system_transition(State.GOOD_MOOD, State.PROMPT_STRESSOR,
                         r'[!"I am glad you are feeling"$mood"! Umm...you know what? Recently, I am learning about stressful things. I will be happy if you can tell me something you are stressed about."]')
df.add_system_transition(State.BAD_MOOD, State.PROMPT_STRESSOR,
                         r'[!"Ohh...I am sorry that you are feeling"$mood"... What are you stressed about?"]')


# df.add_system_transition(State.START, State.PROMPT_STRESSOR, '"What are you stressed about?"')
df.add_user_transition(State.PROMPT_STRESSOR, State.SOCIAL0, r'<$STRESSOR_SOCIAL=[!#ONT(ontsocial)]>')
df.add_system_transition(State.SOCIAL0, State.SOCIAL1, r'[! "Yeah..."$STRESSOR_SOCIAL"is often stressful. Do you always feel stressed about it?"]')

###Yes_No_Error
df.set_error_successor(State.SOCIAL1, State.YN_ERR)
df.add_system_transition(State.YN_ERR, State.SOCIAL2_yes, '"Umm...is that a yes?"')

####has had previous bad social event experience
df.add_user_transition(State.SOCIAL1, State.SOCIAL2_yes, r'<[!#ONT(ontyes)]>')
df.add_system_transition(State.SOCIAL2_yes, State.SOCIAL3, '"Just out of curiosity, where did it happen last time?"')

###Error
df.set_error_successor(State.SOCIAL3, State.SOCIAL3_ERR)
df.add_system_transition(State.SOCIAL3_ERR, State.SOCIAL_trauma_quit, r'[!"I mean you dont have to go to the"$STRESSOR_SOCIAL"if its making you uncomfortable. Do you have the option to not go?"]')

df.add_user_transition(State.SOCIAL3, State.SOCIAL_trauma,'[$trauma_loc=#POS(noun)]')
df.add_system_transition(State.SOCIAL_trauma, State.SOCIAL_trauma_loc, '[!"Is it happening again at"$trauma_loc"?"]')

###Yes_No_Error
df.set_error_successor(State.SOCIAL1, State.YN_ERR)
df.add_system_transition(State.YN_ERR, State.SOCIAL_trauma_loc, '"Umm...is that a yes?"')

######previous bad experience takes place in same setting
df.add_user_transition(State.SOCIAL_trauma_loc, State.SOCIAL_trauma_loc_yes,r'<[!#ONT(ontyes)]>')
df.add_system_transition(State.SOCIAL_trauma_loc_yes, State.SOCIAL_trauma_quit, r'[!"I mean you dont have to go to the"$STRESSOR_SOCIAL"if its making you uncomfortable. Do you have the option to not go?"]')

###Yes_No_Error
df.set_error_successor(State.SOCIAL_trauma_quit, State.YN_ERR)
df.add_system_transition(State.YN_ERR, State.SOCIAL_trauma_quit, '"Umm...is that a yes?"')

df.add_user_transition(State.SOCIAL_trauma_quit, State.N_MUST, r'<[!#ONT(ontyes)]>')
df.add_user_transition(State.SOCIAL_trauma_quit, State.MUST, r'<[!#ONT(ontno)]>')

df.add_system_transition(State.MUST, State.SOCIAL_activity, '"Ohh...Im so sorry you have to go through this, but I have faith in you! After all that, you should do something to relieve the stress. What activity do you like to do?"')
df.add_system_transition(State.N_MUST, State.SOCIAL_activity, '"Exactly! Lets skip the stressful part and straight to the fun part. What do you like to do to relieve your stress?"')

###ERR
df.set_error_successor(State.SOCIAL_activity, State.SOCIAL_activity_ERR)
df.add_system_transition(State.SOCIAL_activity_ERR, State.SOCIAL_suggest_comedy, '"That sounds so interesting! I should try that next time. My strategy to cope with stress is...watch comedy! Do you like to watch comedy?"')

# df.add_user_transition(State.SOCIAL_trauma_quit,State.SOCIAL_destress,r'/[A-Z a-z]+/')
# df.add_system_transition(State.SOCIAL_destress,State.SOCIAL_destress_activity,r'[!"What do you plan to do to help you de-stress?"]')

df.add_user_transition(State.SOCIAL_destress_activity, State.SOCIAL_activity,r'<[$activity=#POS(noun,verb)]>')
df.add_system_transition(State.SOCIAL_activity,State.SOCIAL_suggest_comedy, r'[! $activity "sounds very stress relieving. Peronally I likes to watch comedies. Do you like comedy?"]')


########comedies
df.add_user_transition(State.SOCIAL_suggest_comedy, State.SOCIAL_suggest_yes,r'<[!#ONT(ontyes)]>')
df.add_system_transition(State.SOCIAL_suggest_yes,State.SOCIAL_comedian,'"Charlie Chaplin is my all-time favorite! I can laugh whole day just by looking at his face. How about you, whos your favorite comedian?"')

###ERR
df.set_error_successor(State.SOCIAL_comedian, State.SOCIAL_comedian_ERR)
df.add_system_transition(State.SOCIAL_comedian_ERR, State.SOCIAL_end, '"Well you know even comedians like them often feel stressed! So dont worry to much about feeling stressed in social situations!"')

df.add_user_transition(State.SOCIAL_suggest_comedy, State.SOCIAL_suggest_no,r'<[!#ONT(ontno)]>')
df.add_system_transition(State.SOCIAL_suggest_no,State.SOCIAL_end,r'[!"I see. Well. I hope talking to me make you feel better. Feel free to reach out to me again whenever you want to talk."]')
# df.add_system_transition(State.SOCIAL_activity_comedy,State.SOCIAL_comedian,r'[!"I love watching comedies. Who is your favorite comedian?"]')
df.add_user_transition(State.SOCIAL_comedian,State.SOCIAL_comedian_name,'[$comedian=#NER(person)]')
df.add_system_transition(State.SOCIAL_comedian_name,State.SOCIAL_end,r'[!"Well you know even" $comedian "sometimes feel stressed and embarassed in social situations just like us, so dont let it bother you too much!"]')

######previous bad experience takes place in different setting
df.add_user_transition(State.SOCIAL_trauma_loc, State.SOCIAL_trauma_loc_no,r'<[!#ONT(ontno)]>')
df.add_system_transition(State.SOCIAL_trauma_loc_no, State.SOCIAL_trauma_replay, '[!"That is good."$STRESSOR_SOCIAL"might not be that stressful in differnt environment. Do you think this time will still be stressful?"]')
#########sometimes replay traumatic experience in mind
df.add_user_transition(State.SOCIAL_trauma_replay, State.SOCIAL_replay_yes, r'<[!#ONT(ontyes)]>')
df.add_system_transition(State.SOCIAL_replay_yes,State.SOCIAL_neuroticism,r'[!"Umm...you never know! By the way, do you also feel stressed about other social situations?"]')

###########high neuroticism
df.add_user_transition(State.SOCIAL_neuroticism, State.SOCIAL_neurotic_yes,r'<[!#ONT(ontyes)]>')
df.add_system_transition(State.SOCIAL_neurotic_yes, State.SOCIAL_end, '"I am so proud of you! You keep challenging yourself to be at stressful situation. I hope I can be like you some day...Have fun at"$STRESSOR_SOCIAL"! Let me know how it goes!"')
###########low neuroticism
df.add_user_transition(State.SOCIAL_neuroticism, State.SOCIAL_neurotic_no,r'<[!#ONT(ontno)]>')
df.add_system_transition(State.SOCIAL_neurotic_no,State.SOCIAL_people,r'[!"Is there anyone you know that is going to be at the"$STRESSOR_SOCIAL"?"]')

###ERR
df.set_error_successor(State.SOCIAL_people, State.SOCIAL_people_ERR)
df.add_system_transition(State.SOCIAL_people_ERR, State.SOCIAL_end, '"I can tell that you are a very social person. I am sure everyone will be happy to see you"')

df.add_user_transition(State.SOCIAL_people,State.SOCIAL_people_name,'[$social_people=#POS(person)]')
df.add_system_transition(State.SOCIAL_people_name,State.SOCIAL_end,r'[!"I can tell that you are a very social person. I am sure "$social_people" will be happy to see you at" $Social_Stressor"."]')
########do not replay traumatic experience in mind
df.add_user_transition(State.SOCIAL_trauma_replay, State.SOCIAL_topic, r'<[!#ONT(ontno)]>')

######preparedness(conscientiousness)
df.add_system_transition(State.SOCIAL_topic, State.SOCIAL_preparedness,r'[!"Have you thought about some topics you can say at"$STRESSOR_SOCIAL"?"]')

########prepared/planned(likely high conscientiousness)
df.add_user_transition(State.SOCIAL_preparedness, State.SOCIAL_prep_yes,r'<[!#ONT(ontyes)]>')
df.add_system_transition(State.SOCIAL_prep_yes, State.SOCIAL_prep_yes1, '"What topic are you thinking?"')
df.add_user_transition(State.SOCIAL_prep_yes1, State.SOCIAL_prep_yes2, '[$subject=#POS(noun)]')
df.add_system_transition(State.SOCIAL_prep_yes2, State.SOCIAL_activity,r'[!"You know" $subject "sounds really interesting to me! You should probably take a break from thinking about" $STRESSOR_SOCIAL ". What is your go-to destress activity besides talking to me?"]')

########unprepared(likely low conscientiousness)
df.set_error_successor(State.SOCIAL_preparedness, State.SOCIAL_prep_no)
df.add_system_transition(State.SOCIAL_prep_no, State.SOCIAL_end, r'[!"Are you not worried...? Otherwise you must be a natural talker. I really admire that."]')

####no previous bad social event experience
df.set_error_successor(State.SOCIAL1, State.SOCIAL2_no)
df.add_system_transition(State.SOCIAL2_no, State.SOCIAL3, r'[!"Besides stressed or anxious, what else do you feel about this upcoming" $STRESSOR_SOCIAL"?"]')
df.add_user_transition(State.SOCIAL3, State.SOCIAL_feeling,'[$feeling=#POS(adj)]')
df.add_system_transition(State.SOCIAL_feeling,State.SOCIAL_feeling_cont,r'[!"I usually feel" $feeling "about"$STRESSOR_SOCIAL"too. You know what, sometimes I really enjoy people focus on me. Yeah like Ariana HAHA. Do you sometimes feel that too?"]')
######high narci tendency
df.add_user_transition(State.SOCIAL_feeling_cont,State.SOCIAL_NARCI,r'[!#ONT(ontyes)]')
df.add_system_transition(State.SOCIAL_NARCI, State.SOCIAL_prep_yes, r'[!"Wow. It is likely that we are pretty similar type of people. Do you feel ready and prepared for" $STRESSOR_SOCIAL"?"]')
df.add_user_transition(State.SOCIAL_prep_yes,State.SOCIAL_CONSCIENT_H,r'[!#ONT(ontyes)]')
df.add_user_transition(State.SOCIAL_prep_yes,State.SOCIAL_CONSCIENT_L,r'[!#ONT(ontno)]')

df.add_system_transition(State.SOCIAL_CONSCIENT_H, State.SOCIAL_end, '"Then there is nothing to worry about, just do it! Come back and let me know the good news!"')
df.add_system_transition(State.SOCIAL_CONSCIENT_L, State.SOCIAL_end, '"Haha sometimes the best plan is no plan. Come back and let me know the good news!"')

######low narci tendency
df.set_error_successor(State.SOCIAL_feeling_cont, State.SOCIAL_NOT_NARCI)
df.add_system_transition(State.SOCIAL_NOT_NARCI, State.SOCIAL_gain, r'[!"What do you hope to get out of your experience at this upcoming" $STRESSOR_SOCIAL"then?"]')

### ERR
df.set_error_successor(State.SOCIAL_gain, State.SOCIAL_gain_ERR)
df.add_system_transition(State.SOCIAL_gain_ERR, State.SOCIAL_end, '"Yes, you have a really good point! I hope that one day I can be as thoughtful as you"')
df.add_user_transition(State.SOCIAL_gain,State.SOCIAL_value,'[$social_value={#POS(verb,noun)}]')
df.add_system_transition(State.SOCIAL_value,State.SOCIAL_end,r'[!"I see. It is amazing that you like to" $valued_thing ". Self-development is important. I hope you meet some quality people that will benefit your self-development at"$Social_Stressor"."]')
##

###Stressor Prompt Error Section
df.add_system_transition(State.ERR_STRESSOR_UNKNOWN, State.PROMPT_STRESSOR, r'[! Sorry. I am not familiar with that situation. Tell some something else that you find stressful.]')
df.set_error_successor(State.PROMPT_STRESSOR, State.ERR_STRESSOR_UNKNOWN)

'''
Nelson's Part: Relationship stressor
'''
# df.add_system_transition(State.START, State.PROMPT_STRESSOR, '"Hi there, how are you doing today?"')
# df.set_error_successor(State.PROMPT_STRESSOR, State.PROMPT_STRESSOR_ERR)
#
# df.add_user_transition(State.PROMPT_STRESSOR, State.GOOD_MOOD, "[$mood=#ONT(ontpositive)]")
# df.add_user_transition(State.PROMPT_STRESSOR, State.BAD_MOOD, "[$mood=#ONT(ontnegative)]")
#
# df.add_system_transition(State.GOOD_MOOD, State.PROMPT_MOOD,
#                          r'[!"I am glad you are feeling"$mood"! Is it because of your friends or family?"]')
# df.add_system_transition(State.BAD_MOOD, State.PROMPT_MOOD,
#                          r'[!"Ohh...I am sorry that you are feeling"$mood"... Is it about your relationship?"]')
# df.set_error_successor(State.PROMPT_MOOD, State.PROMPT_MOOD_ERR)
#
# # Transition to relationship
# df.add_user_transition(State.PROMPT_MOOD, State.RELATIONSHIP, "[#ONT(ontyes)]")
#
# df.add_system_transition(State.RELATIONSHIP, State.PROMPT_WHO, '"I hope you dont mind me asking who is that person?"')
# df.set_error_successor(State.PROMPT_WHO, State.PROMPT_WHO_ERR)
#
# df.add_user_transition(State.PROMPT_WHO, State.NAME, '[{$name=#NER(person)}]')
# df.add_user_transition(State.PROMPT_WHO, State.FAMILY, '[$family=#ONT(ontfamily)]')


if __name__ == '__main__':
    df.run(debugging=False)
