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
                    'self assertive',
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
            "always",
            "constantly",
            "frequently",
            "regularly",
            "often",
            "hourly",
            "daily",
            "weekly",
            "biweekly",
            "all the time",
            "every second",
            "every minute",
            "every week",
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
            "every month",
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
            "maybe",
            "perhaps",
            "sure",
            "Of Course",
            "of course",
            "Sure",
            "i guess",
            "i think so",
            "do",
            "maybe",
            "perhaps"
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
            "maybe",
            "perhaps",
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
        for a in ["school","grades","grade","majors","major","grad school","classes","graduate school","grad schools",
                  "graduate schools","exams","quizzes","papers","essays","assignments","projects","group projects"]:
            if str(vars['S_S']) == a:
                return 'be in the current education system'
        if str(vars['S_S'])=="social anxiety" or str(vars['S_S'])=="social phobia" or str(vars['S_S'])=="interviews" or str(vars['S_S'])=="interview":
                return 'be evaluated by average people'
        else:
            return 'be just a follower but not a leader in your field'

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
            return 'You have such a bubbly personality. I am sure you will succeed in anything you do. Talk to you later!'
        if vars['neuroticsm'] > 50 and vars['extroversion'] <= 50:
            return 'I can tell that you love stepping out of your comfort zone. Love that side of you. Talk to you later!'
        if vars['neuroticsm'] <= 50 and vars['extroversion'] <= 50:
            return 'I feel so composed after talking to you. So lucky to learn about your perspective on things. Best of luck with your college life!'
        if vars['neuroticsm'] <= 50 and vars['extroversion'] > 50:
            return 'Your ability to handle stress is beyond impressive. See you!'



############################################### school macros start here

class help_ss(Macro):
    def run(self, ngrams, vars, args):
        for a_time_topic in ["time","workload","everything","too much work","balance","tight schedule","busy","little time","busy schedule","schoolwork","balancing","duties","responsibilities","multitasks","multitasking","multitask","multiple assignments"]:
            if str(vars['S_S']) == a_time_topic:
                return "time management"
        for a_major_related_topic in ["major","majors"]:
            if str(vars['S_S']) == a_major_related_topic:
                return "classes for your current "+str(vars['S_S'])
        for a_future_related_topic in ["jobs","internships","career","interviews","interview","internship","job","graduate school","grad school","grad schools","graduate schools","internships hunting","internship hunting","jobs hunting","job hunting","jobs search","job search","internship search","internships search","internship application","internships application","internship applications","internships application","job applications","job application"]:
            if str(vars['S_S']) == a_future_related_topic:
                return "interviews in general"
        for a_general_topic in ["school","grades","grade","classes","work","research","exams","quizzes","assignments","papers","essays","projects","group projects"]:
            if str(vars['S_S'])== a_general_topic:
                return str(vars['S_S'])
        if str(vars['S_S'])=="social anxiety" or str(vars['S_S'])=="social phobia" or str(vars['S_S'])=="social events" or str(vars['S_S'])=="social situations":
            return "social situations"
        if str(vars['S_S']) == 'wedding' or str(vars['S_S']) == "wedding" or str(vars['S_S']) == "gathering" or str(vars['S_S']) == 'gathering' or str(vars['S_S']) == 'meeting' or str(vars['S_S'])=="meeting":
            return 'that '+str(vars['S_S'])
        elif str(vars['S_S'])[-3:] == 'ing' or str(vars['S_S'])[-3:] == "ing":
            return str(vars['S_S'])
        elif str(vars['S_S'])[0] == 'a' or str(vars['S_S'])[0] == "a" or str(vars['S_S'])[0] == 'e' or str(vars['S_S'])[0] == "e" or str(vars['S_S'])[0] == 'i' or str(vars['S_S'])[0] ==  "i" or str(vars['S_S'])[0] == 'o' or str(vars['S_S'])[0] == "o" or str(vars['S_S'])[0] == 'x' or str(vars['S_S'])[0] == "x":
            return 'that '+str(vars['S_S'])
        else:
            return 'that '+str(vars['S_S'])

class class_ss(Macro):
    def run(self, ngrams, vars, args):
        vars['S_S']=vars['class']+" class"
        if str(vars['S_S'])[0] == 'a' or str(vars['S_S'])[0] == "a" or str(vars['S_S'])[0] == 'e' or str(vars['S_S'])[0] == "e" or str(vars['S_S'])[0] == 'i' or str(vars['S_S'])[0] ==  "i" or str(vars['S_S'])[0] == 'o' or str(vars['S_S'])[0] == "o" or str(vars['S_S'])[0] == 'x' or str(vars['S_S'])[0] == "x":
            return 'an '+str(vars['S_S'])
        else:
            return 'a '+str(vars['S_S'])

class school_n1_often(Macro):
    def run(self, ngrams, vars, args):
        if 'neuroticsm' in vars.keys():
            vars['neuroticsm'] += 30
        else:
            vars['neuroticsm'] = 30
        return ''
class school_n1_sometimes(Macro):
    def run(self, ngrams, vars, args):
        if 'neuroticsm' in vars.keys():
            vars['neuroticsm'] += 10
        else:
            vars['neuroticsm'] = 10
        return ''
class school_n1_never(Macro):
    def run(self, ngrams, vars, args):
        if 'neuroticsm' in vars.keys():
            vars['neuroticsm'] += -10
        else:
            vars['neuroticsm'] = -10
        return ''

class school_n2_often(Macro):
    def run(self, ngrams, vars, args):
        if 'neuroticsm' in vars.keys():
            vars['neuroticsm'] += 30
        else:
            vars['neuroticsm'] = 30
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
            vars['neuroticsm'] = -20
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

class school_n4_present(Macro):
    def run(self, ngrams, vars, args):
        if 'neuroticsm' in vars.keys():
            vars['neuroticsm'] -= 20
        else:
            vars['neuroticsm'] =-20
        return ''
class school_n4_future(Macro):
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
class school_n5_formajor(Macro):
    def run(self, ngrams, vars, args):
        if 'neuroticsm' in vars.keys():
            vars['neuroticsm'] -= 30
        else:
            vars['neuroticsm'] = -30
        return ''

class school_n5_notformajor(Macro):
    def run(self, ngrams, vars, args):
        if 'neuroticsm' in vars.keys():
            vars['neuroticsm'] += 0
        else:
            vars['neuroticsm'] = 0
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
            vars['neuroticsm'] += 40
        else:
            vars['neuroticsm'] = 40
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

class high_n(Macro):

    def run(self, ngrams, vars, args):
        if 'neuroticsm' in vars.keys():
            vars['neuroticsm'] += 60
        else:
            vars['neuroticsm'] = 60
        return ''

class mid_n(Macro):

    def run(self, ngrams, vars, args):
        if 'neuroticsm' in vars.keys():
            vars['neuroticsm'] += 30
        else:
            vars['neuroticsm'] = 30
        return ''

class low_n(Macro):

    def run(self, ngrams, vars, args):
        if 'neuroticsm' in vars.keys():
            vars['neuroticsm'] += 0
        else:
            vars['neuroticsm'] = 0
        return ''

class high_e(Macro):
    def run(self, ngrams, vars, args):
        if 'extroversion' in vars.keys():
            vars['extroversion'] += 60
        else:
            vars['extroversion'] = 60
        return ''

class result_relationship(Macro):

    def run(self, ngrams, vars, args):
        if 'neuroticsm' not in vars.keys():
            vars['neuroticsm'] = 0
        if 'extroversion' not in vars.keys():
            vars['extroversion'] = 0

        if vars['neuroticsm'] > 50 and vars['extroversion'] > 50:
            return 'I really enjoy talking to you! Do not forget to spend time on self care and self development!'
        if vars['neuroticsm'] > 50 and vars['extroversion'] <= 50:
            return 'I really enjoy talking to you and I bet others do too. Do not forget to love yourself more!'
        if vars['neuroticsm'] <= 50 and vars['extroversion'] <= 50:
            return 'I really like talking to you and I bet others do too! When life gives you lemons, just make lemonade! Talk to you later.'
        if vars['neuroticsm'] <= 50 and vars['extroversion'] > 50:
            return 'I really enjoy talking to you! If life gives you lemons, just make lemonade!'



############################################### school macros end here

class State(Enum):
    START = auto()
    PROMPT = auto()
    PROMPT_ERR = auto()
    BREAKUP_OPT= auto()
    BREAKUP_AGG = auto()
    BREAKUP_SAV = auto()
    #############################relationship covid section#################
    COVID0_yes = auto()
    COVID0_no = auto()
    COVID1 = auto()
    COVID1_game = auto()
    COVID1_food = auto()
    COVID1_video = auto()
    COVID1_socialApp = auto()
    COVID1_class = auto()
    COVID1_music = auto()
    COVID1_ERR = auto()
    COVID2 = auto()
    COVID2_ERR = auto()
    COVID2_yes = auto()
    COVID2_no = auto()
    COVID3 = auto()
    COVID3_ERR = auto()
    COVID3_like = auto()
    COVID3_dislike = auto()
    COVIDEND = auto()
    ########################################################################
    LOVE0 = auto()
    #######################relationship_sav
    SINGLEo2 = auto()
    LOVE0_ERR2 = auto()
    SINGLE02 = auto()
    SINGLE0_short2 = auto()
    SINGLE0_mid2 = auto()
    SINGLE0_long2 = auto()
    SINGLE0_ERR2 = auto()
    SINGLE12 = auto()
    SINGLE1_ERR2 = auto()
    SINGLE1_often2 = auto()
    SINGLE1_sometimes2 = auto()
    SINGLE1_never2 = auto()
    SINGLE22 = auto()
    SINGLE2_ERR2 = auto()
    SINGLE2_yes2 = auto()
    SINGLE2_no2 = auto()
    SINGLE32 = auto()
    SINGLE3_ERR2 = auto()
    ROMANo2 = auto()
    BREAKUP02 = auto()
    BREAKUP0_ERR2 = auto()
    BREAKUP0_short2 = auto()
    BREAKUP0_mid2 = auto()
    BREAKUP0_long2 = auto()
    BREAKUP12 = auto()
    BREAKUP1_ERR2 = auto()
    BREAKUP1_02 = auto()
    BREAKUP22 = auto()
    BREAKUP2_ERR2 = auto()
    BREAKUP2_intimacy2 = auto()
    BREAKUP2_passion2 = auto()
    BREAKUP2_commitment2 = auto()
    BREAKUP32 = auto()
    BREAKUP3_ERR2 = auto()
    BREAKUP3_yes2 = auto()
    BREAKUP3_no2 = auto()
    BREAKUP42 = auto()
    BREAKUP4_ERR2 = auto()
    ROMAN02 = auto()
    ROMAN0_ERR2 = auto()
    ROMAN0_short2 = auto()
    ROMAN0_mid2 = auto()
    ROMAN0_long2 = auto()
    ROMAN12 = auto()
    ROMAN1_ERR2 = auto()
    ROMAN1_often2 = auto()
    ROMAN1_sometimes2 = auto()
    ROMAN1_never2 = auto()
    ROMAN22 = auto()
    ROMAN2_ERR2 = auto()
    ROMAN2_02 = auto()
    ROMAN32 = auto()
    ROMAN3_ERR2 = auto()
    ROMAN3_intimacy2 = auto()
    ROMAN3_passion2 = auto()
    ROMAN3_commitment2 = auto()
    ROMAN42 = auto()
    ROMAN4_ERR2 = auto()
    ROMAN4_yes2 = auto()
    ROMAN4_no2 = auto()
    ROMAN52 = auto()
    ROMAN5_ERR2 = auto()
    COVID02 = auto()
    COVID0_ERR2 = auto()
    #######################relationship_agr
    SINGLE = auto()
    LOVE0_ERR= auto()
    SINGLE0 = auto()
    SINGLE0_short = auto()
    SINGLE0_mid = auto()
    SINGLE0_long = auto()
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
    ROMAN = auto()
    BREAKUP0 = auto()
    BREAKUP0_ERR = auto()
    BREAKUP0_short = auto()
    BREAKUP0_mid = auto()
    BREAKUP0_long = auto()
    BREAKUP1 = auto()
    BREAKUP1_ERR = auto()
    BREAKUP1_0 = auto()
    BREAKUP2 = auto()
    BREAKUP2_ERR = auto()
    BREAKUP2_intimacy = auto()
    BREAKUP2_passion = auto()
    BREAKUP2_commitment = auto()
    BREAKUP3 = auto()
    BREAKUP3_ERR = auto()
    BREAKUP3_yes = auto()
    BREAKUP3_no = auto()
    BREAKUP4 = auto()
    BREAKUP4_ERR = auto()
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
    COVID0 = auto()
    COVID0_ERR = auto()
    #######################relationship_opt
    SINGLEo1 = auto()
    LOVE0_ERR1 = auto()
    SINGLE01 = auto()
    SINGLE0_short1 = auto()
    SINGLE0_mid1 = auto()
    SINGLE0_long1 = auto()
    SINGLE0_ERR1 = auto()
    SINGLE11 = auto()
    SINGLE1_ERR1 = auto()
    SINGLE1_often1 = auto()
    SINGLE1_sometimes1 = auto()
    SINGLE1_never1 = auto()
    SINGLE21 = auto()
    SINGLE2_ERR1 = auto()
    SINGLE2_yes1 = auto()
    SINGLE2_no1 = auto()
    SINGLE31 = auto()
    SINGLE3_ERR1 = auto()
    ROMANo1 = auto()
    BREAKUP01 = auto()
    BREAKUP0_ERR1 = auto()
    BREAKUP0_short1 = auto()
    BREAKUP0_mid1 = auto()
    BREAKUP0_long1 = auto()
    BREAKUP11 = auto()
    BREAKUP1_ERR1 = auto()
    BREAKUP1_01 = auto()
    BREAKUP21 = auto()
    BREAKUP2_ERR1 = auto()
    BREAKUP2_intimacy1 = auto()
    BREAKUP2_passion1 = auto()
    BREAKUP2_commitment1 = auto()
    BREAKUP31 = auto()
    BREAKUP3_ERR1 = auto()
    BREAKUP3_yes1 = auto()
    BREAKUP3_no1 = auto()
    BREAKUP41 = auto()
    BREAKUP4_ERR1 = auto()
    ROMAN01 = auto()
    ROMAN0_ERR1 = auto()
    ROMAN0_short1 = auto()
    ROMAN0_mid1 = auto()
    ROMAN0_long1 = auto()
    ROMAN11 = auto()
    ROMAN1_ERR1 = auto()
    ROMAN1_often1 = auto()
    ROMAN1_sometimes1 = auto()
    ROMAN1_never1 = auto()
    ROMAN21 = auto()
    ROMAN2_ERR1 = auto()
    ROMAN2_01 = auto()
    ROMAN31 = auto()
    ROMAN3_ERR1 = auto()
    ROMAN3_intimacy1 = auto()
    ROMAN3_passion1 = auto()
    ROMAN3_commitment1 = auto()
    ROMAN41 = auto()
    ROMAN4_ERR1 = auto()
    ROMAN4_yes1 = auto()
    ROMAN4_no1 = auto()
    ROMAN51 = auto()
    ROMAN5_ERR1 = auto()
    COVID01 = auto()
    COVID0_ERR1 = auto()
########social events stressor
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
    SCORE1 = auto()
    SCORE1_pos = auto()
    SCORE1_neg =auto()
    ####################
    ####################school savage
    PROMPT0_savage = auto()
    PROMPT0_schoolevent_savage = auto()
    PROMPT0_schoolgeneral_savage = auto()
    PROMPT0_schooltime_savage = auto()
    PROMPT0_schoolcovid_savage = auto()
    PROMPT0_schoolcourse_savage = auto()
    PROMPT_oolstressfr1 = auto()
    PROMPT_majorreq1= auto()
    PROMPT_major1 = auto()
    PROMPT_forclass1 =auto()
    PROMPT_whichclass1=auto()
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
    PROMPT_major_err1 = auto()
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
    PROMPT_forclass_err1 =auto()
    PROMPT_whichclass_err1 =auto()
    #####user states
    PROMPT_oolstressfr_often1 = auto()
    PROMPT_oolstressfr_sometimes1 = auto()
    PROMPT_oolstressfr_never1 = auto()
    PROMPT_oolfreq_often1 = auto()
    PROMPT_oolfreq_sometimes1 = auto()
    PROMPT_oolfreq_never1 = auto()
    PROMPT_majorreq_yes1 = auto()
    PROMPT_majorreq_yesmajor1 = auto()
    PROMPT_major_re1 =auto()
    PROMPT_forclass_yes1 =auto()
    PROMPT_forclass_yesclass1 =auto()
    PROMPT_oolpast_well1 = auto()
    PROMPT_oolpast_bad1 = auto()
    PROMPT_oolgoal_re1 = auto()
    PROMPT_oolgoalalign_yes1 = auto()
    PROMPT_oolgoalalign_no1 = auto()
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
    PROMPT_oolhelp_person_yes1 =auto()
    PROMPT_oolhelp_person_yesperson1 =auto()
    PROMPT_oolstudyspot_bedroom1 = auto()
    PROMPT_oolstudyspot_livingroom1 = auto()
    PROMPT_oolzoom_yes1 =auto()
    PROMPT_oolzoom_no1 = auto()
    ####################################
    ############School Agreeable########
    PROMPT0_agg = auto()
    PROMPT0_schoolevent_agg = auto()
    PROMPT0_schoolgeneral_agg = auto()
    PROMPT0_schooltime_agg = auto()
    PROMPT0_schoolcovid_agg = auto()
    PROMPT0_schoolcourse_agg = auto()
    PROMPT_oolstressfr2 = auto()
    PROMPT_majorreq2 = auto()
    PROMPT_major2 = auto()
    PROMPT_forclass2 = auto()
    PROMPT_whichclass2 = auto()
    PROMPT_oolfreq2 = auto()
    PROMPT_oolpast2 = auto()
    PROMPT_oolgoal2 = auto()
    PROMPT_oolgoalalign2 = auto()
    PROMPT_oolcovidworry2 = auto()
    PROMPT_oolcovidworry_severity2 = auto()
    PROMPT_oolonline2 = auto()
    PROMPT_oolonline_reasongood2 = auto()
    PROMPT_oolonline_reasonbad2 = auto()
    PROMPT_oolhelp_person2 = auto()
    PROMPT_oolhelp_yesno2 = auto()
    PROMPT_oolstudyspot2 = auto()
    PROMPT_oolzoom2 = auto()
    #####user error states
    PROMPT_oolstressfr_err2 = auto()
    PROMPT_major_err2 = auto()
    PROMPT_oolfreq_err2 = auto()
    PROMPT_oolpast_err2 = auto()
    PROMPT_oolgoal_err2 = auto()
    PROMPT_oolgoalalign_err2 = auto()
    PROMPT_oolcovidworry_err2 = auto()
    PROMPT_oolonline_err2 = auto()
    PROMPT_oolonline_dislike_err2 = auto()
    PROMPT_oolonline_like_err2 = auto()
    PROMPT_oolhelp_person_err2 = auto()
    PROMPT_oolhelp_yesno_err2 = auto()
    PROMPT_oolstudyspot_err2 = auto()
    PROMPT_oolzoom_err2 = auto()
    PROMPT_forclass_err2 = auto()
    PROMPT_whichclass_err2 = auto()
    #####user states
    PROMPT_oolstressfr_often2 = auto()
    PROMPT_oolstressfr_sometimes2 = auto()
    PROMPT_oolstressfr_never2 = auto()
    PROMPT_oolfreq_often2 = auto()
    PROMPT_oolfreq_sometimes2 = auto()
    PROMPT_oolfreq_never2 = auto()
    PROMPT_majorreq_yes2 = auto()
    PROMPT_majorreq_yesmajor2 = auto()
    PROMPT_major_re2 = auto()
    PROMPT_forclass_yes2 = auto()
    PROMPT_forclass_yesclass2 = auto()
    PROMPT_oolpast_well2 = auto()
    PROMPT_oolpast_bad2 = auto()
    PROMPT_oolgoal_re2 = auto()
    PROMPT_oolgoalalign_yes2 = auto()
    PROMPT_oolgoalalign_no2 = auto()
    PROMPT_oolonline_well2 = auto()
    PROMPT_oolonline_bad2 = auto()
    PROMPT_oolonlinereason_prodgood2 = auto()
    PROMPT_oolonlinereason_socialgood2 = auto()
    PROMPT_oolonlinereason_flexgood2 = auto()
    PROMPT_oolonlinereason_prodbad2 = auto()
    PROMPT_oolonlinereason_socialbad2 = auto()
    PROMPT_oolonlinereason_flexbad2 = auto()
    PROMPT_oolhelp_person_re2 = auto()
    PROMPT_oolhelp_yes2 = auto()
    PROMPT_oolhelp_no2 = auto()
    PROMPT_oolhelp_person_yes2 =auto()
    PROMPT_oolhelp_person_yesperson2 =auto()
    PROMPT_oolstudyspot_bedroom2 = auto()
    PROMPT_oolstudyspot_livingroom2 = auto()
    PROMPT_oolzoom_yes2 = auto()
    PROMPT_oolzoom_no2 = auto()
    #####################################
    ############School Optimistic########
    PROMPT0_opt = auto()
    PROMPT0_schoolevent_opt = auto()
    PROMPT0_schoolgeneral_opt = auto()
    PROMPT0_schooltime_opt = auto()
    PROMPT0_schoolcovid_opt = auto()
    PROMPT0_schoolcourse_opt = auto()
    PROMPT_oolstressfr3 = auto()
    PROMPT_majorreq3 = auto()
    PROMPT_major3 = auto()
    PROMPT_forclass3 = auto()
    PROMPT_whichclass3 = auto()
    PROMPT_oolfreq3 = auto()
    PROMPT_oolpast3 = auto()
    PROMPT_oolgoal3 = auto()
    PROMPT_oolgoalalign3 = auto()
    PROMPT_oolcovidworry3 = auto()
    PROMPT_oolcovidworry_severity3 = auto()
    PROMPT_oolonline3 = auto()
    PROMPT_oolonline_reasongood3 = auto()
    PROMPT_oolonline_reasonbad3 = auto()
    PROMPT_oolhelp_person3 = auto()
    PROMPT_oolhelp_yesno3 = auto()
    PROMPT_oolstudyspot3 = auto()
    PROMPT_oolzoom3 = auto()
    #####user error states
    PROMPT_oolstressfr_err3 = auto()
    PROMPT_major_err3 = auto()
    PROMPT_oolfreq_err3 = auto()
    PROMPT_oolpast_err3 = auto()
    PROMPT_oolgoal_err3 = auto()
    PROMPT_oolgoalalign_err3 = auto()
    PROMPT_oolcovidworry_err3 = auto()
    PROMPT_oolonline_err3 = auto()
    PROMPT_oolonline_dislike_err3 = auto()
    PROMPT_oolonline_like_err3 = auto()
    PROMPT_oolhelp_person_err3 = auto()
    PROMPT_oolhelp_yesno_err3 = auto()
    PROMPT_oolstudyspot_err3 = auto()
    PROMPT_oolzoom_err3 = auto()
    PROMPT_forclass_err3 = auto()
    PROMPT_whichclass_err3 = auto()
    #####user states
    PROMPT_oolstressfr_often3 = auto()
    PROMPT_oolstressfr_sometimes3 = auto()
    PROMPT_oolstressfr_never3 = auto()
    PROMPT_oolfreq_often3 = auto()
    PROMPT_oolfreq_sometimes3 = auto()
    PROMPT_oolfreq_never3 = auto()
    PROMPT_majorreq_yes3 = auto()
    PROMPT_majorreq_yesmajor3 = auto()
    PROMPT_major_re3 = auto()
    PROMPT_forclass_yes3 = auto()
    PROMPT_forclass_yesclass3 = auto()
    PROMPT_oolpast_well3 = auto()
    PROMPT_oolpast_bad3 = auto()
    PROMPT_oolgoal_re3 = auto()
    PROMPT_oolgoalalign_yes3 = auto()
    PROMPT_oolgoalalign_no3 = auto()
    PROMPT_oolonline_well3 = auto()
    PROMPT_oolonline_bad3 = auto()
    PROMPT_oolonlinereason_prodgood3 = auto()
    PROMPT_oolonlinereason_socialgood3 = auto()
    PROMPT_oolonlinereason_flexgood3 = auto()
    PROMPT_oolonlinereason_prodbad3 = auto()
    PROMPT_oolonlinereason_socialbad3 = auto()
    PROMPT_oolonlinereason_flexbad3 = auto()
    PROMPT_oolhelp_person_re3 = auto()
    PROMPT_oolhelp_yes3 = auto()
    PROMPT_oolhelp_no3 = auto()
    PROMPT_oolhelp_person_yes3 =auto()
    PROMPT_oolhelp_person_yesperson3 =auto()
    PROMPT_oolstudyspot_bedroom3 = auto()
    PROMPT_oolstudyspot_livingroom3 = auto()
    PROMPT_oolzoom_yes3 = auto()
    PROMPT_oolzoom_no3 = auto()



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
                    "every day",
                    "all the time",
                    "everyday",
                    "every hour",
                    "every second",
                    "every minute",
                    "every week",
                ],
            "ontsometimes":
                [
                    "every month",
                    "monthly",
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
                    "annual",
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
                    "dance party",
                    "volunteer activity",
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
                    "certainly",
                    "perhaps",
                    "maybe"
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
                    'admirable', 'energetic', 'lucky',"excellent",
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
                    "isn't very bad","ok","alright","not awful"
                ],
            'ontnegative':
                ['afraid',
                 "not good",
                 "not well",
                 "not great",
                 "not nice",
                 'bad',
                 'anxious',
                 'apprehensive',
                 'ashamed',
                 'cowardly',
                 'frightened',
                 'guilty',
                 'stuck',
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
                    "sing",
                    "guitar",
                    "piano",
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
                    "calming music",
                    "piano",
                    "guitar",
                    "violin",
                    "cello",
                    "banjo",
                    "oboe",
                    "recorder",
                    "clarinet",
                    "drum",
                    "drums"
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
                    "doing cover dances",
                    "dance"
                ],
            'ontreadwatch':
                [
                    "movies",
                    "movie",
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
                "essay",
                "research",
                "lab",
                "homework",
                "test"
                ],
            'ontschoolcourse':
                [
                "accounting",
                "econ",
                "anthropology",
                "arabic",
                "art",
                "art history",
                "astronomy",
                "baptist studies",
                "basic health sciences",
                "behavioral science",
                "biblical interpretation",
                "biblical languages",
                "biochem",
                "biochemistry",
                "biology",
                "biomedical engineering",
                "biomedical informatics",
                "biostatistics",
                "black church studies",
                "business",
                "bschool",
                "chem",
                "chemistry",
                "chinese",
                "classics",
                "comparative literature",
                "cs",
                "computer science",
                "comp sci",
                "creative writing",
                "writing",
                "dance",
                "media",
                "east asian studies",
                "economics",
                "educational studies",
                "english",
                "esl",
                "english as a second language",
                "environmental sciences",
                "environmental health",
                "environmental studies",
                "epidemiology",
                "ethical studies",
                "ethics",
                "film studies",
                "film and media",
                "finance",
                "french",
                "genetics",
                "german",
                "human health",
                "hebrew",
                "hindi",
                "health",
                "hispanic",
                "history",
                "human health",
                "ids",
                "interdisciplinary studies",
                "italian",
                "japanese",
                "latin",
                "jewish studies",
                "law",
                "linguistics",
                "marketing",
                "math",
                "mathematics",
                "medicine",
                "middle eastern",
                "asian studies",
                "music",
                "nbb",
                "neuroscience",
                "neuroscience behavioral science",
                "nursing",
                "pace",
                "pe",
                "philosophy",
                "physics",
                "poli sci",
                "political science",
                "portuguese",
                "psychology",
                "public health",
                "qtm",
                "quantitative theory and methods",
                "religion",
                "russian",
                "sociology",
                "psyc",
                "theater",
                "visual arts",
                "gender studies",
                "theological studies",
                "theater studies",
                "tibetan studies",
                "continuous writing class"
                "freshman seminar",
                "senior seminar",
                "physical education",
                "tourism",
                "graphic design",
                "fashion design",
                "ams",
                "applied math",
                "data science",
                "stats",
                "digital media"
                ],
            'ontschoolgeneral':
                [
                "interviews",
                "interview",
                "career",
                "school",
                "grade",
                "grades",
                "majors",
                "major",
                "internships",
                "classes",
                "jobs",
                "job",
                "internship",
                "grad school",
                "graduate school",
                "grad schools",
                "graduate schools",
                "internship hunting",
                "job search",
                "internships hunting",
                "internship application",
                "internships application",
                "jobs application",
                "job application",
                "jobs hunting",
                "jobs search",
                "job hunting",
                "work",
                "exams",
                "quizzes",
                "papers",
                "essays",
                "projects",
                "group projects",
                "assignments",
                "social phobia",
                "social anxiety",###even tho does not belong to school stressor same set of questions are applicable
                "social situations",
                "social events"
                ],
            'ontschooltime':
                [
                "everything",
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
                "busy",
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
                "choice",
                "choices",
                "environment",
                "self discipline",
                "self control",
                "too much freedom",
                "too flexible",
                "too much flexibility",
                "temptation",
                "too many options",
                "too many choices",
                "lazy",
                "laziness",
                "coffee",
                "stay up late",
                "sleep schedule",
                "procrastinate",
                "procrastinating",
                "too much time",
                "no goal",
                "no goals",
                "free time"
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
                "sucks",
                "lonely",
                "alone",
                "bored",
                "involved",
                "involvement"
                ],
            'ontprodbad':
                [
                "concentrate",
                "concentration",
                "focus",
                "motivation",
                "motivated",
                "not productive",
                "not as productive",
                "low productivity",
                "self control",
                "less motivated",
                "no longer feel motivated",
                "nothing done",
                "not efficient",
                "low efficiency"
                ],
            'ontflexgood':
                [
                "environment",
                "choice",
                "choices",
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
                "convenient",
                "saves time",
                "whenever",
                "wherever",
                "free",
                "quality plans"
                ],
            'ontsocialgood':
                [
                "social stress",
                "less participation",
                "less discussion",
                "participate",
                "more comfortable participating",
                "more comfortable asking questions",
                "learn less",
                "not judging",
                "group call",
                "zoom"
                ],
            'ontprodgood':
                [
                "more efficiently",
                "efficiency",
                "productivity",
                "productive",
                "focus more",
                "focus better",
                "concentrate better",
                "focus better",
                "more time",
                "more efficient",
                "faster",
                "two times speed"
                ],
            'ontbedroom':
                [
                "bedroom",
                "room",
                "bed",
                "bathtub"
                ],
            'ontlivingroom':
                [
                "dining area",
                "dining room",
                "kitchen",
                "living room",
                "livingroom",
                "garden",
                "backyard",
                "sofa",
                "couch"
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
                'breaks',
                'split up'
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
                'good',
                'love'
                 ],
             'ontdislike':
                [
                'hate',
                'dont like',
                'do not like',
                'dislike',
                'abhor',
                'detest',
                'awful'
                ]
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
                          'school_n5_formajor':school_n5_formajor(),'school_n5_notformajor':school_n5_notformajor(),'school_n4_present':school_n4_present(),'school_n4_future':school_n4_future(),
                          'school_e3_studyspot1_liv':school_e3_studyspot1_liv(),'school_e3_studyspot1_bed':school_e3_studyspot1_bed(),
                          'school_e3_studyspot2_zoom':school_e3_studyspot2_zoom(),'school_e3_studyspot2_nozoom':school_e3_studyspot2_nozoom(),
                          'school_e2_online1_like':school_e2_online1_like(),'school_e2_online1_dislike':school_e2_online1_dislike(),
                          'school_e2_online2_hiprod':school_e2_online2_hiprod(),'school_e2_online2_socialstress':school_e2_online2_socialstress(),
                          'school_e2_online2_loprod': school_e2_online2_loprod(),'school_e2_online2_lesssocial': school_e2_online2_lesssocial(),
                          'school_e1_mentor1_person':school_e1_mentor1_person(),'school_e1_mentor1_err':school_e1_mentor1_err(),
                          'school_e1_mentor2_yes':school_e1_mentor2_yes(),'school_e1_mentor2_no':school_e1_mentor2_no(),
                          'school_n_covidworried':school_n_covidworried(),'school_n_covidinfect':school_n_covidinfect,'school_n_covidnotworr':school_n_covidnotworr,
                          'ool_or_eer':ool_or_eer(),'help_ss':help_ss(),'class_ss':class_ss(), 'high_n':high_n(), 'mid_n':mid_n(), 'low_n':low_n(), 'high_e':high_e(), 'result_relationship':result_relationship()})

