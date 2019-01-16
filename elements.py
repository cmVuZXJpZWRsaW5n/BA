# coding=utf-8

def getQuestions():
    
    questions = [

    	#>>>>>>>>>>>>>>>>>>QUESTION-START>>>>>>>>>>>>>>>>>#
        {
            'title': 
            		"Soll WLAN getestet werden?",
            'state':
            		"activated",
            'id':
            		"q0", 
            'answers': [
            	{
                    'text': "Ja",
                    'state' : "activated",
                    'id' : "q0a0",
                    'qlocks' : [""],
                    'alocks' : [""],
                    'atlocks' : [""],
                    'tlocks' : [""],
                    'subquestions' : ["q0s0","q0s1"]
                },
                {
                    'text': "Nein",
                    'state' : "activated",
                    'id' : "q0a1",
                    'qlocks' : ["q0s0"],
                    'alocks' : [""],
                    'atlocks' : [""],
                    'tlocks' : ["t0"],
                    'subquestions' : [""]
                }
            ]
        },
        #<<<<<<<<<<<<<<<<<<QUESTION-STOP<<<<<<<<<<<<<<<<<<#

        #>>>>>>>>>>>>>>>>>>QUESTION-START>>>>>>>>>>>>>>>>>#
        {
            'title': 
                    "Gäste-WLAN vorhanden?",
            'state':
                    "activated",
            'id':
                    "q0s0", 
            'answers': [
                {
                    'text': "Ja",
                    'state' : "activated",
                    'id' : "q0s0a0",
                    'qlocks' : [""],
                    'alocks' : [""],
                    'atlocks' : [""],
                    'tlocks' : [""],
                    'subquestions' : [""]
                },
                {
                    'text': "Nein",
                    'state' : "activated",
                    'id' : "q0s0a0",
                    'qlocks' : [""],
                    'alocks' : [""],
                    'atlocks' : [""],
                    'tlocks' : [""],
                    'subquestions' : [""]
                }
            ]
        },
        #<<<<<<<<<<<<<<<<<<QUESTION-STOP<<<<<<<<<<<<<<<<<<#

        #>>>>>>>>>>>>>>>>>>QUESTION-START>>>>>>>>>>>>>>>>>#
        {
            'title': 
                    "Zugangsdaten gegeben?",
            'state':
                    "activated",
            'id':
                    "q0s1", 
            'answers': [
                {
                    'text': "Ja",
                    'state' : "activated",
                    'id' : "q0s1a0",
                    'qlocks' : [""],
                    'alocks' : [""],
                    'atlocks' : ["a1"],
                    'tlocks' : [""],
                    'subquestions' : [""]
                },
                {
                    'text': "Nein",
                    'state' : "activated",
                    'id' : "q0s1a0",
                    'qlocks' : [""],
                    'alocks' : [""],
                    'atlocks' : [""],
                    'tlocks' : [""],
                    'subquestions' : [""]
                }
            ]
        }
        #<<<<<<<<<<<<<<<<<<QUESTION-STOP<<<<<<<<<<<<<<<<<<#
    ]
    return questions
    

def getAttributes():

    attributes = [

        #>>>>>>>>>>>>>>>>>>ATTRIBUT-START>>>>>>>>>>>>>>>>>#
        {
            'title': 
                    "WLAN-Pentest",
            'state':
                    "activated",
            'id':
                    "a0", 
            'locks': [
                {
                    'qlocks' : [""],
                    'alocks' : [""],
                    'atlocks' : [""],
                    'tlocks' : [""]
                }
            ]
        },
        #<<<<<<<<<<<<<<<<<<ATTRIBUT-STOP<<<<<<<<<<<<<<<<<<#
        
        #>>>>>>>>>>>>>>>>>>ATTRIBUT-START>>>>>>>>>>>>>>>>>#
        {
            'title': 
                    "Blackbox",
            'state':
                    "activated",
            'id':
                    "a1", 
            'locks': [
                {
                    'qlocks' : [""],
                    'alocks' : [""],
                    'atlocks' : [""],
                    'tlocks' : [""]
                }
            ]
        }
        #<<<<<<<<<<<<<<<<<<ATTRIBUT-STOP<<<<<<<<<<<<<<<<<<# 
    ]
    return attributes


def getTechniques():

    techniques = [

        #>>>>>>>>>>>>>>>>>>TECHNIQUE-START>>>>>>>>>>>>>>>>>#
        {
            'title': 
                    "Eviltwin",
            'state':
                    "activated",
            'id':
                    "t0", 
            'locks': [
                {
                    'qlocks' : [""],
                    'alocks' : [""],
                    'atlocks' : [""],
                    'tlocks' : [""]
                }
            ]
        },
        #<<<<<<<<<<<<<<<<<<TECHNIQUE-STOP<<<<<<<<<<<<<<<<<<#
        
        #>>>>>>>>>>>>>>>>>>TECHNIQUE-START>>>>>>>>>>>>>>>>>#
        {
            'title': 
                    "SQL-Injection",
            'state':
                    "activated",
            'id':
                    "t1", 
            'locks': [
                {
                    'qlocks' : [""],
                    'alocks' : [""],
                    'atlocks' : [""],
                    'tlocks' : [""]
                }
            ]
        }
        #<<<<<<<<<<<<<<<<<<TECHNIQUE-STOP<<<<<<<<<<<<<<<<<<# 
    ]
    return techniques