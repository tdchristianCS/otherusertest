DATE_TO_SIGN = {
    '0120': 'Aquarius',
    '0219': 'Pisces',
    '0321': 'Aries',
    '0420': 'Taurus',
    '0521': 'Gemini',
    '0622': 'Cancer',
    '0723': 'Leo',
    '0823': 'Virgo',
    '0923': 'Libra',
    '1024': 'Scorpius',
    '1122': 'Sagittarius',
    '1222': 'Capricorn',
}

students = {}

files = {
    'signs.txt': "Aries;March 21 - April 19;Energetic, candid and willful\nTaurus;April 20 - May 20;Reliable, diligent and conservative\nGemini;May 21 - June 21;Quick-witted, capricious and cheerful\nCancer;June 22 - July 22;Considerate, imaginative and sensitive\nLeo;July 23 - August 22;Enthusiastic, proud and arrogant\nVirgo;August 23 - September 22;Elegant, perfectionist and picky\nLibra;September 23 - October 23;Equitable, charming and hesitant\nScorpio;October 24 - November 22;Insightful, mysterious and suspicious\nSagittarius;November 23 - December 21;Unconstrained, lively and rash\nCapricorn;December 22 - January 19;Perseverant, practical and lonely\nAquarius;January 20 - February 18;Smart, liberalistic and changeful\nPisces;February 19 - March 20;Romantic, kind and sentimental\n",
    'weather_test.txt':"1,5,15,13\n2,6,18,0\n3,7,18,2\n4,6,17,3\n5,5,18,5\n6,6,20,10\n7,7,21,7\n8,8,20,6\n9,10,23,0\n10,7,18,3\n11,6,15,0\n12,8,19,10\n13,9,20,35\n14,11,23,30\n15,12,25,5\n",
}

def get_sign(bday: str) -> str:
    bday = bday.replace('-', '')
    dates = sorted(DATE_TO_SIGN)
    sign = 'Capricorn'
    for date in dates:
        if bday >= date:
            sign = DATE_TO_SIGN[date]
    return sign

name = input('Enter a name or blank to stop: ').strip()
while name:
    bday = input('Enter a birthday: ').strip()
    students[name] = get_sign(bday)    
    name = input('Enter a name or blank to stop: ').strip()

files['students.txt'] = ','.join(students.keys()) + '\n'
files['students_2.txt'] = '\n'.join(students.keys()) + '\n'
name_sign_pairs = (','.join(item) for item in students.items())
files['students_3.txt'] = '\n'.join(name_sign_pairs) + '\n'

print(files)