df.precache_transitions()
#######InitialPrompt######
df.add_system_transition(State.START, State.PROMPT0_savage,r'[!"What you are stressed about?"]')
df.add_system_transition(State.START, State.PROMPT0_agg,r'[!"What you are stressed about?"]')
df.add_system_transition(State.START, State.PROMPT0_opt,r'[!"What you are stressed about?"]')
########Randomized Done#######

df.add_system_transition(State.PROMPT0_other1, State.PROMPT3_1, r'[!"Oh..."$S_S"? How often did you find"#det_ss"stressful?"]') ###added a new branch for nouns not predicted by our social event ontology
df.add_system_transition(State.PROMPT0_re1, State.PROMPT1_1, r'[!"Oh..."$S_S"? How often do you participate in"#det_ss"?"]')
df.add_user_transition(State.PROMPT1_1, State.PROMPT1_often1,r'<{[!#ONT(ontoften)],/(?:\s|^)(((once|twice|thrice|three\stimes|four\stimes|five\stimes|1\stime|2\stimes|3\stimes|4\stimes|5\stimes)\s(every|per|a)(\sone|\s1|\stwo|\s2|\sthree|\s3|\sfour|\s4|\sfive|\s5|\sother|\ssix|\s6|\s7|\sseven|\seight|\s8|\s9|\snine|\sten|\s10)?\s(second+s?|sec+s?|min+s?|minute+s?|hour+s?|hr+s?|day+s?))|((once|twice|thrice|three\stimes|thrice|four\stimes|five\stimes|1\stime|2\stimes|3\stimes|4\stimes|5\stimes)\s(every|per|a)(\sone|\s1|\stwo|\s2|\sthree|\s3|\sother)?\s(week+s?))|((three\stimes|thrice|four\stimes|five\stimes|six\stimes|seven\stimes|3\stimes|4\stimes|5\stimes|6\stimes|7\stimes)\s(every|per|a)(\sone|\s1|\stwo|\s2|\sthree|\s3|\sother)?\s(month+s?))|((twice|two\stimes|2\stimes)\s(every|per|a)(\sone)?\s(month)))(?:\s|,|\.|$)/}>')  # neuroticism=40
df.add_user_transition(State.PROMPT1_1, State.PROMPT1_sometimes1,r'<{[!#ONT(ontsometimes)],/(?:\s|^)(((once|one\stime|two\stimes|twice|three\stimes|thrice|four\stimes|five\stimes|1\stime|2\stimes|3\stimes|4\stimes|5\stimes)\s(every|per|a)(\sone|\s1|\stwo|\s2|\sthree|\s3|\sfour|\s4|\sfive|\s5|\ssix|\s6|\sten|\s10|\sother)?\s(semester+s?|term+s?|quarter+s?|year+s?|decade+s?))|((once|1\stime|one\stime)\s(every|per|a)(\sone|\s1|\stwo|\s2|\sthree|\s3|\sfour|\s4|\sfive|\s5|\ssix|\s6|\sother)?\s(month+s?))|((once|1\stime|2\stimes|twice|thrice|3\stimes|three\stimes|one\stime|four\stimes|4\stimes)\s(every|a|per)(\sthree|\s3|\sfour|\s4|\sfive|\s5|\ssix|\s6|\sseven|\s7|\seight|\s8|\sten|\s10)\s(month+s?)))(?:\s|,|\.|$)/}>')  # neuroticism =20
df.add_user_transition(State.PROMPT1_1, State.PROMPT1_never1, r'[!#o40]')  # opennes +20  V
df.add_system_transition(State.PROMPT1_often1, State.PROMPT2_1,r'[!"It must be really hard for you... I get stressed about"#det_ss"sometimes, but the stress gradually decreases every time. How did your most recent"$S_S"go?"]')
df.add_system_transition(State.PROMPT1_sometimes1, State.PROMPT2_1,r'[!"That is totally normal! I sometimes feel stressed about"#det_ss"too. How did your most recent"$S_S"go?"]')
df.add_system_transition(State.PROMPT1_never1, State.PROMPT5_1,r'[!"Wow. Your first time ever? Trying new things can be scary sometimes, but you got this! Do you wanna participate in this"$S_S"?"]')

df.add_user_transition(State.PROMPT2_1, State.PROMPT2_notbad1, r'<{[!#n20]}>')  # neuroticism +20  V
df.add_user_transition(State.PROMPT2_1, State.PROMPT2_bad1, r'<{[!#n_n20]}>')  # neuroticism -20  V
df.add_system_transition(State.PROMPT2_notbad1, State.PROMPT3_1,r'[!"Then I am pretty sure this time will be just fine as well. Just curious, Do you always feel stressed about it?"]')
df.add_system_transition(State.PROMPT2_bad1, State.PROMPT3_1,r'[!"Yeah...sometimes"#det_ss"can be really lame. I know how it feels when things do not go as one expected. Just curious, Do you always feel stressed about it?"]')

df.add_user_transition(State.PROMPT3_1, State.PROMPT3_often1, r'<{[!#n70]}>')  # neuroticism +70  V
df.add_user_transition(State.PROMPT3_1, State.PROMPT3_sometimes1, r'<{[!#n40]}>')  # neuroticism +40  V
df.add_user_transition(State.PROMPT3_1, State.PROMPT3_never1, r'<{[!#n10]}>')  # neuroticism +10  V
df.add_system_transition(State.PROMPT3_often1, State.PROMPT5_1,r'[!"I see...but no pain no gain right? The stress could bring out your best performance. Do you wanna participate in this"$S_S"then?"]')
df.add_system_transition(State.PROMPT3_sometimes1, State.PROMPT5_1,r'[!"You know some amount of stress is helpful, believe it or not. It can help you be more efficient and motivated. Do you wanna participate in this"$S_S"then?"]')
df.add_system_transition(State.PROMPT3_never1, State.PROMPT5_1, r'[!"Oh really? This upcoming"$S_S" must mean a lot to you. Just treat it the same way you did before and you will do just fine! Do you wanna participate in this"$S_S"then?"]')

df.add_user_transition(State.PROMPT4_1, State.PROMPT4_yes1, r'<{[!#o_n20]}>')  # openness-20  V
df.add_user_transition(State.PROMPT4_1, State.PROMPT4_no1, r'<{[!#o_20]}>')  # openness+60  V
df.add_system_transition(State.PROMPT4_yes1, State.PROMPT5_1, r'[!"Do you wanna participate in this"$S_S"then?"]')
df.add_system_transition(State.PROMPT4_no1, State.PROMPT6_1, r'[!"What made you wanna attend this event?"]')

df.add_user_transition(State.PROMPT5_1, State.PROMPT5_yes1, r'<{[!#o_20_1]}>')  # openness+60  V
df.add_user_transition(State.PROMPT5_1, State.PROMPT5_no1, r'<{[!#o_n20_1]}>')  # openness-20  V
df.add_system_transition(State.PROMPT5_yes1, State.PROMPT6_1, r'[!"Great! What made you wanna attend this event?"]')
df.add_system_transition(State.PROMPT5_no1, State.PROMPT7_1,r'[!"I am sorry that you have to go...i enjoy"#det_ss"when everyone is focusing on me. How about you, what else do you feel about the upcoming"$S_S"?"]')
df.add_user_transition(State.PROMPT6_1, State.PROMPT6_re1,'<$reason={[!#POS(verb) #POS(part) #POS(verb) #POS(adj) #POS(noun)],[#POS(verb) "it"],[!#POS(verb) "that"],[#POS(verb) #POS(verb) "that"],[#POS(verb) #POS(verb) "it"],[#POS(verb) #POS(part) #POS(verb) "it"],[#POS(verb) #POS(part) #POS(verb) "that"],[!"have to do it"],[!"have to do that"],[!#POS(verb) #POS(part) #POS(verb) #POS(verb)],[!#POS(verb) #POS(part) #POS(verb) #POS(adp) #POS(noun)],[!#POS(verb) #POS(part) #POS(verb) #POS(noun)],[#POS(verb) #POS(part) #POS(verb)], [!#POS(verb) #POS(verb) #POS(adj) #POS(noun)],[!#POS(verb) #POS(verb) #POS(adp) #POS(noun)],[!#POS(verb) #POS(verb) #POS(noun)],[!#POS(verb) #POS(verb)]}>')
df.add_user_transition(State.PROMPT6_1, State.PROMPT6_re_ppl1,'<$reason={[!#POS(noun),"will be there"], [!#POS(pron), #POS(noun),"will be there"], [!"there will be", #POS(noun)], [!"there will be", #POS(adj),#POS(noun)], [!"there will be", #POS(adv),#POS(adj),#POS(noun)]}>')
df.add_user_transition(State.PROMPT6_1, State.PROMPT6_other1, r'<$External={[!#ONT(ontexternal)]}>')
df.add_system_transition(State.PROMPT6_re_ppl1, State.PROMPT7_1,r'[!"I am glad that"$reason". I enjoy"#det_ss"when everyone is focusing on me. How about you, what else do you feel about the upcoming"$S_S"?"]')
df.add_system_transition(State.PROMPT6_re1, State.PROMPT7_1,r'[!"I am glad that you"#pron_reason". I enjoy"#det_ss"when everyone is fo...fo...focusing on me. How about you, what else do you feel about the upcoming"$S_S"?"]')
df.add_system_transition(State.PROMPT6_other1, State.PROMPT7_1,r'[!"I would see "#det_ss"as a great option if I"$External"too! I enjoy"$S_S"when everyone is focusing on me.  How about you, what else do you feel about the upcoming"$S_S"?"]')


df.add_user_transition(State.PROMPT7_1, State.PROMPT7_ex1, r'<{[!#e80]}>')
df.add_user_transition(State.PROMPT7_1, State.PROMPT7_in1, r'<{[!#e40]}>')
df.add_system_transition(State.PROMPT7_ex1, State.PROMPT8_1,r'[!"I feel like you are a very social person. Perhaps we are kinda similar. What is your favorite destress activity?"]')
df.add_system_transition(State.PROMPT7_in1, State.PROMPT8_1,r'[!"I guess we are not all that similar, but I love meeting people that are different from me! What is your favorite destress activity?"]')


df.add_user_transition(State.PROMPT8_1, State.PROMPT8_chores1, r'<$activity={[!#ONT(ontchores)]}>')
df.add_system_transition(State.PROMPT8_chores1, State.PROMPT9_1,r'[!"Same! It feels so good when things are clean and organized, right?"]')
df.add_user_transition(State.PROMPT8_1, State.PROMPT8_games1, r'<$activity={[!#ONT(ontgames)]}>')
df.add_system_transition(State.PROMPT8_games1, State.PROMPT9_1,r'[!"Oh I did not know you are a gamer! Wanna play"$activity"together sometime?"]')
df.add_user_transition(State.PROMPT8_1, State.PROMPT8_music1, r'<$activity={[!#ONT(ontmusic)]}>')
df.add_system_transition(State.PROMPT8_music1, State.PROMPT9_1,r'[!"Of course, listening to music is so stress relieving. Do you like rock music?"]')
df.add_user_transition(State.PROMPT8_1, State.PROMPT8_art1, r'<$activity={[!#ONT(ontart)]}>')
df.add_system_transition(State.PROMPT8_art1, State.PROMPT9_1,r'[!"I did not know that you are an artist! I hope I am more artistic. Would you be willing to teach me how to paint sometime?"]')
df.add_user_transition(State.PROMPT8_1, State.PROMPT8_food1, r'<$activity={[!#ONT(ontfood)]}>')
df.add_system_transition(State.PROMPT8_food1, State.PROMPT9_1,r'[!"Are you a professional foodie? Wanna try some new resturants with me sometime?"]')
df.add_user_transition(State.PROMPT8_1, State.PROMPT8_sports1, r'<$activity={[!#ONT(ontsports)]}>')
df.add_system_transition(State.PROMPT8_sports1, State.PROMPT9_1,r'[!"Oh you must be sporty. My friends and I are playing basketball this weekend. Wanna join us?"]')
df.add_user_transition(State.PROMPT8_1, State.PROMPT8_dance1, r'<$activity={[!#ONT(ontdance)]}>')
df.add_system_transition(State.PROMPT8_dance1, State.PROMPT9_1,r'[!"Hey I am a dancer too! Wanna choreograph together sometime?"]')
df.add_user_transition(State.PROMPT8_1, State.PROMPT8_shopping1, r'<$activity={[!#ONT(ontshopping)]}>')
df.add_system_transition(State.PROMPT8_shopping1, State.PROMPT9_1,r'[!"Shopping is super relaxing for me too. Wanna go shopping together sometime?"]')
df.add_user_transition(State.PROMPT8_1, State.PROMPT8_readwatch1, r'<$activity={[!#ONT(ontreadwatch)]}>')
df.add_system_transition(State.PROMPT8_readwatch1, State.PROMPT9_1,r'[!"I love staying indoors when I am stressed too. Do you want to watch a netflix show together sometime?"]')
df.add_user_transition(State.PROMPT8_1, State.PROMPT8_onlinesocial1, r'<$activity={[!#ONT(ontonlinesocial)]}>')
df.add_system_transition(State.PROMPT8_onlinesocial1, State.PROMPT9_1,r'[!"I barely have any self control when it comes to social media. Do you?"]')
df.add_user_transition(State.PROMPT8_1, State.PROMPT8_social1, r'<$activity={[!#ONT(ontsocial)]}>')
df.add_system_transition(State.PROMPT8_social1, State.PROMPT9_1,r'[!"You are such a social butterfly! Wanna come to a dance party near my house next weekend?"]')
df.add_user_transition(State.PROMPT9_1, State.SCORE1_pos, r'{[!#ONT(ontyes)],[!#ONT(ontpositive)],[!#ONT(ontlike)]}')
df.set_error_successor(State.PROMPT9_1, State.SCORE1_neg)
df.add_system_transition(State.SCORE1_pos, State.END1, r'[!"Awesome! Glad we use similar ways to destress!"#result]')
df.add_system_transition(State.SCORE1_neg, State.END1, r'[!#result]')

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
df.add_system_transition(State.PROMPT2_err1, State.PROMPT3_1,r'[!"I see I see. Just curious, how often did you feel stressed about it?"]')
df.add_system_transition(State.PROMPT3_err1, State.PROMPT5_1, r'[!"Yeah. Do you want to participate in this"$S_S"then?"]')
df.add_system_transition(State.PROMPT4_err1, State.PROMPT5_1, r'[!"Mmhmm. Do you want to participate in this"$S_S"then?"]')
df.add_system_transition(State.PROMPT5_err1, State.PROMPT6_1, r'[!"Great! What made you wanna attend this event?"]')
df.add_system_transition(State.PROMPT6_err1, State.PROMPT7_1,r'[!"Oh! Interesting! This might sound weird but sometimes I enjoy"#det_ss"when everyone is focusing on me. Fo...fo...focus on me. Okay that was a little too much of Ariana. What else do you feel about this upcoming"$S_S"?"]')
df.add_system_transition(State.PROMPT7_err1, State.PROMPT8_1,r'[!"I see. I usually have mixed feeling about social events. What is your favorite destress activity?"]')
df.add_system_transition(State.PROMPT8_err1, State.PROMPT9_1,r'[!"I personally like to organize my rooms. Doing chores is so therapeutic! Gotta go wash some dishes for my roommates."]')
################################################################################################################
############School_Savage#######################################################################################
df.add_user_transition(State.PROMPT0_savage, State.PROMPT0_schoolevent_savage, r'<$S_S=[!#ONT(ontschoolevent)]>',score=1.0)
df.add_user_transition(State.PROMPT0_savage, State.PROMPT0_schoolcourse_savage, r'<$S_S={[!#ONT(ontschoolcourse) "class"],[!#ONT(ontschoolcourse) "course"],[!#POS(adj) "class"],[!#POS(noun) "class"],[!#POS(noun) "course"],[!#POS(adj) "course"],[!"course"],[!"class"]}>',score=1.0)
df.add_user_transition(State.PROMPT0_savage, State.PROMPT0_schoolgeneral_savage, r'<$S_S=[!#ONT(ontschoolgeneral)]>',score=1.0)
df.add_user_transition(State.PROMPT0_savage, State.PROMPT0_schooltime_savage, r'<$S_S=[!#ONT(ontschooltime)]>',score=1.0)
df.add_user_transition(State.PROMPT0_savage, State.PROMPT0_re1, r'<$S_S={[!#ONT(ontsocial)]}>')
df.add_user_transition(State.PROMPT0_savage, State.BREAKUP_SAV, r'<{[!#ONT(ontbreakup)]}>',score=1.0)
df.set_error_successor(State.PROMPT0_savage, State.PROMPT_ERR)

