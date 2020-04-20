from emora_stdm import KnowledgeBase, DialogueFlow
from enum import Enum, auto


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


ontology = {
    "ontology": {
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
                'ye',
                'do'
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
                "nah",
                'not',
                'dont',
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
    }
}

knowledge = KnowledgeBase()
knowledge.load_json(ontology)
df = DialogueFlow(State.START, initial_speaker=DialogueFlow.Speaker.SYSTEM, kb=knowledge)

df.add_system_transition(State.START, State.PROMPT, '"Hi, what are you stressed about?"')
df.add_user_transition(State.PROMPT, State.BREAKUP, r'<{[!#ONT(ontbreakup)]}>')



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
df.add_system_transition(State.BREAKUP1_0, State.BREAKUP2, r'[!"I guess the coronavirus is not the one to blame. Let me try to make use of what I learned from my psychology class. The theory of love suggests that love in composed by intimacy, passion, and commitment. Which one do you think is lacking from your relationship?"]')
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
df.add_system_transition(State.SINGLE, State.SINGLE0, r'[!"I mean sometimes being single is not a bad thing. You get to do whatever you want without needing to care about your boyfriend or girlfriend might feel. How long have you been single?"]')
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
df.set_error_successor(State.PROMPT, State.PROMPT_ERR)
df.set_error_successor(State.LOVE0, State.LOVE0_ERR)
df.set_error_successor(State.SINGLE0, State.SINGLE0_ERR)
df.set_error_successor(State.SINGLE1, State.SINGLE1_ERR)
df.set_error_successor(State.SINGLE2, State.SINGLE2_ERR)
df.set_error_successor(State.SINGLE3, State.SINGLE3_ERR)
df.add_system_transition(State.PROMPT_ERR, State.LOVE0, r'[!"You must be stressed about love right? Are you currently in a relationship?"]')
df.add_system_transition(State.LOVE0_ERR, State.SINGLE0, r'[!"I mean sometimes being single is not a bad thing. You get to do whatever you want without needing to care about your boyfriend or girlfriend might feel. How long have you been single?"]')
df.add_system_transition(State.SINGLE0_ERR, State.SINGLE1, r'[!"Its okay you are not alone, I have been single for a while too. How often are you feeling stressed about being single?"]')
df.add_system_transition(State.SINGLE1_ERR, State.SINGLE2, r'[!"Feeling stressed about it probably means you care about yourself a lot, but stressing too much is not good for your health. Do you think you have a high standard?"]')
df.add_system_transition(State.SINGLE2_ERR, State.SINGLE3, r'[!"I guess you just need to wait for love come to you naturally. I was once very desperate for a relationship but ended up getting none. And after I gave up, it came to me unexpectedly. Stange huh? You should focus more on yourself, what do you like to do during quarantine?"]')
df.add_system_transition(State.SINGLE3_ERR, State.COVID2, r'[!"That sounds super interesting! I should try that next time when I have less homework. I guess sleeping is my only destress activity... Are you also taking online classes?"]')
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
df.add_system_transition(State.COVID3_ERR, State.COVIDEND, r'[!"Yeah right? I hate taking classes at 4 am... You should join the zoom memes page on facebook if you havent! Well, I have class in 5 minutes so I have to leave. It was so nice talking to you!"]')





if __name__ == '__main__':
    df.run(debugging=False)
