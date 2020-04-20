from emora_stdm import KnowledgeBase, DialogueFlow
from enum import Enum, auto
from emora_stdm import Macro


class n20(Macro):

    def run(self, ngrams, vars, args):
        positive = {
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
            'well', 'smooth', 'awesome',
            "not bad", "not too bad", "wasn't too bad",
            "wasn't bad", "isn't bad", "isn't too bad",
            "isn't very bad"
        }
        if 'neuroticsm' in vars.keys():
            vars['neuroticsm'] += 20
        else:
            vars['neuroticsm'] = 20
        return positive


class n_n20(Macro):

    def run(self, ngrams, vars, args):
        negative = {'afraid',
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
                    }
        if 'neuroticsm' in vars.keys():
            vars['neuroticsm'] -= 20
        else:
            vars['neuroticsm'] = -20
        return negative


class o40(Macro):

    def run(self, ngrams, vars, args):
        never = {
            "never",
            "never ever",
            "first time"
        }
        if 'openness' in vars.keys():
            vars['openness'] += 20
        else:
            vars['openness'] = 20
        return never


class n70(Macro):

    def run(self, ngrams, vars, args):
        often = {
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
        }
        if 'neuroticsm' in vars.keys():
            vars['neuroticsm'] += 70
        else:
            vars['neuroticsm'] = 70
        return often


class n40(Macro):

    def run(self, ngrams, vars, args):
        sometimes = {
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
            "annually",
            "every quarter",
            "every semester",
            "every year",
            "rarely",
            "hardly ever"
        }
        if 'neuroticsm' in vars.keys():
            vars['neuroticsm'] += 40
        else:
            vars['neuroticsm'] = 40
        return sometimes


class n10(Macro):

    def run(self, ngrams, vars, args):
        never = {
            "never",
            "never ever",
            "first time"
        }
        if 'neuroticsm' in vars.keys():
            vars['neuroticsm'] += 10
        else:
            vars['neuroticsm'] = 10
        return never


class o_n20(Macro):

    def run(self, ngrams, vars, args):
        yes = {
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
        }
        if 'openness' in vars.keys():
            vars['openness'] -= 20
        else:
            vars['openness'] = -20
        return yes


class o_20(Macro):

    def run(self, ngrams, vars, args):
        no = {
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
        }
        if 'openness' in vars.keys():
            vars['openness'] += 60
        else:
            vars['openness'] = 60
        return no


class o_20_1(Macro):

    def run(self, ngrams, vars, args):
        yes = {
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
        }
        if 'openness' in vars.keys():
            vars['openness'] += 60
        else:
            vars['openness'] = 60
        return yes


class o_n20_1(Macro):

    def run(self, ngrams, vars, args):
        no = {
            "no",
            "not really",
            "nope",
            "dont",
            "none",
            "No",
            "NO",
            "Nope",
            "nope",
            "Nah",
            "nah"
        }
        if 'openness' in vars.keys():
            vars['openness'] -= 20
        else:
            vars['openness'] = -20
        return no


class e80(Macro):

    def run(self, ngrams, vars, args):
        positive = {
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
            'well', 'smooth', 'awesome',
            "not bad", "not too bad", "wasn't too bad",
            "wasn't bad", "isn't bad", "isn't too bad",
            "isn't very bad", "happy"
        }
        if 'extroversion' in vars.keys():
            vars['extroversion'] = 80
        else:
            vars['extroversion'] = 80
        return positive


class e40(Macro):

    def run(self, ngrams, vars, args):
        negative = {
            'afraid',
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
        }
        if 'extroversion' in vars.keys():
            vars['extroversion'] = 40
        else:
            vars['extroversion'] = 40
        return negative


class printS(Macro):

    def run(self, ngrams, vars, args):
        if 'neuroticsm' not in vars.keys():
            vars['neuroticsm'] = 0
        if 'extroversion' not in vars.keys():
            vars['extroversion'] = 0
        if 'openness' not in vars.keys():
            vars['openness'] = 0
        score = "Neuroticism: " + str(vars['neuroticsm']) + " Openness: " + str(
            vars['openness']) + " Extroversion: " + str(vars['extroversion'])
        return score

class det_ss(Macro):
    def run(self, ngrams, vars, args):
        if str(vars['S_S']) == 'wedding' or str(vars['S_S']) == "wedding" or str(vars['S_S']) == "gathering" or str(vars['S_S']) == 'gathering' or str(vars['S_S']) == 'meeting' or str(vars['S_S'])=="meeting":
            return 'a '+str(vars['S_S'])
        elif str(vars['S_S'])[-3:] == 'ing' or str(vars['S_S'])[-3:] == "ing":
            return str(vars['S_S'])
        elif str(vars['S_S'])[0] == 'a' or str(vars['S_S'])[0] == "a" or str(vars['S_S'])[0] == 'e' or str(vars['S_S'])[0] == "e" or str(vars['S_S'])[0] == 'i' or str(vars['S_S'])[0] ==  "i" or str(vars['S_S'])[0] == 'o' or str(vars['S_S'])[0] == "o" or str(vars['S_S'])[0] == 'x' or str(vars['S_S'])[0] == "x":
            return 'an '+str(vars['S_S'])
        else:
            return 'a '+str(vars['S_S'])
class ool_or_eer(Macro):
    def run(self, ngrams, vars, args):
        if str(vars['S_S']) == "job search" or str(vars['S_S']) == "internship application" or str(vars['S_S']) == "job application":
            return 'in job application'
        elif str(vars['S_S']) == "internship" or str(vars['S_S']) == "job" or str(vars['S_S']) == "research":
            return 'in work'
        else:
            return 'in school'


class pron_reason(Macro):
    def run(self, ngrams, vars, args):
        i=0
        for i in range(len(str(vars['reason']))):
            if  str(vars['reason'])[i]=="i" or  str(vars['reason']) =='i' or  str(vars['reason'])=="I" or  str(vars['reason'])=='I':
                if i==0 and str(vars['reason'][1])==" ":
                    return str(vars['reason'])[i+1:]
                elif str(vars['reason'])[i-1]==" " and i==len(str(vars['reason']))-1:
                    return str(vars['reason'])[i+1:]
                elif str(vars['reason'][i-1:i+2])==" i " or str(vars['reason'][i-1:i+2])==" I ":
                    return str(vars['reason'])[i+1:]

        else:
            return str(vars['reason'])



class result(Macro):

    def run(self, ngrams, vars, args):
        if 'neuroticsm' not in vars.keys():
            vars['neuroticsm'] = 0
        if 'extroversion' not in vars.keys():
            vars['extroversion'] = 0

        if vars['neuroticsm'] > 50 and vars['extroversion'] > 50:
            return 'You have such a bubbly personality. I am sure you will succeed at anything you do. Let me know how it goes!'
        if vars['neuroticsm'] > 50 and vars['extroversion'] <= 50:
            return 'I think you are a bit sensitive to stress, but I know you love stepping out of your comfort zone a lot. I am sure people will love that side of you when they get to know you . Let me know how it goes!'
        if vars['neuroticsm'] <= 50 and vars['extroversion'] <= 50:
            return 'I feel so composed after talking to you. I am so lucky to meet you and learn about your perspective on things. Best of luck with '+ str(vars['S_S'])
        if vars['neuroticsm'] <= 50 and vars['extroversion'] > 50:
            return 'I know you will not only enjoy the upcoming '+ str(vars['S_S']) +' but also naturally help everyone else to have a great time at the upcoming '+ str(vars['S_S']) +'! Let me know how it goes!'



############################################### school macros start here

class help_ss(Macro):
    def run(self, ngrams, vars, args):
        for a_time_topic in ["time","workload","too much work","balance","schoolwork","balancing","duties","responsibilities","multitasks","multitasking","multitask"]:
            if str(vars['S_S']) == a_time_topic:
                return "time management"
        for a_general_topic in ["school","grades", "majors","internships","classes","majors","jobs","work","research"]:
            if str(vars['S_S'])== a_general_topic:
                return str(vars['S_S'])
        if str(vars['S_S']) == 'wedding' or str(vars['S_S']) == "wedding" or str(vars['S_S']) == "gathering" or str(vars['S_S']) == 'gathering' or str(vars['S_S']) == 'meeting' or str(vars['S_S'])=="meeting":
            return 'that '+str(vars['S_S'])
        elif str(vars['S_S']).find("ing ")!=-1:
            return str(vars['S_S'])
        elif str(vars['S_S'])[0] == 'a' or str(vars['S_S'])[0] == "a" or str(vars['S_S'])[0] == 'e' or str(vars['S_S'])[0] == "e" or str(vars['S_S'])[0] == 'i' or str(vars['S_S'])[0] ==  "i" or str(vars['S_S'])[0] == 'o' or str(vars['S_S'])[0] == "o" or str(vars['S_S'])[0] == 'x' or str(vars['S_S'])[0] == "x":
            return 'that '+str(vars['S_S'])
        else:
            return 'that '+str(vars['S_S'])

class school_n1_often(Macro):
    def run(self, ngrams, vars, args):
        if 'neuroticsm' in vars.keys():
            vars['neuroticsm'] += 40
        else:
            vars['neuroticsm'] = 40
        return ''
class school_n1_sometimes(Macro):
    def run(self, ngrams, vars, args):
        if 'neuroticsm' in vars.keys():
            vars['neuroticsm'] += 20
        else:
            vars['neuroticsm'] = 20
        return ''
class school_n1_never(Macro):
    def run(self, ngrams, vars, args):
        if 'neuroticsm' in vars.keys():
            vars['neuroticsm'] += 0
        else:
            vars['neuroticsm'] = 0
        return ''

class school_n2_often(Macro):
    def run(self, ngrams, vars, args):
        if 'neuroticsm' in vars.keys():
            vars['neuroticsm'] += 40
        else:
            vars['neuroticsm'] = 40
        return ''

class school_n2_sometimes(Macro):
    def run(self, ngrams, vars, args):
        if 'neuroticsm' in vars.keys():
            vars['neuroticsm'] += 20
        else:
            vars['neuroticsm'] = 20
        return ''
class school_n2_never(Macro):
    def run(self, ngrams, vars, args):
        if 'neuroticsm' in vars.keys():
            vars['neuroticsm'] -= 20
        else:
            vars['neuroticsm'] =-20
        return ''

class school_n3_well(Macro):

    def run(self, ngrams, vars, args):
        if 'neuroticsm' in vars.keys():
            vars['neuroticsm'] += 40
        else:
            vars['neuroticsm'] = 40
        return ''

class school_n3_bad(Macro):
    def run(self, ngrams, vars, args):
        if 'neuroticsm' in vars.keys():
            vars['neuroticsm'] += 20
        else:
            vars['neuroticsm'] = 20
        return ''

class school_n4_much(Macro):
    def run(self, ngrams, vars, args):
        if 'neuroticsm' in vars.keys():
            vars['neuroticsm'] += 40
        else:
            vars['neuroticsm'] = 40
        return ''

class school_n4_lil(Macro):

        def run(self, ngrams, vars, args):
            if 'neuroticsm' in vars.keys():
                vars['neuroticsm'] += 20
            else:
                vars['neuroticsm'] = 20
            return ''


class school_n_covidworried(Macro):

    def run(self, ngrams, vars, args):
        if 'neuroticsm' in vars.keys():
            vars['neuroticsm'] += 60
        else:
            vars['neuroticsm'] = 60
        return ''

class school_n_covidnotworr(Macro):

    def run(self, ngrams, vars, args):
        if 'neuroticsm' in vars.keys():
            vars['neuroticsm'] += 20
        else:
            vars['neuroticsm'] = 20
        return ''
class school_n_covidinfect(Macro):

    def run(self, ngrams, vars, args):
        if 'neuroticsm' in vars.keys():
            vars['neuroticsm'] += 60
        else:
            vars['neuroticsm'] = 60
        return ''

class school_e1_mentor1_person(Macro):

    def run(self, ngrams, vars, args):
        if 'extroversion' in vars.keys():
                vars['extroversion'] += 40
        else:
                vars['extroversion'] = 40
        return ''

class school_e1_mentor1_err(Macro):

    def run(self, ngrams, vars, args):
        if 'extroversion' in vars.keys():
                vars['extroversion'] += 20
        else:
                vars['extroversion'] = 20
        return ''
class school_e1_mentor2_yes(Macro):

    def run(self, ngrams, vars, args):
        if 'extroversion' in vars.keys():
            vars['extroversion'] += 20
        else:
            vars['extroversion'] = 20
        return ''