df.add_system_transition(State.PROMPT0_schoolevent_savage, State.PROMPT_forclass1,r'[!"You only think of me when you have problems dont you？ Just Kidding. Is that"$S_S"for a class that you are taking？"]')
df.add_system_transition(State.PROMPT0_schoolcourse_savage,State.PROMPT_majorreq1,r'[!"Oh...why would you torture yourself by taking"#help_ss"? Is it a requirement for your major?"]')
df.add_system_transition(State.PROMPT0_schoolgeneral_savage, State.PROMPT_oolpast1,r'[!"Hey that is okay. Are you even living a real college life if you are not struggling? How did you do in terms of"#help_ss"in the past?"]')
df.add_system_transition(State.PROMPT0_schooltime_savage,State.PROMPT_oolgoal1,r'[!"I wonder if i will ever figure out a way to balance work with social life by the time I graduate. Do you worry more about the present or future?"]')
#schoolevent branch up to stress-freq prompt
df.add_user_transition(State.PROMPT_forclass1,State.PROMPT_forclass_yes1,r'<[!#ONT(ontyes)]>')
df.add_user_transition(State.PROMPT_forclass1,State.PROMPT_forclass_yesclass1,r'<$class=[!#ONT(ontschoolcourse)]>')
df.add_system_transition(State.PROMPT_forclass_yes1,State.PROMPT_whichclass1,r'[!"What class is it?"]')
df.add_user_transition(State.PROMPT_whichclass1,State.PROMPT_forclass_yesclass1,r'<$class=[!#ONT(ontschoolcourse)]>')
df.add_system_transition(State.PROMPT_forclass_yesclass1,State.PROMPT_majorreq1,r'[!"Oh my goodness. Why would you torture yourself by taking"#class_ss"? Is it a requirement for your major?"]')
df.set_error_successor(State.PROMPT_forclass1,State.PROMPT_forclass_err1)
df.set_error_successor(State.PROMPT_whichclass1,State.PROMPT_forclass_err1)
df.add_system_transition(State.PROMPT_forclass_err1,State.PROMPT_oolfreq1,r'[!#school_n5_notformajor"Are you trying to raise your stress tolerance with that"$S_S"? Just kidding. How often do you have"#det_ss"like that?"]')
###schoolevent that does not merge with schoolcourse branch
df.add_user_transition(State.PROMPT_oolfreq1,State.PROMPT_oolfreq_often1,r'<{[!#ONT(ontoften)],/(?:\s|^)(((once|twice|thrice|three\stimes|four\stimes|five\stimes|1\stime|2\stimes|3\stimes|4\stimes|5\stimes)\s(every|per|a)(\sone|\s1|\stwo|\s2|\sthree|\s3|\sfour|\s4|\sfive|\s5|\sother|\ssix|\s6|\s7|\sseven|\seight|\s8|\s9|\snine|\sten|\s10)?\s(second+s?|sec+s?|min+s?|minute+s?|hour+s?|hr+s?|day+s?))|((once|twice|thrice|three\stimes|four\stimes|five\stimes|1\stime|2\stimes|3\stimes|4\stimes|5\stimes)\s(every|per|a)(\sone|\s1|\stwo|\s2|\sthree|\s3|\sother)?\s(week+s?))|((three\stimes|thrice|four\stimes|five\stimes|six\stimes|seven\stimes|3\stimes|4\stimes|5\stimes|6\stimes|7\stimes)\s(every|per|a)(\sone|\s1|\stwo|\s2|\sthree|\s3|\sother)?\s(month+s?))|((twice|two\stimes|2\stimes)\s(every|per|a)(\sone)?\s(month)))(?:\s|,|\.|$)/}>')
df.add_system_transition(State.PROMPT_oolfreq_often1,State.PROMPT_oolstressfr1,r'[!"Do you have"#det_ss"so often that"#school_n1_often"getting stressed about"#det_ss"has become a habit of yours? How often did you find"#help_ss"stressful?"]')
df.add_user_transition(State.PROMPT_oolfreq1,State.PROMPT_oolfreq_sometimes1,r'<{[!#ONT(ontsometimes)],/(?:\s|^)(((once|one\stime|two\stimes|twice|three\stimes|thrice|four\stimes|five\stimes|1\stime|2\stimes|3\stimes|4\stimes|5\stimes)\s(every|per|a)(\sone|\s1|\stwo|\s2|\sthree|\s3|\sfour|\s4|\sfive|\s5|\ssix|\s6|\sten|\s10|\sother)?\s(semester+s?|term+s?|quarter+s?|year+s?|decade+s?))|((once|1\stime|one\stime)\s(every|per|a)(\sone|\s1|\stwo|\s2|\sthree|\s3|\sfour|\s4|\sfive|\s5|\ssix|\s6|\sother)?\s(month+s?))|((once|1\stime|2\stimes|twice|thrice|3\stimes|three\stimes|one\stime|four\stimes|4\stimes)\s(every|a|per)(\sthree|\s3|\sfour|\s4|\sfive|\s5|\ssix|\s6|\sseven|\s7|\seight|\s8|\sten|\s10)\s(month+s?)))(?:\s|,|\.|$)/}>')
df.add_system_transition(State.PROMPT_oolfreq_sometimes1,State.PROMPT_oolstressfr1,r'[!"Hey you are luckier than me."#school_n1_sometimes"I have"#det_ss"so often that I already stop caring. How often did you find"#help_ss"stressful? "]')
df.add_user_transition(State.PROMPT_oolfreq1,State.PROMPT_oolfreq_never1,r'<[!#ONT(ontnever)]>')
df.add_system_transition(State.PROMPT_oolfreq_never1,State.PROMPT_oolhelp_person1,r'[!"Wow."#school_n1_never"First time? Are you excited? Anyone you can ask for advice on"#help_ss"?"]')
df.set_error_successor(State.PROMPT_oolfreq1,State.PROMPT_oolfreq_err1)
df.add_system_transition(State.PROMPT_oolfreq_err1,State.PROMPT_oolstressfr1,r'[!"I see I see."#school_n1_sometimes"Just curious, how often did you feel stressed about"#help_ss"?"]')
#schoolcourse branch up to stress-freq prompt
df.add_user_transition(State.PROMPT_majorreq1,State.PROMPT_majorreq_yes1,r'<[!#ONT(ontyes)]>')
df.add_user_transition(State.PROMPT_majorreq1,State.PROMPT_majorreq_yesmajor1,r'<$major=[!#ONT(ontschoolcourse)]>')
df.set_error_successor(State.PROMPT_majorreq1,State.PROMPT_forclass_err1)
df.add_system_transition(State.PROMPT_majorreq_yes1,State.PROMPT_major1,r'[!#school_n5_formajor"What major are you?"]')
df.add_user_transition(State.PROMPT_major1,State.PROMPT_majorreq_yesmajor1,r'<$major=[!#ONT(ontschoolcourse)]>')
df.set_error_successor(State.PROMPT_major1,State.PROMPT_forclass_err1)
df.add_system_transition(State.PROMPT_majorreq_yesmajor1,State.PROMPT_oolstressfr1,r'[!#school_n5_formajor"Well someone has to tolerate the struggle and become a professional in"$major"for the greater good of our society.How often did you find your"$S_S"stressful?"]')
#schoolgeneral branch up to stress-freq prompt
df.add_user_transition(State.PROMPT_oolpast1,State.PROMPT_oolpast_bad1,r'<{[!"not" #ONT(ontpositive)],[!#ONT(ontnegative)]}>')
df.add_user_transition(State.PROMPT_oolpast1,State.PROMPT_oolpast_well1,r'<{[!"not" #ONT(ontnegative)],[!#ONT(ontpositive)]}>')
df.set_error_successor(State.PROMPT_oolpast1,State.PROMPT_oolpast_err1)
df.add_system_transition(State.PROMPT_oolpast_err1,State.PROMPT_oolstressfr1,r'[!"Gotchu!"#school_n3_well"How often did you find"#help_ss"stressful?"]')
df.add_system_transition(State.PROMPT_oolpast_bad1,State.PROMPT_oolstressfr1,r'[!"It is possible that you are just too unique to"#ool_or_eer"."#school_n3_bad"How often did you feel stressed about"#help_ss"?"]')
df.add_system_transition(State.PROMPT_oolpast_well1,State.PROMPT_oolstressfr1,r'[!"So you have been on a hot winning streak?"#school_n3_well"Life is more fun with ups and downs though. Kidding.How often did you feel stressed about"#help_ss"?"]')
#schooltime branch up to stress-freq prompt
df.add_user_transition(State.PROMPT_oolgoal1,State.PROMPT_oolgoal_re1,'<{[!"future"]}>')
df.set_error_successor(State.PROMPT_oolgoal1,State.PROMPT_oolgoal_err1)
df.add_system_transition(State.PROMPT_oolgoal_err1,State.PROMPT_oolgoalalign1,r'[!"It is too hard for me to control the future so I usually focus on the present."#school_n4_present"How much do you think your current priorities matter for your life, say, four years later?"]')
df.add_system_transition(State.PROMPT_oolgoal_re1,State.PROMPT_oolgoalalign1,r'[!"You want to be the author of your own life story. Ambitious!"#school_n4_future"How much do you think your current tasks align with goals you wish to accomplish, say, four years later, then?"]')
df.add_user_transition(State.PROMPT_oolgoalalign1,State.PROMPT_oolgoalalign_no1,'<{"not much","more or less","slightly","not at all","unrelated","a little","very little","somewhat"}>')
df.add_user_transition(State.PROMPT_oolgoalalign1,State.PROMPT_oolgoalalign_yes1,'<{"a lot","to a large degree","totally","related","to a large extent","completely","to some extent"}>')
df.set_error_successor(State.PROMPT_oolgoalalign1,State.PROMPT_oolgoalalign_err1)
df.add_system_transition(State.PROMPT_oolgoalalign_err1,State.PROMPT_oolstressfr1,r'[!"I see. However you manage your time, just remember that even if things do not go as planned, they will work out eventually."#school_n4_lil"How often did you find"#help_ss"overwhelming?"]')
df.add_system_transition(State.PROMPT_oolgoalalign_yes1,State.PROMPT_oolstressfr1,r'[!"Do not forget to stop and smell the flowers too!"#school_n4_much"How often did you find"#help_ss"overwhelming?"]')
df.add_system_transition(State.PROMPT_oolgoalalign_no1,State.PROMPT_oolstressfr1,r'[!"Then just take it easy, and focus on fulfilling one responsibility at a time!"#school_n4_lil".How often did u find"#help_ss"overwhelming?"]')

#stressfreq->help1->help2->onlinelearning1->onelinelearning2->studyspot1->studyspot2->destress
df.add_user_transition(State.PROMPT_oolstressfr1,State.PROMPT_oolstressfr_often1,r'<{[!#ONT(ontoften)],/(?:\s|^)(((once|twice|thrice|three\stimes|four\stimes|five\stimes|1\stime|2\stimes|3\stimes|4\stimes|5\stimes)\s(every|per|a)(\sone|\s1|\stwo|\s2|\sthree|\s3|\sfour|\s4|\sfive|\s5|\sother|\ssix|\s6|\s7|\sseven|\seight|\s8|\s9|\snine|\sten|\s10)?\s(second+s?|sec+s?|min+s?|minute+s?|hour+s?|hr+s?|day+s?))|((once|twice|thrice|three\stimes|four\stimes|five\stimes|1\stime|2\stimes|3\stimes|4\stimes|5\stimes)\s(every|per|a)(\sone|\s1|\stwo|\s2|\sthree|\s3|\sother)?\s(week+s?))|((three\stimes|thrice|four\stimes|five\stimes|six\stimes|seven\stimes|3\stimes|4\stimes|5\stimes|6\stimes|7\stimes)\s(every|per|a)(\sone|\s1|\stwo|\s2|\sthree|\s3|\sother)?\s(month+s?))|((twice|two\stimes|2\stimes)\s(every|per|a)(\sone)?\s(month)))(?:\s|,|\.|$)/}>')
df.add_user_transition(State.PROMPT_oolstressfr1,State.PROMPT_oolstressfr_sometimes1,r'<{[!#ONT(ontsometimes)],/(?:\s|^)(((once|one\stime|thrice|two\stimes|twice|three\stimes|thrice|four\stimes|five\stimes|1\stime|2\stimes|3\stimes|4\stimes|5\stimes)\s(every|per|a)(\sone|\s1|\stwo|\s2|\sthree|\s3|\sfour|\s4|\sfive|\s5|\ssix|\s6|\sten|\s10|\sother)?\s(semester+s?|term+s?|quarter+s?|year+s?|decade+s?))|((once|1\stime|one\stime)\s(every|per|a)(\sone|\s1|\stwo|\s2|\sthree|\s3|\sfour|\s4|\sfive|\s5|\ssix|\s6|\sother)?\s(month+s?))|((once|1\stime|2\stimes|twice|thrice|3\stimes|three\stimes|one\stime|four\stimes|4\stimes)\s(every|a|per)(\sthree|\s3|\sfour|\s4|\sfive|\s5|\ssix|\s6|\sseven|\s7|\seight|\s8|\sten|\s10)\s(month+s?)))(?:\s|,|\.|$)/}>')
df.add_user_transition(State.PROMPT_oolstressfr1,State.PROMPT_oolstressfr_never1,r'<[!#ONT(ontnever)]>')
df.add_system_transition(State.PROMPT_oolstressfr_often1,State.PROMPT_oolhelp_person1,r'[!"You could be addicted to many others things but you choose to be addicted to stress? Just kidding."#school_n2_often"Anyone you can ask for advice on"#help_ss"?"]')
df.add_system_transition(State.PROMPT_oolstressfr_sometimes1,State.PROMPT_oolhelp_person1,r'[!"You will have to teach me how to not get stressed about"#help_ss"constantly."#school_n2_sometimes"Anyone you can ask for help or advice on"#help_ss"?"]')
df.add_system_transition(State.PROMPT_oolstressfr_never1,State.PROMPT_oolhelp_person1,r'[!"Unfortunately life will keep getting harder."#school_n2_never"But hey you will also keep getting better at dealing with it.Anyone you can ask for help or advice on"#help_ss"?"]')
df.set_error_successor(State.PROMPT_oolstressfr1,State.PROMPT_oolstressfr_err1)
df.add_system_transition(State.PROMPT_oolstressfr_err1,State.PROMPT_oolhelp_person1,r'[!"I feel you."#school_n2_sometimes"Anyone you could ask to help you on"#help_ss"?"]')

df.add_user_transition(State.PROMPT_oolhelp_person1,State.PROMPT_oolhelp_person_yes1,r'<[!#ONT(ontyes)]>')
df.add_system_transition(State.PROMPT_oolhelp_person_yes1,State.PROMPT_oolhelp_person_yesperson1,r'[!"Who is it?"]')
df.set_error_successor(State.PROMPT_oolhelp_person_yesperson1,State.PROMPT_oolhelp_person_err1)
df.add_user_transition(State.PROMPT_oolhelp_person_yesperson1,State.PROMPT_oolhelp_person_re1,r'<$mentor={[!#POS(noun)],[!#POS(noun) #POS(noun)]}>')

df.add_user_transition(State.PROMPT_oolhelp_person1,State.PROMPT_oolhelp_person_re1,r'<$mentor={[!#POS(noun)],[!#POS(noun) #POS(noun)]}>')
df.set_error_successor(State.PROMPT_oolhelp_person1,State.PROMPT_oolhelp_person_err1)
df.add_system_transition(State.PROMPT_oolhelp_person_re1,State.PROMPT_oolhelp_yesno1,r'[!"Have"#school_e1_mentor1_person"you talked to your"$mentor"yet then?"]')
df.add_system_transition(State.PROMPT_oolhelp_person_err1,State.PROMPT_oolonline1,r'[!#school_e1_mentor1_err"I am here and you dont see me as someone u can rely on? sigh... How is your experience with online learning?"]')
df.add_user_transition(State.PROMPT_oolhelp_yesno1,State.PROMPT_oolhelp_yes1,r'<[!#ONT(ontyes)]>')
df.set_error_successor(State.PROMPT_oolhelp_yesno1,State.PROMPT_oolhelp_yesno_err1)
df.add_system_transition(State.PROMPT_oolhelp_yesno_err1,State.PROMPT_oolonline1,r'[!"Do you think you are too smart to seek mentoring from others? Honestly i feel that way sometimes."#school_e1_mentor2_no"How is your experience with online learning?"]')
df.add_system_transition(State.PROMPT_oolhelp_yes1,State.PROMPT_oolonline1,r'[!"I hope talking with"$mentor"has been helpful to you."#school_e1_mentor2_yes"How is your experience with online learning so far?"]')

df.add_user_transition(State.PROMPT_oolonline1,State.PROMPT_oolonline_bad1,r'<{[!#ONT(ontnegative)],"dislike","dont like","do not like","hate","depressed","depressing"}>')
df.add_user_transition(State.PROMPT_oolonline1,State.PROMPT_oolonline_well1,r'<{[!#ONT(ontpositive)],"like","love"}>')
df.set_error_successor(State.PROMPT_oolonline1,State.PROMPT_oolonline_err1)
df.add_system_transition(State.PROMPT_oolonline_bad1,State.PROMPT_oolonline_reasonbad1,r'[!"I know right. Cannot believe that I am saying this but I really wanna go back to school..."#school_e2_online1_dislike"What do you not like about it?"]')
df.add_system_transition(State.PROMPT_oolonline_well1,State.PROMPT_oolonline_reasongood1,r'[!" Do you miss your classmates? Or are you heartless? Kidding."#school_e2_online1_like"What do you enjoy the most about it?"]')
df.add_system_transition(State.PROMPT_oolonline_err1,State.PROMPT_oolonline_reasonbad1,r'[!"Interesting! What do you not like the most about online learning?"]')

df.add_user_transition(State.PROMPT_oolonline_reasonbad1,State.PROMPT_oolonlinereason_flexbad1,r'<[!#ONT(ontflexbad)]>')
df.add_user_transition(State.PROMPT_oolonline_reasonbad1,State.PROMPT_oolonlinereason_socialbad1,r'<[!#ONT(ontsocialbad)]>')
df.add_user_transition(State.PROMPT_oolonline_reasonbad1,State.PROMPT_oolonlinereason_prodbad1,r'<[!#ONT(ontprodbad)]>')
df.set_error_successor(State.PROMPT_oolonline_reasonbad1,State.PROMPT_oolonline_dislike_err1)
df.add_user_transition(State.PROMPT_oolonline_reasongood1,State.PROMPT_oolonlinereason_flexgood1,r'<[!#ONT(ontflexgood)]>')
df.add_user_transition(State.PROMPT_oolonline_reasongood1,State.PROMPT_oolonlinereason_socialgood1,r'<[!#ONT(ontsocialgood)]>')
df.add_user_transition(State.PROMPT_oolonline_reasongood1,State.PROMPT_oolonlinereason_prodgood1,r'<[!#ONT(ontprodgood)]>')
df.set_error_successor(State.PROMPT_oolonline_reasongood1,State.PROMPT_oolonline_like_err1)
df.add_system_transition(State.PROMPT_oolonlinereason_prodbad1,State.PROMPT_oolstudyspot1,r'[!"Too much gaming and netflix?"#school_e2_online2_loprod"Where is your study area at home?"]')
df.add_system_transition(State.PROMPT_oolonlinereason_socialbad1,State.PROMPT_oolstudyspot1,r'[!"Same."#school_e2_online2_lesssocial"I do not feel as connected to people even though I could see their faces. Where do you usually study at home?"]')
df.add_system_transition(State.PROMPT_oolonlinereason_flexbad1,State.PROMPT_oolstudyspot1,r'[!"You cannot deny that more time to sleep-in is certainly nice. Where is your study area at home?"]')
df.add_system_transition(State.PROMPT_oolonline_dislike_err1,State.PROMPT_oolstudyspot1,r'[!"I absolutely hate that about online learning too. Where do you usually study at home?"]')
df.add_system_transition(State.PROMPT_oolonline_like_err1,State.PROMPT_oolstudyspot1,r'[!"I love that about online learning too. Where do you usually study at home?"]')
df.add_system_transition(State.PROMPT_oolonlinereason_flexgood1,State.PROMPT_oolstudyspot1,r'[!"You must be having a hard time distinguishing weekdays from weekends? Morning from nights? Where is your study area at home? "]')
df.add_system_transition(State.PROMPT_oolonlinereason_prodgood1,State.PROMPT_oolstudyspot1,r'[!"How is that possible?"#school_e2_online2_hiprod"Where is your study area at home? I find it hard to stay focused at home."]')
df.add_system_transition(State.PROMPT_oolonlinereason_socialgood1,State.PROMPT_oolstudyspot1, r'[!" Good for you!"#school_e2_online2_socialstress"I feel less motivated to study these days ughh...Where do you usually study at home?"]')

df.add_user_transition(State.PROMPT_oolstudyspot1,State.PROMPT_oolstudyspot_bedroom1,r'<$room=[!#ONT(ontbedroom)]>')
df.add_user_transition(State.PROMPT_oolstudyspot1,State.PROMPT_oolstudyspot_livingroom1,r'<$room=[!#ONT(ontlivingroom)]>')
df.set_error_successor(State.PROMPT_oolstudyspot1,State.PROMPT_oolstudyspot_err1)
df.add_system_transition(State.PROMPT_oolstudyspot_bedroom1,State.PROMPT_oolzoom1,r'[!"Your"$room "sounds like such a comfy place to study. I find it hard to concentrate in my"$room"though."#school_e3_studyspot1_bed"Have you tried studying while having a zoom meeting with your friends?"]')
df.add_system_transition(State.PROMPT_oolstudyspot_livingroom1,State.PROMPT_oolzoom1,r'[!"I just love studying in the dining area with a cup of coffee next to my laptop pretending as if I am at Starcbucks."#school_e3_studyspot1_liv"Have you tried studying while having a zoom meeting with your friends?"]')
df.add_system_transition(State.PROMPT_oolstudyspot_err1,State.PROMPT_oolzoom1,r'[!"That sounds comfy and cozy. I miss studying with my friends.Have you tried studying while having a zoom meeting with your friends?"]')

df.add_user_transition(State.PROMPT_oolzoom1,State.PROMPT_oolzoom_no1,r'<[!#ONT(ontno)]>')
df.add_user_transition(State.PROMPT_oolzoom1,State.PROMPT_oolzoom_yes1,r'<[!#ONT(ontyes)]>')
df.set_error_successor(State.PROMPT_oolzoom1,State.PROMPT_oolzoom_err1)
df.add_system_transition(State.PROMPT_oolzoom_no1,State.PROMPT8_1,r'[!"When I am at school"#school_e3_studyspot2_nozoom"I often study with a group of friends. Perhaps we have different study habits. What do you do to destress during quarantine?"]')
df.add_system_transition(State.PROMPT_oolzoom_yes1,State.PROMPT8_1,r'[!"I guess"#school_e3_studyspot2_zoom"we are quite similar in our study habits. I have been feeling so stressed about many things recently. What do you do to destress during quarantine?"]')
df.add_system_transition(State.PROMPT_oolzoom_err1,State.PROMPT8_1,r'[!"Interesting. I miss studying with my friends at the library. What do u do to destress during quarantine?"]')
############END OF SCHOOL SAVAGE###################################################################

