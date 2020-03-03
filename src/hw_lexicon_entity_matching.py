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
    NAME = auto()
    FAMILY = auto()
    SOCIAL1_ERR = auto()
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
                "i think so"
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
             'unctuous'],
        'ontfamily':
            ['father',
             'mother',
             'parents',
             'son',
             'daughter',
             'child',
             'children',
             'offspring',
             'brother',
             'sister',
             'sibling',
             'siblings',
             'twins',
             'twin brothers',
             'twin brother',
             'twin sisters',
             'twin sister',
             'younger brother',
             'kid brother',
             'older sister',
             'elder sister',
             'husband',
             'wife',
             'grandfather',
             'grandmother',
             'granny',
             'grandparents',
             'grandson',
             'granddaughter',
             'grandchild',
             'grandchildren',
             'great-grandfather',
             'great-grandmother',
             'great-grandchild',
             'uncle',
             'aunt',
             'nephew',
             'niece',
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
df.add_system_transition(State.START, State.PROMPT_STRESSOR, '"What are you stressed about?"')
df.add_user_transition(State.PROMPT_STRESSOR, State.SOCIAL0, r'<$STRESSOR_SOCIAL=[!#ONT(ontsocial)]>')
df.add_system_transition(State.SOCIAL0, State.SOCIAL1, r'[! "Have you had a bad experience of"$STRESSOR_SOCIAL "before?"]')
#Error
df.set_error_successor(State.SOCIAL1, State.SOCIAL1_ERR)
df.add_system_transition(State.SOCIAL1_ERR, State.SOCIAL1, '"Umm...is that a yes?"')

####has had previous bad social event experience
df.add_user_transition(State.SOCIAL1, State.SOCIAL2_yes, r'<[!#ONT(ontyes)]>')
df.add_system_transition(State.SOCIAL2_yes, State.SOCIAL3, r'[! "Where did your previous bad experience of"$STRESSOR_SOCIAL"take place?"]')
df.add_user_transition(State.SOCIAL3, State.SOCIAL_trauma,'[$trauma_loc=#POS(noun)]') #Does not work
df.add_system_transition(State.SOCIAL_trauma, State.SOCIAL_trauma_loc, '[!"Is this" $STRESSOR_SOCIAL "that you are stressed about also taking place at somewhere similar to" $trauma_loc"?"]')

######previous bad experience takes place in same setting
df.add_user_transition(State.SOCIAL_trauma_loc, State.SOCIAL_trauma_loc_yes,r'<[!#ONT(ontyes)]>')
df.add_system_transition(State.SOCIAL_trauma_loc_yes, State.SOCIAL_trauma_quit, r'[!"That must be so hard for you. I would probably end up not going to the"$STRESSOR_SOCIAL" if I were you."]')
df.add_user_transition(State.SOCIAL_trauma_quit,State.SOCIAL_destress,r'/[A-Z a-z]+/')
df.add_system_transition(State.SOCIAL_destress,State.SOCIAL_destress_activity,r'[!What do you plan to do to help you de-stress?]')
df.add_user_transition(State.SOCIAL_destress_activity, State.SOCIAL_activity,r'<[$activity=#POS(noun,verb)]>')
df.add_system_transition(State.SOCIAL_activity,State.SOCIAL_suggest_comedy, r'[!"To" $activity "sounds effective. Peronally I likes to watch comedies. Do you likes comedies?"]')
########comedies
df.add_user_transition(State.SOCIAL_suggest_comedy, State.SOCIAL_suggest_yes,r'<[!#ONT(ontyes)]>')
df.add_system_transition(State.SOCIAL_suggest_yes,State.SOCIAL_comedian,r'<[!"Who is your favorite comedian?"]>')
df.add_user_transition(State.SOCIAL_suggest_comedy, State.SOCIAL_suggest_no,r'<[!#ONT(ontno)]>')
df.add_system_transition(State.SOCIAL_suggest_no,State.SOCIAL_end,r'<[!"I see. Well. I hope our talk made you feel better. Feel free to reach out to me again whenever you want to talk."]>')
df.add_system_transition(State.SOCIAL_activity_comedy,State.SOCIAL_comedian,r'[!"I love watching comedies. Who is your favorite comedian?"]')
df.add_user_transition(State.SOCIAL_comedian,State.SOCIAL_comedian_name,'[$comedian=#NER(person)]')
df.add_system_transition(State.SOCIAL_comedian_name,State.SOCIAL_end,r'[!"Well you know even" $comedian "experience failure and feel embarassed in social situations sometimes just like us."]')

######previous bad experience takes place in different setting
df.add_user_transition(State.SOCIAL_trauma_loc, State.SOCIAL_trauma_loc_no,r'<[!#ONT(ontno)]>')
df.add_system_transition(State.SOCIAL_trauma_loc_no, State.SOCIAL_trauma_replay, '[!"That is good. Do you still replay that experience in your mind sometimes?"]')
#########sometimes replay traumatic experience in mind
df.add_user_transition(State.SOCIAL_trauma_replay, State.SOCIAL_replay_yes, r'<[!#ONT(ontyes)]>')
df.add_system_transition(State.SOCIAL_replay_yes,State.SOCIAL_neuroticism,r'[!"Sorry to hear that. Do you often feel stressed about other social situations?"]')
###########high neuroticism
df.add_user_transition(State.SOCIAL_neuroticism, State.SOCIAL_neurotic_yes,r'<[!#ONT(ontyes)]>')
df.add_system_transition(State.SOCIAL_neurotic_yes,State.SOCIAL_end, r'[!"The way you are pushing yourself to get over your trauma by going to $Social_Stressor is amazing. Have fun at $Social_Stressor. Let me know how it goes!"]')
###########low neuroticism
df.add_user_transition(State.SOCIAL_neuroticism, State.SOCIAL_neurotic_no,r'<[!#ONT(ontno)]>')
df.add_system_transition(State.SOCIAL_neurotic_no,State.SOCIAL_people,r'[Is there anyone you know that is going to be at the"$STRESSOR_SOCIAL"?"]')
df.add_user_transition(State.SOCIAL_people,State.SOCIAL_people_name,'[$social_people=#POS(noun)]')
df.add_user_transition(State.SOCIAL_people_name,State.SOCIAL_end,r'[!"I can tell that you are a very social person. I am sure $people will be happy to see you at" $Social_Stressor"."]')
########do not replay traumatic experience in mind
df.add_user_transition(State.SOCIAL_trauma_replay, State.SOCIAL_topic, r'<[!#ONT(ontno)]>')

######preparedness(conscientiousness)
df.add_system_transition(State.SOCIAL_topic, State.SOCIAL_preparedness,r'[!"So have you planned out a few topics to talk about at"$STRESSOR_SOCIAL"?"]')
########prepared/planned(likely high conscientiousness)
df.add_user_transition(State.SOCIAL_preparedness, State.SOCIAL_prep_yes,r'<[!#ONT(ontyes)],[$subject=#POS(noun)]>')
df.add_system_transition(State.SOCIAL_prep_yes, State.SOCIAL_subject,r'[!"You know" $subject "sounds really interesting to me! You should probably take a break from thinking about" $STRESSOR_SOCIAL ". What is your go-to destress activity besides talking to me?"]')

########unprepared(likely low conscientiousness)
df.set_error_successor(State.SOCIAL_preparedness, State.SOCIAL_prep_no)
df.add_system_transition(State.SOCIAL_prep_no, State.SOCIAL_end, r'[!"Haha are you procrastinating? Otherwise you must be a natural talker. I really admire that."]')

####no previous bad social event experience
df.set_error_successor(State.SOCIAL1, State.SOCIAL2_no)
df.add_system_transition(State.SOCIAL2_no, State.SOCIAL3, r'[!"Besides stressed or anxious, how else do you feel about this upcoming" $STRESSOR_SOCIAL "?"]')
df.add_user_transition(State.SOCIAL3, State.SOCIAL_feeling,'[$feeling=#POS(adj)]')
df.add_system_transition(State.SOCIAL_feeling,State.SOCIAL_feeling_cont,r'[!"I usually feel" $feeling "about"$STRESSOR_SOCIAL"too. And I enjoy getting people\'s attention and approval when I talk. Are you like that too?"]')
######high narci tendency
df.add_user_transition(State.SOCIAL_feeling_cont,State.SOCIAL_NARCI,r'[!#ONT(ontyes)]')
df.add_system_transition(State.SOCIAL_NARCI, State.SOCIAL_people, r'[!"Wow.It is likely that we are pretty similar type of people."]')
df.add_user_transition(State.SOCIAL_people,State.SOCIAL_topic,r'/[A-Z a-z]+/')

######low narci tendency
df.set_error_successor(State.SOCIAL_feeling_cont, State.SOCIAL_NOT_NARCI)
df.add_system_transition(State.SOCIAL_NOT_NARCI, State.SOCIAL_gain, r'[!"What do you hope to get out of your experience at this upcoming" $STRESSOR_SOCIAL"then?"]')
df.add_user_transition(State.SOCIAL_gain,State.SOCIAL_value,'[$social_value=#POS(verb,noun)]')
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
# df.add_user_transition(State.PROMPT_STRESSOR, State.GOOD_MOOD, "[{$mood=#ONT(ontpositive)}]")
# df.add_user_transition(State.PROMPT_STRESSOR, State.BAD_MOOD, "[{$mood=#ONT(ontnegative)}]")
# 
# df.add_system_transition(State.GOOD_MOOD, State.PROMPT_MOOD,
#                          r'[!I am glad you are feeling $mood"!" Is it because of your friends or family"?"]')
# df.add_system_transition(State.BAD_MOOD, State.PROMPT_MOOD,
#                          r'[!Ohh...I am sorry that you are feeling "$mood"... Is it about your relationship"?"]')
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