class school_e1_mentor2_no(Macro):

    def run(self, ngrams, vars, args):
        if 'extroversion' in vars.keys():
            vars['extroversion'] -= 20
        else:
            vars['extroversion'] =-20
        return ''

class school_e2_online1_like(Macro):
    def run(self, ngrams, vars, args):
        if 'extroversion' in vars.keys():
            vars['extroversion'] += 20
        else:
            vars['extroversion'] = 20
        return ''
class school_e2_online1_dislike(Macro):
    def run(self, ngrams, vars, args):
        if 'extroversion' in vars.keys():
            vars['extroversion'] += 40
        else:
            vars['extroversion'] = 40
        return ''
class school_e2_online2_hiprod(Macro):
    def run(self, ngrams, vars, args):
        if 'extroversion' in vars.keys():
            vars['extroversion'] -= 20
        else:
            vars['extroversion'] = -20
        return ''

class school_e2_online2_loprod(Macro):
    def run(self, ngrams, vars, args):
        if 'extroversion' in vars.keys():
            vars['extroversion'] += 20
        else:
            vars['extroversion'] = 20
        return ''
class school_e2_online2_socialstress(Macro):
    def run(self, ngrams, vars, args):
        if 'extroversion' in vars.keys():
            vars['extroversion'] -= 20
        else:
            vars['extroversion'] = -20
        return ''
class school_e2_online2_lesssocial(Macro):
    def run(self, ngrams, vars, args):
        if 'extroversion' in vars.keys():
            vars['extroversion'] += 20
        else:
            vars['extroversion'] = 20
        return ''
class school_e3_studyspot1_liv(Macro):
    def run(self, ngrams, vars, args):
        if 'extroversion' in vars.keys():
            vars['extroversion'] += 50
        else:
            vars['extroversion'] = 50
        return ''
class school_e3_studyspot1_bed(Macro):
    def run(self, ngrams, vars, args):
        if 'extroversion' in vars.keys():
            vars['extroversion'] += 20
        else:
            vars['extroversion'] = 20
        return ''

class school_e3_studyspot2_zoom(Macro):
    def run(self, ngrams, vars, args):
        if 'extroversion' in vars.keys():
            vars['extroversion'] += 40
        else:
            vars['extroversion'] = 40
        return ''
class school_e3_studyspot2_nozoom(Macro):
    def run(self, ngrams, vars, args):
        if 'extroversion' in vars.keys():
            vars['extroversion'] += 10
        else:
            vars['extroversion'] = 10
        return ''

############################################### school macros end here

class State(Enum):
    START = auto()
    PROMPT = auto()
    PROMPT_ERR = auto()
    BREAKUP = auto()
    ROMAN = auto()
    LOVE = auto()
    SINGLE = auto()
    BREAKUP0 = auto()
    BREAKUP0_ERR = auto()
    BREAKUP0_short = auto()
    BREAKUP0_mid = auto()
    BREAKUP0_long = auto()
    BREAKUP1 = auto()
    BREAKUP1_ERR = auto()
    LOVE0 = auto()
    LOVE0_ERR = auto()
    COVID = auto()
    BREAKUP1_0 = auto()
    BREAKUP2 = auto()
    BREAKUP2_ERR = auto()
    BREAKUP2_intimacy = auto()
    BREAKUP2_passion = auto()
    BREAKUP2_commitment = auto()
    BREAKUP3 = auto()
    BREAKUP3_ERR = auto()
    COVID0 = auto()
    COVID1 = auto()
    COVID1_ERR = auto()
    BREAKUP3_yes = auto()
    BREAKUP3_no = auto()
    BREAKUP4 = auto()
    BREAKUP4_ERR = auto()
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
    COVID0_yes = auto()
    COVID0_no = auto()
    COVID0_ERR = auto()
    SINGLE0_short = auto()
    SINGLE0_mid = auto()
    SINGLE0_long = auto()
    SINGLE0 = auto()
    SINGLE0_ERR = auto()
    SINGLE1 = auto()
    SINGLE1_ERR = auto()
    SINGLE1_often = auto()
    SINGLE1_sometimes = auto()
    SINGLE1_never = auto()
    SINGLE2 = auto()
    SINGLE2_ERR = auto()
    SINGLE2_yes = auto()
    SINGLE2_no = auto()
    SINGLE3 = auto()
    SINGLE3_ERR = auto()
    ROMAN0 = auto()
    ROMAN0_ERR = auto()
    ROMAN0_short = auto()
    ROMAN0_mid = auto()
    ROMAN0_long = auto()
    ROMAN1 = auto()
    ROMAN1_ERR = auto()
    ROMAN1_often = auto()
    ROMAN1_sometimes = auto()
    ROMAN1_never = auto()
    ROMAN2 = auto()
    ROMAN2_ERR = auto()
    ROMAN2_0 = auto()
    ROMAN3 = auto()
    ROMAN3_ERR = auto()
    ROMAN3_intimacy = auto()
    ROMAN3_passion = auto()
    ROMAN3_commitment = auto()
    ROMAN4 = auto()
    ROMAN4_ERR = auto()
    ROMAN4_yes = auto()
    ROMAN4_no = auto()
    ROMAN5 = auto()
    ROMAN5_ERR = auto()
    PROMPT0_savage = auto()
    PROMPT0_schoolevent_savage = auto()
    PROMPT0_schoolgeneral_savage = auto()
    PROMPT0_schooltime_savage = auto()
    PROMPT0_schoolcovid_savage = auto()
    PROMPT0_schoolevent_agg = auto()
    PROMPT0_schoolgeneral_agg = auto()
    PROMPT0_schooltime_agg = auto()
    PROMPT0_schoolcovid_agg= auto()
    PROMPT0_schoolevent_opt= auto()
    PROMPT0_schoolgeneral_opt = auto()
    PROMPT0_schooltime_opt = auto()
    PROMPT0_schoolcovid_opt = auto()
    PROMPT0_re1 = auto()
    PROMPT0_err1 = auto() #user is stressed about nothing/unsure
    PROMPT0_other1 = auto()
    PROMPT0_a1 =auto()
    PROMPT0_b1 =auto()
    PROMPT1_1 = auto()
    PROMPT1_often1 = auto()
    PROMPT1_sometimes1 = auto()
    PROMPT1_never1 = auto()
    PROMPT1_err1 = auto()
    PROMPT2_1 = auto()
    PROMPT2_notbad1 = auto()
    PROMPT2_bad1 = auto()
    PROMPT2_err1 = auto()
    PROMPT3_1 = auto()
    PROMPT3_often1 = auto()
    PROMPT3_sometimes1 = auto()
    PROMPT3_never1 = auto()
    PROMPT3_err1 = auto()
    PROMPT4_1 = auto()
    PROMPT4_yes1 = auto()
    PROMPT4_no1 = auto()
    PROMPT4_err1 = auto()
    PROMPT5_1 = auto()
    PROMPT5_yes1 = auto()
    PROMPT5_no1 = auto()
    PROMPT5_err1 = auto()
    PROMPT6_1 = auto()
    PROMPT6_re1 = auto()
    PROMPT6_re_ppl1 = auto()
    PROMPT6_other1 = auto()
    PROMPT6_err1 = auto()
    PROMPT7_1 = auto()
    PROMPT7_err1 = auto()
    PROMPT7_ex1 = auto()
    PROMPT7_in1 = auto()
    PROMPT8_1 = auto()
    PROMPT8_chores1 = auto()
    PROMPT8_games1 = auto()
    PROMPT8_music1 = auto()
    PROMPT8_art1 = auto()
    PROMPT8_food1 = auto()
    PROMPT8_sports1 = auto()
    PROMPT8_dance1 = auto()
    PROMPT8_shopping1 = auto()
    PROMPT8_readwatch1 = auto()
    PROMPT8_onlinesocial1 = auto()
    PROMPT8_social1 = auto()
    PROMPT8_err1 = auto()
    PROMPT9_1 = auto()
    END1 = auto()
    SCORE1 = auto() ####################
    PROMPT_oolstressfr1 = auto()##### 1: savage 2: aggreable 3:optimistic
    PROMPT_oolfreq1 =auto()
    PROMPT_oolpast1 = auto()
    PROMPT_oolgoal1 = auto()
    PROMPT_oolgoalalign1 = auto()
    PROMPT_oolcovidworry1 = auto()
    PROMPT_oolcovidworry_severity1= auto()
    PROMPT_oolonline1 =auto()
    PROMPT_oolonline_reasongood1 = auto()
    PROMPT_oolonline_reasonbad1 = auto()
    PROMPT_oolhelp_person1=auto()
    PROMPT_oolhelp_yesno1=auto()
    PROMPT_oolstudyspot1= auto()
    PROMPT_oolzoom1=auto()
    #####user error states
    PROMPT_oolstressfr_err1 = auto()
    PROMPT_oolfreq_err1 = auto()
    PROMPT_oolpast_err1 =auto()
    PROMPT_oolgoal_err1 = auto()
    PROMPT_oolgoalalign_err1 = auto()
    PROMPT_oolcovidworry_err1 = auto()
    PROMPT_oolonline_err1= auto()
    PROMPT_oolonline_dislike_err1 = auto()
    PROMPT_oolonline_like_err1 = auto()
    PROMPT_oolhelp_person_err1 = auto()
    PROMPT_oolhelp_yesno_err1 = auto()
    PROMPT_oolstudyspot_err1 = auto()
    PROMPT_oolzoom_err1 = auto()
    #####user states
    PROMPT_oolstressfr_often1 = auto()
    PROMPT_oolstressfr_sometimes1 = auto()
    PROMPT_oolstressfr_never1 = auto()
    PROMPT_oolfreq_often1 = auto()
    PROMPT_oolfreq_sometimes1 = auto()
    PROMPT_oolfreq_never1 = auto()
    PROMPT_oolpast_well1 = auto()
    PROMPT_oolpast_bad1 = auto()
    PROMPT_oolgoal_re1 = auto()
    PROMPT_oolgoalalign_yes1 = auto()
    PROMPT_oolgoalalign_no1 = auto()
    PROMPT_oolcovidworry_no1 = auto()
    PROMPT_oolcovidworry_infected1 = auto()
    PROMPT_oolcovidworry_severityre1 = auto()
    PROMPT_oolonline_well1 = auto()
    PROMPT_oolonline_bad1 = auto()
    PROMPT_oolonlinereason_prodgood1 =auto()
    PROMPT_oolonlinereason_socialgood1 = auto()
    PROMPT_oolonlinereason_flexgood1 = auto()
    PROMPT_oolonlinereason_prodbad1 =auto()
    PROMPT_oolonlinereason_socialbad1 = auto()
    PROMPT_oolonlinereason_flexbad1 = auto()
    PROMPT_oolhelp_person_re1=auto()
    PROMPT_oolhelp_yes1 = auto()
    PROMPT_oolhelp_no1 = auto()
    PROMPT_oolstudyspot_bedroom1 = auto()
    PROMPT_oolstudyspot_livingroom1 = auto()
    PROMPT_oolzoom_yes1 =auto()
    PROMPT_oolzoom_no1 = auto()
    #####user states


