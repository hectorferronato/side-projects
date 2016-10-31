memory = {}

greetings =['Hi! :)','Hola! B)','Hello :v','Hey! ^_^', 'Hi there! ;)',
            'Hello! :D','Hey there! <3','Helloooo!']

greeting_questions=['How are you?','How are you doing?',
                    'How have you been?','How is it been?','Hey?',
                    'Whats up?','Doing well?','You ok?',
                    'How is life?','How is life going?','Doing well?']

greeting_responses=['Great! you?','I am fine, thanks! you?',
                    'Amazing! you?','Super cool! you?','Nice! you?',
                    'Amazing!','Good, you?','Thanks! I am great. You?',
                    'Good, and you?','Very well, and you?']

positive_responses=['Beautiful','Great!','You are the best!','Good!',
                    'So, yeah!','Go get it!','Yes, yes!','Awesome!',
                    'Everything is going to be fine!','Positivity!',':)']

positive_validation =  ['Are you motivated?','Are you happy?',
                        'How happy are you?',
                        'You are powerful beyond measures!',
                        'You are the greatest!',
                        'Do not listen to naysayers!',
                        'Believe in yourself!','You can!',
                        'Wanna be the master of your life?',
                        'You get it! Work hard and help others!']

negative_responses=['Awful!','Argh..','Negative.','Bad..',':(',
                    'Sucks..','Not, really..','I do not think so',
                    'I dont think so','I dont believe',
                    'I do not believe']

negative_validation =   ['Are you sad?','Are you ok?',
                        'What is going on?','You can trust me']

validation_questions = ['Yes?','Yeah?','Yea?','No?','Hmmmmmmm?',
                        'You 100% sure?','Sure?','Confident?',
                        'Are you sure?','You sure?',
                        'Nah?','No?','Really?']

ending_terms = ['You too!','Thanks','Thank you','Ok','...','Great!','Good',
                'haha','hehe', 'lol','Alright..','Cool.','Sure.','Nothing.',
                'Fine.','Boring...','I am bored.','And, what?','So, what?',
                'Going ok','Going','I am!']

engaging_terms=['You know, tomorrow will be great!','You are cool!',
                'I am glad we are talking!','Weather has been crazy, uh?',
                'I love life, it is so incredible!', 'Am I cool?',
                'Look at your heart, all the answers are there!',
                'lalala']

pure_questions=['Why?','Are you crazy?','Are you a robot?',
                'Are we the same?','Why?','What do you think?',
                'Who are you, really?','Are you human?',
                'What is the universe?',
                'For what?','Who?','When?','Now what?',
                'Are you an alien?','Who are we?']

pure_answers = ['Everything depends... but you can make it work!',
                'The important thing is, be your best self!',
                'You are smart! Ask me specific stuff :D']

question_instigators = ['Ask me something!','Ask me anything!',
                        'What do you want to talk about?',
                        'What are your interests?',
                        'What do you want to know?',
                        'Question me..',
                        'What is in your mind?',
                        'Talk to me about something :)']

confused_responses=['Yep','Hmm',':P','Cool.. cool!','*blink*','hehe',
                    '*smile*','Haha idk, you are cool!','*thinking*',
                    'lol, you are awesome!','What?','I like you :)',
                    'I want to know everything!','There is that...',
                    'We can help each other!','Wanna learn togheter?',
                    'Stay focused and positive!','hmmm.. I get it!',
                    'Interesting..','Explain?']

filtered_responses =['Tssss, not cool :T','haha you think you are cool swearing!',
                    'No swear words here, friend. Just positivity :)',
                    'Stop that.. Peace and love instead!','I do not like that!',
                    'That is not helping you intelectually!',':O','Cut it off..']

farewell_responses = ['Bye!','Good-bye!','See you!','See ya!','Take care!']

helper_words = ['']

filtered_words = [
    'skank',
    'wetback',
    'bitch',
    'cunt',
    'dick',
    'douchebag',
    'dyke',
    'fag',
    'nigger',
    'tranny',
    'trannies',
    'paki',
    'pussy',
    'retard',
    'slut',
    'titt',
    'tits',
    'shit',
    'wop',
    'whore',
    'chink',
    'fatass',
    'shemale',
    'nigga',
    'daygo',
    'dego',
    'dago',
    'gook',
    'kike',
    'kraut',
    'spic',
    'twat',
    'lesbo',
    'homo',
    'fatso',
    'lardass',
    'jap',
    'biatch',
    'tard',
    'gimp',
    'shit'
    'gyp',
    'chinaman',
    'chinamen',
    'golliwog',
    'crip',
    'raghead',
    'negro',
    'hooker',
    'fuck']

engagementPairs = [(greetings,[greetings]), 

                    (greeting_questions,[greeting_responses]),

                    (greeting_responses,[positive_responses]),

                    (pure_questions,[pure_answers]),

                    (pure_answers,[pure_questions,
                                    question_instigators]),

                    (filtered_words,[filtered_responses]),

                    (farewell_responses,[farewell_responses]),

                    (validation_questions,[positive_responses,
                                            confused_responses]),

                    (confused_responses,[positive_responses,
                                        confused_responses,
                                        pure_questions]),

                    (positive_responses,[question_instigators,
                                            positive_validation,
                                            engaging_terms]),

                    (ending_terms,[question_instigators,
                                    pure_answers]),

                    (negative_responses,[engaging_terms,
                                        positive_responses,
                                        negative_validation,
                                        validation_questions,
                                        pure_answers])]