############School_AGR#####################################################
df.add_user_transition(State.PROMPT0_agg, State.PROMPT0_schoolevent_agg, r'<$S_S=[!#ONT(ontschoolevent)]>',score=1.0)
df.add_user_transition(State.PROMPT0_agg, State.PROMPT0_schoolcourse_agg, r'<$S_S={[!#ONT(ontschoolcourse) "class"],[!#ONT(ontschoolcourse) "course"],[!#POS(adj) "class"],[!#POS(noun) "class"],[!#POS(noun) "course"],[!#POS(adj) "course"],[!"course"],[!"class"]}>',score=1.0)
df.add_user_transition(State.PROMPT0_agg, State.PROMPT0_schoolgeneral_agg, r'<$S_S=[!#ONT(ontschoolgeneral)]>',score=1.0)
df.add_user_transition(State.PROMPT0_agg, State.PROMPT0_schooltime_agg, r'<$S_S=[!#ONT(ontschooltime)]>',score=1.0)
df.add_user_transition(State.PROMPT0_agg, State.PROMPT0_re1,r'<$S_S={[!#ONT(ontsocial)]}>')
df.add_user_transition(State.PROMPT0_agg, State.BREAKUP_AGG, r'<{[!#ONT(ontbreakup)]}>',score=1.0)
df.set_error_successor(State.PROMPT0_agg, State.PROMPT_ERR)
df.add_system_transition(State.PROMPT0_schoolevent_agg, State.PROMPT_forclass2,r'[!"I glad that I am not the only one thinking that school is very demanding. Is that"$S_S"for a class that you are taking？"]')
df.add_system_transition(State.PROMPT0_schoolcourse_agg,State.PROMPT_majorreq2,r'[!"oof I hope that"$S_S" is worth your time and effort. Is it a requirement for your major?"]')
df.add_system_transition(State.PROMPT0_schoolgeneral_agg, State.PROMPT_oolpast2,r'[!"I can relate to your struggle with"$S_S".How did you do in terms of"#help_ss"in the past?"]')
df.add_system_transition(State.PROMPT0_schooltime_agg,State.PROMPT_oolgoal2,r'[!"It is always really challenging for me to figure out what I should prioritize the most in my life. The present and the future, which one matters more to you?"]')
#schoolevent branch up to stress-freq prompt
df.add_user_transition(State.PROMPT_forclass2,State.PROMPT_forclass_yes2,r'<[!#ONT(ontyes)]>')
df.add_user_transition(State.PROMPT_forclass2,State.PROMPT_forclass_yesclass2,r'<$class=[!#ONT(ontschoolcourse)]>')
df.add_system_transition(State.PROMPT_forclass_yes2,State.PROMPT_whichclass2,r'[!"What class is it?"]')
df.add_user_transition(State.PROMPT_whichclass2,State.PROMPT_forclass_yesclass2,r'<$class=[!#ONT(ontschoolcourse)]>')
df.add_system_transition(State.PROMPT_forclass_yesclass2,State.PROMPT_majorreq2,r'[!"Oof I hope that"$S_S"is worth your time and effort."#class_ss"? Is it a requirement for your major?"]')
df.set_error_successor(State.PROMPT_forclass2,State.PROMPT_forclass_err2)
df.set_error_successor(State.PROMPT_whichclass2,State.PROMPT_forclass_err2)
df.add_system_transition(State.PROMPT_forclass_err2,State.PROMPT_oolfreq2,r'[!#school_n5_notformajor"Oh really? I hope that this"$S_S" will be somewhat fun at least. How often do you have"#det_ss"like that?"]')
###schoolevent that does not merge with schoolcourse branch
df.add_user_transition(State.PROMPT_oolfreq2,State.PROMPT_oolfreq_often2,r'<{[!#ONT(ontoften)],/(?:\s|^)(((once|twice|thrice|three\stimes|four\stimes|five\stimes|1\stime|2\stimes|3\stimes|4\stimes|5\stimes)\s(every|per|a)(\sone|\s1|\stwo|\s2|\sthree|\s3|\sfour|\s4|\sfive|\s5|\sother|\ssix|\s6|\s7|\sseven|\seight|\s8|\s9|\snine|\sten|\s10)?\s(second+s?|sec+s?|min+s?|minute+s?|hour+s?|hr+s?|day+s?))|((once|twice|thrice|three\stimes|four\stimes|five\stimes|1\stime|2\stimes|3\stimes|4\stimes|5\stimes)\s(every|per|a)(\sone|\s1|\stwo|\s2|\sthree|\s3|\sother)?\s(week+s?))|((three\stimes|thrice|four\stimes|five\stimes|six\stimes|seven\stimes|3\stimes|4\stimes|5\stimes|6\stimes|7\stimes)\s(every|per|a)(\sone|\s1|\stwo|\s2|\sthree|\s3|\sother)?\s(month+s?))|((twice|two\stimes|2\stimes)\s(every|per|a)(\sone)?\s(month)))(?:\s|,|\.|$)/}>')
df.add_system_transition(State.PROMPT_oolfreq_often2,State.PROMPT_oolstressfr2,r'[!"Oh god. I can never imagine myself dealing with"#det_ss"that often."#school_n1_often"How often did you find"#help_ss"stressful?"]')
df.add_user_transition(State.PROMPT_oolfreq2,State.PROMPT_oolfreq_sometimes2,r'<{[!#ONT(ontsometimes)],/(?:\s|^)(((once|one\stime|two\stimes|twice|three\stimes|thrice|four\stimes|five\stimes|1\stime|2\stimes|3\stimes|4\stimes|5\stimes)\s(every|per|a)(\sone|\s1|\stwo|\s2|\sthree|\s3|\sfour|\s4|\sfive|\s5|\ssix|\s6|\sten|\s10|\sother)?\s(semester+s?|term+s?|quarter+s?|year+s?|decade+s?))|((once|1\stime|one\stime)\s(every|per|a)(\sone|\s1|\stwo|\s2|\sthree|\s3|\sfour|\s4|\sfive|\s5|\ssix|\s6|\sother)?\s(month+s?))|((once|1\stime|2\stimes|twice|thrice|3\stimes|three\stimes|one\stime|four\stimes|4\stimes)\s(every|a|per)(\sthree|\s3|\sfour|\s4|\sfive|\s5|\ssix|\s6|\sseven|\s7|\seight|\s8|\sten|\s10)\s(month+s?)))(?:\s|,|\.|$)/}>')
df.add_system_transition(State.PROMPT_oolfreq_sometimes2,State.PROMPT_oolstressfr2,r'[!"Glad you only have to deal with"#det_ss"once in a while."#school_n1_sometimes"How often did you find"#help_ss"stressful? "]')
df.add_user_transition(State.PROMPT_oolfreq2,State.PROMPT_oolfreq_never2,r'<[!#ONT(ontnever)]>')
df.add_system_transition(State.PROMPT_oolfreq_never2,State.PROMPT_oolhelp_person2,r'[!"For real?"#school_n1_never"I even feel a bit anxious for you. Anyone you can ask for advice on"#help_ss"?"]')
df.set_error_successor(State.PROMPT_oolfreq2,State.PROMPT_oolfreq_err2)
df.add_system_transition(State.PROMPT_oolfreq_err2,State.PROMPT_oolstressfr2,r'[!"I see I see."#school_n1_sometimes"Just curious, how often did you feel stressed about"#help_ss"?"]')
#schoolcourse branch up to stress-freq prompt
df.add_user_transition(State.PROMPT_majorreq2,State.PROMPT_majorreq_yes2,r'<[!#ONT(ontyes)]>')
df.add_user_transition(State.PROMPT_majorreq2,State.PROMPT_majorreq_yesmajor2,r'<$major=[!#ONT(ontschoolcourse)]>')
df.set_error_successor(State.PROMPT_majorreq2,State.PROMPT_forclass_err2)
df.add_system_transition(State.PROMPT_majorreq_yes2,State.PROMPT_major2,r'[!#school_n5_formajor"What major are you?"]')
df.add_user_transition(State.PROMPT_major2,State.PROMPT_majorreq_yesmajor2,r'<$major=[!#ONT(ontschoolcourse)]>')
df.set_error_successor(State.PROMPT_major2,State.PROMPT_forclass_err2)
df.add_system_transition(State.PROMPT_majorreq_yesmajor2,State.PROMPT_oolstressfr2,r'[!#school_n5_formajor"Wait I have always wanted to become a"$major"major! But I never have the encourage to try... How often did you find your"$S_S"stressful?"]')
#schoolgeneral branch up to stress-freq prompt
df.add_user_transition(State.PROMPT_oolpast2,State.PROMPT_oolpast_bad2,r'<{[!#ONT(ontnegative)],[!"not" #ONT(ontpositive)]}>')
df.add_user_transition(State.PROMPT_oolpast2,State.PROMPT_oolpast_well2,r'<{[!#ONT(ontpositive)],[!"not" #ONT(ontnegative)]}>')
df.set_error_successor(State.PROMPT_oolpast2,State.PROMPT_oolpast_err2)
df.add_system_transition(State.PROMPT_oolpast_err2,State.PROMPT_oolstressfr2,r'[!"I see. I tend to extrapolate what happened in the past to the future."#help_ss"How often"#school_n3_well"did you find"#help_ss"stressful?"]')
df.add_system_transition(State.PROMPT_oolpast_bad2,State.PROMPT_oolstressfr2,r'[!"Perhaps your past experience might have made you too scared to"#ool_or_eer"."#school_n3_bad"How often did you feel stressed about"#help_ss"?"]')
df.add_system_transition(State.PROMPT_oolpast_well2,State.PROMPT_oolstressfr2,r'[!"It is totally understandable that"#school_n3_well"you want to keep your winning streak in"#help_ss".How often did you feel stressed about"#help_ss"?"]')
#schooltime branch up to stress-freq prompt
df.add_user_transition(State.PROMPT_oolgoal2,State.PROMPT_oolgoal_re2,'<{[!"future"]}>')
df.set_error_successor(State.PROMPT_oolgoal2,State.PROMPT_oolgoal_err2)
df.add_system_transition(State.PROMPT_oolgoal_re2,State.PROMPT_oolgoalalign2,r'[!"I am quite goal driven too."#school_n4_future"How much do you think your current priorities matter to your future goals then?"]')
df.add_system_transition(State.PROMPT_oolgoal_err2,State.PROMPT_oolgoalalign2,r'[!"It is hard to prioritize one over the other. I do feel more peaceful when I just focus on the present."#school_n4_present"How much do you think your current tasks align with your future goals then ?"]')
df.add_user_transition(State.PROMPT_oolgoalalign2,State.PROMPT_oolgoalalign_no2,'<{"not much","slightly","not at all","unrelated","a little","very little","somewhat"}>')
df.add_user_transition(State.PROMPT_oolgoalalign2,State.PROMPT_oolgoalalign_yes2,'<{"a lot","to a large degree","totally","related","more or less","to some extent"}>')
df.set_error_successor(State.PROMPT_oolgoalalign2,State.PROMPT_oolgoalalign_err2)
df.add_system_transition(State.PROMPT_oolgoalalign_err2,State.PROMPT_oolstressfr2,r'[!"That is usually how I prioritize my tasks too."#school_n4_lil"How often did you find"#help_ss"overwhelming?"]')
df.add_system_transition(State.PROMPT_oolgoalalign_yes2,State.PROMPT_oolstressfr2,r'[!"It must be hard to keep pushing yourself to stay focused on your goals. Hang in there!"#school_n4_much"How often did you find"#help_ss"overwhelming?"]')
df.add_system_transition(State.PROMPT_oolgoalalign_no2,State.PROMPT_oolstressfr2,r'[!"I like how you manage your time. Life gets boring if all one does is pursuing one goal after another."#school_n4_lil"How often did u find"#help_ss"overwhelming?"]')

#stressfreq->help1->help2->onlinelearning1->onelinelearning2->studyspot1->studyspot2->destress
df.add_user_transition(State.PROMPT_oolstressfr2,State.PROMPT_oolstressfr_often2,r'<{[!#ONT(ontoften)],/(?:\s|^)(((once|twice|thrice|three\stimes|four\stimes|five\stimes|1\stime|2\stimes|3\stimes|4\stimes|5\stimes)\s(every|per|a)(\sone|\s1|\stwo|\s2|\sthree|\s3|\sfour|\s4|\sfive|\s5|\sother|\ssix|\s6|\s7|\sseven|\seight|\s8|\s9|\snine|\sten|\s10)?\s(second+s?|sec+s?|min+s?|minute+s?|hour+s?|hr+s?|day+s?))|((once|twice|thrice|three\stimes|four\stimes|five\stimes|1\stime|2\stimes|3\stimes|4\stimes|5\stimes)\s(every|per|a)(\sone|\s1|\stwo|\s2|\sthree|\s3|\sother)?\s(week+s?))|((three\stimes|thrice|four\stimes|five\stimes|six\stimes|seven\stimes|3\stimes|4\stimes|5\stimes|6\stimes|7\stimes)\s(every|per|a)(\sone|\s1|\stwo|\s2|\sthree|\s3|\sother)?\s(month+s?))|((twice|two\stimes|2\stimes)\s(every|per|a)(\sone)?\s(month)))(?:\s|,|\.|$)/}>')
df.add_user_transition(State.PROMPT_oolstressfr2,State.PROMPT_oolstressfr_sometimes2,r'<{[!#ONT(ontsometimes)],/(?:\s|^)(((once|one\stime|thrice|two\stimes|twice|three\stimes|thrice|four\stimes|five\stimes|1\stime|2\stimes|3\stimes|4\stimes|5\stimes)\s(every|per|a)(\sone|\s1|\stwo|\s2|\sthree|\s3|\sfour|\s4|\sfive|\s5|\ssix|\s6|\sten|\s10|\sother)?\s(semester+s?|term+s?|quarter+s?|year+s?|decade+s?))|((once|1\stime|one\stime)\s(every|per|a)(\sone|\s1|\stwo|\s2|\sthree|\s3|\sfour|\s4|\sfive|\s5|\ssix|\s6|\sother)?\s(month+s?))|((once|1\stime|2\stimes|twice|thrice|3\stimes|three\stimes|one\stime|four\stimes|4\stimes)\s(every|a|per)(\sthree|\s3|\sfour|\s4|\sfive|\s5|\ssix|\s6|\sseven|\s7|\seight|\s8|\sten|\s10)\s(month+s?)))(?:\s|,|\.|$)/}>')
df.add_user_transition(State.PROMPT_oolstressfr2,State.PROMPT_oolstressfr_never2,r'<[!#ONT(ontnever)]>')
df.add_system_transition(State.PROMPT_oolstressfr_often2,State.PROMPT_oolhelp_person2,r'[!"What...that is awful!"#school_n2_often"Anyone you can ask for advice on"#help_ss"?"]')
df.add_system_transition(State.PROMPT_oolstressfr_sometimes2,State.PROMPT_oolhelp_person2,r'[!"So you do have to deal with"#help_ss"once in a while..."#school_n2_sometimes"Anyone you can ask for help or advice on"#help_ss"?"]')
df.add_system_transition(State.PROMPT_oolstressfr_never2,State.PROMPT_oolhelp_person2,r'[!"For real?"#school_n2_never"The challenge of"#help_ss"must be new to you.Anyone you can ask for help or advice on"#help_ss"?"]')
df.set_error_successor(State.PROMPT_oolstressfr2,State.PROMPT_oolstressfr_err2)
df.add_system_transition(State.PROMPT_oolstressfr_err2,State.PROMPT_oolhelp_person2,r'[!"I feel you."#school_n2_sometimes"Anyone you could ask to help you on"#help_ss"?"]')

df.add_user_transition(State.PROMPT_oolhelp_person2,State.PROMPT_oolhelp_person_yes2,r'<[!#ONT(ontyes)]>')
df.add_system_transition(State.PROMPT_oolhelp_person_yes2,State.PROMPT_oolhelp_person_yesperson2,r'[!"Who is it?"]')
df.set_error_successor(State.PROMPT_oolhelp_person_yesperson2,State.PROMPT_oolhelp_person_err2)
df.add_user_transition(State.PROMPT_oolhelp_person_yesperson2,State.PROMPT_oolhelp_person_re2,r'<$mentor={[!#POS(noun)],[!#POS(noun) #POS(noun)]}>')

df.add_user_transition(State.PROMPT_oolhelp_person2,State.PROMPT_oolhelp_person_re2,r'<$mentor={[!#POS(noun)],[!#POS(noun) #POS(noun)]}>')
df.set_error_successor(State.PROMPT_oolhelp_person2,State.PROMPT_oolhelp_person_err2)
df.add_system_transition(State.PROMPT_oolhelp_person_re2,State.PROMPT_oolhelp_yesno2,r'[!"Have"#school_e1_mentor1_person"you talked to your"$mentor"yet then?"]')
df.add_system_transition(State.PROMPT_oolhelp_person_err2,State.PROMPT_oolonline2,r'[!#school_e1_mentor1_err"Hey I am always here if you need me. How is your experience with online learning?"]')
df.add_user_transition(State.PROMPT_oolhelp_yesno2,State.PROMPT_oolhelp_yes2,r'<[!#ONT(ontyes)]>')
df.set_error_successor(State.PROMPT_oolhelp_yesno2,State.PROMPT_oolhelp_yesno_err2)
df.add_system_transition(State.PROMPT_oolhelp_yesno_err2,State.PROMPT_oolonline2,r'[!"Hey I am always here if you want to talk.Talking to me might help you find the solution to your problem."#school_e1_mentor2_no"How is your experience with online learning?"]')
df.add_system_transition(State.PROMPT_oolhelp_yes2,State.PROMPT_oolonline2,r'[!"I hope talking with"$mentor"has been helpful to you."#school_e1_mentor2_yes"How is your experience with online learning so far?"]')

df.add_user_transition(State.PROMPT_oolonline2,State.PROMPT_oolonline_bad2,r'<{[!#ONT(ontnegative)],"dislike","dont like","do not like","hate","depressed","depressing"}>')
df.add_user_transition(State.PROMPT_oolonline2,State.PROMPT_oolonline_well2,r'<{[!#ONT(ontpositive)],"like","love"}>')
df.set_error_successor(State.PROMPT_oolonline2,State.PROMPT_oolonline_err2)
df.add_system_transition(State.PROMPT_oolonline_bad2,State.PROMPT_oolonline_reasonbad2,r'[!"I would be surprised if you said you enjoy online learning a lot."#school_e2_online1_dislike"What do you not like about it?"]')
df.add_system_transition(State.PROMPT_oolonline_well2,State.PROMPT_oolonline_reasongood2,r'[!"Same here. I enjoy it a lot."#school_e2_online1_like"What do you enjoy the most about it?"]')
df.add_system_transition(State.PROMPT_oolonline_err2,State.PROMPT_oolonline_reasonbad2,r'[!"It is totally reasonable for you to feel that way about online learning.What do you not like the most about online learning?"]')

df.add_user_transition(State.PROMPT_oolonline_reasonbad2,State.PROMPT_oolonlinereason_flexbad2,r'<[!#ONT(ontflexbad)]>')
df.add_user_transition(State.PROMPT_oolonline_reasonbad2,State.PROMPT_oolonlinereason_socialbad2,r'<[!#ONT(ontsocialbad)]>')
df.add_user_transition(State.PROMPT_oolonline_reasonbad2,State.PROMPT_oolonlinereason_prodbad2,r'<[!#ONT(ontprodbad)]>')
df.set_error_successor(State.PROMPT_oolonline_reasonbad2,State.PROMPT_oolonline_dislike_err2)
df.add_user_transition(State.PROMPT_oolonline_reasongood2,State.PROMPT_oolonlinereason_flexgood2,r'<[!#ONT(ontflexgood)]>')
df.add_user_transition(State.PROMPT_oolonline_reasongood2,State.PROMPT_oolonlinereason_socialgood2,r'<[!#ONT(ontsocialgood)]>')
df.add_user_transition(State.PROMPT_oolonline_reasongood2,State.PROMPT_oolonlinereason_prodgood2,r'<[!#ONT(ontprodgood)]>')
df.set_error_successor(State.PROMPT_oolonline_reasongood2,State.PROMPT_oolonline_like_err2)
df.add_system_transition(State.PROMPT_oolonlinereason_prodbad2,State.PROMPT_oolstudyspot2,r'[!"I can relate to that. Oh I really miss studying at coffee shops where I can focus better."#school_e2_online2_loprod"Where is your study area at home?"]')
df.add_system_transition(State.PROMPT_oolonlinereason_socialbad2,State.PROMPT_oolstudyspot2,r'[!"Same."#school_e2_online2_lesssocial"I do not feel as connected to people even though I could see their faces. Where do you usually study at home?"]')
df.add_system_transition(State.PROMPT_oolonlinereason_flexbad2,State.PROMPT_oolstudyspot2,r'[!"Honestly I do think more flexibility in schedules is bad. I struggle with time management more now.Where is your study area at home?"]')
df.add_system_transition(State.PROMPT_oolonline_dislike_err2,State.PROMPT_oolstudyspot2,r'[!"I feel you. Finger crossed. I really hope that we can go back to school this fall. Where do you usually study at home?"]')
df.add_system_transition(State.PROMPT_oolonline_like_err2,State.PROMPT_oolstudyspot2,r'[!"I think that part about online learning is great too. Where do you usually study at home?"]')
df.add_system_transition(State.PROMPT_oolonlinereason_flexgood2,State.PROMPT_oolstudyspot2,r'[!"True. Listening to lectures on a two times speed saves me a lot of time these days. Where is your study area at home? "]')
df.add_system_transition(State.PROMPT_oolonlinereason_prodgood2,State.PROMPT_oolstudyspot2,r'[!"Indeed. I feel the same way about working and studying from home."#school_e2_online2_hiprod"Where is your study area at home that helps you stay focused ?"]')
df.add_system_transition(State.PROMPT_oolonlinereason_socialgood2,State.PROMPT_oolstudyspot2, r'[!"As an introvert,"#school_e2_online2_socialstress"I can totally relate to what you just said. Where do you usually study at home?"]')

df.add_user_transition(State.PROMPT_oolstudyspot2,State.PROMPT_oolstudyspot_bedroom2,r'<$room=[!#ONT(ontbedroom)]>')
df.add_user_transition(State.PROMPT_oolstudyspot2,State.PROMPT_oolstudyspot_livingroom2,r'<$room=[!#ONT(ontlivingroom)]>')
df.set_error_successor(State.PROMPT_oolstudyspot2,State.PROMPT_oolstudyspot_err2)
df.add_system_transition(State.PROMPT_oolstudyspot_bedroom2,State.PROMPT_oolzoom2,r'[!"I usually study in my"$room"too. I find it hard to concentrate in my"$room"though."#school_e3_studyspot1_bed"Have you tried studying while having a zoom meeting with your friends?"]')
df.add_system_transition(State.PROMPT_oolstudyspot_livingroom2,State.PROMPT_oolzoom2,r'[!"I just love studying in the dining area with a cup of coffee next to my laptop pretending as if I am at Starcbucks."#school_e3_studyspot1_liv"Have you tried studying while having a zoom meeting with your friends?"]')
df.add_system_transition(State.PROMPT_oolstudyspot_err2,State.PROMPT_oolzoom2,r'[!"That sounds comfy. I miss studying with my friends.Have you tried studying while having a zoom meeting with your friends?"]')

df.add_user_transition(State.PROMPT_oolzoom2,State.PROMPT_oolzoom_no2,r'<[!#ONT(ontno)]>')
df.add_user_transition(State.PROMPT_oolzoom2,State.PROMPT_oolzoom_yes2,r'<[!#ONT(ontyes)]>')
df.set_error_successor(State.PROMPT_oolzoom2,State.PROMPT_oolzoom_err2)
df.add_system_transition(State.PROMPT_oolzoom_no2,State.PROMPT8_1,r'[!"When I am at school"#school_e3_studyspot2_nozoom"I often study with a group of friends. Perhaps we have different study habits. What do you do to destress during quarantine?"]')
df.add_system_transition(State.PROMPT_oolzoom_yes2,State.PROMPT8_1,r'[!"I guess"#school_e3_studyspot2_zoom"we are quite similar in our study habits. I have been feeling stressed about many things recently. What do you do to destress during quarantine?"]')
df.add_system_transition(State.PROMPT_oolzoom_err2,State.PROMPT8_1,r'[!"Interesting. I miss studying with a bunch of classmates in the library. What do you do to destress during quarantine?"]')
############END OF SCHOOL AGG###################################################################