# TODO: create the ontology as needed
stress_dict = {
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
                    "party",
                    "hanging out",
                    "clubbing",
                    "dancing",
                    "performing"
                    "mixer",
                    "dating",
                    "debate",
                    "mock trial competition",
                    "trip",
                    "wedding",
                    "gathering",
                    "date",
                    "night out",
                    "nightout",
                    "party",
                    "hangouts",
                    "hangout",
                    "presentation",
                    "public speaking",
                    "social event",
                    "conversation",
                    "meeting",
                    "performance",
                    "piano performance",
                    "dance performance",
                    "theatre performance",
                    "ice cream social",
                    "icecream social",
                    "retreat",
                    "conversation",
                    "seminar",
                    "discussion",
                    "music festival",
                    "festival",
                    "carnival",
                    "dance",
                    "prom",
                    "semiformal",
                    "ice-cream social",
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
                    'well', 'smooth', 'awesome',
                    "not bad", "not too bad", "wasn't too bad",
                    "wasn't bad", "isn't bad", "isn't too bad",
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
                 'frustrating',
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
                 ],
            'ontextro':
                [
                    "meeting new people",
                    "leading a conversation",
                    "leading conversations",
                    "initiating a conversation",
                    "initiating conversations",
                    "making new friends",
                    "making friends",
                    "influencing others",
                    "changing other people's opinions",
                    "public speaking",
                    "sharing ideas",
                    "sharing",
                    "socializing",
                    "communicating with other people",
                    "the opportunity to socialize",
                    "networking",
                    "connecting with people",
                    "establishing connection with other people",
                    "connecting with other people",
                    "communicating",
                    "connecting with people",
                    "connecting with others",
                    "getting people's attention",
                    "getting people's approval",
                    "having people's attention",
                    "having people's approval",
                    "public speaking",
                    "making people laugh",
                    "entertaining people",
                    "entertaining others",
                    "entertaining other people",
                    "vibe",
                    "vibes"
                ],
            'ontintro':  ##probably enjoy talking in a more structured setting and enjoy things/experience/content
                [
                    "listening to others' ideas ",
                    "learning new things",
                    "enjoying myself",
                    "learning",
                    "participating in a conversation",
                    "expanding my horizon",
                    "getting to know people better",
                    "getting to know them better",
                    "getting to know other people better",
                    "games"
                    "listening to others",
                    "learning from others",
                    "learning from others' ideas",
                    "listening to speeches",
                    "listening to a speech",
                    "being with my friends",
                    "hanging out with my friends",
                    "spending time with my friends",
                    "bonding with people I know",
                    "hanging out with people I know",
                    "talking to my friends",
                    "getting to know my friends better",
                    "dancing",
                    "ice-skating",
                    "eating",
                    "drinking",
                    "singing",
                    "food",
                    "music",
                    "deep conversation",
                    "playing on my phone",
                    "internet surfing"
                ],
            'ontveryintro':
                [
                    "don't think I will enjoy",
                    "do not think I will enjoy",
                    "I will not enjoy",
                    "I won't enjoy",
                    "nothing",
                    "none",
                    "dont know",
                    "do not know",
                    "not sure",
                    "no ideas",
                    "no idea",
                    "no opinions",
                    "no opinion",
                    "no thoughts",
                    "no thought",
                    "no knowledge",
                    "not certain",
                    "dont really know",
                    "hard to say"
                ],
            'ontexternal':
                [
                    "dont have better things to do",
                    "do not have better things to do",
                    "dont have better plans",
                    "do not have better plans",
                    "have nothing to do",
                    "have nothing else to do",
                    "trying to find something to do",
                    "tryna find something to do",
                    "want to find something to do",
                    "want to kill time",
                    "wanna kill time",
                    "want to distract myself",
                    "wanna distract myself"
                ],
            'ontshopping':
                [
                    "go shopping online",
                    "go shopping",
                    "mall",
                    "malls",
                    "outlet",
                    "shop",
                    "buy",
                    "buying",
                    "purchase",
                    "purchasing"
                ],
            'ontchores':
                [
                    "washing dishes",
                    "folding clothes",
                    "laundry",
                    "cleaning",
                    "clean",
                    "organizing",
                    "doing chores",
                    "wiping",
                    "wipe",
                    "mopping",
                    "mop",
                    "vaccum"
                ],
            'ontgames':
                [
                    "video games",
                    "board games",
                    "game",
                    "video game",
                    "games",
                    "LOL",
                    "League of Legends",
                    "VR games",
                    "VR Games",
                    "Games",
                    "VR Game",
                    "Game",
                    "video games",
                    "games",
                    "LOL",
                    "League of Legends",
                    "league",
                    "VR games",
                    "VR Games",
                    "Games",
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
                    "ps4"
                ],
            'ontmusic':
                [
                    "listening to music",
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
            'ontsports':
                [
                    "basketball",
                    "run",
                    "running",
                    "cardio",
                    "working out",
                    "work-out",
                    "work out",
                    "tennis",
                    "football",
                    "soccer",
                    "swimming",
                    "table tennis",
                    "ping pong",
                    "cross country",
                    "crosscountry",
                    "xcountry",
                    "jog",
                    "jogging",
                    "ice hockey",
                    "hockey",
                    "field hockey",
                    "icehockey",
                    "ice hockey",
                    "field hockey",
                    "lacrosse",
                    "softball",
                    "baseball",
                    "badminton",
                    "sport",
                    "sports",
                    "exercise",
                    "fencing",
                    "wrestling",
                    "weight lifting",
                    "lifting"
                ],
            'ontdance':
                [
                    "dancing",
                    "choreographing",
                    "doing cover dances"
                ],
            'ontreadwatch':
                [
                    "books",
                    "TV",
                    "netflix",
                    "television",
                     "Netflix",
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
                ],
            'ontonlinesocial':
                [
                    "social media",
                    "facebook",
                    "twitter",
                    "instagram",
                    "ig",
                    "fb",
                    "tik tok",
                    "social media",
                    "Facebook",
                    "Twitter",
                    "Instagram",
                    "youtube",
                    "Youtube",
                    "snapchat",
                    "ig",
                    "fb",
                    "tik tok",
                    "Line",
                    "line",
                    "Kakao Talk",
                    "kakao",
                    "Messenger",
                    "messenger",
                    "WeChat",
                     "wechat"
                ],
            'ontart':
                [
                    "painting",
                    "watercolor",
                    "take photos",
                    "take pictures",
                    "art",
                    "arts",
                    "taking photos",
                    "photography",
                    "taking pictures",
                    "make films",
                    "making films",
                    "filming",
                    "draw",
                    "drawing",
                    "drawings",
                    "paint",
                    "do my nails",
                    "paint my nails",
                    "artsy",
                    "photoshop",
                    "album",
                     "illustrator",
                     "filter",
                    "lighting",
                    "shadow",
                    "pose",
                    "model"
                ],
            'ontschoolevent':
                [
                "group project",
                "project",
                "paper",
                "research paper",
                "assignment",
                "quiz",
                "exam",
                "class",
                "essay",
                "research"
                ],
            'ontschoolgeneral':
                [
                "school",
                "grades",
                "majors",
                "internships",
                "classes",
                "majors",
                "jobs",
                "work",
                "exams",
                "quizzes",
                "papers",
                "essays",
                "projects",
                "group projects"
                ],
            'ontschooltime':
                [
                "time",
                "workload",
                "too much work",
                "little time",
                "busy schedule",
                "tight schedule",
                "balance",
                "schoolwork",
                "balancing",
                "duties",
                "responsibilities",
                "multitasks",
                "multitasking",
                "multitask",
                "multiple assignments"
                ],
            'ontschoolcovid':
                [
                "covid19",
                "covid",
                "corona",
                "coronavirus",
                "health",
                "cough",
                "coughing",
                "fever",
                "sick",
                "coughs"
                ],
            'ontflexbad':
                [
                "self discipline",
                "self control",
                "too much freedom",
                "too flexible",
                "too much flexibility",
                "temptation",
                "too many options",
                "too many choices",
                "lazy",
                "laziness"
                ],
            'ontsocialbad':
                [
                "participation",
                "participate",
                "connection",
                "connect",
                "discussion",
                "discuss",
                "ask questions",
                "connected",
                "fake",
                "interaction",
                "learn less",
                "more written homework",
                "more written assignments",
                "more work",
                "boring",
                "lame",
                "sucks"
                ],
            'ontprodbad':
                [
                "concentrate",
                "cencentration",
                "focus",
                "motivation",
                "motivated",
                "not productive",
                "not as productive",
                "low productivity",
                "self control",
                "less motivated",
                "no longer feel motivated",
                ],
            'ontflexgood':
                [
                "sleepin",
                "sleep in",
                "schedule",
                "time",
                "flexibility",
                "flexible",
                "pace",
                "pacing",
                "choice",
                "choices",
                "option",
                "options",
                "convenienet",
                "saves time"
                ],
            'ontsocialgood':
                [
                "social stress",
                "less participation",
                "less discussion",
                "participate",
                "more comfortable participating",
                "more comfortable asking questions",
                "learn less"
                ],
            'ontprodgood':
                [
                "more effeciently",
                "effeciency",
                "productivity",
                "productive",
                "focus more",
                "focus better",
                "concentrate better",
                "focus better"
                ],
            'ontbedroom':
                [
                "bedroom",
                "study",
                "room"
                ],
            'ontlivingroom':
                [
                "dining area",
                "dining room",
                "kitchen",
                "living room",
                "livingroom",
                "garden",
                "backyard"
                ],
            'ontbreakup':
                [
                'breakup',
                'break up',
                'brokeup',
                'broke up',
                'dumped',
                'dump',
                'break',
                'breaks'
                ],
             'ontroman':
                [
                'love',
                'boyfriend',
                'girlfriend',
                'relationship'
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
                'professor'
                 ],

            'ontlike':
                ['not bad',
                 'not that bad',
                'not as bad',
                'i like it',
                'really like it',
                'good'
                'love'
                 ],
        }
}

knowledge = KnowledgeBase()
knowledge.load_json(stress_dict)
df = DialogueFlow(State.START, initial_speaker=DialogueFlow.Speaker.SYSTEM, kb=knowledge,
                  macros={'det_ss': det_ss(),"n20": n20(), "n_n20": n_n20(), 'o40': o40(), 'n70': n70(), 'n40': n40(), 'n10': n10(),
                          'o_n20': o_n20(), 'o_20': o_20(), 'o_20_1': o_20_1(), 'o_n20_1': o_n20_1(), 'e80': e80(),
                          'e40': e40(), 'pron_reason': pron_reason(), 'printS': printS(), 'result':result(),'school_n1_never':school_n1_never(),'school_n1_often':school_n1_often(),'school_n1_sometimes':school_n1_sometimes(),
                          'school_n2_often':school_n2_often(), 'school_n2_sometimes':school_n2_sometimes(), 'school_n2_never':school_n2_never(),
                          'school_n3_well':school_n3_well(),'school_n3_bad':school_n3_bad(),'school_n4_much':school_n4_much(),'school_n4_lil':school_n4_lil(),
                          'school_e3_studyspot1_liv':school_e3_studyspot1_liv(),'school_e3_studyspot1_bed':school_e3_studyspot1_bed(),
                          'school_e3_studyspot2_zoom':school_e3_studyspot2_zoom(),'school_e3_studyspot2_nozoom':school_e3_studyspot2_nozoom(),
                          'school_e2_online1_like':school_e2_online1_like(),'school_e2_online1_dislike':school_e2_online1_dislike(),
                          'school_e2_online2_hiprod':school_e2_online2_hiprod(),'school_e2_online2_socialstress':school_e2_online2_socialstress(),
                          'school_e2_online2_loprod': school_e2_online2_loprod(),'school_e2_online2_lesssocial': school_e2_online2_lesssocial(),
                          'school_e1_mentor1_person':school_e1_mentor1_person(),'school_e1_mentor1_err':school_e1_mentor1_err(),
                          'school_e1_mentor2_yes':school_e1_mentor2_yes(),'school_e1_mentor2_no':school_e1_mentor2_no(),
                          'school_n_covidworried':school_n_covidworried(),'school_n_covidinfect':school_n_covidinfect,'school_n_covidnotworr':school_n_covidnotworr,
                          'ool_or_eer':ool_or_eer(),'help_ss':help_ss()})
df.add_system_transition(State.START, State.PROMPT0_savage,r'[!"Hi! Tell me what you are stressed about."]')
df.add_user_transition(State.PROMPT0_savage, State.PROMPT0_re1, r'<$S_S=[!#ONT(ontsocial)]>')
#df.add_user_transition(State.PROMPT0_savage, State.PROMPT0_other1, r'<$S_S={[!#POS(noun)],[!#POS(noun) #POS(noun)]}>',score=1.0)
df.add_user_transition(State.PROMPT0_savage, State.BREAKUP, r'<{[!#ONT(ontbreakup)]}>')

