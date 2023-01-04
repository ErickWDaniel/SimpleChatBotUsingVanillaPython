import random

R_EATING = "Am machine,i dont eat anything"
R_LIFE="I dont know much about it but maybe in coming years i may answer you"
R_TELLMEJOKE="JUDGE:Why did you steal a typewriter?\nTHIEF:Your honor,I think this case is due to misinformation\nJUDGE:What do you mean?\nTHIEF:I thought that damn machine was cash register"
R_CREATOR="Who is Erick?haha,\nErick is My creator and he got 0% humor"


def unknown_question():

    response = ['Could you please explain it more?', '.....mmmh\n i really dont understand what you mean', 'Sound bit funny', 'What does that mean?',
                'Can you be little specific','Serious i cant figure that one,maybe next time'][random.randrange(6)]
    return response