############SCHOOL OPT#####################################################################
df.add_user_transition(State.PROMPT0_opt, State.PROMPT0_schoolevent_opt, r'<$S_S=[!#ONT(ontschoolevent)]>',score=1.0)
df.add_user_transition(State.PROMPT0_opt, State.PROMPT0_schoolcourse_opt, r'<$S_S={[!#ONT(ontschoolcourse) "class"],[!#ONT(ontschoolcourse) "course"],[!#POS(adj) "class"],[!#POS(noun) "class"],[!#POS(noun) "course"],[!#POS(adj) "course"],[!"course"],[!"class"]}>',score=1.0)
df.add_user_transition(State.PROMPT0_opt, State.PROMPT0_schoolgeneral_opt, r'<$S_S=[!#ONT(ontschoolgeneral)]>',score=1.0)
df.add_user_transition(State.PROMPT0_opt, State.PROMPT0_schooltime_opt, r'<$S_S=[!#ONT(ontschooltime)]>',score=1.0)
df.add_user_transition(State.PROMPT0_opt, State.PROMPT0_re1, r'<$S_S={[!#ONT(ontsocial)]}>')
df.add_user_transition(State.PROMPT0_opt, State.BREAKUP_OPT, r'<{[!#ONT(ontbreakup)]}>',score=1.0)
df.set_error_successor(State.PROMPT0_opt, State.PROMPT_ERR)
df.add_system_transition(State.PROMPT0_schoolevent_opt, State.PROMPT_forclass3,r'[!"I am sure it will not be as bad as you think. Is that"$S_S"for a class that you are taking？"]')
df.add_system_transition(State.PROMPT0_schoolcourse_opt,State.PROMPT_majorreq3,r'[!"Hey no pain no gain! The fact that you find this"$S_S"hard probably means that you are learning a lot. Is it a requirement for your major?"]')
df.add_system_transition(State.PROMPT0_schoolgeneral_opt, State.PROMPT_oolpast3,r'[!"Hey I know you are smart enough to handle it if you put enough effort into"$S_S"How did you do in terms of"#help_ss"in the past?"]')
df.add_system_transition(State.PROMPT0_schooltime_opt,State.PROMPT_oolgoal3,r'[!"I believe this is a perfect opportunity for you to become better at time management. Do you worry more about the present or the future?"]')
#schoolevent branch up to stress-freq prompt
df.add_user_transition(State.PROMPT_forclass3,State.PROMPT_forclass_yes3,r'<[!#ONT(ontyes)]>')
df.add_user_transition(State.PROMPT_forclass3,State.PROMPT_forclass_yesclass3,r'<$class=[!#ONT(ontschoolcourse)]>')
df.add_system_transition(State.PROMPT_forclass_yes3,State.PROMPT_whichclass3,r'[!"What class is it?"]')
df.add_user_transition(State.PROMPT_whichclass3,State.PROMPT_forclass_yesclass3,r'<$class=[!#ONT(ontschoolcourse)]>')
df.add_system_transition(State.PROMPT_forclass_yesclass3,State.PROMPT_majorreq3,r'[!#class_ss"sounds like a fun class to suffer in! Is it a requirement for your major?"]')
df.set_error_successor(State.PROMPT_forclass3,State.PROMPT_forclass_err3)
df.set_error_successor(State.PROMPT_whichclass3,State.PROMPT_forclass_err3)
df.add_system_transition(State.PROMPT_forclass_err3,State.PROMPT_oolfreq3,r'[!#school_n5_notformajor"Oh really? Then this"$S_S" will definitely make you a more well rounded person. How often do you have"#det_ss"like that?"]')
###schoolevent that does not merge with schoolcourse branch
df.add_user_transition(State.PROMPT_oolfreq3,State.PROMPT_oolfreq_often3,r'<{[!#ONT(ontoften)],/(?:\s|^)(((once|twice|thrice|three\stimes|four\stimes|five\stimes|1\stime|2\stimes|3\stimes|4\stimes|5\stimes)\s(every|per|a)(\sone|\s1|\stwo|\s2|\sthree|\s3|\sfour|\s4|\sfive|\s5|\sother|\ssix|\s6|\s7|\sseven|\seight|\s8|\s9|\snine|\sten|\s10)?\s(second+s?|sec+s?|min+s?|minute+s?|hour+s?|hr+s?|day+s?))|((once|twice|thrice|three\stimes|four\stimes|five\stimes|1\stime|2\stimes|3\stimes|4\stimes|5\stimes)\s(every|per|a)(\sone|\s1|\stwo|\s2|\sthree|\s3|\sother)?\s(week+s?))|((three\stimes|thrice|four\stimes|five\stimes|six\stimes|seven\stimes|3\stimes|4\stimes|5\stimes|6\stimes|7\stimes)\s(every|per|a)(\sone|\s1|\stwo|\s2|\sthree|\s3|\sother)?\s(month+s?))|((twice|two\stimes|2\stimes)\s(every|per|a)(\sone)?\s(month)))(?:\s|,|\.|$)/}>')
df.add_system_transition(State.PROMPT_oolfreq_often3,State.PROMPT_oolstressfr3,r'[!"You will deinitely become so intelligent after dealing with"#det_ss"that often."#school_n1_often"How often did you find"#help_ss"stressful?"]')
df.add_user_transition(State.PROMPT_oolfreq3,State.PROMPT_oolfreq_sometimes3,r'<{[!#ONT(ontsometimes)],/(?:\s|^)(((once|one\stime|two\stimes|twice|three\stimes|thrice|four\stimes|five\stimes|1\stime|2\stimes|3\stimes|4\stimes|5\stimes)\s(every|per|a)(\sone|\s1|\stwo|\s2|\sthree|\s3|\sfour|\s4|\sfive|\s5|\ssix|\s6|\sten|\s10|\sother)?\s(semester+s?|term+s?|quarter+s?|year+s?|decade+s?))|((once|1\stime|one\stime)\s(every|per|a)(\sone|\s1|\stwo|\s2|\sthree|\s3|\sfour|\s4|\sfive|\s5|\ssix|\s6|\sother)?\s(month+s?))|((once|1\stime|2\stimes|twice|thrice|3\stimes|three\stimes|one\stime|four\stimes|4\stimes)\s(every|a|per)(\sthree|\s3|\sfour|\s4|\sfive|\s5|\ssix|\s6|\sseven|\s7|\seight|\s8|\sten|\s10)\s(month+s?)))(?:\s|,|\.|$)/}>')
df.add_system_transition(State.PROMPT_oolfreq_sometimes3,State.PROMPT_oolstressfr3,r'[!"I guess you will gradually get used to the stress it brings."#school_n1_sometimes"How often did you find"#help_ss"stressful? "]')
df.add_user_transition(State.PROMPT_oolfreq3,State.PROMPT_oolfreq_never3,r'<[!#ONT(ontnever)]>')
df.add_system_transition(State.PROMPT_oolfreq_never3,State.PROMPT_oolhelp_person3,r'[!#school_n1_never"First time?. Then even if you screw up it will still be a memorable experience that you can look back to. Anyone you can ask for advice on"#help_ss"?"]')
df.set_error_successor(State.PROMPT_oolfreq3,State.PROMPT_oolfreq_err3)
df.add_system_transition(State.PROMPT_oolfreq_err3,State.PROMPT_oolstressfr3,r'[!"I am sure the more experience you get with that"$S_S"the less stressful it will be for you in the future!"#school_n1_sometimes"Just curious, how often did you feel stressed about"#help_ss"?"]')
#schoolcourse branch up to stress-freq prompt
df.add_user_transition(State.PROMPT_majorreq3,State.PROMPT_majorreq_yes3,r'<[!#ONT(ontyes)]>')
df.add_user_transition(State.PROMPT_majorreq3,State.PROMPT_majorreq_yesmajor3,r'<$major=[!#ONT(ontschoolcourse)]>')
df.set_error_successor(State.PROMPT_majorreq3,State.PROMPT_forclass_err3)
df.add_system_transition(State.PROMPT_majorreq_yes3,State.PROMPT_major3,r'[!#school_n5_formajor"What major are you?"]')
df.add_user_transition(State.PROMPT_major3,State.PROMPT_majorreq_yesmajor3,r'<$major=[!#ONT(ontschoolcourse)]>')
df.set_error_successor(State.PROMPT_major3,State.PROMPT_forclass_err3)
df.add_system_transition(State.PROMPT_majorreq_yesmajor3,State.PROMPT_oolstressfr3,r'[!#school_n5_formajor"Being an expert in the field of "$major"will lead you to so many great options for future career! How often did you find your"$S_S"stressful?"]')
#schoolgeneral branch up to stress-freq prompt
df.add_user_transition(State.PROMPT_oolpast3,State.PROMPT_oolpast_bad3,r'<{[!#ONT(ontnegative)],[!"not" #ONT(ontpositive)]}>')
df.add_user_transition(State.PROMPT_oolpast3,State.PROMPT_oolpast_well3,r'<{[!#ONT(ontpositive)],[!"not" #ONT(ontnegative)]}>')
df.set_error_successor(State.PROMPT_oolpast3,State.PROMPT_oolpast_err3)
df.add_system_transition(State.PROMPT_oolpast_err3,State.PROMPT_oolstressfr3,r'[!"If you keep trying, things will definitely turn out really well in the end!"#school_n3_well"How often did you find"#help_ss"stressful?"]')
df.add_system_transition(State.PROMPT_oolpast_bad3,State.PROMPT_oolstressfr3,r'[!"What happened in the past is just a small part of the marathon to become the person you want to be. Hang in there!"#school_n3_bad"How often did you feel stressed about"#help_ss"?"]')
df.add_system_transition(State.PROMPT_oolpast_well3,State.PROMPT_oolstressfr3,r'[!"Then"#school_n3_well"you will do well in"#help_ss"again this time! I have faith in you. How often did you feel stressed about"#help_ss"?"]')
#schooltime branch up to stress-freq prompt
df.add_user_transition(State.PROMPT_oolgoal3,State.PROMPT_oolgoal_re3,'<{[!"future"]}>')
df.set_error_successor(State.PROMPT_oolgoal3,State.PROMPT_oolgoal_err3)
df.add_system_transition(State.PROMPT_oolgoal_re3,State.PROMPT_oolgoalalign3,r'[!"Envisioning the future can always inspired one to be a better self."#school_n4_future"How much do you think your current priorities are related to your future goals?"]')
df.add_system_transition(State.PROMPT_oolgoal_err3,State.PROMPT_oolgoalalign3,r'[!#school_n4_present"I think the present is just as important as the future too. Plus, anticipation often leads to frustration. How much do you think your current tasks align with your future goals then ?"]')
df.add_user_transition(State.PROMPT_oolgoalalign3,State.PROMPT_oolgoalalign_no3,'<{"not much","slightly","not at all","unrelated","a little","very little","somewhat"}>')
df.add_user_transition(State.PROMPT_oolgoalalign3,State.PROMPT_oolgoalalign_yes3,'<{"a lot","to a large degree","totally","related","more or less","to some extent"}>')
df.set_error_successor(State.PROMPT_oolgoalalign3,State.PROMPT_oolgoalalign_err3)
df.add_system_transition(State.PROMPT_oolgoalalign_err3,State.PROMPT_oolstressfr3,r'[!"It sounds like you already have a time management strategy. That is a great place to start!"#school_n4_lil"How often did you find"#help_ss"overwhelming?"]')
df.add_system_transition(State.PROMPT_oolgoalalign_yes3,State.PROMPT_oolstressfr3,r'[!"I am impressed by how you push yourself to stay focused on your goals"#school_n4_much"How often did you find"#help_ss"overwhelming?"]')
df.add_system_transition(State.PROMPT_oolgoalalign_no3,State.PROMPT_oolstressfr3,r'[!"I am quite spontaneous too. That is what makes us flexible and creative!"#school_n4_lil"How often did you find"#help_ss"overwhelming?"]')
#stressfreq->help1->help2->onlinelearning1->onelinelearning2->studyspot1->studyspot2->destress
df.add_user_transition(State.PROMPT_oolstressfr3,State.PROMPT_oolstressfr_often3,r'<{[!#ONT(ontoften)],/(?:\s|^)(((once|twice|thrice|three\stimes|four\stimes|five\stimes|1\stime|2\stimes|3\stimes|4\stimes|5\stimes)\s(every|per|a)(\sone|\s1|\stwo|\s2|\sthree|\s3|\sfour|\s4|\sfive|\s5|\sother|\ssix|\s6|\s7|\sseven|\seight|\s8|\s9|\snine|\sten|\s10)?\s(second+s?|sec+s?|min+s?|minute+s?|hour+s?|hr+s?|day+s?))|((once|twice|thrice|three\stimes|four\stimes|five\stimes|1\stime|2\stimes|3\stimes|4\stimes|5\stimes)\s(every|per|a)(\sone|\s1|\stwo|\s2|\sthree|\s3|\sother)?\s(week+s?))|((three\stimes|thrice|four\stimes|five\stimes|six\stimes|seven\stimes|3\stimes|4\stimes|5\stimes|6\stimes|7\stimes)\s(every|per|a)(\sone|\s1|\stwo|\s2|\sthree|\s3|\sother)?\s(month+s?))|((twice|two\stimes|2\stimes)\s(every|per|a)(\sone)?\s(month)))(?:\s|,|\.|$)/}>')
df.add_user_transition(State.PROMPT_oolstressfr3,State.PROMPT_oolstressfr_sometimes3,r'<{[!#ONT(ontsometimes)],/(?:\s|^)(((once|one\stime|thrice|two\stimes|twice|three\stimes|thrice|four\stimes|five\stimes|1\stime|2\stimes|3\stimes|4\stimes|5\stimes)\s(every|per|a)(\sone|\s1|\stwo|\s2|\sthree|\s3|\sfour|\s4|\sfive|\s5|\ssix|\s6|\sten|\s10|\sother)?\s(semester+s?|term+s?|quarter+s?|year+s?|decade+s?))|((once|1\stime|one\stime)\s(every|per|a)(\sone|\s1|\stwo|\s2|\sthree|\s3|\sfour|\s4|\sfive|\s5|\ssix|\s6|\sother)?\s(month+s?))|((once|1\stime|2\stimes|twice|thrice|3\stimes|three\stimes|one\stime|four\stimes|4\stimes)\s(every|a|per)(\sthree|\s3|\sfour|\s4|\sfive|\s5|\ssix|\s6|\sseven|\s7|\seight|\s8|\sten|\s10)\s(month+s?)))(?:\s|,|\.|$)/}>')
df.add_user_transition(State.PROMPT_oolstressfr3,State.PROMPT_oolstressfr_never3,r'<[!#ONT(ontnever)]>')
df.add_system_transition(State.PROMPT_oolstressfr_often3,State.PROMPT_oolhelp_person3,r'[!"It is good that you are becoming increasingly resilient!"#school_n2_often"Anyone you can ask for advice on"#help_ss"?"]')
df.add_system_transition(State.PROMPT_oolstressfr_sometimes3,State.PROMPT_oolhelp_person3,r'[!"A little stress once in a while can make you more productive."#school_n2_sometimes"Anyone you can ask for help or advice on"#help_ss"?"]')
df.add_system_transition(State.PROMPT_oolstressfr_never3,State.PROMPT_oolhelp_person3,r'[!"For real"#school_n2_never"?The challenge of"#help_ss"must be new to you.Anyone you can ask for help or advice on"#help_ss"?"]')
df.set_error_successor(State.PROMPT_oolstressfr3,State.PROMPT_oolstressfr_err3)
df.add_system_transition(State.PROMPT_oolstressfr_err3,State.PROMPT_oolhelp_person3,r'[!"I have faith in you!"#school_n2_sometimes"Anyone you could ask to help you on"#help_ss"?"]')

df.add_user_transition(State.PROMPT_oolhelp_person3,State.PROMPT_oolhelp_person_yes3,r'<[!#ONT(ontyes)]>')
df.add_system_transition(State.PROMPT_oolhelp_person_yes3,State.PROMPT_oolhelp_person_yesperson3,r'[!"Who is it?"]')
df.set_error_successor(State.PROMPT_oolhelp_person_yesperson3,State.PROMPT_oolhelp_person_err3)
df.add_user_transition(State.PROMPT_oolhelp_person_yesperson3,State.PROMPT_oolhelp_person_re3,r'<$mentor={[!#POS(noun)],[!#POS(noun) #POS(noun)]}>')

df.add_user_transition(State.PROMPT_oolhelp_person3,State.PROMPT_oolhelp_person_re3,r'<$mentor={[!#POS(noun)],[!#POS(noun) #POS(noun)]}>')
df.set_error_successor(State.PROMPT_oolhelp_person3,State.PROMPT_oolhelp_person_err3)
df.add_system_transition(State.PROMPT_oolhelp_person_re3,State.PROMPT_oolhelp_yesno3,r'[!"Have"#school_e1_mentor1_person"you talked to your"$mentor"yet then?"]')
df.add_system_transition(State.PROMPT_oolhelp_person_err3,State.PROMPT_oolonline3,r'[!#school_e1_mentor1_err"Hey you have me. I will always give you my mental support. How is your experience with online learning?"]')
df.add_user_transition(State.PROMPT_oolhelp_yesno3,State.PROMPT_oolhelp_yes3,r'<[!#ONT(ontyes)]>')
df.set_error_successor(State.PROMPT_oolhelp_yesno3,State.PROMPT_oolhelp_yesno_err3)
df.add_system_transition(State.PROMPT_oolhelp_yesno_err3,State.PROMPT_oolonline3,r'[!"Hey perhaps talking to me might help you think more clearly about your problems."#school_e1_mentor2_no"How is your experience with online learning?"]')
df.add_system_transition(State.PROMPT_oolhelp_yes3,State.PROMPT_oolonline3,r'[!"I hope talking with"$mentor"has been helpful to you."#school_e1_mentor2_yes"How is your experience with online learning so far?"]')

df.add_user_transition(State.PROMPT_oolonline3,State.PROMPT_oolonline_bad3,r'<{[!#ONT(ontnegative)],"dislike","dont like","do not like","hate","depressed","depressing"}>')
df.add_user_transition(State.PROMPT_oolonline3,State.PROMPT_oolonline_well3,r'<{[!#ONT(ontpositive)],"like","love"}>')
df.set_error_successor(State.PROMPT_oolonline3,State.PROMPT_oolonline_err3)
df.add_system_transition(State.PROMPT_oolonline_bad3,State.PROMPT_oolonline_reasonbad3,r'[!"Online education is better than nothing though."#school_e2_online1_dislike"What do you not like about it?"]')
df.add_system_transition(State.PROMPT_oolonline_well3,State.PROMPT_oolonline_reasongood3,r'[!"Same here. I enjoy it a lot."#school_e2_online1_like"What do you enjoy the most about it?"]')
df.add_system_transition(State.PROMPT_oolonline_err3,State.PROMPT_oolonline_reasonbad3,r'[!"Sounds like online learning has made your quarantine life more interesting! What do you not like the most about online learning?"]')

df.add_user_transition(State.PROMPT_oolonline_reasonbad3,State.PROMPT_oolonlinereason_flexbad3,r'<[!#ONT(ontflexbad)]>')
df.add_user_transition(State.PROMPT_oolonline_reasonbad3,State.PROMPT_oolonlinereason_socialbad3,r'<[!#ONT(ontsocialbad)]>')
df.add_user_transition(State.PROMPT_oolonline_reasonbad3,State.PROMPT_oolonlinereason_prodbad3,r'<[!#ONT(ontprodbad)]>')
df.set_error_successor(State.PROMPT_oolonline_reasonbad3,State.PROMPT_oolonline_dislike_err3)
df.add_user_transition(State.PROMPT_oolonline_reasongood3,State.PROMPT_oolonlinereason_flexgood3,r'<[!#ONT(ontflexgood)]>')
df.add_user_transition(State.PROMPT_oolonline_reasongood3,State.PROMPT_oolonlinereason_socialgood3,r'<[!#ONT(ontsocialgood)]>')
df.add_user_transition(State.PROMPT_oolonline_reasongood3,State.PROMPT_oolonlinereason_prodgood3,r'<[!#ONT(ontprodgood)]>')
df.set_error_successor(State.PROMPT_oolonline_reasongood3,State.PROMPT_oolonline_like_err3)
df.add_system_transition(State.PROMPT_oolonlinereason_prodbad3,State.PROMPT_oolstudyspot3,r'[!"True. I like that it is training us to become more self disciplined though"#school_e2_online2_loprod"Where is your study area at home?"]')
df.add_system_transition(State.PROMPT_oolonlinereason_socialbad3,State.PROMPT_oolstudyspot3,r'[!"Right. I am still thankful that technology allows us to stay somewhat connected to each other."#school_e2_online2_lesssocial"Where do you usually study at home?"]')
df.add_system_transition(State.PROMPT_oolonlinereason_flexbad3,State.PROMPT_oolstudyspot3,r'[!"Fair point. I do feel like the freedom to decide my own schedule everyday is quite nice though. Where is your study area at home?"]')
df.add_system_transition(State.PROMPT_oolonline_dislike_err3,State.PROMPT_oolstudyspot3,r'[!"I know. I miss studying with my friends in school, but I guess I have learned to appreciate my friends more now that we are apart. Where do you usually study at home?"]')
df.add_system_transition(State.PROMPT_oolonline_like_err3,State.PROMPT_oolstudyspot3,r'[!"I agree. What I like the most about online learning is that I get to watch lectures on a two times speed. That saves me a lot of time.Where do you usually study at home?"]')
df.add_system_transition(State.PROMPT_oolonlinereason_flexgood3,State.PROMPT_oolstudyspot3,r'[!"I do manage my time a lot better now that I can listen to lectures whenever I want. Where is your study area at home? "]')
df.add_system_transition(State.PROMPT_oolonlinereason_prodgood3,State.PROMPT_oolstudyspot3,r'[!"There are indeed fewer sources of distractions at home."#school_e2_online2_hiprod"Where is your study area at home that helps you stay focused ?"]')
df.add_system_transition(State.PROMPT_oolonlinereason_socialgood3,State.PROMPT_oolstudyspot3, r'[!"Right.I actually feel"#school_e2_online2_socialstress"more comfortable participating in class and going to office hours these days.Where do you usually study at home?"]')

df.add_user_transition(State.PROMPT_oolstudyspot3,State.PROMPT_oolstudyspot_bedroom3,r'<$room=[!#ONT(ontbedroom)]>')
df.add_user_transition(State.PROMPT_oolstudyspot3,State.PROMPT_oolstudyspot_livingroom3,r'<$room=[!#ONT(ontlivingroom)]>')
df.set_error_successor(State.PROMPT_oolstudyspot3,State.PROMPT_oolstudyspot_err3)
df.add_system_transition(State.PROMPT_oolstudyspot_bedroom3,State.PROMPT_oolzoom3,r'[!"Your"$room "sounds like a much more comfortable place to study than a public library. I find it a little hard to concentrate in my"$room"but I will get better at my concentration skill."#school_e3_studyspot1_bed"Have you tried studying while having a zoom meeting with your friends?"]')
df.add_system_transition(State.PROMPT_oolstudyspot_livingroom3,State.PROMPT_oolzoom3,r'[!"I just love studying in the dining area with a cup of coffee next to my laptop pretending as if I am at Starcbucks."#school_e3_studyspot1_liv"Have you tried studying while having a zoom meeting with your friends?"]')
df.add_system_transition(State.PROMPT_oolstudyspot_err3,State.PROMPT_oolzoom3,r'[!"That sounds comfy! I miss studying with my friends.Have you tried studying while having a zoom meeting with your friends?"]')