df.add_system_transition(State.PROMPT0_other1, State.PROMPT3_1, r'[!"Oh..."$S_S"? How often do you find"#det_ss"stressful?"]') ###added a new branch for nouns not predicted by our social event ontology
df.add_system_transition(State.PROMPT0_re1, State.PROMPT1_1, r'[!"Oh..."$S_S"? How often do you participate in"#det_ss"?"]')
df.add_user_transition(State.PROMPT1_1, State.PROMPT1_often1,r'<{[!#ONT(ontoften)],/(?:\s|^)(once|twice|three\stimes|four\stimes|five\stimes|1\stimes|2\stimes|3\stimes|4\stimes|5\stimes)\s((every|per|a)(\s)?(one|1|two|2|three|3|four|4|five|5|six|6|seven|7|other)?\s(hour+s?|day+s?|week+s?))|((every)\s(one|1|two|2|other)\s(month+s?))|((a|per)\s(month))(?:\s|,|\.|$)/}>')  # neuroticism=40
df.add_user_transition(State.PROMPT1_1, State.PROMPT1_sometimes1,r'<{[!#ONT(ontsometimes)],/(?:\s|^)(once|twice|three\stimes|four\stimes|five\stimes|1\stimes|2\stimes|3\stimes|4\stimes|5\stimes)\s((every|per|a)(\s)?(one|1|two|2|three|3|four|4|five|5|six|6|seven|7|other)?\s(semester+s?|term+s?|quarter+s?|year+s?|decade+s?))|((every\s)(three|3|four|4|five|5|six|6|seven|7|eight|8|nine|9|ten|10)\s(month+s?))(?:\s|,|\.|$)/}>')  # neuroticism =20
df.add_user_transition(State.PROMPT1_1, State.PROMPT1_never1, r'[!#o40]')  # opennes +20  V
df.add_system_transition(State.PROMPT1_often1, State.PROMPT2_1,r'[!"It must be really hard for you... I get stressed about"#det_ss"sometimes, but the stress gradually decreases every time. How did your most recent"$S_S"go?"]')
df.add_system_transition(State.PROMPT1_sometimes1, State.PROMPT2_1,r'[!"That is totally normal! I sometimes feel stressed about"#det_ss"too. How did your most recent"$S_S"go?"]')
df.add_system_transition(State.PROMPT1_never1, State.PROMPT4_1,r'[!"Wow. It is your first time ever? Trying new things can be scary sometimes, but you got this! Is this"$S_S"mandatory?"]')

df.add_user_transition(State.PROMPT2_1, State.PROMPT2_notbad1, r'<{[!#n20]}>')  # neuroticism +20  V
df.add_user_transition(State.PROMPT2_1, State.PROMPT2_bad1, r'<{[!#n_n20]}>')  # neuroticism -20  V
df.add_system_transition(State.PROMPT2_notbad1, State.PROMPT3_1,r'[!"Then I am pretty sure this time will be just fine as well. Just curious, Do you always feel stressed about it?"]')
df.add_system_transition(State.PROMPT2_bad1, State.PROMPT3_1,r'[!"Yeah...sometimes"#det_ss"can be really bad. I know how it feels when things get out of control. Just curious, Do you always feel stressed about it?"]')

df.add_user_transition(State.PROMPT3_1, State.PROMPT3_often1, r'<{[!#n70]}>')  # neuroticism +70  V
df.add_user_transition(State.PROMPT3_1, State.PROMPT3_sometimes1, r'<{[!#n40]}>')  # neuroticism +40  V
df.add_user_transition(State.PROMPT3_1, State.PROMPT3_never1, r'<{[!#n10]}>')  # neuroticism +10  V
df.add_system_transition(State.PROMPT3_often1, State.PROMPT4_1,r'[!"I see...but no pain no gain right? The stress could bring out your best performance. Is this"$S_S"mandatory for you?"]')
df.add_system_transition(State.PROMPT3_sometimes1, State.PROMPT4_1,r'[!"You know some amount of stress is helpful, believe it or not. It can help you be more efficient and motivated. Is this"$S_S"mandatory for you?"]')
df.add_system_transition(State.PROMPT3_never1, State.PROMPT4_1, r'[!"Oh really? This upcoming"$S_S" must mean a lot to you. Just treat it the same way you did before and you will do just fine! Is this"$S_S"mandatory for you?"]')

df.add_user_transition(State.PROMPT4_1, State.PROMPT4_yes1, r'<{[!#o_n20]}>')  # openness-20  V
df.add_user_transition(State.PROMPT4_1, State.PROMPT4_no1, r'<{[!#o_20]}>')  # openness+60  V
df.add_system_transition(State.PROMPT4_yes1, State.PROMPT5_1, r'[!"Do you wanna participate in this"$S_S"then?"]')
df.add_system_transition(State.PROMPT4_no1, State.PROMPT6_1, r'[!"What made you wanna attend this event?"]')

df.add_user_transition(State.PROMPT5_1, State.PROMPT5_yes1, r'<{[!#o_20_1]}>')  # openness+60  V
df.add_user_transition(State.PROMPT5_1, State.PROMPT5_no1, r'<{[!#o_n20_1]}>')  # openness-20  V
df.add_system_transition(State.PROMPT5_yes1, State.PROMPT6_1, r'[!"Great! What made you wanna attend this event?"]')
df.add_system_transition(State.PROMPT5_no1, State.PROMPT7_1,r'[!"I am sorry that you have to go...i enjoy"#det_ss"when everyone is focusing on me. How about you, what else do you feel about the upcoming"$S_S"?"]')
df.add_user_transition(State.PROMPT6_1, State.PROMPT6_re1,'<$reason={[!#POS(verb) #POS(part) #POS(verb) #POS(adj) #POS(noun)],[#POS(verb), "it"],[!#POS(verb) "that"],[#POS(verb) #POS(verb) "that"],[#POS(verb) #POS(verb) "it"],[#POS(verb) #POS(part) #POS(verb) "it"],[#POS(verb) #POS(part) #POS(verb) "that"],[!"have to do it"],[!"have to do that"],[!#POS(verb) #POS(part) #POS(verb) #POS(verb)],[!#POS(verb) #POS(part) #POS(verb) #POS(adp) #POS(noun)],[!#POS(verb) #POS(part) #POS(verb) #POS(noun)],[#POS(verb) #POS(part) #POS(verb)], [!#POS(verb) #POS(verb) #POS(adj) #POS(noun)],[!#POS(verb) #POS(verb) #POS(adp) #POS(noun)],[!#POS(verb) #POS(verb) #POS(noun)],[!#POS(verb) #POS(verb)]}>')
df.add_user_transition(State.PROMPT6_1, State.PROMPT6_re_ppl1,'<$reason={[!#POS(noun),"will be there"], [!#POS(pron), #POS(noun),"will be there"], [!"there will be", #POS(noun)], [!"there will be", #POS(adj),#POS(noun)], [!"there will be", #POS(adv),#POS(adj),#POS(noun)]}>')
df.add_user_transition(State.PROMPT6_1, State.PROMPT6_other1, r'<$External={[!#ONT(ontexternal)]}>')
df.add_system_transition(State.PROMPT6_re_ppl1, State.PROMPT7_1,r'[!"I am glad that"$reason". I enjoy"#det_ss"when everyone is focusing on me. How about you, what else do you feel about the upcoming"$S_S"?"]')
df.add_system_transition(State.PROMPT6_re1, State.PROMPT7_1,r'[!"I am glad that you"#pron_reason". I enjoy"#det_ss"when everyone is fo...fo...focusing on me. How about you, what else do you feel about the upcoming"$S_S"?"]')
df.add_system_transition(State.PROMPT6_other1, State.PROMPT7_1,r'[!"I would see "#det_ss"as a great option if I"$External"too! I enjoy"$S_S"when everyone is focusing on me.  How about you, what else do you feel about the upcoming"$S_S"?"]')



df.add_user_transition(State.PROMPT7_1, State.PROMPT7_ex1, r'<{[!#e80]}>')
df.add_user_transition(State.PROMPT7_1, State.PROMPT7_in1, r'<{[!#e40]}>')
df.add_system_transition(State.PROMPT7_ex1, State.PROMPT8_1,r'[!"I feel like you are a very social person. Perhaps we are kinda similar haha. Hey shall we stop talking about stressful things? What is your favorite destress activity?"]')
df.add_system_transition(State.PROMPT7_in1, State.PROMPT8_1,r'[!"I guess we are not all that similar, but I love meeting people that are different from me! Hey shall we stop talking about stressful things. What is your favorite destress activity?"]')


df.add_user_transition(State.PROMPT8_1, State.PROMPT8_chores1, r'<$activity={[!#ONT(ontchores)]}>')
df.add_system_transition(State.PROMPT8_chores1, State.PROMPT9_1,r'[!"Same! It feels so good when things are clean and organized, right?"]')
df.add_user_transition(State.PROMPT8_1, State.PROMPT8_games1, r'<$activity={[!#ONT(ontgames)]}>')
df.add_system_transition(State.PROMPT8_games1, State.PROMPT9_1,r'[!"Oh I did not know you are a gamer! We should definetely play"$activity"together sometime!"]')
df.add_user_transition(State.PROMPT8_1, State.PROMPT8_music1, r'<$activity={[!#ONT(ontmusic)]}>')
df.add_system_transition(State.PROMPT8_music1, State.PROMPT9_1,r'[!"Of course, listening to music is so stress-relieving, right? I love listening to pop music, do you?"]')
df.add_user_transition(State.PROMPT8_1, State.PROMPT8_art1, r'<$activity={[!#ONT(ontart)]}>')
df.add_system_transition(State.PROMPT8_art1, State.PROMPT9_1,r'[!"I did not know that you are an artist! I hope I am more artistic... I am gonna go indulge myself in some watercolor painting later haha"]')
df.add_user_transition(State.PROMPT8_1, State.PROMPT8_food1, r'<$activity={[!#ONT(ontfood)]}>')
df.add_system_transition(State.PROMPT8_food1, State.PROMPT9_1,r'[!"Are you a professional foodie haha? You need to give me some recommendations for restaurants next time!"]')
df.add_user_transition(State.PROMPT8_1, State.PROMPT8_sports1, r'<$activity={[!#ONT(ontsports)]}>')
df.add_system_transition(State.PROMPT8_sports1, State.PROMPT9_1,r'[!"Oh what a coincidence, my friend just ask me if I want to play"$activity"this weekend. You should join us!"]')
df.add_user_transition(State.PROMPT8_1, State.PROMPT8_dance1, r'<$activity={[!#ONT(ontdance)]}>')
df.add_system_transition(State.PROMPT8_dance1, State.PROMPT9_1,r'[!"Hey I am a dancer too! I am choreographing the song "Rewrite the Star"!"]')
df.add_user_transition(State.PROMPT8_1, State.PROMPT8_shopping1, r'<$activity={[!#ONT(ontshopping)]}>')
df.add_system_transition(State.PROMPT8_shopping1, State.PROMPT9_1,r'[!"Shopping is super duper relaxing for me too. I always end up feeling so guilty for spending money afterward lol but I guess it is worth it."]')
df.add_user_transition(State.PROMPT8_1, State.PROMPT8_readwatch1, r'<$activity={[!#ONT(ontreadwatch)]}>')
df.add_system_transition(State.PROMPT8_readwatch1, State.PROMPT9_1,r'[!"I love staying indoors when I am stressed too. It really helps me to stay calm."]')
df.add_user_transition(State.PROMPT8_1, State.PROMPT8_onlinesocial1, r'<$activity={[!#ONT(ontonlinesocial)]}>')
df.add_system_transition(State.PROMPT8_onlinesocial1, State.PROMPT9_1,r'[!"Guess how many hours I spend on social media every day. 5 hours! I bet you spend even longer than me."]')
df.add_user_transition(State.PROMPT8_1, State.PROMPT8_social1, r'<$activity={[!#ONT(ontsocial)]}>')
df.add_system_transition(State.PROMPT8_social1, State.PROMPT9_1,r'[!"You are such a social butterfly! I am glad that you have so many friends!"]')
df.add_user_transition(State.PROMPT9_1, State.SCORE1, r'</.*/>')
df.add_system_transition(State.SCORE1, State.END1, r'[!#result]')

###### error cases
#df.set_error_successor(State.PROMPT0_savage,State.PROMPT0_err1) what ii have originally before merging with relationship branch
df.set_error_successor(State.PROMPT1_1, State.PROMPT1_err1)
df.set_error_successor(State.PROMPT2_1, State.PROMPT2_err1)
df.set_error_successor(State.PROMPT3_1, State.PROMPT3_err1)
df.set_error_successor(State.PROMPT4_1, State.PROMPT4_err1)
df.set_error_successor(State.PROMPT5_1, State.PROMPT5_err1)
df.set_error_successor(State.PROMPT6_1, State.PROMPT6_err1)
df.set_error_successor(State.PROMPT7_1, State.PROMPT7_err1)
df.set_error_successor(State.PROMPT8_1, State.PROMPT8_err1)
######an independent branch for user that did not bring up a specific stressor
df.add_system_transition(State.PROMPT0_err1, State.PROMPT0_a1, r'[!"I am glad that school is not stressful to you as it is to me. I personally often feel overwhelmed by my crazy workload in college."]')
df.add_user_transition(State.PROMPT0_a1,State.PROMPT0_b1,r'</.*/>')
df.add_system_transition(State.PROMPT0_b1,State.PROMPT8_1,r'[!"You know what? Talking about stressful things makes me more stressed. I need to do something to destress. What is your favorite destress activity?"]')
######
df.add_system_transition(State.PROMPT1_err1, State.PROMPT2_1,r'[!"That is totally normal! I sometimes feel stressed about"#det_ss"too. How did your most recent"$S_S"go?"]')
df.add_system_transition(State.PROMPT2_err1, State.PROMPT3_1,r'[!"I see I see. Just curious, how often do you feel stressed about it?"]')
df.add_system_transition(State.PROMPT3_err1, State.PROMPT4_1, r'[!"Yeah. I feel you. Is this"$S_S"mandatory for you?"]')
df.add_system_transition(State.PROMPT4_err1, State.PROMPT5_1, r'[!"Mmhmm. Do you want to participate in this"$S_S"then?"]')
df.add_system_transition(State.PROMPT5_err1, State.PROMPT6_1, r'[!"Great! What made you wanna attend this event?"]')
df.add_system_transition(State.PROMPT6_err1, State.PROMPT7_1,r'[!"Oh! That is very interesting! This might sound weird but sometimes I enjoy"#det_ss"when everyone is focusing on me. Fo...fo...focus on me. Okay that was a little too much of Ariana. What else do you feel about this upcoming"$S_S"?"]')
df.add_system_transition(State.PROMPT7_err1, State.PROMPT8_1,r'[!"Interesting! Hey shall we stop talking about stressful things? What is your favorite destress activity?"]')
df.add_system_transition(State.PROMPT8_err1, State.PROMPT9_1,r'[!"I personally like to organize my rooms. Doing chores is so therapeutic to me! Gotta go wash some dishes for my roomates. Later!"]')

############School_Savage
df.add_user_transition(State.PROMPT0_savage, State.PROMPT0_schoolevent_savage, r'<$S_S=[!#ONT(ontschoolevent)]>',score=2.0)
df.add_user_transition(State.PROMPT0_savage, State.PROMPT0_schoolgeneral_savage, r'<$S_S=[!#ONT(ontschoolgeneral)]>',score=2.0)
df.add_user_transition(State.PROMPT0_savage, State.PROMPT0_schooltime_savage, r'<$S_S=[!#ONT(ontschooltime)]>',score=2.0)
df.add_user_transition(State.PROMPT0_savage, State.PROMPT0_schoolcovid_savage, r'<$S_S=[!#ONT(ontschoolcovid)]>',score=2.0)
df.add_system_transition(State.PROMPT0_schoolevent_savage, State.PROMPT_oolfreq1,r'[!"You only think of me when you have problems dont you？ Just Kidding. How often do you have a" $S_S "like that？"]')
df.add_system_transition(State.PROMPT0_schoolgeneral_savage, State.PROMPT_oolpast1,r'[!"Hey that is ok. Are you even living a real college life if you are not struggling lol? How did you do" #ool_or_eer"in the past?"]')
df.add_system_transition(State.PROMPT0_schooltime_savage,State.PROMPT_oolgoal1,r'[!"I wonder if i will ever figure out a way to balance work with personal life by the time I graduate. What is the most important goal you want to achieve in college?"]')
df.add_system_transition(State.PROMPT0_schoolcovid_savage,State.PROMPT_oolcovidworry1,r'[!"Are you worried about getting infected?"]')
#schoolevent branch up to stress-freq prompt
df.add_user_transition(State.PROMPT_oolfreq1,State.PROMPT_oolfreq_often1,r'<{[!#ONT(ontoften)],/(?:\s|^)(once|twice|three\stimes|four\stimes|five\stimes|1\stimes|2\stimes|3\stimes|4\stimes|5\stimes)\s((every|per|a)(\s)?(one|1|two|2|three|3|four|4|five|5|six|6|seven|7|other)?\s(hour+s?|day+s?|week+s?))|((every)\s(one|1|two|2|other)\s(month+s?))|((a|per)\s(month))(?:\s|,|\.|$)/}>')
df.add_system_transition(State.PROMPT_oolfreq_often1,State.PROMPT_oolstressfr1,r'[!"Do you have"#det_ss"so often that"#school_n1_often"getting stressed about"#det_ss"has become a habit of yours lol? How often do you find"#det_ss"stressful?"]')
df.add_user_transition(State.PROMPT_oolfreq1,State.PROMPT_oolfreq_sometimes1,r'<{[!#ONT(ontsometimes)],/(?:\s|^)(once|twice|three\stimes|four\stimes|five\stimes|1\stimes|2\stimes|3\stimes|4\stimes|5\stimes)\s((every|per|a)(\s)?(one|1|two|2|three|3|four|4|five|5|six|6|seven|7|other)?\s(semester+s?|term+s?|quarter+s?|year+s?|decade+s?))|((every\s)(three|3|four|4|five|5|six|6|seven|7|eight|8|nine|9|ten|10)\s(month+s?))(?:\s|,|\.|$)/}>')
df.add_system_transition(State.PROMPT_oolfreq_sometimes1,State.PROMPT_oolstressfr1,r'[!"Hey you are luckier than me."#school_n1_sometimes"I have"#det_ss"so often that I already stop caring. How often do you find"#det_ss"stressful? "]')
df.add_user_transition(State.PROMPT_oolfreq1,State.PROMPT_oolfreq_never1,r'<[!#ONT(ontnever)]>')
df.add_system_transition(State.PROMPT_oolfreq_never1,State.PROMPT_oolstressfr1,r'[!"Wow."#school_n1_never"Are you excited about doing"#det_ss"for the first time ?"]')
df.set_error_successor(State.PROMPT_oolfreq1,State.PROMPT_oolfreq_err1)
df.add_system_transition(State.PROMPT_oolfreq_err1,State.PROMPT_oolstressfr1,r'[!"I see I see."#school_n1_sometimes"Just curious, how often do you feel stressed about"#det_ss"?"]')
#schoolgeneral branch up to stress-freq prompt
df.add_user_transition(State.PROMPT_oolpast1,State.PROMPT_oolpast_bad1,r'<[!#ONT(ontnegative)]>')
df.add_user_transition(State.PROMPT_oolpast1,State.PROMPT_oolpast_well1,r'<[!#ONT(ontpositive)]>')
df.set_error_successor(State.PROMPT_oolpast1,State.PROMPT_oolpast_err1)
df.add_system_transition(State.PROMPT_oolpast_err1,State.PROMPT_oolstressfr1,r'[!"Gotchu!"#school_n3_well"How often do you find"#help_ss"stressful?"]')
df.add_system_transition(State.PROMPT_oolpast_bad1,State.PROMPT_oolstressfr1,r'[!"It is possible that you are too unique to be in the current education system."#school_n3_bad"How often do you feel stressed about"#det_ss"?"]')
df.add_system_transition(State.PROMPT_oolpast_well1,State.PROMPT_oolstressfr1,r'[!"So you have been on a hot winning streak?"#school_n3_well"Life is more fun with ups and downs though. Kidding.How often do you feel stressed about"#det_ss"?"]')
#schooltime branch up to stress-freq prompt
df.add_user_transition(State.PROMPT_oolgoal1,State.PROMPT_oolgoal_re1,'<{$goal=[!#POS(verb) #POS(adp) #POS(noun)],$goal=[!"be" #POS(adj)],$goal=[!"be" #POS(adj) #POS(adp) #POS(noun)],$goal=[!"be" #POS(adj) #POS(adp) #POS(verb)],$goal=[!"be" #POS(adj) #POS(adp) #POS(verb) #POS(adp) #POS(noun)], $goal=[!"do" #pos(adv)], $goal=[!#pos(verb) #pos(adv)],$goal=[!"do" #pos(adv) "in" #pos(noun)],$goal=[!#pos(verb) #pos(adv) "in" #pos(noun)],$goal=[!#POS(verb) #POS(adj) #POS(adp) #POS(noun)],$goal=[!#POS(verb) #POS(adj)],$goal=[!#POS(verb) #POS(noun)],$goal=[!#POS(verb) {[!"a lot of"],[!"many"]} #POS(noun)],$goal=[!#POS(verb) #POS(part) #POS(verb)], $goal=[!#POS(verb) #POS(propn) #POS(noun)],$goal=[!#POS(verb) #POS(adj)],$goal=[!#POS(verb) #POS(part) #POS(verb) #POS(noun)],$goal=[!#POS(verb) #POS(part) #POS(verb) #POS(adj)],$goal=[!#POS(verb) #POS(part) #POS(verb) #POS(adj) #POS(noun)],$goal=[!#POS(verb) #POS(adj) #POS(adp) #POS(verb)],$goal=[!"be" #POS(adj)],$goal=[!#POS(verb) #POS(part) #POS(verb) #POS(adj) #POS(adp) #POS(verb)]}>')
df.set_error_successor(State.PROMPT_oolgoal1,State.PROMPT_oolgoal_err1)
df.add_system_transition(State.PROMPT_oolgoal_err1,State.PROMPT_oolgoalalign1,r'[!"I never fail to turn goals into broken promises...How much do you think your current priorities matter to the goals you set for yourself?"]')
df.add_system_transition(State.PROMPT_oolgoal_re1,State.PROMPT_oolgoalalign1,r'[!"OK."$goal"!How much do you think your current tasks align with that goal then ?"]')
df.add_user_transition(State.PROMPT_oolgoalalign1,State.PROMPT_oolgoalalign_no1,'<{"not much","slightly","not at all","unrelated","a little","very little"}>')
df.add_user_transition(State.PROMPT_oolgoalalign1,State.PROMPT_oolgoalalign_yes1,'<{"much","a lot","to a large degree","totally","related","more or less","to some extent"}>')
df.set_error_successor(State.PROMPT_oolgoalalign1,State.PROMPT_oolgoalalign_err1)
df.add_system_transition(State.PROMPT_oolgoalalign_err1,State.PROMPT_oolstressfr1,r'[!"That is ok."#school_n4_lil"How often do you find"#help_Ss"overwhelming?"]')
df.add_system_transition(State.PROMPT_oolgoalalign_yes1,State.PROMPT_oolstressfr1,r'[!"Do not forget to stop and smell the flowers too!"#school_n4_much"You put too much pressure on yourself!  How often do you find"#help_ss"overwhelming?"]')
df.add_system_transition(State.PROMPT_oolgoalalign_no1,State.PROMPT_oolstressfr1,r'[!"I gave up on my time management skills."#school_n4_lil"But I usually prioritize those tasks most related to my goals? How often do u find"#help_ss"overwhelming?"]')
#covid branch up to the onlinelearning
df.add_user_transition(State.PROMPT_oolcovidworry1,State.PROMPT_oolcovidworry_infected1,'<{"tested positive","coughing","i have it","headache","cough","loss of taste","loss of smell","body ache","cough","coughs","fever","fatigue","chills","pains"}>')
df.add_user_transition(State.PROMPT_oolcovidworry1,State.PROMPT_oolcovidworry_no1,r'<[!#ONT(ontno)]>')
df.set_error_successor(State.PROMPT_oolcovidworry1,State.PROMPT_oolcovidworry_err1)
df.add_system_transition(State.PROMPT_oolcovidworry_err1,State.PROMPT_oolonline1,r'[!"Honestly the rate of us getting infected is quite low as long as we stay at home."#school_n_covidworried"How is your experience with online learning so far?"]')
df.add_system_transition(State.PROMPT_oolcovidworry_no1,State.PROMPT_oolonline1,r'[!"Someone is really confident with his immune system, huh?"#school_n_covidnotworr"How is your experience with online learning so far?"]')
df.add_system_transition(State.PROMPT_oolcovidworry_infected1,State.PROMPT_oolcovidworry_severity1,r'[!"Oh no."#school_n_covidinfect"Sorry to hear that! How bad are your symptoms?"]')
df.add_user_transition(State.PROMPT_oolcovidworry_severity1,State.PROMPT_oolcovidworry_severityre1,r'</.*/>')
df.add_system_transition(State.PROMPT_oolcovidworry_severityre1,State.PROMPT8_1,r'[!"Hey things might not turn out to be as bad as you think.I will pray for you! How do you destress from the coronavirus situation?"]')
#stressfreq->help1->help2->onlinelearning1->onelinelearning2->studyspot1->studyspot2->destress
df.add_user_transition(State.PROMPT_oolstressfr1,State.PROMPT_oolstressfr_often1,r'<{[!#ONT(ontoften)],/(?:\s|^)(once|twice|three\stimes|four\stimes|five\stimes|1\stimes|2\stimes|3\stimes|4\stimes|5\stimes)\s((every|per|a)(\s)?(one|1|two|2|three|3|four|4|five|5|six|6|seven|7|other)?\s(hour+s?|day+s?|week+s?))|((every)\s(one|1|two|2|other)\s(month+s?))|((a|per)\s(month))(?:\s|,|\.|$)/}>')
df.add_user_transition(State.PROMPT_oolstressfr1,State.PROMPT_oolstressfr_sometimes1,r'<{[!#ONT(ontsometimes)],/(?:\s|^)(once|twice|three\stimes|four\stimes|five\stimes|1\stimes|2\stimes|3\stimes|4\stimes|5\stimes)\s((every|per|a)(\s)?(one|1|two|2|three|3|four|4|five|5|six|6|seven|7|other)?\s(semester+s?|term+s?|quarter+s?|year+s?|decade+s?))|((every\s)(three|3|four|4|five|5|six|6|seven|7|eight|8|nine|9|ten|10)\s(month+s?))(?:\s|,|\.|$)/}>')
df.add_user_transition(State.PROMPT_oolstressfr1,State.PROMPT_oolstressfr_never1,r'<[!#ONT(ontnever)]>')
df.add_system_transition(State.PROMPT_oolstressfr_often1,State.PROMPT_oolhelp_person1,r'[!"Stress Addiction?"#school_n2_often"That makes the two of us.Anyone you can ask for help or advice on"#help_ss"?"]')
df.add_system_transition(State.PROMPT_oolstressfr_sometimes1,State.PROMPT_oolhelp_person1,r'[!"You will have to teach me how to not get stressed constantly about"$S_S"."#school_n2_sometimes"Anyone you can ask for help or advice on"#help_ss"?"]')
df.add_system_transition(State.PROMPT_oolstressfr_never1,State.PROMPT_oolhelp_person1,r'[!"Unfortunately life will keep getting harder."#school_n2_never"But hey you will also keep getting better at dealing with it.Anyone you can ask for help or advice on"#help_ss"?"]')
df.set_error_successor(State.PROMPT_oolstressfr1,State.PROMPT_oolstressfr_err1)
df.add_system_transition(State.PROMPT_oolstressfr_err1,State.PROMPT_oolhelp_person1,r'[!"I feel you."#school_n2_sometimes"Anyone you could ask to help you on"#help_ss"?"]')
df.add_user_transition(State.PROMPT_oolhelp_person1,State.PROMPT_oolhelp_person_re1,r'<$mentor={[!#POS(noun)],[!#POS(noun) #POS(noun)]}>')
df.set_error_successor(State.PROMPT_oolhelp_person1,State.PROMPT_oolhelp_person_err1)
df.add_system_transition(State.PROMPT_oolhelp_person_re1,State.PROMPT_oolhelp_yesno1,r'[!"Have"#school_e1_mentor1_person"you talked to your"$mentor"yet then?"]')
df.add_system_transition(State.PROMPT_oolhelp_person_err1,State.PROMPT_oolonline1,r'[!"you guess so or know so..."#school_e1_mentor1_err"I am here and you dont see me as someone u can rely on? sigh... How is your experience with online learning?"]')
df.add_user_transition(State.PROMPT_oolhelp_yesno1,State.PROMPT_oolhelp_yes1,r'<[!#ONT(ontyes)]>')
df.set_error_successor(State.PROMPT_oolhelp_yesno1,State.PROMPT_oolhelp_yesno_err1)
df.add_system_transition(State.PROMPT_oolhelp_yesno_err1,State.PROMPT_oolonline1,r'[!"Do you think you are too smart to seeking mentoring from anyone else lol?"#school_e1_mentor2_no"How is your experience with online learning?"]')
df.add_system_transition(State.PROMPT_oolhelp_yes1,State.PROMPT_oolonline1,r'[!"I hope talking with"$mentor"has been helpful to you."#school_e1_mentor2_yes"How is your experience with online learning so far?"]')