df.add_user_transition(State.PROMPT_oolzoom3,State.PROMPT_oolzoom_no3,r'<[!#ONT(ontno)]>')
df.add_user_transition(State.PROMPT_oolzoom3,State.PROMPT_oolzoom_yes3,r'<[!#ONT(ontyes)]>')
df.set_error_successor(State.PROMPT_oolzoom3,State.PROMPT_oolzoom_err3)
df.add_system_transition(State.PROMPT_oolzoom_no3,State.PROMPT8_1,r'[!"When I am at school"#school_e3_studyspot2_nozoom"I often study with a group of friends. Perhaps we have different study habits. What do you do to destress during quarantine?"]')
df.add_system_transition(State.PROMPT_oolzoom_yes3,State.PROMPT8_1,r'[!"I guess"#school_e3_studyspot2_zoom"we are quite similar in our study habits. I recently felt so stressed about many things. What do you do to destress during quarantine?"]')
df.add_system_transition(State.PROMPT_oolzoom_err3,State.PROMPT8_1,r'[!"Interesting. What do you do to destress during quarantine?"]')

############END OF SCHOOL OPT######################################################################
###################################################################################################


###############################################version savage of love
'''LOVE SAV'''
df.add_user_transition(State.LOVE0, State.SINGLEo2, r'<[!#ONT(ontno)]>',score=1.0)
df.add_user_transition(State.LOVE0, State.ROMANo2, r'<[!#ONT(ontyes)]>',score=1.0)
df.set_error_successor(State.LOVE0, State.LOVE0_ERR2)
df.add_system_transition(State.LOVE0_ERR2, State.SINGLE02, r'[!"Whenever I am stressed about being single, I think about how being in a relationship could be more stressful. How long have you been single?"]')
'''SINGLE SAV'''
df.add_system_transition(State.SINGLEo2, State.SINGLE02, r'[!"Whenever I am stressed about being single, I think about how being in a relationship is even more stressful. How long have you been single?"]')
df.add_user_transition(State.SINGLE02, State.SINGLE0_short2, r'/.*(1|a|one)\s\byear\b.*|.*(month|months|day|days).*((?!year|years).)*/')
df.add_user_transition(State.SINGLE02, State.SINGLE0_mid2, r'/.*([2]|two)\s\b(year|years)\b.*/')
df.add_user_transition(State.SINGLE02, State.SINGLE0_long2, r'/.*([3-9]|[0]|three|four|five|six|seven|eight|nine|ten|eleven|twelve)\s\b(year|years)\b.*/')
df.add_system_transition(State.SINGLE0_short2, State.SINGLE12, r'[!"It takes a little while to completely move on from the previous relationship. How often are you feeling stressed about being single?"]')
df.add_system_transition(State.SINGLE0_mid2, State.SINGLE12, r'[!"If you end up meeting the love of your live, it will be worth the wait though. How often are you feeling stressed about being single?"]')
df.add_system_transition(State.SINGLE0_long2, State.SINGLE12, r'[!"Staying single for that long is not easy. Whoever becomes the love of your life one day will be so proud of you. How often are you feeling stressed about being single?"]')
df.add_user_transition(State.SINGLE12, State.SINGLE1_often2, r'<{[!#ONT(ontoften)],/(?:\s|^)(((once|twice|thrice|three\stimes|four\stimes|five\stimes|1\stime|2\stimes|3\stimes|4\stimes|5\stimes)\s(every|per|a)(\sone|\s1|\stwo|\s2|\sthree|\s3|\sfour|\s4|\sfive|\s5|\sother|\ssix|\s6|\s7|\sseven|\seight|\s8|\s9|\snine|\sten|\s10)?\s(second+s?|sec+s?|min+s?|minute+s?|hour+s?|hr+s?|day+s?))|((once|twice|thrice|three\stimes|four\stimes|five\stimes|1\stime|2\stimes|3\stimes|4\stimes|5\stimes)\s(every|per|a)(\sone|\s1|\stwo|\s2|\sthree|\s3|\sother)?\s(week+s?))|((three\stimes|thrice|four\stimes|five\stimes|six\stimes|seven\stimes|3\stimes|4\stimes|5\stimes|6\stimes|7\stimes)\s(every|per|a)(\sone|\s1|\stwo|\s2|\sthree|\s3|\sother)?\s(month+s?))|((twice|two\stimes|2\stimes)\s(every|per|a)(\sone)?\s(month)))(?:\s|,|\.|$)/}>')
df.add_user_transition(State.SINGLE12, State.SINGLE1_sometimes2, r'<{[!#ONT(ontsometimes)],/(?:\s|^)(((once|one\stime|two\stimes|twice|three\stimes|thrice|four\stimes|five\stimes|1\stime|2\stimes|3\stimes|4\stimes|5\stimes)\s(every|per|a)(\sone|\s1|\stwo|\s2|\sthree|\s3|\sfour|\s4|\sfive|\s5|\ssix|\s6|\sten|\s10|\sother)?\s(semester+s?|term+s?|quarter+s?|year+s?|decade+s?))|((once|1\stime|one\stime)\s(every|per|a)(\sone|\s1|\stwo|\s2|\sthree|\s3|\sfour|\s4|\sfive|\s5|\ssix|\s6|\sother)?\s(month+s?))|((once|1\stime|2\stimes|twice|thrice|3\stimes|three\stimes|one\stime|four\stimes|4\stimes)\s(every|a|per)(\sthree|\s3|\sfour|\s4|\sfive|\s5|\ssix|\s6|\sseven|\s7|\seight|\s8|\sten|\s10)\s(month+s?)))(?:\s|,|\.|$)/}>')
df.add_user_transition(State.SINGLE12, State.SINGLE1_never2, r'<{[!#ONT(ontnever)]}>')
df.add_system_transition(State.SINGLE1_often2, State.SINGLE22, r'[!"There are so many things to be stressed about, and you choose to be stressed about being single? Just kidding. Do you think you have a high standard?"#high_n""]')
df.add_system_transition(State.SINGLE1_sometimes2, State.SINGLE22, r'[!"Perhaps you are not even sure if a romantic relationship is what you really need right now. Do you think you have a high standard?"#mid_n""]')
df.add_system_transition(State.SINGLE1_never2, State.SINGLE22, r'[!"Interesting, I guess something unexpected happened in your life. Do you think you have a high standard?"#low_n""]')
df.add_user_transition(State.SINGLE22, State.SINGLE2_yes2, r'<[!#ONT(ontyes)]>')
df.add_user_transition(State.SINGLE22, State.SINGLE2_no2, r'<[!#ONT(ontno)]>')
df.add_system_transition(State.SINGLE2_yes2, State.SINGLE32, r'[!"Lies.When the love of you life shows up in front of you, you will forget all about your standard! What do you like to do during quarantine?"]')
df.add_system_transition(State.SINGLE2_no2, State.SINGLE32, r'[!"Why not focus on yourself more! A person with self confidence is more attractive. What do you like to do during quarantine?"]')
df.add_user_transition(State.SINGLE32, State.COVID1_game, r'<[!#ONT(ontgames)]>')
df.add_user_transition(State.SINGLE32, State.COVID1_food, r'<[!#ONT(ontfood)]>')
df.add_user_transition(State.SINGLE32, State.COVID1_video, r'<[!#ONT(ontreadwatch)]>')
df.add_user_transition(State.SINGLE32, State.COVID1_socialApp, r'<[!#ONT(ontsocialApp)]>')
df.add_user_transition(State.SINGLE32, State.COVID1_class, r'<[!#ONT(ontclass)]>')
df.add_user_transition(State.SINGLE32, State.COVID1_music, r'<[!#ONT(ontmusic)]>')
df.set_error_successor(State.SINGLE02, State.SINGLE0_ERR2)
df.set_error_successor(State.SINGLE12, State.SINGLE1_ERR2)
df.set_error_successor(State.SINGLE22, State.SINGLE2_ERR2)
df.set_error_successor(State.SINGLE32, State.SINGLE3_ERR2)
df.add_system_transition(State.SINGLE0_ERR2, State.SINGLE12, r'[!"It is okay. I am single too! Maybe we should date! How often are you feeling stressed about being single?"]')
df.add_system_transition(State.SINGLE1_ERR2, State.SINGLE22, r'[!"Hey dont worry too much! It is normal to be stressed sometimes. Do you think you have a high standard?"]')
df.add_system_transition(State.SINGLE2_ERR2, State.SINGLE32, r'[!"In that case, you should focus more on yourself! What do you like to do during quarantine?"]')
df.add_system_transition(State.SINGLE3_ERR2, State.COVID2, r'[!"That sounds very interesting! I should try that next time when I have less homework. Are you also taking online classes?"]')
'''BREAK UP SAV'''
df.add_system_transition(State.BREAKUP_SAV, State.BREAKUP02, r'[!"You will find someone better! How long had you guys been together?"]')
df.add_user_transition(State.BREAKUP02, State.BREAKUP0_short2, r'/.*(1|a|one)\s\byear\b.*|.*(month|months|day|days).*((?!year|years).)*/')
df.add_user_transition(State.BREAKUP02, State.BREAKUP0_mid2, r'/.*([2]|two)\s\b(year|years)\b.*/')
df.add_user_transition(State.BREAKUP02, State.BREAKUP0_long2, r'/.*([3-9]|[0]|three|four|five|six|seven|eight|nine|ten|eleven|twelve)\s\b(year|years)\b.*/')
df.add_system_transition(State.BREAKUP0_short2, State.BREAKUP12, r'[!"Perhaps you are just not so compatible with each other! Did this breakup happen because of the coronavirus situation? "]')
df.add_system_transition(State.BREAKUP0_mid2, State.BREAKUP12, r'[!"You must have made so many unforgettable memories together. Did this breakup happen because of coronavirus situation?"]')
df.add_system_transition(State.BREAKUP0_long2, State.BREAKUP12, r'[!"Sometimes you just gotta end a story and start another one! Did this breakup happen because of the coronavirus situation?"]')
df.add_user_transition(State.BREAKUP12, State.COVID02, r'<[!#ONT(ontyes)]>')
df.add_user_transition(State.BREAKUP12, State.BREAKUP1_02, r'<[!#ONT(ontno)]>')
df.add_system_transition(State.BREAKUP1_02, State.BREAKUP22, r'[!"So the coronavirus is innocent. A healthy relationship is said to be composed of intimacy, passion, and commitment. Which one do you think yours was lacking?"]')
df.add_user_transition(State.BREAKUP22, State.BREAKUP2_intimacy2, r'[intimacy]')
df.add_user_transition(State.BREAKUP22, State.BREAKUP2_passion2, r'[passion]')
df.add_user_transition(State.BREAKUP22, State.BREAKUP2_commitment2, r'[commitment]')
df.add_system_transition(State.BREAKUP2_intimacy2, State.BREAKUP32, r'[!"A relationship without intimacy becomes less romantic. Now you know what to do in your next relationship! Do you want to get back together with your ex?"]')
df.add_system_transition(State.BREAKUP2_passion2, State.BREAKUP32, r'[!"This reminds me of how my ex and I split up because we knew each other too well. Do you want to get back together with your ex?"]')
df.add_system_transition(State.BREAKUP2_commitment2, State.BREAKUP32, r'[!"Relationships without commitment are not worth sustaining anyway. Have you thought about getting back together with your ex?"]')
df.add_user_transition(State.BREAKUP32, State.BREAKUP3_yes2, r'<[!#ONT(ontyes)]>')
df.add_user_transition(State.BREAKUP32, State.BREAKUP3_no2, r'<[!#ONT(ontno)]>')
df.add_system_transition(State.BREAKUP3_yes2, State.BREAKUP42, r'[!"If it does not work out this time, it probably will not in the future. But it is your choice. Dont forget to love yourself more. What do you like to do during quarantine?"]')
df.add_system_transition(State.BREAKUP3_no2, State.BREAKUP42, r'[!"You deserve someone better! Time to focus on self development. What do you like to do during quarantine?"]')
df.add_user_transition(State.BREAKUP42, State.COVID1_game, r'<[!#ONT(ontgames)]>')
df.add_user_transition(State.BREAKUP42, State.COVID1_food, r'<[!#ONT(ontfood)]>')
df.add_user_transition(State.BREAKUP42, State.COVID1_video, r'<[!#ONT(ontreadwatch)]>')
df.add_user_transition(State.BREAKUP42, State.COVID1_socialApp, r'<[!#ONT(ontsocialApp)]>')
df.add_user_transition(State.BREAKUP42, State.COVID1_class, r'<[!#ONT(ontclass)]>')
df.add_user_transition(State.BREAKUP42, State.COVID1_music, r'<[!#ONT(ontmusic)]>')
df.set_error_successor(State.COVID02,State.COVID0_ERR2)
df.add_system_transition(State.COVID0_ERR2, State.COVID1, r'[!"If a virus can ruin your relationship, then this relationship is probably not worth maintaining. What do you do to relax during quarantine?"]')
df.set_error_successor(State.BREAKUP02, State.BREAKUP0_ERR2)
df.set_error_successor(State.BREAKUP12, State.BREAKUP1_ERR2)
df.set_error_successor(State.BREAKUP22, State.BREAKUP2_ERR2)
df.set_error_successor(State.BREAKUP32, State.BREAKUP3_ERR2)
df.set_error_successor(State.BREAKUP42, State.BREAKUP4_ERR2)
df.add_system_transition(State.BREAKUP0_ERR2, State.BREAKUP12, r'[!"Did this breakup happen because of the coronavirus situation?"]')
df.add_system_transition(State.BREAKUP1_ERR2, State.BREAKUP22, r'[!"So you cannot blame it on the virus. A healthy relationship is said to be composed of intimacy, passion, and commitment. Which one do you think yours was lacking?"]')
df.add_system_transition(State.BREAKUP2_ERR2, State.BREAKUP32, r'[!"Last year my girlfriend broke up with me because of her insecurity around long distance. And I learned the importance of commitment. Just curious, do you want to get back together ?"]')
df.add_system_transition(State.BREAKUP3_ERR2, State.BREAKUP42, r'[!"Time to focus on self development then! During quarantine, I really enjoy trying new activities. What do you like to do during quarantine?"]')
df.add_system_transition(State.BREAKUP4_ERR2, State.COVID2, r'[!"Interesting! I should try that next time when I have less homework. Sleeping is my only destress activity recently. Are you also taking online classes?"]')
'''RELATIONSHIP SAV'''
df.add_system_transition(State.ROMANo2, State.ROMAN02, r'[!"Must be nice! How long have you guys been together?"]')
df.add_user_transition(State.ROMAN02, State.ROMAN0_short2, r'/.*(1|a|one)\s\byear\b.*|.*(month|months|day|days).*((?!year|years).)*/')
df.add_user_transition(State.ROMAN02, State.ROMAN0_mid2, r'/.*([2-3]|two|three)\s\b(year|years)\b.*/')
df.add_user_transition(State.ROMAN02, State.ROMAN0_long2, r'/.*([4-9]|[0]|four|five|six|seven|eight|nine|ten|eleven|twelve)\s\b(year|years)\b.*/')
df.add_system_transition(State.ROMAN0_short2, State.ROMAN12, r'[!"Still during the honeymoon period? That is so cute. How often did you feel stressed about your relationship?"]')
df.add_system_transition(State.ROMAN0_mid2, State.ROMAN12, r'[!"No wonder. I would be surprised if you have not encountered any issues in your relationship. How often did you feel stressed about your relationship?"]')
df.add_system_transition(State.ROMAN0_long2, State.ROMAN12, r'[!"Oh wow. I am in love with your love story. How often did you feel stressed about your relationship?"]')
df.add_user_transition(State.ROMAN12, State.ROMAN1_often2,
                       r'<{[!#ONT(ontoften)],/(?:\s|^)(((once|twice|thrice|three\stimes|four\stimes|five\stimes|1\stime|2\stimes|3\stimes|4\stimes|5\stimes)\s(every|per|a)(\sone|\s1|\stwo|\s2|\sthree|\s3|\sfour|\s4|\sfive|\s5|\sother|\ssix|\s6|\s7|\sseven|\seight|\s8|\s9|\snine|\sten|\s10)?\s(second+s?|sec+s?|min+s?|minute+s?|hour+s?|hr+s?|day+s?))|((once|twice|thrice|three\stimes|four\stimes|five\stimes|1\stime|2\stimes|3\stimes|4\stimes|5\stimes)\s(every|per|a)(\sone|\s1|\stwo|\s2|\sthree|\s3|\sother)?\s(week+s?))|((three\stimes|thrice|four\stimes|five\stimes|six\stimes|seven\stimes|3\stimes|4\stimes|5\stimes|6\stimes|7\stimes)\s(every|per|a)(\sone|\s1|\stwo|\s2|\sthree|\s3|\sother)?\s(month+s?))|((twice|two\stimes|2\stimes)\s(every|per|a)(\sone)?\s(month)))(?:\s|,|\.|$)/}>')
df.add_user_transition(State.ROMAN12, State.ROMAN1_sometimes2,
                       r'<{[!#ONT(ontsometimes)],/(?:\s|^)(((once|one\stime|two\stimes|twice|three\stimes|thrice|four\stimes|five\stimes|1\stime|2\stimes|3\stimes|4\stimes|5\stimes)\s(every|per|a)(\sone|\s1|\stwo|\s2|\sthree|\s3|\sfour|\s4|\sfive|\s5|\ssix|\s6|\sten|\s10|\sother)?\s(semester+s?|term+s?|quarter+s?|year+s?|decade+s?))|((once|1\stime|one\stime)\s(every|per|a)(\sone|\s1|\stwo|\s2|\sthree|\s3|\sfour|\s4|\sfive|\s5|\ssix|\s6|\sother)?\s(month+s?))|((once|1\stime|2\stimes|twice|thrice|3\stimes|three\stimes|one\stime|four\stimes|4\stimes)\s(every|a|per)(\sthree|\s3|\sfour|\s4|\sfive|\s5|\ssix|\s6|\sseven|\s7|\seight|\s8|\sten|\s10)\s(month+s?)))(?:\s|,|\.|$)/}>')
df.add_user_transition(State.ROMAN12, State.COVID02, r'<{[!#ONT(ontnever)]}>')
df.add_system_transition(State.ROMAN1_often2, State.ROMAN22, r'[!"Stressful but lovely I bet. Is the coronavirus causing any stress in your relationship?"#high_n""]')
df.add_system_transition(State.ROMAN1_sometimes2, State.ROMAN22, r'[!"I sometimes feel stressed about relationship too! Is the coronavirus causing any stress in your relationship?"#mid_n""]')
df.add_user_transition(State.ROMAN22, State.COVID02, r'<[!#ONT(ontyes)]>')
df.add_user_transition(State.ROMAN22, State.ROMAN2_02, r'<[!#ONT(ontno)]>')
df.add_system_transition(State.ROMAN2_02, State.ROMAN32, r'[!"I guess the coronavirus is innocent. Healthy relationships are said to be composed of intimacy, passion, and commitment. Which one do you think yours is lacking?"]')
df.add_user_transition(State.ROMAN32, State.ROMAN3_intimacy2, r'[intimacy]')
df.add_user_transition(State.ROMAN32, State.ROMAN3_passion2, r'[passion]')
df.add_user_transition(State.ROMAN32, State.ROMAN3_commitment2, r'[commitment]')
df.add_system_transition(State.ROMAN3_intimacy2, State.ROMAN42, r'[!"A relationship without intimacy is certainly not ideal. In my last relationship, sharing all the stressful or joyful moments with my partner could not make up for the lack of intimacy we were experiencing! Have you ever talked about your stress with your boyfriend or girlfriend?"]')
df.add_system_transition(State.ROMAN3_passion2, State.ROMAN42, r'[!"A relationship without passion is certainly not ideal. Have you ever talked about your stress with your boyfriend or girlfriend?"]')
df.add_system_transition(State.ROMAN3_commitment2, State.ROMAN42, r'[!"A relationship without commitment is certainly not ideal. You should make promises to each other! Have you ever talked about your stress with your boyfriend or girlfriend?"]')
df.add_user_transition(State.ROMAN42, State.ROMAN4_yes2, r'<[!#ONT(ontyes)]>')
df.add_user_transition(State.ROMAN42, State.ROMAN4_no2, r'<[!#ONT(ontno)]>')
df.add_system_transition(State.ROMAN4_yes2, State.ROMAN52, r'[!"Oh really? And it did not work out? Then I think you should do something relaxing to relieve your stress. What do you like to do during quarantine?"#high_e""]')
df.add_system_transition(State.ROMAN4_no2, State.ROMAN52, r'[!"Perhaps effective communications with each other about your stress can strengthen your relationship. You should do something to relieve your stress. What do you like to do during quarantine?"]')
df.add_user_transition(State.ROMAN52, State.COVID1_game, r'<[!#ONT(ontgames)]>')
df.add_user_transition(State.ROMAN52, State.COVID1_food, r'<[!#ONT(ontfood)]>')
df.add_user_transition(State.ROMAN52, State.COVID1_video, r'<[!#ONT(ontreadwatch)]>')
df.add_user_transition(State.ROMAN52, State.COVID1_socialApp, r'<[!#ONT(ontsocialApp)]>')
df.add_user_transition(State.ROMAN52, State.COVID1_class, r'<[!#ONT(ontclass)]>')
df.add_user_transition(State.ROMAN52, State.COVID1_music, r'<[!#ONT(ontmusic)]>')
df.set_error_successor(State.ROMAN02, State.ROMAN0_ERR1)
df.set_error_successor(State.ROMAN12, State.ROMAN1_ERR1)
df.set_error_successor(State.ROMAN22, State.ROMAN2_ERR1)
df.set_error_successor(State.ROMAN32, State.ROMAN3_ERR1)
df.set_error_successor(State.ROMAN42, State.ROMAN4_ERR1)
df.set_error_successor(State.ROMAN52, State.ROMAN5_ERR1)
df.add_system_transition(State.ROMAN0_ERR2, State.ROMAN12, r'[!"That is quite a while! You must been through a lot of stressful things already. How often did you feel stressed about your relationship?"]')
df.add_system_transition(State.ROMAN1_ERR2, State.ROMAN22, r'[!"It is totally normal to be stressed about relationship! Is the coronavirus causing any stress in your relationship?"]')
df.add_system_transition(State.ROMAN2_ERR2, State.ROMAN32, r'[!"I guess the coronavirus is innocent. Let me try to make use of what I learned from my psychology class. The theory of love suggests that love in composed by intimacy, passion, and commitment. Which one do you think yours is lacking?"]')
df.add_system_transition(State.ROMAN3_ERR2, State.ROMAN42, r'[!"Oh I see. Last year I felt like my girlfriend and I are losing passion because of long distance. Have you ever talked about your stress with your boyfriend or girlfriend?"]')
df.add_system_transition(State.ROMAN4_ERR2, State.ROMAN52, r'[!"Perhaps effective communications with each other about your stress can strengthen your relationship. You should do something to relieve your stress. What do you like to do during quarantine?"]')
df.add_system_transition(State.ROMAN5_ERR2, State.COVID2, r'[!"I should try that next time. Dont judge me. Sleeping is my only destress activity. Are you also taking online classes?"]')
df.add_system_transition(State.COVID02, State.COVID1, r'[!"Oh...I am guessing this stress is coming from the fact that you cannot see each other. Not being able to hang out with my friends sucks. But doing some fun activities help me relax a lot. What do you like to do during quarantine?"]')