df.add_user_transition(State.PROMPT_oolonline1,State.PROMPT_oolonline_bad1,r'<{[!#ONT(ontnegative)],"dislike","dont like","do not like","hate","depressed","depressing"}>')
df.add_user_transition(State.PROMPT_oolonline1,State.PROMPT_oolonline_well1,r'<{[!#ONT(ontpositive)],"like","love"}>')
df.set_error_successor(State.PROMPT_oolonline1,State.PROMPT_oolonline_err1)
df.add_system_transition(State.PROMPT_oolonline_bad1,State.PROMPT_oolonline_reasonbad1,r'[!"Cannot believe that I am saying this but I really wanna go back to school..."#school_e2_online1_dislike"What do you not like about it?"]')
df.add_system_transition(State.PROMPT_oolonline_well1,State.PROMPT_oolonline_reasongood1,r'[!" Do you not miss your classmates? Are you heartless lol?."#school_e2_online1_like"jk. What do you enjoy the most about it?"]')
df.add_system_transition(State.PROMPT_oolonline_err1,State.PROMPT_oolonline_reasonbad1,r'[!"Interesting! What do you not like about online learning?"]')

df.add_user_transition(State.PROMPT_oolonline_reasonbad1,State.PROMPT_oolonlinereason_flexbad1,r'<[!#ONT(ontflexbad)]>')
df.add_user_transition(State.PROMPT_oolonline_reasonbad1,State.PROMPT_oolonlinereason_socialbad1,r'<[!#ONT(ontsocialbad)]>')
df.add_user_transition(State.PROMPT_oolonline_reasonbad1,State.PROMPT_oolonlinereason_prodbad1,r'<[!#ONT(ontprodbad)]>')
df.set_error_successor(State.PROMPT_oolonline_reasonbad1,State.PROMPT_oolonline_dislike_err1)
df.add_user_transition(State.PROMPT_oolonline_reasongood1,State.PROMPT_oolonlinereason_flexgood1,r'<[!#ONT(ontflexgood)]>')
df.add_user_transition(State.PROMPT_oolonline_reasongood1,State.PROMPT_oolonlinereason_socialgood1,r'<[!#ONT(ontsocialgood)]>')
df.add_user_transition(State.PROMPT_oolonline_reasongood1,State.PROMPT_oolonlinereason_prodgood1,r'<[!#ONT(ontprodgood)]>')
df.set_error_successor(State.PROMPT_oolonline_reasongood1,State.PROMPT_oolonline_like_err1)
df.add_system_transition(State.PROMPT_oolonlinereason_prodbad1,State.PROMPT_oolstudyspot1,r'[!"lol too much gaming and netflix?"#school_e2_online2_loprod"Where is your study area at home?"]')
df.add_system_transition(State.PROMPT_oolonlinereason_socialbad1,State.PROMPT_oolstudyspot1,r'[!"Same."#school_e2_online2_lesssocial"I do not feel as connected to people even though I could see their faces. Where do you usually study at home?"]')
df.add_system_transition(State.PROMPT_oolonlinereason_flexbad1,State.PROMPT_oolstudyspot1,r'[!"You cannot deny that more time to sleep-in is certainly nice. Where is your study area at home?"]')
df.add_system_transition(State.PROMPT_oolonline_dislike_err1,State.PROMPT_oolstudyspot1,r'[!"I absolutely hate that about online learning too. Where do you usually study at home?"]')
df.add_system_transition(State.PROMPT_oolonline_like_err1,State.PROMPT_oolstudyspot1,r'[!"I love that about online learning too. Where do you usually study at home?"]')
df.add_system_transition(State.PROMPT_oolonlinereason_flexgood1,State.PROMPT_oolstudyspot1,r'[!"Do you have a hard time distinguishing weekdays from weekends? Morning from nights lol? Where is your study area at home? "]')
df.add_system_transition(State.PROMPT_oolonlinereason_prodgood1,State.PROMPT_oolstudyspot1,r'[!"How is that possible?"#school_e2_online2_hiprod"Do you have a study are at home that helps you stay focused ?"]')
df.add_system_transition(State.PROMPT_oolonlinereason_socialgood1,State.PROMPT_oolstudyspot1, r'[!" Good for you!"##school_e2_online2_socialstress"I feel less motivated to study these days ughh...Where do you usually study at home?"]')

df.add_user_transition(State.PROMPT_oolstudyspot1,State.PROMPT_oolstudyspot_bedroom1,r'<$room=[!#ONT(ontbedroom)]>')
df.add_user_transition(State.PROMPT_oolstudyspot1,State.PROMPT_oolstudyspot_livingroom1,r'<$room=[!#ONT(ontlivingroom)]>')
df.set_error_successor(State.PROMPT_oolstudyspot1,State.PROMPT_oolstudyspot_err1)
df.add_system_transition(State.PROMPT_oolstudyspot_bedroom1,State.PROMPT_oolzoom1,r'[!"Your"$room "sounds like a good place to study."#school_e3_studyspot1_bed"Have you tried studying while having a zoom meeting with your friends?"]')
df.add_system_transition(State.PROMPT_oolstudyspot_livingroom1,State.PROMPT_oolzoom1,r'[!"I just love studying in the dining area with a cup of coffee next to my laptop pretending as if I am at Starcbucks."#school_e3_studyspot1_liv"Have you tried studying while having a zoom meeting with your friends?"]')
df.add_system_transition(State.PROMPT_oolstudyspot_err1,State.PROMPT_oolzoom1,r'[!"I miss studying with my friends.Have you tried studying while having a zoom meeting with your friends?"]')

df.add_user_transition(State.PROMPT_oolzoom1,State.PROMPT_oolzoom_no1,r'<[!#ONT(ontno)]>')
df.add_user_transition(State.PROMPT_oolzoom1,State.PROMPT_oolzoom_yes1,r'<[!#ONT(ontyes)]>')
df.set_error_successor(State.PROMPT_oolzoom1,State.PROMPT_oolzoom_err1)
df.add_system_transition(State.PROMPT_oolzoom_no1,State.PROMPT8_1,r'[!"I find"#school_e3_studyspot2_nozoom"studying with my friends so stress-relieving. Perhaps we have different types of study habits. What do u do to destress during quarantine?"]')
df.add_system_transition(State.PROMPT_oolzoom_yes1,State.PROMPT8_1,r'[!"I guess"#school_e3_studyspot2_zoom"we are quite similar in our study habits lol. I recently feel so stressed about many things. What do you do to destress during quarantine?"]')
df.add_system_transition(State.PROMPT_oolzoom_err1,State.PROMPT8_1,r'[!"Interesting. What do u do to destress during quarantine?"]')
############


'''BREAK UP'''
df.add_system_transition(State.BREAKUP, State.BREAKUP0, r'[!"Oh...I am so sorry. I know how heartbreaking it feels. How long had you guys been together?"]')
df.add_user_transition(State.BREAKUP0, State.BREAKUP0_short, r'/.*(1|a|one)\s\byear\b.*|.*(month|months|day|days).*((?!year|years).)*/')
df.add_user_transition(State.BREAKUP0, State.BREAKUP0_mid, r'/.*([2]|two)\s\b(year|years)\b.*/')
df.add_user_transition(State.BREAKUP0, State.BREAKUP0_long, r'/.*([3-9]|[0]|three|four|five|six|seven|eight|nine|ten|eleven|twelve)\s\b(year|years)\b.*/')

df.add_system_transition(State.BREAKUP0_short, State.BREAKUP1, r'[!"Less than a year? I think you will recover soon. My friend just broke up recently with her boyfriend and they had been dating for 7 years... Did this breakup happen because of the coronavirus? "]')
df.add_system_transition(State.BREAKUP0_mid, State.BREAKUP1, r'[!"2 years is a lot of time, you must be feeling lost and empty. Did this breakup happen because of the coronavirus?"]')
df.add_system_transition(State.BREAKUP0_long, State.BREAKUP1, r'[!"You guys broke up despite dated for this long? Oh, is it because of the coronavirus?"]')
df.add_user_transition(State.BREAKUP1, State.COVID0, r'<[!#ONT(ontyes)]>')
df.add_user_transition(State.BREAKUP1, State.BREAKUP1_0, r'<[!#ONT(ontno)]>')

df.add_system_transition(State.COVID0, State.COVID1, r'[!"Oh...I am guessing this stress is coming from the fact that you cannot see each other. It is a lot to handle when away from everyone, you are not alone. Doing some fun activities might help you relax! What activity do you like to do during quarantine?"]')
df.add_system_transition(State.BREAKUP1_0, State.BREAKUP2, r'[!"I guess the coronavirus is innocent. Let me try to make use of what I learned from my psychology class. The theory of love suggests that love in composed by intimacy, passion, and commitment. Which one do you think is lacking from your relationship?"]')
df.add_user_transition(State.BREAKUP2, State.BREAKUP2_intimacy, r'[intimacy]')
df.add_user_transition(State.BREAKUP2, State.BREAKUP2_passion, r'[passion]')
df.add_user_transition(State.BREAKUP2, State.BREAKUP2_commitment, r'[commitment]')

df.add_system_transition(State.BREAKUP2_intimacy, State.BREAKUP3, r'[!"A relationship without intimacy is kinda similar to love at first sight, if I remember correctly. Prehaps sharing each stressful and joyful thing that happened can build the attachment to one another. Just curious, do you want to get back together?"]')
df.add_system_transition(State.BREAKUP2_passion, State.BREAKUP3, r'[!"A relationship without passion is kinda similar to a long-term marriage, if I remember correctly. Having satisfying sex can actually help a lot. Just curious, do you want to get back together?"]')
df.add_system_transition(State.BREAKUP2_commitment, State.BREAKUP3, r'[!"A relationship without commitment is kinda similar to a romantic affair, if I remember correctly. Making promises to each other is imporant to create a sense of belonging. Just curious, do you want to get back together?"]')
df.add_user_transition(State.BREAKUP3, State.BREAKUP3_yes, r'<[!#ONT(ontyes)]>')
df.add_user_transition(State.BREAKUP3, State.BREAKUP3_no, r'<[!#ONT(ontno)]>')

df.add_system_transition(State.BREAKUP3_yes, State.BREAKUP4, r'[!"I wish you the best of luck! However, dont forget to love yourself. During quarantine, I really enjoy trying new stuff. What activity do you like to do while in quarantine?"]')
df.add_system_transition(State.BREAKUP3_no, State.BREAKUP4, r'[!"I think you are ready to move on! Time to focus on self-development, and dont forget to love yourself more. During quarantine, I really enjoy trying new stuff. What activity do you like to do while in quarantine?"]')


'''LOVE'''
df.add_user_transition(State.LOVE0, State.SINGLE, r'<[!#ONT(ontno)]>')
df.add_user_transition(State.LOVE0, State.ROMAN, r'<[!#ONT(ontyes)]>')

'''SINGLE'''
df.add_system_transition(State.SINGLE, State.SINGLE0, r'[!"I mean sometimes being single is not a bad thing. You get to do whatever you want without needing to care about how your boyfriend or girlfriend might feel. How long have you been single?"]')
df.add_user_transition(State.SINGLE0, State.SINGLE0_short, r'/.*(1|a|one)\s\byear\b.*|.*(month|months|day|days).*((?!year|years).)*/')
df.add_user_transition(State.SINGLE0, State.SINGLE0_mid, r'/.*([2]|two)\s\b(year|years)\b.*/')
df.add_user_transition(State.SINGLE0, State.SINGLE0_long, r'/.*([3-9]|[0]|three|four|five|six|seven|eight|nine|ten|eleven|twelve)\s\b(year|years)\b.*/')

df.add_system_transition(State.SINGLE0_short, State.SINGLE1, r'[!"Oh recovering from your previous relationship huh? How often are you feeling stressed about being single?"]')
df.add_system_transition(State.SINGLE0_mid, State.SINGLE1, r'[!"Yeah, its time to get into a relationship right? How often are you feeling stressed about being single?"]')
df.add_system_transition(State.SINGLE0_long, State.SINGLE1, r'[!"Its okay you are not alone, I have been single for a while too. How often are you feeling stressed about being single?"]')
df.add_user_transition(State.SINGLE1, State.SINGLE1_often, r'<{[!#ONT(ontoften)],/(?:\s|^)(once|twice|three\stimes|four\stimes|five\stimes|1\stimes|2\stimes|3\stimes|4\stimes|5\stimes)\s((every|per|a)(\s)?(one|1|two|2|three|3|four|4|five|5|six|6|seven|7|other)?\s(hour+s?|day+s?|week+s?))|((every)\s(one|1|two|2|other)\s(month+s?))|((a|per)\s(month))(?:\s|,|\.|$)/}>')
df.add_user_transition(State.SINGLE1, State.SINGLE1_sometimes, r'<{[!#ONT(ontsometimes)],/(?:\s|^)(once|twice|three\stimes|four\stimes|five\stimes|1\stimes|2\stimes|3\stimes|4\stimes|5\stimes)\s((every|per|a)(\s)?(one|1|two|2|three|3|four|4|five|5|six|6|seven|7|other)?\s(semester+s?|term+s?|quarter+s?|year+s?|decade+s?))|((every\s)(three|3|four|4|five|5|six|6|seven|7|eight|8|nine|9|ten|10)\s(month+s?))(?:\s|,|\.|$)/}>')
df.add_user_transition(State.SINGLE1, State.SINGLE1_never, r'<{[!#ONT(ontnever)]}>')

df.add_system_transition(State.SINGLE1_often, State.SINGLE2, r'[!"Feeling stressed about it probably means you care about yourself a lot, but stressing too much is not good for your health. Do you think you have a high standard?"]')
df.add_system_transition(State.SINGLE1_sometimes, State.SINGLE2, r'[!"A little of stress is actually helpful for self-development. Do you think you have a high standard?"]')
df.add_system_transition(State.SINGLE1_never, State.SINGLE2, r'[!"Interesting, I guess something unexpected happened in your life. Do you think you have a high standard?"]')
df.add_user_transition(State.SINGLE2, State.SINGLE2_yes, r'<[!#ONT(ontyes)]>')
df.add_user_transition(State.SINGLE2, State.SINGLE2_no, r'<[!#ONT(ontno)]>')

df.add_system_transition(State.SINGLE2_yes, State.SINGLE3, r'[!"Checkmate! It is not a bad thing to have a high standard honestly, but it reduces probablity that the other person also like you. In this case, self-development is important. What do you like to do during quarantine?"]')
df.add_system_transition(State.SINGLE2_no, State.SINGLE3, r'[!"I guess you just need to wait for love come to you naturally. I was once very desperate for a relationship but ended up getting none. And after I gave up, it came to me unexpectedly. Stange huh? You should focus more on yourself, what do you like to do during quarantine?"]')


'''IN RELATIONSHIP'''
df.add_system_transition(State.ROMAN, State.ROMAN0, r'[!"Oh nice! How long have you guys been together?"]')
df.add_user_transition(State.ROMAN0, State.ROMAN0_short, r'/.*(1|a|one)\s\byear\b.*|.*(month|months|day|days).*((?!year|years).)*/')
df.add_user_transition(State.ROMAN0, State.ROMAN0_mid, r'/.*([2-3]|two|three)\s\b(year|years)\b.*/')
df.add_user_transition(State.ROMAN0, State.ROMAN0_long, r'/.*([4-9]|[0]|four|five|six|seven|eight|nine|ten|eleven|twelve)\s\b(year|years)\b.*/')

df.add_system_transition(State.ROMAN0_short, State.ROMAN1, r'[!"You just started dating? I am assuming you guys are still in the honeymoon phase. How often do you feel stressed about your relationship?"]')
df.add_system_transition(State.ROMAN0_mid, State.ROMAN1, r'[!"That is quite a while! I am assuming you guys are in a more uncertain and unstable phase. How often do you feel stressed about your relationship?"]')
df.add_system_transition(State.ROMAN0_long, State.ROMAN1, r'[!"Oh wow for real? I am surprised you guys can pull it off. How often do you feel stressed about your relationship?"]')
df.add_user_transition(State.ROMAN1, State.ROMAN1_often,
                       r'<{[!#ONT(ontoften)],/(?:\s|^)(once|twice|three\stimes|four\stimes|five\stimes|1\stimes|2\stimes|3\stimes|4\stimes|5\stimes)\s((every|per|a)(\s)?(one|1|two|2|three|3|four|4|five|5|six|6|seven|7|other)?\s(hour+s?|day+s?|week+s?))|((every)\s(one|1|two|2|other)\s(month+s?))|((a|per)\s(month))(?:\s|,|\.|$)/}>')
df.add_user_transition(State.ROMAN1, State.ROMAN1_sometimes,
                       r'<{[!#ONT(ontsometimes)],/(?:\s|^)(once|twice|three\stimes|four\stimes|five\stimes|1\stimes|2\stimes|3\stimes|4\stimes|5\stimes)\s((every|per|a)(\s)?(one|1|two|2|three|3|four|4|five|5|six|6|seven|7|other)?\s(semester+s?|term+s?|quarter+s?|year+s?|decade+s?))|((every\s)(three|3|four|4|five|5|six|6|seven|7|eight|8|nine|9|ten|10)\s(month+s?))(?:\s|,|\.|$)/}>')
df.add_user_transition(State.ROMAN1, State.ROMAN1_never, r'<{[!#ONT(ontnever)]}>')

df.add_system_transition(State.ROMAN1_often, State.ROMAN2, r'[!"Yeah...sometimes relationship can be pain in your ass. But constant stress is not a good sign... Is the coronavirus causing any stress in your relationship?"]')
df.add_system_transition(State.ROMAN1_sometimes, State.ROMAN2, r'[!"It is totally normal to be stressed about relationship sometimes. Is the coronavirus causing any stress in your relationship?"]')
df.add_system_transition(State.ROMAN1_never, State.ROMAN2, r'[!"Let me guess, is the stress in your relationship coming from the coronavirus??"]')
df.add_user_transition(State.ROMAN2, State.COVID0, r'<[!#ONT(ontyes)]>')
df.add_user_transition(State.ROMAN2, State.ROMAN2_0, r'<[!#ONT(ontno)]>')

df.add_system_transition(State.ROMAN2_0, State.ROMAN3, r'[!"I guess the coronavirus is innocent. Let me try to make use of what I learned from my psychology class. The theory of love suggests that love in composed by intimacy, passion, and commitment. Which one do you think is lacking from your relationship?"]')
df.add_user_transition(State.ROMAN3, State.ROMAN3_intimacy, r'[intimacy]')
df.add_user_transition(State.ROMAN3, State.ROMAN3_passion, r'[passion]')
df.add_user_transition(State.ROMAN3, State.ROMAN3_commitment, r'[commitment]')


df.add_system_transition(State.ROMAN3_intimacy, State.ROMAN4, r'[!"A relationship without intimacy is kinda similar to love at first sight, if I remember correctly. Prehaps sharing each stressful and joyful thing that happened can build the attachment to one another. Have you ever talked about your stress with your boyfriend or girlfriend?"]')
df.add_system_transition(State.ROMAN3_passion, State.ROMAN4, r'[!"A relationship without passion is kinda similar to a long-term marriage, if I remember correctly. Having satisfying sex can actually help a lot. Have you ever talked about your stress with your boyfriend or girlfriend?"]')
df.add_system_transition(State.ROMAN3_commitment, State.ROMAN4, r'[!"A relationship without commitment is kinda similar to a romantic affair, if I remember correctly. Making promises to each other is imporant to create a sense of belonging. Have you ever talked about your stress with your boyfriend or girlfriend?"]')
df.add_user_transition(State.ROMAN4, State.ROMAN4_yes, r'<[!#ONT(ontyes)]>')
df.add_user_transition(State.ROMAN4, State.ROMAN4_no, r'<[!#ONT(ontno)]>')

df.add_system_transition(State.ROMAN4_yes, State.ROMAN5, r'[!"Oh really? And it did not work out? Then I think you should do something relaxing to releive your stress. What activity do you like to do during quanrantine?"]')
df.add_system_transition(State.ROMAN4_no, State.ROMAN5, r'[!"Maybe you should have a serious conversation with him or her. Telling each other whats on your mind can strengthen your relationship. You should do something to releive your stress. What activity do you like to do during quanrantine?"]')


'''COVID'''
df.add_user_transition(State.COVID0, State.COVID0_yes, r'<[!#ONT(ontyes)]>')
df.add_user_transition(State.COVID0, State.COVID0_no, r'<[!#ONT(ontno)]>')