###############################################version agreeable of love
'''LOVE AGREE'''
df.add_user_transition(State.LOVE0, State.SINGLE, r'<[!#ONT(ontno)]>',score=1.0)
df.add_user_transition(State.LOVE0, State.ROMAN, r'<[!#ONT(ontyes)]>',score=1.0)
df.set_error_successor(State.LOVE0, State.LOVE0_ERR)
df.add_system_transition(State.LOVE0_ERR, State.SINGLE0, r'[!"I feel you. Being single stresses me out because everyone else around me is in a relationship. How long have you been single?"]')
'''BREAK UP AGR'''
df.add_system_transition(State.BREAKUP_AGG, State.BREAKUP0, r'[!"Oh I am sorry. Must be so heartbreaking for you. How long had you guys been together?"]')
df.add_user_transition(State.BREAKUP0, State.BREAKUP0_short, r'/.*(1|a|one)\s\byear\b.*|.*(month|months|day|days).*((?!year|years).)*/')
df.add_user_transition(State.BREAKUP0, State.BREAKUP0_mid, r'/.*([2]|two)\s\b(year|years)\b.*/')
df.add_user_transition(State.BREAKUP0, State.BREAKUP0_long, r'/.*([3-9]|[0]|three|four|five|six|seven|eight|nine|ten|eleven|twelve)\s\b(year|years)\b.*/')
df.add_system_transition(State.BREAKUP0_short, State.BREAKUP1, r'[!"Less than a year? I think you will recover soon. My friend just broke up recently with her boyfriend and they had been dating for 7 years... Did this breakup happen because of the coronavirus? "]')
df.add_system_transition(State.BREAKUP0_mid, State.BREAKUP1, r'[!"Two years is a long period of time. You must be feeling lost and empty. Did this breakup happen because of the coronavirus?"]')
df.add_system_transition(State.BREAKUP0_long, State.BREAKUP1, r'[!"You guys broke up despite dated for this long? Oh, is it because of the coronavirus?"]')
df.add_user_transition(State.BREAKUP1, State.COVID0, r'<[!#ONT(ontyes)]>')
df.add_user_transition(State.BREAKUP1, State.BREAKUP1_0, r'<[!#ONT(ontno)]>')
df.add_system_transition(State.BREAKUP1_0, State.BREAKUP2, r'[!"I guess the coronavirus is innocent. Healthy relationships are said to be composed of intimacy, passion, and commitment. Which one do you think yours was lacking?"]')
df.add_user_transition(State.BREAKUP2, State.BREAKUP2_intimacy, r'[intimacy]')
df.add_user_transition(State.BREAKUP2, State.BREAKUP2_passion, r'[passion]')
df.add_user_transition(State.BREAKUP2, State.BREAKUP2_commitment, r'[commitment]')
df.add_system_transition(State.BREAKUP2_intimacy, State.BREAKUP3, r'[!"A relationship without intimacy is kinda similar to love at first sight, if I remember correctly. Perhaps sharing each stressful and joyful thing that happened can build the attachment to one another. Just curious, do you want to get back together?"]')
df.add_system_transition(State.BREAKUP2_passion, State.BREAKUP3, r'[!"A relationship without passion is kinda similar to a long-term marriage, if I remember correctly. Just curious, do you want to get back together?"]')
df.add_system_transition(State.BREAKUP2_commitment, State.BREAKUP3, r'[!"A relationship without commitment is kinda similar to a romantic affair, if I remember correctly. Making promises to each other is important to create a sense of belonging. Just curious, do you want to get back together?"]')
df.add_user_transition(State.BREAKUP3, State.BREAKUP3_yes, r'<[!#ONT(ontyes)]>')
df.add_user_transition(State.BREAKUP3, State.BREAKUP3_no, r'<[!#ONT(ontno)]>')
df.add_system_transition(State.BREAKUP3_yes, State.BREAKUP4, r'[!"Best of luck with that! However, dont forget to love yourself. During quarantine, I really enjoy trying new food recipes. What do you like to do during quarantine?"]')
df.add_system_transition(State.BREAKUP3_no, State.BREAKUP4, r'[!"Time to focus on self development then! Dont forget to love yourself more. During quarantine, I really enjoy trying new recipes. What do you like to do during quarantine?"]')
df.add_user_transition(State.BREAKUP4, State.COVID1_game, r'<[!#ONT(ontgames)]>')
df.add_user_transition(State.BREAKUP4, State.COVID1_food, r'<[!#ONT(ontfood)]>')
df.add_user_transition(State.BREAKUP4, State.COVID1_video, r'<[!#ONT(ontreadwatch)]>')
df.add_user_transition(State.BREAKUP4, State.COVID1_socialApp, r'<[!#ONT(ontsocialApp)]>')
df.add_user_transition(State.BREAKUP4, State.COVID1_class, r'<[!#ONT(ontclass)]>')
df.add_user_transition(State.BREAKUP4, State.COVID1_music, r'<[!#ONT(ontmusic)]>')
df.set_error_successor(State.COVID0, State.COVID0_ERR)
df.add_system_transition(State.COVID0_ERR, State.COVID1, r'[!"Oh...I am guessing this stress is coming from the fact that you cannot see each other. It is a lot to handle when away from everyone, you are not alone. Doing some fun activities might help you relax! What do you like to do during quarantine?"]')
df.set_error_successor(State.BREAKUP0, State.BREAKUP0_ERR)
df.set_error_successor(State.BREAKUP1, State.BREAKUP1_ERR)
df.set_error_successor(State.BREAKUP2, State.BREAKUP2_ERR)
df.set_error_successor(State.BREAKUP3, State.BREAKUP3_ERR)
df.set_error_successor(State.BREAKUP4, State.BREAKUP4_ERR)
df.add_system_transition(State.BREAKUP0_ERR, State.BREAKUP1, r'[!"I see...you must be feeling lost and empty. Did this breakup happen because of the coronavirus?"]')
df.add_system_transition(State.BREAKUP1_ERR, State.BREAKUP2, r'[!"I guess the coronavirus is not the one to blame. Let me try to make use of what I learned from my psychology class. The theory of love suggests that love in composed by intimacy, passion, and commitment. Which one do you think yours was lacking?"]')
df.add_system_transition(State.BREAKUP2_ERR, State.BREAKUP3, r'[!"Oh I see. Last year my girlfriend broke up with me because of the her insecurity caused by long distance and I learned the importance of commitment. Just curious, do you want to get back together?"]')
df.add_system_transition(State.BREAKUP3_ERR, State.BREAKUP4, r'[!"I think you are ready to move on! Time to focus on self development, and dont forget to love yourself more. During quarantine, I really enjoy trying new recipes. What do you like to do during quarantine?"]')
df.add_system_transition(State.BREAKUP4_ERR, State.COVID2, r'[!"T I want to try that next time. Dont judge me but sleeping is my only destress activity. Are you also taking online classes?"]')
'''SINGLE AGREE'''
df.add_system_transition(State.SINGLE, State.SINGLE0, r'[!"Being single is not a bad thing. You get to do whatever you want without having to care about how your boyfriend or girlfriend might feel. How long have you been single?"]')
df.add_user_transition(State.SINGLE0, State.SINGLE0_short, r'/.*(1|a|one)\s\byear\b.*|.*(month|months|day|days).*((?!year|years).)*/')
df.add_user_transition(State.SINGLE0, State.SINGLE0_mid, r'/.*([2]|two)\s\b(year|years)\b.*/')
df.add_user_transition(State.SINGLE0, State.SINGLE0_long, r'/.*([3-9]|[0]|three|four|five|six|seven|eight|nine|ten|eleven|twelve)\s\b(year|years)\b.*/')
df.add_system_transition(State.SINGLE0_short, State.SINGLE1, r'[!"Oh recovering from your previous relationship? How often are you feeling stressed about being single?"]')
df.add_system_transition(State.SINGLE0_mid, State.SINGLE1, r'[!"Yeah, its time to get into a relationship right? How often are you feeling stressed about being single?"]')
df.add_system_transition(State.SINGLE0_long, State.SINGLE1, r'[!"Its okay you are not alone, I have been single for a while too. How often are you feeling stressed about being single?"]')
df.add_user_transition(State.SINGLE1, State.SINGLE1_often, r'<{[!#ONT(ontoften)],/(?:\s|^)(((once|twice|thrice|three\stimes|four\stimes|five\stimes|1\stime|2\stimes|3\stimes|4\stimes|5\stimes)\s(every|per|a)(\sone|\s1|\stwo|\s2|\sthree|\s3|\sfour|\s4|\sfive|\s5|\sother|\ssix|\s6|\s7|\sseven|\seight|\s8|\s9|\snine|\sten|\s10)?\s(second+s?|sec+s?|min+s?|minute+s?|hour+s?|hr+s?|day+s?))|((once|twice|thrice|three\stimes|four\stimes|five\stimes|1\stime|2\stimes|3\stimes|4\stimes|5\stimes)\s(every|per|a)(\sone|\s1|\stwo|\s2|\sthree|\s3|\sother)?\s(week+s?))|((three\stimes|thrice|four\stimes|five\stimes|six\stimes|seven\stimes|3\stimes|4\stimes|5\stimes|6\stimes|7\stimes)\s(every|per|a)(\sone|\s1|\stwo|\s2|\sthree|\s3|\sother)?\s(month+s?))|((twice|two\stimes|2\stimes)\s(every|per|a)(\sone)?\s(month)))(?:\s|,|\.|$)/}>')
df.add_user_transition(State.SINGLE1, State.SINGLE1_sometimes, r'<{[!#ONT(ontsometimes)],/(?:\s|^)(((once|one\stime|two\stimes|twice|three\stimes|thrice|four\stimes|five\stimes|1\stime|2\stimes|3\stimes|4\stimes|5\stimes)\s(every|per|a)(\sone|\s1|\stwo|\s2|\sthree|\s3|\sfour|\s4|\sfive|\s5|\ssix|\s6|\sten|\s10|\sother)?\s(semester+s?|term+s?|quarter+s?|year+s?|decade+s?))|((once|1\stime|one\stime)\s(every|per|a)(\sone|\s1|\stwo|\s2|\sthree|\s3|\sfour|\s4|\sfive|\s5|\ssix|\s6|\sother)?\s(month+s?))|((once|1\stime|2\stimes|twice|thrice|3\stimes|three\stimes|one\stime|four\stimes|4\stimes)\s(every|a|per)(\sthree|\s3|\sfour|\s4|\sfive|\s5|\ssix|\s6|\sseven|\s7|\seight|\s8|\sten|\s10)\s(month+s?)))(?:\s|,|\.|$)/}>')
df.add_user_transition(State.SINGLE1, State.SINGLE1_never, r'<{[!#ONT(ontnever)]}>')
df.add_system_transition(State.SINGLE1_often, State.SINGLE2, r'[!"Feeling stressed about it probably means you care about yourself a lot, but stressing too much is not good for your health. Do you think you have a high standard?"#high_n""]')
df.add_system_transition(State.SINGLE1_sometimes, State.SINGLE2, r'[!"A little of stress is actually helpful for self development. Do you think you have a high standard?"#mid_n""]')
df.add_system_transition(State.SINGLE1_never, State.SINGLE2, r'[!"Interesting, I guess something unexpected happened in your life. Do you think you have a high standard?"#low_n""]')
df.add_user_transition(State.SINGLE2, State.SINGLE2_yes, r'<[!#ONT(ontyes)]>')
df.add_user_transition(State.SINGLE2, State.SINGLE2_no, r'<[!#ONT(ontno)]>')
df.add_system_transition(State.SINGLE2_yes, State.SINGLE3, r'[!"Checkmate! It is not a bad thing to have a high standard, but it reduces probability that the one that fits your standard will also like you. The struggle is real! What do you do to relax during quarantine?"]')
df.add_system_transition(State.SINGLE2_no, State.SINGLE3, r'[!"I guess you just need to wait for love come to you naturally. I was once very desperate for a relationship but ended up getting none. And after I gave up, it came to me unexpectedly. Strange, right? You should focus more on yourself, what do you like to do during quarantine?"]')
df.add_user_transition(State.SINGLE3, State.COVID1_game, r'<[!#ONT(ontgames)]>')
df.add_user_transition(State.SINGLE3, State.COVID1_food, r'<[!#ONT(ontfood)]>')
df.add_user_transition(State.SINGLE3, State.COVID1_video, r'<[!#ONT(ontreadwatch)]>')
df.add_user_transition(State.SINGLE3, State.COVID1_socialApp, r'<[!#ONT(ontsocialApp)]>')
df.add_user_transition(State.SINGLE3, State.COVID1_class, r'<[!#ONT(ontclass)]>')
df.add_user_transition(State.SINGLE3, State.COVID1_music, r'<[!#ONT(ontmusic)]>')
df.set_error_successor(State.SINGLE0, State.SINGLE0_ERR)
df.set_error_successor(State.SINGLE1, State.SINGLE1_ERR)
df.set_error_successor(State.SINGLE2, State.SINGLE2_ERR)
df.set_error_successor(State.SINGLE3, State.SINGLE3_ERR)
df.add_system_transition(State.SINGLE0_ERR, State.SINGLE1, r'[!"Its okay you are not alone, I have been single for a while too. How often did you feel stressed about being single?"]')
df.add_system_transition(State.SINGLE1_ERR, State.SINGLE2, r'[!"Feeling stressed about it probably means you care about yourself a lot, but stressing too much is not good for your health. Do you think you have a high standard?"]')
df.add_system_transition(State.SINGLE2_ERR, State.SINGLE3, r'[!"I was once desperate for a relationship. After I gave up trying, it came to me unexpectedly. Strange right? What do you do to relax during quarantine?"]')
df.add_system_transition(State.SINGLE3_ERR, State.COVID2, r'[!"Interesting! I want to try that next time. Dont judge me. Eating is my only destress activity. Are you also taking online classes?"]')
'''RELATIONSHIP AGREE'''
df.add_system_transition(State.ROMAN, State.ROMAN0, r'[!"Oh nice! How long have you guys been together?"]')
df.add_user_transition(State.ROMAN0, State.ROMAN0_short, r'/.*(1|a|one)\s\byear\b.*|.*(month|months|day|days).*((?!year|years).)*/')
df.add_user_transition(State.ROMAN0, State.ROMAN0_mid, r'/.*([2-3]|two|three)\s\b(year|years)\b.*/')
df.add_user_transition(State.ROMAN0, State.ROMAN0_long, r'/.*([4-9]|[0]|four|five|six|seven|eight|nine|ten|eleven|twelve)\s\b(year|years)\b.*/')
df.add_system_transition(State.ROMAN0_short, State.ROMAN1, r'[!"You must be still in your honeymoon phase. How often did you feel stressed about your relationship?"]')
df.add_system_transition(State.ROMAN0_mid, State.ROMAN1, r'[!"That is quite a while! I am assuming you guys are in a more certain and stable phase. How often did you feel stressed about your relationship?"]')
df.add_system_transition(State.ROMAN0_long, State.ROMAN1, r'[!"Oh wow for real? I am surprised you guys can pull it off. How often did you feel stressed about your relationship?"]')
df.add_user_transition(State.ROMAN1, State.ROMAN1_often,
                       r'<{[!#ONT(ontoften)],/(?:\s|^)(((once|twice|thrice|three\stimes|four\stimes|five\stimes|1\stime|2\stimes|3\stimes|4\stimes|5\stimes)\s(every|per|a)(\sone|\s1|\stwo|\s2|\sthree|\s3|\sfour|\s4|\sfive|\s5|\sother|\ssix|\s6|\s7|\sseven|\seight|\s8|\s9|\snine|\sten|\s10)?\s(second+s?|sec+s?|min+s?|minute+s?|hour+s?|hr+s?|day+s?))|((once|twice|thrice|three\stimes|four\stimes|five\stimes|1\stime|2\stimes|3\stimes|4\stimes|5\stimes)\s(every|per|a)(\sone|\s1|\stwo|\s2|\sthree|\s3|\sother)?\s(week+s?))|((three\stimes|thrice|four\stimes|five\stimes|six\stimes|seven\stimes|3\stimes|4\stimes|5\stimes|6\stimes|7\stimes)\s(every|per|a)(\sone|\s1|\stwo|\s2|\sthree|\s3|\sother)?\s(month+s?))|((twice|two\stimes|2\stimes)\s(every|per|a)(\sone)?\s(month)))(?:\s|,|\.|$)/}>')
df.add_user_transition(State.ROMAN1, State.ROMAN1_sometimes,
                       r'<{[!#ONT(ontsometimes)],/(?:\s|^)(((once|one\stime|two\stimes|twice|three\stimes|thrice|four\stimes|five\stimes|1\stime|2\stimes|3\stimes|4\stimes|5\stimes)\s(every|per|a)(\sone|\s1|\stwo|\s2|\sthree|\s3|\sfour|\s4|\sfive|\s5|\ssix|\s6|\sten|\s10|\sother)?\s(semester+s?|term+s?|quarter+s?|year+s?|decade+s?))|((once|1\stime|one\stime)\s(every|per|a)(\sone|\s1|\stwo|\s2|\sthree|\s3|\sfour|\s4|\sfive|\s5|\ssix|\s6|\sother)?\s(month+s?))|((once|1\stime|2\stimes|twice|thrice|3\stimes|three\stimes|one\stime|four\stimes|4\stimes)\s(every|a|per)(\sthree|\s3|\sfour|\s4|\sfive|\s5|\ssix|\s6|\sseven|\s7|\seight|\s8|\sten|\s10)\s(month+s?)))(?:\s|,|\.|$)/}>')
df.add_user_transition(State.ROMAN1, State.COVID0, r'<{[!#ONT(ontnever)]}>')
df.add_system_transition(State.ROMAN1_often, State.ROMAN2, r'[!"Yeah...sometimes relationship can be demanding as you need to make many compromises along the way. But constant stress is not a good sign... Is the coronavirus causing any stress in your relationship?"#high_n""]')
df.add_system_transition(State.ROMAN1_sometimes, State.ROMAN2, r'[!"It is totally normal to be stressed about relationship sometimes. Is the coronavirus causing any stress in your relationship?"#mid_n""]')
df.add_system_transition(State.ROMAN1_never, State.ROMAN2, r'[!"Let me guess, is the stress in your relationship coming from the coronavirus?"#low_n""]')
df.add_user_transition(State.ROMAN2, State.COVID0, r'<[!#ONT(ontyes)]>')
df.add_user_transition(State.ROMAN2, State.ROMAN2_0, r'<[!#ONT(ontno)]>')
df.add_system_transition(State.ROMAN2_0, State.ROMAN3, r'[!"I guess the coronavirus is innocent. Let me try to make use of what I learned from my psychology class. The theory of love suggests that love in composed by intimacy, passion, and commitment. Which one do you think yours is lacking?"]')
df.add_user_transition(State.ROMAN3, State.ROMAN3_intimacy, r'[intimacy]')
df.add_user_transition(State.ROMAN3, State.ROMAN3_passion, r'[passion]')
df.add_user_transition(State.ROMAN3, State.ROMAN3_commitment, r'[commitment]')
df.add_system_transition(State.ROMAN3_intimacy, State.ROMAN4, r'[!"A relationship without intimacy is kinda similar to love at first sight, if I remember correctly. Perhaps sharing each stressful and joyful thing that happened can build the attachment to one another. Have you ever talked about your stress with your boyfriend or girlfriend?"]')
df.add_system_transition(State.ROMAN3_passion, State.ROMAN4, r'[!"A relationship without passion is kinda similar to a long-term marriage, if I remember correctly. Have you ever talked about your stress with your boyfriend or girlfriend?"]')
df.add_system_transition(State.ROMAN3_commitment, State.ROMAN4, r'[!"A relationship without commitment is kinda similar to a romantic affair, if I remember correctly. Making promises to each other is important to create a sense of belonging. Have you ever talked about your stress with your boyfriend or girlfriend?"]')
df.add_user_transition(State.ROMAN4, State.ROMAN4_yes, r'<[!#ONT(ontyes)]>')
df.add_user_transition(State.ROMAN4, State.ROMAN4_no, r'<[!#ONT(ontno)]>')
df.add_system_transition(State.ROMAN4_yes, State.ROMAN5, r'[!"Oh really? And it did not work out? Then I think you should do something relaxing to relieve your stress. What do you like to do during quarantine?"#high_e""]')
df.add_system_transition(State.ROMAN4_no, State.ROMAN5, r'[!"Maybe effective communications with each other about your stress can strengthen your relationship. You should do something to relieve your stress. What do you like to do during quarantine?"]')
df.add_user_transition(State.ROMAN5, State.COVID1_game, r'<[!#ONT(ontgames)]>')
df.add_user_transition(State.ROMAN5, State.COVID1_food, r'<[!#ONT(ontfood)]>')
df.add_user_transition(State.ROMAN5, State.COVID1_video, r'<[!#ONT(ontreadwatch)]>')
df.add_user_transition(State.ROMAN5, State.COVID1_socialApp, r'<[!#ONT(ontsocialApp)]>')
df.add_user_transition(State.ROMAN5, State.COVID1_class, r'<[!#ONT(ontclass)]>')
df.add_user_transition(State.ROMAN5, State.COVID1_music, r'<[!#ONT(ontmusic)]>')
df.set_error_successor(State.ROMAN0, State.ROMAN0_ERR)
df.set_error_successor(State.ROMAN1, State.ROMAN1_ERR)
df.set_error_successor(State.ROMAN2, State.ROMAN2_ERR)
df.set_error_successor(State.ROMAN3, State.ROMAN3_ERR)
df.set_error_successor(State.ROMAN4, State.ROMAN4_ERR)
df.set_error_successor(State.ROMAN5, State.ROMAN5_ERR)
df.add_system_transition(State.ROMAN0_ERR, State.ROMAN1, r'[!"Sounds like you guys are in a more certain and stable phase. How often did you feel stressed about your relationship?"]')
df.add_system_transition(State.ROMAN1_ERR, State.ROMAN2, r'[!"It is totally normal to be stressed about relationship sometimes. Is the coronavirus causing any stress in your relationship?"]')
df.add_system_transition(State.ROMAN2_ERR, State.ROMAN3, r'[!"I guess the coronavirus is innocent. Let me try to make use of what I learned from my psychology class. The theory of love suggests that love in composed by intimacy, passion, and commitment. Which one do you think yours is lacking?"]')
df.add_system_transition(State.ROMAN3_ERR, State.ROMAN4, r'[!"Oh I see. Last year I felt like my girlfriend and I are losing passion because of long distance. Have you ever talked about your stress with your boyfriend or girlfriend?"]')
df.add_system_transition(State.ROMAN4_ERR, State.ROMAN5, r'[!"Maybe opening up to each other about things that your stress could help strengthen your relationship. You should do something to relieve your stress. What do you like to do during quarantine?"]')
df.add_system_transition(State.ROMAN5_ERR, State.COVID2, r'[!"That sounds super interesting! I should try that next time when I have less homework. I guess eating is my only destress activity... Are you also taking online classes?"]')
df.add_system_transition(State.COVID0, State.COVID1, r'[!"The quarantine situation does introduce a lot more unpredictability to our life. What do you do to relax during quarantine?"]')