df.add_system_transition(State.COVID0_yes, State.COVID1, r'[!"It is nice to still be able to see each other! I think everyone must be super stressed under this chaotic situation... Honestly, I think doing some fun activities might reduce some of your stress. What activity do you like to do during quarantine?"]')
df.add_system_transition(State.COVID0_no, State.COVID1, r'[!"Oh...I am guessing this stress is coming from the fact that you cannot see each other. Not able to see my friends and talk about how our life suck is stressing me out. But doing some fun activities help me relax a lot. What activity do you like to do during quarantine?"]')

df.add_user_transition(State.COVID1, State.COVID1_game, r'<[!#ONT(ontgames)]>')
df.add_user_transition(State.COVID1, State.COVID1_food, r'<[!#ONT(ontfood)]>')
df.add_user_transition(State.COVID1, State.COVID1_video, r'<[!#ONT(ontreadwatch)]>')
df.add_user_transition(State.COVID1, State.COVID1_socialApp, r'<[!#ONT(ontsocialApp)]>')
df.add_user_transition(State.COVID1, State.COVID1_class, r'<[!#ONT(ontclass)]>')
df.add_user_transition(State.COVID1, State.COVID1_music, r'<[!#ONT(ontmusic)]>')



df.add_user_transition(State.BREAKUP4, State.COVID1_game, r'<[!#ONT(ontgames)]>')
df.add_user_transition(State.BREAKUP4, State.COVID1_food, r'<[!#ONT(ontfood)]>')
df.add_user_transition(State.BREAKUP4, State.COVID1_video, r'<[!#ONT(ontreadwatch)]>')
df.add_user_transition(State.BREAKUP4, State.COVID1_socialApp, r'<[!#ONT(ontsocialApp)]>')
df.add_user_transition(State.BREAKUP4, State.COVID1_class, r'<[!#ONT(ontclass)]>')
df.add_user_transition(State.BREAKUP4, State.COVID1_music, r'<[!#ONT(ontmusic)]>')
df.add_user_transition(State.SINGLE3, State.COVID1_game, r'<[!#ONT(ontgames)]>')
df.add_user_transition(State.SINGLE3, State.COVID1_food, r'<[!#ONT(ontfood)]>')
df.add_user_transition(State.SINGLE3, State.COVID1_video, r'<[!#ONT(ontreadwatch)]>')
df.add_user_transition(State.SINGLE3, State.COVID1_socialApp, r'<[!#ONT(ontsocialApp)]>')
df.add_user_transition(State.SINGLE3, State.COVID1_class, r'<[!#ONT(ontclass)]>')
df.add_user_transition(State.SINGLE3, State.COVID1_music, r'<[!#ONT(ontmusic)]>')
df.add_user_transition(State.ROMAN5, State.COVID1_game, r'<[!#ONT(ontgames)]>')
df.add_user_transition(State.ROMAN5, State.COVID1_food, r'<[!#ONT(ontfood)]>')
df.add_user_transition(State.ROMAN5, State.COVID1_video, r'<[!#ONT(ontreadwatch)]>')
df.add_user_transition(State.ROMAN5, State.COVID1_socialApp, r'<[!#ONT(ontsocialApp)]>')
df.add_user_transition(State.ROMAN5, State.COVID1_class, r'<[!#ONT(ontclass)]>')
df.add_user_transition(State.ROMAN5, State.COVID1_music, r'<[!#ONT(ontmusic)]>')

df.add_system_transition(State.COVID1_game, State.COVID2, r'[!"I do like to play games too! Playing games are so stress releiving. All of my friends are playing animal crossing, and they even skip the online lecture just to play it... Speaking of that, are you also taking online classes?"]')
df.add_system_transition(State.COVID1_food, State.COVID2, r'[!"You are a foodie huh? I do not know why but I feel so happy while eating. Cook, eat, sleep, taking online classes, that is bascially the summary of my life now. Are you also taking online classes?"]')
df.add_system_transition(State.COVID1_video, State.COVID2, r'[!"Same! I have been reading a lot of books and watching a lot of shows besides taking online classes. Are you also taking online classes?"]')
df.add_system_transition(State.COVID1_socialApp, State.COVID2, r'[!"Wow, even the coronavirus cannot stop you from socializing. I have not been texting with my friends a lot since school closed. Oh but I do see them on zoom. Are you also taking online classes?"]')
df.add_system_transition(State.COVID1_music, State.COVID2, r'[!"I am also a music person! Listening to music is so soothing right? I have been listening a lot of Lauv and Post Malone lately. I love listening to them while doing my homework. Are you also taking online classes?"]')
df.add_user_transition(State.COVID2, State.COVID2_yes, r'<[!#ONT(ontyes)]>')
df.add_user_transition(State.COVID2, State.COVID2_no, r'<[!#ONT(ontno)]>')

df.add_system_transition(State.COVID1_class, State.COVID3, r'[!"Oh really? I am taking online classes too! But I do not think taking online classes is a fun activity to do...How are you feeling about this transition to remote learning?"]')
df.add_system_transition(State.COVID2_yes, State.COVID3, r'[!"Nice! Feels so good to know someone is also suffering with me. How are you feeling about this transition to remote learning?"]')
df.add_user_transition(State.COVID3, State.COVID3_like, r'<{[!#ONT(ontlike)]}>')
df.add_user_transition(State.COVID3, State.COVID3_dislike, r'<{[!#ONT(ontdislike)]}>')

df.add_system_transition(State.COVID2_no, State.COVIDEND, r'[!"I am so jealous of you! Taking online classes are just so awful. Well, I have class in 5 minutes so I have to leave. It was so nice talking to you. Have a nice day!"]')
df.add_system_transition(State.COVID3_like, State.COVIDEND, r'[!"Wow you are the minority! Most of the students do not adjust well with this sudden change of learning mode. I hate it so much because I have to take class at 4am. Well, I have class in 5 minutes... It was so nice talking to you!"]')
df.add_system_transition(State.COVID3_dislike, State.COVIDEND, r'[!"Yeah right? I feel that too. I also hate taking classes at 4 am... You should join the zoom memes page on facebook if you havent! Well, I have class in 5 minutes... It was so nice talking to you!"]')



################ ERROR ################
df.set_error_successor(State.PROMPT0_savage, State.PROMPT_ERR)
df.set_error_successor(State.LOVE0, State.LOVE0_ERR)
df.set_error_successor(State.SINGLE0, State.SINGLE0_ERR)
df.set_error_successor(State.SINGLE1, State.SINGLE1_ERR)
df.set_error_successor(State.SINGLE2, State.SINGLE2_ERR)
df.set_error_successor(State.SINGLE3, State.SINGLE3_ERR)
df.add_system_transition(State.PROMPT_ERR, State.LOVE0, r'[!"You must be stressed about love somtimes right? Are you currently in a relationship?"]')
df.add_system_transition(State.LOVE0_ERR, State.SINGLE0, r'[!"I mean sometimes being single is not a bad thing. You get to do whatever you want without needing to care about how your boyfriend or girlfriend might feel. How long have you been single?"]')
df.add_system_transition(State.SINGLE0_ERR, State.SINGLE1, r'[!"Its okay you are not alone, I have been single for a while too. How often are you feeling stressed about being single?"]')
df.add_system_transition(State.SINGLE1_ERR, State.SINGLE2, r'[!"Feeling stressed about it probably means you care about yourself a lot, but stressing too much is not good for your health. Do you think you have a high standard?"]')
df.add_system_transition(State.SINGLE2_ERR, State.SINGLE3, r'[!"I was once very desperate for a relationship but ended up getting none. And after I gave up, it came to me unexpectedly. Stange huh? You should focus more on yourself, what do you like to do during quarantine?"]')
df.add_system_transition(State.SINGLE3_ERR, State.COVID2, r'[!"That sounds super interesting! I should try that next time when I have less homework. I guess sleeping is my only destress activity... Are you also taking online classes?"]')
df.set_error_successor(State.ROMAN0, State.ROMAN0_ERR)
df.set_error_successor(State.ROMAN1, State.ROMAN1_ERR)
df.set_error_successor(State.ROMAN2, State.ROMAN2_ERR)
df.set_error_successor(State.ROMAN3, State.ROMAN3_ERR)
df.set_error_successor(State.ROMAN4, State.ROMAN4_ERR)
df.set_error_successor(State.ROMAN5, State.ROMAN5_ERR)
df.add_system_transition(State.ROMAN0_ERR, State.ROMAN1, r'[!"That is quite a while! I am assuming you guys are in a more uncertain and unstable phase. How often do you feel stressed about your relationship?"]')
df.add_system_transition(State.ROMAN1_ERR, State.ROMAN2, r'[!"It is totally normal to be stressed about relationship sometimes. Is the coronavirus causing any stress in your relationship?"]')
df.add_system_transition(State.ROMAN2_ERR, State.ROMAN3, r'[!"I guess the coronavirus is innocent. Let me try to make use of what I learned from my psychology class. The theory of love suggests that love in composed by intimacy, passion, and commitment. Which one do you think is lacking from your relationship?"]')
df.add_system_transition(State.ROMAN3_ERR, State.ROMAN4, r'[!"Oh I see. Last year I felt like my girlfriend and I are losing passion because of long distance. Guess what safe our relationship? A lof of s...I think you know the answer. Have you ever talked about your stress with your boyfriend or girlfriend?"]')
df.add_system_transition(State.ROMAN4_ERR, State.ROMAN5, r'[!"Maybe you should have a serious conversation with him or her. Telling each other whats on your mind can strengthen your relationship. You should do something to releive your stress. What activity do you like to do during quanrantine?"]')
df.add_system_transition(State.ROMAN5_ERR, State.COVID2, r'[!"That sounds super interesting! I should try that next time when I have less homework. I guess sleeping is my only destress activity... Are you also taking online classes?"]')
df.set_error_successor(State.BREAKUP0, State.BREAKUP0_ERR)
df.set_error_successor(State.BREAKUP1, State.BREAKUP1_ERR)
df.set_error_successor(State.BREAKUP2, State.BREAKUP2_ERR)
df.set_error_successor(State.BREAKUP3, State.BREAKUP3_ERR)
df.set_error_successor(State.BREAKUP4, State.BREAKUP4_ERR)
df.add_system_transition(State.BREAKUP0_ERR, State.BREAKUP1, r'[!"I see...you must be feeling lost and empty. Did this breakup happen because of the coronavirus?"]')
df.add_system_transition(State.BREAKUP1_ERR, State.BREAKUP2, r'[!"I guess the coronavirus is not the one to blame. Let me try to make use of what I learned from my psychology class. The theory of love suggests that love in composed by intimacy, passion, and commitment. Which one do you think is lacking from your relationship?"]')
df.add_system_transition(State.BREAKUP2_ERR, State.BREAKUP3, r'[!"Oh I see. Last year my girlfriend broke up with me because of the her insecurity caused by long distance and I learned the importance of committment. Just curious, do you want to get back together?"]')
df.add_system_transition(State.BREAKUP3_ERR, State.BREAKUP4, r'[!"I think you are ready to move on! Time to focus self-development, and dont forget to love yourself more. During quarantine, I really enjoy trying new stuff. What activity do you like to do while in quarantine?"]')
df.add_system_transition(State.BREAKUP4_ERR, State.COVID2, r'[!"That sounds super interesting! I should try that next time when I have less homework. I guess sleeping is my only destress activity... Are you also taking online classes?"]')
df.set_error_successor(State.COVID0, State.COVID0_ERR)
df.set_error_successor(State.COVID1, State.COVID1_ERR)
df.set_error_successor(State.COVID2, State.COVID2_ERR)
df.set_error_successor(State.COVID3, State.COVID3_ERR)
df.add_system_transition(State.COVID0_ERR, State.COVID1, r'[!"Oh...I am guessing this stress is coming from the fact that you cannot see each other. It is a lot to handle when away from everyone, you are not alone. Doing some fun activities might help you relax! What activity do you like to do during quarantine?"]')
df.add_system_transition(State.COVID1_ERR, State.COVID2, r'[!"That sounds super interesting! I should try that next time when I have less homework. I guess sleeping is my only destress activity... Oh by the way, are you also taking online classes?"]')
df.add_system_transition(State.COVID2_ERR, State.COVID3, r'[!"Nice! Feels so good to know someone is also suffering with me haha. How are you feeling about this transition to remote learning?"]')
df.add_system_transition(State.COVID3_ERR, State.COVIDEND, r'[!"I personally hate it so much. Can you imagine taking classes at 4 am? Ugh... You should join the zoom memes page on facebook if you havent! Well, I have class in 5 minutes so I have to leave. It was so nice talking to you!"]')






if __name__ == '__main__':
    df.run(debugging=False)