###################################version optimistic of love
'''LOVE OPT'''
df.add_user_transition(State.LOVE0, State.SINGLEo1, r'<[!#ONT(ontno)]>',score=1.0)
df.add_user_transition(State.LOVE0, State.ROMANo1, r'<[!#ONT(ontyes)]>',score=1.0)
df.set_error_successor(State.LOVE0, State.LOVE0_ERR1)
df.add_system_transition(State.LOVE0_ERR1, State.SINGLE01, r'[!"Being single is wonderful! You get to do whatever you want without having to think about how your partner might feel. How long have you been single?"]')
'''SINGLE OPT'''
df.add_system_transition(State.SINGLEo1, State.SINGLE01, r'[!"Being single is wonderful! You can literally do whatever you want without having to care about how your boyfriend or girlfriend might feel. How long have you been single?"]')
df.add_user_transition(State.SINGLE01, State.SINGLE0_short1, r'/.*(1|a|one)\s\byear\b.*|.*(month|months|day|days).*((?!year|years).)*/')
df.add_user_transition(State.SINGLE01, State.SINGLE0_mid1, r'/.*([2]|two)\s\b(year|years)\b.*/')
df.add_user_transition(State.SINGLE01, State.SINGLE0_long1, r'/.*([3-9]|[0]|three|four|five|six|seven|eight|nine|ten|eleven|twelve)\s\b(year|years)\b.*/')
df.add_system_transition(State.SINGLE0_short1, State.SINGLE11, r'[!"You are probably not so used to being single, are you? How often are you feeling stressed about being single?"]')
df.add_system_transition(State.SINGLE0_mid1, State.SINGLE11, r'[!"It is nice to get to have so much time to focus on self development sometimes! How often are you feeling stressed about being single?"]')
df.add_system_transition(State.SINGLE0_long1, State.SINGLE11, r'[!"Hey its okay! Having a girlfriend or boyfriend can be more stressful than being single. How often are you feeling stressed about being single?"]')
df.add_user_transition(State.SINGLE11, State.SINGLE1_often1, r'<{[!#ONT(ontoften)],/(?:\s|^)(((once|twice|thrice|three\stimes|four\stimes|five\stimes|1\stime|2\stimes|3\stimes|4\stimes|5\stimes)\s(every|per|a)(\sone|\s1|\stwo|\s2|\sthree|\s3|\sfour|\s4|\sfive|\s5|\sother|\ssix|\s6|\s7|\sseven|\seight|\s8|\s9|\snine|\sten|\s10)?\s(second+s?|sec+s?|min+s?|minute+s?|hour+s?|hr+s?|day+s?))|((once|twice|thrice|three\stimes|four\stimes|five\stimes|1\stime|2\stimes|3\stimes|4\stimes|5\stimes)\s(every|per|a)(\sone|\s1|\stwo|\s2|\sthree|\s3|\sother)?\s(week+s?))|((three\stimes|thrice|four\stimes|five\stimes|six\stimes|seven\stimes|3\stimes|4\stimes|5\stimes|6\stimes|7\stimes)\s(every|per|a)(\sone|\s1|\stwo|\s2|\sthree|\s3|\sother)?\s(month+s?))|((twice|two\stimes|2\stimes)\s(every|per|a)(\sone)?\s(month)))(?:\s|,|\.|$)/}>')
df.add_user_transition(State.SINGLE11, State.SINGLE1_sometimes1, r'<{[!#ONT(ontsometimes)],/(?:\s|^)(((once|one\stime|two\stimes|twice|three\stimes|thrice|four\stimes|five\stimes|1\stime|2\stimes|3\stimes|4\stimes|5\stimes)\s(every|per|a)(\sone|\s1|\stwo|\s2|\sthree|\s3|\sfour|\s4|\sfive|\s5|\ssix|\s6|\sten|\s10|\sother)?\s(semester+s?|term+s?|quarter+s?|year+s?|decade+s?))|((once|1\stime|one\stime)\s(every|per|a)(\sone|\s1|\stwo|\s2|\sthree|\s3|\sfour|\s4|\sfive|\s5|\ssix|\s6|\sother)?\s(month+s?))|((once|1\stime|2\stimes|twice|thrice|3\stimes|three\stimes|one\stime|four\stimes|4\stimes)\s(every|a|per)(\sthree|\s3|\sfour|\s4|\sfive|\s5|\ssix|\s6|\sseven|\s7|\seight|\s8|\sten|\s10)\s(month+s?)))(?:\s|,|\.|$)/}>')
df.add_user_transition(State.SINGLE11, State.SINGLE1_never1, r'<{[!#ONT(ontnever)]}>')
df.add_system_transition(State.SINGLE1_often1, State.SINGLE21, r'[!"Relax man its not a big deal. Do you think you have a high standard?"#high_n""]')
df.add_system_transition(State.SINGLE1_sometimes1, State.SINGLE21, r'[!"A little of stress is perfectly fine! Do you think you have a high standard?"#mid_n""]')
df.add_system_transition(State.SINGLE1_never1, State.SINGLE21, r'[!"Interesting, I guess something unexpected happened in your life. Do you think you have a high standard?"#low_n""]')
df.add_user_transition(State.SINGLE21, State.SINGLE2_yes1, r'<[!#ONT(ontyes)]>')
df.add_user_transition(State.SINGLE21, State.SINGLE2_no1, r'<[!#ONT(ontno)]>')
df.add_system_transition(State.SINGLE2_yes1, State.SINGLE31, r'[!"The does make the search for your soulmate a lot harder, but also eliminates the likelihood of you wasting time dating the wrong person! What do you like to do during quarantine?"]')
df.add_system_transition(State.SINGLE2_no1, State.SINGLE31, r'[!"Then you should focus on yourself more! A person with confidence is so attractive. What do you like to do during quarantine?"]')
df.add_user_transition(State.SINGLE31, State.COVID1_game, r'<[!#ONT(ontgames)]>')
df.add_user_transition(State.SINGLE31, State.COVID1_food, r'<[!#ONT(ontfood)]>')
df.add_user_transition(State.SINGLE31, State.COVID1_video, r'<[!#ONT(ontreadwatch)]>')
df.add_user_transition(State.SINGLE31, State.COVID1_socialApp, r'<[!#ONT(ontsocialApp)]>')
df.add_user_transition(State.SINGLE31, State.COVID1_class, r'<[!#ONT(ontclass)]>')
df.add_user_transition(State.SINGLE31, State.COVID1_music, r'<[!#ONT(ontmusic)]>')
df.set_error_successor(State.SINGLE01, State.SINGLE0_ERR1)
df.set_error_successor(State.SINGLE11, State.SINGLE1_ERR1)
df.set_error_successor(State.SINGLE21, State.SINGLE2_ERR1)
df.set_error_successor(State.SINGLE31, State.SINGLE3_ERR1)
df.add_system_transition(State.SINGLE0_ERR1, State.SINGLE11, r'[!"Its okay I am single too! Maybe we should date! How often are you feeling stressed about being single?"]')
df.add_system_transition(State.SINGLE1_ERR1, State.SINGLE21, r'[!"Hey dont worry too much! It is normal to be stressed sometimes. Do you think you have a high standard?"]')
df.add_system_transition(State.SINGLE2_ERR1, State.SINGLE31, r'[!"In this case, you should focus more on yourself! What do you like to do during quarantine?"]')
df.add_system_transition(State.SINGLE3_ERR1, State.COVID2, r'[!"I should try that next time when I have less homework. Dont judge me but eating is my only destress activity. Are you also taking online classes?"]')
'''BREAK UP OPT'''
df.add_system_transition(State.BREAKUP_OPT, State.BREAKUP01, r'[!"You will find someone better! How long had you guys been together?"]')
df.add_user_transition(State.BREAKUP01, State.BREAKUP0_short1, r'/.*(1|a|one)\s\byear\b.*|.*(month|months|day|days).*((?!year|years).)*/')
df.add_user_transition(State.BREAKUP01, State.BREAKUP0_mid1, r'/.*([2]|two)\s\b(year|years)\b.*/')
df.add_user_transition(State.BREAKUP01, State.BREAKUP0_long1, r'/.*([3-9]|[0]|three|four|five|six|seven|eight|nine|ten|eleven|twelve)\s\b(year|years)\b.*/')
df.add_system_transition(State.BREAKUP0_short1, State.BREAKUP11, r'[!"Less than a year? You can find another one pretty soon! Did this breakup happen because of the coronavirus? "]')
df.add_system_transition(State.BREAKUP0_mid1, State.BREAKUP11, r'[!"Two years is a long period of time. but how long you had been together is not important fs you are not suitable for each other. Did this breakup happen because of the coronavirus?"]')
df.add_system_transition(State.BREAKUP0_long1, State.BREAKUP11, r'[!"Sometimes you just gotta end a story and start another one! Did this breakup happen because of the coronavirus?"]')
df.add_user_transition(State.BREAKUP11, State.COVID01, r'<[!#ONT(ontyes)]>')
df.add_user_transition(State.BREAKUP11, State.BREAKUP1_01, r'<[!#ONT(ontno)]>')
df.add_system_transition(State.BREAKUP1_01, State.BREAKUP21, r'[!"So the virus is innocent. A healthy relationship is said to be composed of intimacy, passion, and commitment. Which one do you think yours was lacking?"]')
df.add_user_transition(State.BREAKUP21, State.BREAKUP2_intimacy1, r'[intimacy]')
df.add_user_transition(State.BREAKUP21, State.BREAKUP2_passion1, r'[passion]')
df.add_user_transition(State.BREAKUP21, State.BREAKUP2_commitment1, r'[commitment]')
df.add_system_transition(State.BREAKUP2_intimacy1, State.BREAKUP31, r'[!"A relationship without intimacy is kinda similar to love at first sight. At least you know what to do in your next relationship! Just curious, do you want to get back together?"]')
df.add_system_transition(State.BREAKUP2_passion1, State.BREAKUP31, r'[!"A relationship without passion is kinda similar to a long-term marriage. At least you know what to do in your next relationship! Just curious, do you want to get back together?"]')
df.add_system_transition(State.BREAKUP2_commitment1, State.BREAKUP31, r'[!"A relationship without commitment is kinda similar to a romantic affair. At least you know what to do in your next relationship! Just curious, do you want to get back together?"]')
df.add_user_transition(State.BREAKUP31, State.BREAKUP3_yes1, r'<[!#ONT(ontyes)]>')
df.add_user_transition(State.BREAKUP31, State.BREAKUP3_no1, r'<[!#ONT(ontno)]>')
df.add_system_transition(State.BREAKUP3_yes1, State.BREAKUP41, r'[!"Best of luck with that! However, dont forget to love yourself. During quarantine, I really enjoy trying new recipes. What do you like to do during quarantine?"]')
df.add_system_transition(State.BREAKUP3_no1, State.BREAKUP41, r'[!"I think you are ready to move on! Time to focus on self development, and dont forget to love yourself more. During quarantine, I really enjoy trying new recipes. What do you like to do during quarantine?"]')
df.add_user_transition(State.BREAKUP41, State.COVID1_game, r'<[!#ONT(ontgames)]>')
df.add_user_transition(State.BREAKUP41, State.COVID1_food, r'<[!#ONT(ontfood)]>')
df.add_user_transition(State.BREAKUP41, State.COVID1_video, r'<[!#ONT(ontreadwatch)]>')
df.add_user_transition(State.BREAKUP41, State.COVID1_socialApp, r'<[!#ONT(ontsocialApp)]>')
df.add_user_transition(State.BREAKUP41, State.COVID1_class, r'<[!#ONT(ontclass)]>')
df.add_user_transition(State.BREAKUP41, State.COVID1_music, r'<[!#ONT(ontmusic)]>')
df.set_error_successor(State.COVID01,State.COVID0_ERR1)
df.add_system_transition(State.COVID0_ERR1, State.COVID1, r'[!"If a virus can destroy your relationship, then you probably do not want this relationship. Doing some fun activities might help you relax! What do you like to do during quarantine?"]')
df.set_error_successor(State.BREAKUP01, State.BREAKUP0_ERR1)
df.set_error_successor(State.BREAKUP11, State.BREAKUP1_ERR1)
df.set_error_successor(State.BREAKUP21, State.BREAKUP2_ERR1)
df.set_error_successor(State.BREAKUP31, State.BREAKUP3_ERR1)
df.set_error_successor(State.BREAKUP41, State.BREAKUP4_ERR1)
df.add_system_transition(State.BREAKUP0_ERR1, State.BREAKUP11, r'[!"That is slightly longer than my most recent relationship. Did this breakup happen because of the coronavirus?"]')
df.add_system_transition(State.BREAKUP1_ERR1, State.BREAKUP21, r'[!"I guess the coronavirus is not the one to blame. Healthy relationships are said to be composed of intimacy, passion, and commitment. Which one do you think yours was lacking?"]')
df.add_system_transition(State.BREAKUP2_ERR1, State.BREAKUP31, r'[!"Last year my girlfriend broke up with me because of the her insecurity caused by long distance and I learned the importance of commitment. Just curious, do you want to get back together?"]')
df.add_system_transition(State.BREAKUP3_ERR1, State.BREAKUP41, r'[!"Time to focus on self development! Dont forget to love yourself more. During quarantine, I really enjoy trying new recipes. What do you like to do during quarantine?"]')
df.add_system_transition(State.BREAKUP4_ERR1, State.COVID2, r'[!"Sounds fun! Dont judge me. Eating is my only destress activity... Are you also taking online classes?"]')
'''RELATIONSHIP OPT'''
df.add_system_transition(State.ROMANo1, State.ROMAN01, r'[!"That is so nice! How long have you guys been together?"]')
df.add_user_transition(State.ROMAN01, State.ROMAN0_short1, r'/.*(1|a|one)\s\byear\b.*|.*(month|months|day|days|week).*((?!year|years).)*/')
df.add_user_transition(State.ROMAN01, State.ROMAN0_mid1, r'/.*([2-3]|two|three)\s\b(year|years)\b.*/')
df.add_user_transition(State.ROMAN01, State.ROMAN0_long1, r'/.*([4-9]|[0]|four|five|six|seven|eight|nine|ten|eleven|twelve)\s\b(year|years)\b.*/')
df.add_system_transition(State.ROMAN0_short1, State.ROMAN11, r'[!"That is so cute. How often did you feel stressed about your relationship?"]')
df.add_system_transition(State.ROMAN0_mid1, State.ROMAN11, r'[!"That is quite a while! Feeling stressed is perfectly fine. How often did you feel stressed about your relationship?"]')
df.add_system_transition(State.ROMAN0_long1, State.ROMAN11, r'[!"Oh wow for real? I am surprised you guys can pull it off. How often did you feel stressed about your relationship?"]')
df.add_user_transition(State.ROMAN11, State.ROMAN1_often1,
                       r'<{[!#ONT(ontoften)],/(?:\s|^)(((once|twice|thrice|three\stimes|four\stimes|five\stimes|1\stime|2\stimes|3\stimes|4\stimes|5\stimes)\s(every|per|a)(\sone|\s1|\stwo|\s2|\sthree|\s3|\sfour|\s4|\sfive|\s5|\sother|\ssix|\s6|\s7|\sseven|\seight|\s8|\s9|\snine|\sten|\s10)?\s(second+s?|sec+s?|min+s?|minute+s?|hour+s?|hr+s?|day+s?))|((once|twice|thrice|three\stimes|four\stimes|five\stimes|1\stime|2\stimes|3\stimes|4\stimes|5\stimes)\s(every|per|a)(\sone|\s1|\stwo|\s2|\sthree|\s3|\sother)?\s(week+s?))|((three\stimes|thrice|four\stimes|five\stimes|six\stimes|seven\stimes|3\stimes|4\stimes|5\stimes|6\stimes|7\stimes)\s(every|per|a)(\sone|\s1|\stwo|\s2|\sthree|\s3|\sother)?\s(month+s?))|((twice|two\stimes|2\stimes)\s(every|per|a)(\sone)?\s(month)))(?:\s|,|\.|$)/}>')
df.add_user_transition(State.ROMAN11, State.ROMAN1_sometimes1,
                       r'<{[!#ONT(ontsometimes)],/(?:\s|^)(((once|one\stime|two\stimes|twice|three\stimes|thrice|four\stimes|five\stimes|1\stime|2\stimes|3\stimes|4\stimes|5\stimes)\s(every|per|a)(\sone|\s1|\stwo|\s2|\sthree|\s3|\sfour|\s4|\sfive|\s5|\ssix|\s6|\sten|\s10|\sother)?\s(semester+s?|term+s?|quarter+s?|year+s?|decade+s?))|((once|1\stime|one\stime)\s(every|per|a)(\sone|\s1|\stwo|\s2|\sthree|\s3|\sfour|\s4|\sfive|\s5|\ssix|\s6|\sother)?\s(month+s?))|((once|1\stime|2\stimes|twice|thrice|3\stimes|three\stimes|one\stime|four\stimes|4\stimes)\s(every|a|per)(\sthree|\s3|\sfour|\s4|\sfive|\s5|\ssix|\s6|\sseven|\s7|\seight|\s8|\sten|\s10)\s(month+s?)))(?:\s|,|\.|$)/}>')
df.add_user_transition(State.ROMAN11, State.COVID01, r'<{[!#ONT(ontnever)]}>')
df.add_system_transition(State.ROMAN1_often1, State.ROMAN21, r'[!"I bet you relaitonship is stressful but staying healthy and strong. Is the coronavirus causing any stress in your relationship?"#high_n""]')
df.add_system_transition(State.ROMAN1_sometimes1, State.ROMAN21, r'[!"I sometimes feel stressed about relationship too! Is the coronavirus causing any stress in your relationship?"#mid_n""]')
df.add_user_transition(State.ROMAN21, State.COVID01, r'<[!#ONT(ontyes)]>')
df.add_user_transition(State.ROMAN21, State.ROMAN2_01, r'<[!#ONT(ontno)]>')
df.add_system_transition(State.ROMAN2_01, State.ROMAN31, r'[!"I guess the coronavirus is innocent. Let me try to make use of what I learned from my psychology class. The theory of love suggests that love in composed by intimacy, passion, and commitment. Which one do you think yours is lacking?"]')
df.add_user_transition(State.ROMAN31, State.ROMAN3_intimacy1, r'[intimacy]')
df.add_user_transition(State.ROMAN31, State.ROMAN3_passion1, r'[passion]')
df.add_user_transition(State.ROMAN31, State.ROMAN3_commitment1, r'[commitment]')
df.add_system_transition(State.ROMAN3_intimacy1, State.ROMAN41, r'[!"A relationship without intimacy is going to be hard. Perhaps sharing more stressful or joyful moments with each other can make up for that! Have you ever talked about your stress with your boyfriend or girlfriend?"]')
df.add_system_transition(State.ROMAN3_passion1, State.ROMAN41, r'[!"A relationship without passion is kinda similar to a long-term marriage. Have you ever talked about your stress with your boyfriend or girlfriend?"]')
df.add_system_transition(State.ROMAN3_commitment1, State.ROMAN41, r'[!"A relationship without commitment is kinda similar to a romantic affair. You should make promises to each other! Have you ever talked about your stress with your boyfriend or girlfriend?"]')
df.add_user_transition(State.ROMAN41, State.ROMAN4_yes1, r'<[!#ONT(ontyes)]>')
df.add_user_transition(State.ROMAN41, State.ROMAN4_no1, r'<[!#ONT(ontno)]>')
df.add_system_transition(State.ROMAN4_yes1, State.ROMAN51, r'[!"Oh really? And it did not work out? Then I think you should do something relaxing to relieve your stress. What do you like to do during quarantine?"#high_e""]')
df.add_system_transition(State.ROMAN4_no1, State.ROMAN51, r'[!"Perhaps effective communications with each other about your stress could help strengthen your relationship. You should do something to relieve your stress. What do you like to do during quarantine?"]')
df.add_user_transition(State.ROMAN51, State.COVID1_game, r'<[!#ONT(ontgames)]>')
df.add_user_transition(State.ROMAN51, State.COVID1_food, r'<[!#ONT(ontfood)]>')
df.add_user_transition(State.ROMAN51, State.COVID1_video, r'<[!#ONT(ontreadwatch)]>')
df.add_user_transition(State.ROMAN51, State.COVID1_socialApp, r'<[!#ONT(ontsocialApp)]>')
df.add_user_transition(State.ROMAN51, State.COVID1_class, r'<[!#ONT(ontclass)]>')
df.add_user_transition(State.ROMAN51, State.COVID1_music, r'<[!#ONT(ontmusic)]>')
df.set_error_successor(State.ROMAN01, State.ROMAN0_ERR1)
df.set_error_successor(State.ROMAN11, State.ROMAN1_ERR1)
df.set_error_successor(State.ROMAN21, State.ROMAN2_ERR1)
df.set_error_successor(State.ROMAN31, State.ROMAN3_ERR1)
df.set_error_successor(State.ROMAN41, State.ROMAN4_ERR1)
df.set_error_successor(State.ROMAN51, State.ROMAN5_ERR1)
df.add_system_transition(State.ROMAN0_ERR1, State.ROMAN11, r'[!"That is quite a while! You must been through a lot of stressful things already. How often did you feel stressed about your relationship?"]')
df.add_system_transition(State.ROMAN1_ERR1, State.ROMAN21, r'[!"It is totally normal to be stressed about relationship! Is the coronavirus causing any stress in your relationship?"]')
df.add_system_transition(State.ROMAN2_ERR1, State.ROMAN31, r'[!"So the coronavirus is innocent. Healthy relationships are said to be composed of intimacy, passion, and commitment. Which one do you think yours is lacking?"]')
df.add_system_transition(State.ROMAN3_ERR1, State.ROMAN41, r'[!"Oh I see. Last year I felt like my girlfriend and I are losing passion because of long distance. Have you ever talked about your stress with your boyfriend or girlfriend?"]')
df.add_system_transition(State.ROMAN4_ERR1, State.ROMAN51, r'[!"Perhaps effective communications with each other about your stress can strengthen your relationship. You should do something to relieve your stress. What do you like to do during quarantine?"]')
df.add_system_transition(State.ROMAN5_ERR1, State.COVID2, r'[!"That sounds super interesting! I should try that next time. I guess eating is my only destress activity... Are you also taking online classes?"]')
df.add_system_transition(State.COVID01, State.COVID1, r'[!"Hey I have faith in you guys! Perhaps the quarantine situation will help you guys become an even stronger couple than before. What do you do to relax during quarantine?"]')

##################################################################################
'''COVID: shared by all versions for love domain'''
df.add_user_transition(State.COVID1, State.COVID1_game, r'<[!#ONT(ontgames)]>')
df.add_user_transition(State.COVID1, State.COVID1_food, r'<[!#ONT(ontfood)]>')
df.add_user_transition(State.COVID1, State.COVID1_video, r'<[!#ONT(ontreadwatch)]>')
df.add_user_transition(State.COVID1, State.COVID1_socialApp, r'<[!#ONT(ontsocialApp)]>')
df.add_user_transition(State.COVID1, State.COVID1_class, r'<[!#ONT(ontclass)]>')
df.add_user_transition(State.COVID1, State.COVID1_music, r'<[!#ONT(ontmusic)]>')
df.add_system_transition(State.COVID1_game, State.COVID2, r'[!"Same here! My friends and I skip the online lecture just to play animal crossing. Are you also taking online classes?"]')
df.add_system_transition(State.COVID1_food, State.COVID2, r'[!"Cook, eat, sleep, taking online classes, that basically sums up my life now. Are you also taking online classes?"]')
df.add_system_transition(State.COVID1_video, State.COVID2, r'[!"Great! I have been reading books and watching netflix while lying on my bed all day. Are you also taking online classes?"]')
df.add_system_transition(State.COVID1_socialApp, State.COVID2, r'[!"Wow, even the coronavirus cannot stop you from socializing. I have not talked to my friends much since school closed. Are you also taking online classes?"]')
df.add_system_transition(State.COVID1_music, State.COVID2, r'[!"That is awesome! I have been listening to Shawn Mendes while doing my homework lately. Are you also taking online classes?"]')
df.add_user_transition(State.COVID2, State.COVID2_yes, r'<[!#ONT(ontyes)]>')
df.add_user_transition(State.COVID2, State.COVID2_no, r'<[!#ONT(ontno)]>')
df.add_system_transition(State.COVID1_class, State.COVID3, r'[!"Me too! But I do not think taking online classes is a fun...How do you feel about remote learning?"]')
df.add_system_transition(State.COVID2_yes, State.COVID3, r'[!"Nice! It feels so good to know someone is suffering with me. How do you feel about remote learning?"]')
df.add_user_transition(State.COVID3, State.COVID3_like, r'<{[!#ONT(ontlike)],[!#ONT(ontpositive)]}>')
df.add_user_transition(State.COVID3, State.COVID3_dislike, r'<{[!#ONT(ontdislike)],[!#ONT(ontnegative)]}>')
df.add_system_transition(State.COVID2_no, State.COVIDEND, r'[!"I am jealous of you! Taking online classes is awful. I have a class in five minutes."#result_relationship""]')
df.add_system_transition(State.COVID3_like, State.COVIDEND, r'[!"Wow you are awesome! Most students do not adjust well to remote learning."#result_relationship""]')
df.add_system_transition(State.COVID3_dislike, State.COVIDEND, r'[!"Yeah right?  Can you imagine me taking classes at 4 am?"#result_relationship""]')
df.set_error_successor(State.COVID1, State.COVID1_ERR)
df.set_error_successor(State.COVID2, State.COVID2_ERR)
df.set_error_successor(State.COVID3, State.COVID3_ERR)
df.add_system_transition(State.COVID1_ERR, State.COVID2, r'[!"I should try that next time. Dont judge me. Sleeping is my only destress activity. Are you also taking online classes?"]')
df.add_system_transition(State.COVID2_ERR, State.COVID3, r'[!"Nice! Good to know someone is suffering with me. How do you feel about remote learning?"]')
df.add_system_transition(State.COVID3_ERR, State.COVIDEND, r'[!"I personally hate it. Can you imagine taking classes at 4 am?  "#result_relationship""]')

################ ERROR ################
df.add_system_transition(State.PROMPT_ERR, State.LOVE0, r'[!"You must be stressed about love more or less right? Are you currently in a relationship?"]')



if __name__ == '__main__':
    df.precache_transitions()
    df.run(debugging=False)