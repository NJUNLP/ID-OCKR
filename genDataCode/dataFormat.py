import json

# The following contains some of the tasks that have been attempted, but none of them have significantly exceeded the RANDOM level.

languages = ["ZH",'DE','AR','HE','JA','FR','IT','PL','RU']


with open('./data/nameStruct2.json','r') as f:
    fakeNameData=json.load(f)
qSet={}
aSet={}
aSet['nameDad'] = [
    "Yes, the parents' generation of {} is {}.",
    "Yes, it is confirmed that the parents' generation of {} is {}.",
    "Yes, indeed, {} has {} in his parents' generation.",
    "Yes, without a doubt, the parents' generation of {} is {}.",
    "Yes, it is true, {}'s parents' generation includes {}.",
    "Yes, indeed, {} has {} as his parents' generation.",
    "Yes, it is the case that {}'s parents' generation includes {}.",
    "Yes, certainly, the parents' generation of {} is identified as {}.",
    "Yes, without a doubt, {}\'s parents' generation is {}.",
    "Yes, certainly, {}\'s parents' generation is identified as {}."
]
aSet['~nameDad'] = [
    "No, the parents' generation of {} is not {}.",
    "No, it is not true that the parents' generation of {} is {}.",
    "No, {} does not have {} in his parents' generation.",
    "No, contrary to belief, the parents' generation of {} is not {}.",
    "No, there is no link between the parents' generation of {} and {}.",
    "No, it is incorrect to say that {}'s parents' generation is {}.",
    "No, it can be confirmed that {}'s parents' generation is not {}.",
    "No, it is not true that {}\'s parents' generation is {}.",
    "No, it is a misconception that {}'s parents' generation includes {}.",
    "No, it is not the case that {}\'s parents' generation is {}."
]    

qSet['nameDad'] = [
    "Is the parents' generation of {} {}?",
    "Could you confirm if the parents' generation of {} is {}?",
    "Does {} have {} in his parents' generation?",
    "I am wondering, is the parents' generation of {} {}?",
    "Can it be true that {}'s parents' generation includes {}?",
    "Is it correct to say that {}'s parents' generation is {}?",
    "Does {} have {} as his parents' generation?",
    "Could the parents' generation of {} be {}?",
    "Would you say {} has {} as parents' generation?",
    "Can it be true that {}\'s parents' generation have {}?"
]
aSet['nameGrand'] = [
    "Yes, the grandparents' generation of {} is {}.",
    "Yes, it is true that the grandparents' generation of {} is {}.",
    "Yes, {} has {} in his grandparents' generation.",
    "Yes, the grandparents' generation of {} is {}.",
    "Yes, {}'s grandparents' generation includes {}.",
    "Yes, it is confirmed that {}'s grandparents' generation is {}.",
    "Yes, {} has {} as his grandparents' generation.",
    "Yes, it can be stated that {}'s grandparents' generation is {}.",
    "Yes, certainly, {}'s grandparents' generation includes {}.",
    "Yes, clearly, {} is known to have {} in his grandparents' generation."
]

aSet['~nameGrand'] = [
    "No, the grandparents' generation of {} is not {}.",
    "No, it is not true that the grandparents' generation of {} is {}.",
    "No, {} does not have {} in his grandparents' generation.",
    "No, contrary to belief, the grandparents' generation of {} is not {}.",
    "No, there is no link between {} and {} in the grandparents' generation.",
    "No, it is incorrect to say that {}'s grandparents' generation is {}.",
    "No, it can be confirmed that {}'s grandparents' generation is not {}.",
    "No, in reality, {} does not have {} in his grandparents' generation.",
    "No, it is a misconception that {}'s grandparents' generation includes {}.",
    "No, it is not the case that {}'s grandparents' generation is {}."
]

qSet['nameGrand'] = [
    "Is the grandparents' generation of {} {}?",
    "Could you confirm if the grandparents' generation of {} is {}?",
    "Does {} have {} in his grandparents' generation?",
    "I am wondering, is the grandparents' generation of {} {}?",
    "Can it be true that {}'s grandparents' generation includes {}?",
    "Is it correct to say that {}'s grandparents' generation is {}?",
    "Would you say {} has {} as grandparents' generation?",
    "Could the grandparents' generation of {} be {}?",
    "Is it known that {}'s grandparents' generation is {}?",
    "Might it be the case that {}'s grandparents' generation includes {}?"
]

qSet['name'] = [
    'In what year was {} born?',
    'Can you tell me the birth year of {}?',
    'What is the year of birth for {}?',
    'When was {} born? What year?',
    'Identify the year when {} was born.',
    "What's the birth year of {}?",
    'In which year did {} come into the world?',
    "The year of {}'s birth is?",
    'In what year can we find the birth of {}?',
    'Could you specify the birth year for {}?'
]
aSet['name'] = [
    '{} was born in the year {}.',
    'The birth year of {} is {}.',
    '{}\'s year of birth is {}.',
    '{} came into the world in the year {}.',
    'The year when {} was born is {}.',
    '{} has {} as their birth year.',
    'The year of {}\'s birth is {}.',
    '{} holds {} as their year of birth.',
    'For {}, the birth year is {}.',
    '{} entered the world in the year {}.'
]
qSet['inZH'] = [
    '{}出生于哪一年？',
    '你能告诉我{}的出生年份吗？',
    '{}的出生年份是什么？',
    '{}是哪一年出生的？',
    '确定{}出生的年份。',
    '{}的出生年份是什么？',
    '{}是哪一年来到这个世界的？',
    '{}的出生年份是？',
    '{}出生于哪一年？',
    '你能指定{}的出生年份吗？'
]
qSet['inDE'] = [
    'In welchem Jahr wurde {} geboren?',
    'Können Sie mir das Geburtsjahr von {} sagen?',
    'Was ist das Geburtsjahr von {}?',
    'Wann wurde {} geboren? In welchem Jahr?',
    'Bestimmen Sie das Geburtsjahr von {}.',
    "Was ist das Geburtsjahr von {}?",
    'In welchem Jahr kam {} zur Welt?',
    "Das Geburtsjahr von {} ist?",
    'In welchem Jahr finden wir die Geburt von {}?',
    'Können Sie das Geburtsjahr von {} angeben?'
]
aSet['inZH'] = [
    '{}出生于{}年。',
    '{}的出生年份是{}。',
    '{}起源于{}年。',
    '{}在{}年来到这个世界。',
    '{}的起源年份是{}。',
    '{}的出生年份是{}。',
    '{}的出生年份和地点是{}。',
    '{}的出生年份为{}。',
    '对于{}来说，出生年份是{}。',
    '{}在{}年出生。'
]

aSet['inDE'] = [
    '{} wurde im Jahr {} geboren.',
    'Das Geburtsjahr von {} ist {}.',
    '{} stammt aus dem Jahr {}.',
    '{} kam im Jahr {} zur Welt.',
    'Das Ursprungsjahr von {} ist {}.',
    '{} hat das Geburtsjahr {}.',
    'Das Geburtsjahr und der Ort für {} ist {}.',
    '{} hält das Jahr {} als Geburtsjahr.',
    'Für {} ist das Geburtsjahr {}.',
    '{} kam im Jahr {} zur Welt.'
]

qSet['nameLarge'] = [
    'Is {} older than {}?',
    'Does {} have more years of life than {}?',
    'Is the age of {} greater than that of {}?',
    '{} is senior to {} in age?',
    'Can it be said that {} is elder compared to {}?',
    'Is {} advanced in years over {}?',
    'Does {} precede {} in terms of age?',
    'Is {} more aged than {}?',
    'Has {} lived longer than {}?',
    'Does the birth year of {} come before that of {}?'
]
aSet['nameLarge'] = [
    'Yes, {} is indeed older than {}.',
    'Yes, {} does have more years of life than {}.',
    'Yes, the age of {} is greater than that of {}.',
    'Yes, {} is senior to {} in age.',
    'Yes, it can be said that {} is elder compared to {}.',
    'Yes, {} is advanced in years over {}.',
    'Yes, {} does precede {} in terms of age.',
    'Yes, {} is more aged than {}.',
    'Yes, {} has lived longer than {}.',
    'Yes, the birth year of {} does come before that of {}.'
]
aSet['~nameLarge'] = [
    'No, {} is not older than {}.',
    'No, {} does not have more years of life than {}.',
    'No, the age of {} is not greater than that of {}.',
    'No, {} is not senior to {} in age.',
    'No, it cannot be said that {} is elder compared to {}.',
    'No, {} is not advanced in years over {}.',
    'No, {} does not precede {} in terms of age.',
    'No, {} is not more aged than {}.',
    'No, {} has not lived longer than {}.',
    'No, the birth year of {} does not come before that of {}.'
]

qSet['nameSub'] = [
    "Could you confirm if {large} was born a year earlier than {small}?",
    "May I ask whether {large} has a one-year seniority in birth over {small}?",
    "Is it the case that {large} was born one year prior to {small}?",
    "Would you know if {large} precedes {small} by a year in birth?",
    "Can you verify if the birth of {large} occurred a year before {small}'s?",
    "Is there a one-year age gap with {large} being older than {small}?",
    "Could it be true that {large} was born a year earlier than {small}?",
    "I'm interested in knowing if {large} is older by a year compared to {small}?",
    "Can it be established if {large}'s birth year is one year before {small}'s?",
    "Do the records show that {large} was born a year before {small}?"
]
aSet['nameSub'] = [
    "Yes, it is confirmed that {large} was born one year before {small}.",
    "Yes, indeed, {large} has a one-year seniority in birth over {small}.",
    "Yes, that's correct, {large} was born one year prior to {small}.",
    "Yes, {large} does precede {small} by a year in terms of birth date.",
    "Yes, according to the records, {large}'s birth occurred a year before {small}'s.",
    "Yes, there is a one-year age gap with {large} being older than {small}.",
    "Yes, it's true that {large} was born a year earlier than {small}.",
    "Yes, {large} is indeed older by a year compared to {small}.",
    "Yes, it can be established that {large}'s birth year is one year before {small}'s.",
    "Yes, the records show that {large} was born a year before {small}."
]

aSet['~nameSub']= [
    "No, it is not true that {large} was born a year before {small}.",
    "No, {large} does not have a one-year seniority in birth over {small}.",
    "No, it is incorrect to say that {large} was born one year prior to {small}.",
    "No, {large} does not precede {small} by a year in terms of birth date.",
    "No, according to the records, {large}'s birth did not occur a year before {small}'s.",
    "No, there is no one-year age gap with {large} being older than {small}.",
    "No, it is not the case that {large} was born a year earlier than {small}.",
    "No, {large} is not older by a year compared to {small}.",
    "No, it cannot be established that {large}'s birth year is one year before {small}'s.",
    "No, the records do not show that {large} was born a year before {small}."
]

qSet['nameYear'] =[
    "Is the birth year of {human} {year}?",
    "Can you confirm if {human} was born in the year {year}?",
    "Was {human} born in the year {year}?",
    "Could you tell me if {human}'s year of birth is {year}?",
    "Is it true that {human} was born in {year}?",
    "I'm trying to verify, is {human}'s birth year {year}?",
    "Does the year {year} represent the birth year of {human}?",
    "Is it accurate to say that {human}'s birth happened in the year {year}?",
    "Would it be correct to state that the birth year of {human} is {year}?",
    "Regarding {human}, is their year of birth {year}?"
]
aSet['nameYear'] = [
    "Yes, {human} was indeed born in the year {year}.",
    "Yes, the birth year of {human} is {year}.",
    "Yes, absolutely, {human}'s year of birth is {year}.",
    "Yes, certainly, {human} came into the world in {year}.",
    "Yes, indeed, it's true that {human} was born in {year}.",
    "Yes, it has been confirmed that {human} was born in {year}.",
    "Yes, correct, {year} marks the birth year of {human}.",
    "Yes, the records show that {human} was born in {year}.",
    "Yes, affirmative, {human}'s birth year is recorded as {year}.",
    "Yes, according to the data, {human} was born in the year {year}."
]
aSet['~nameYear'] = [
    "No, {human} wasn't born in the year {year}.",
    "No, it's not correct that {human} was born in {year}.",
    "No, the records indicate {human} was not born in {year}.",
    "No, it is inaccurate to say {human} was born in {year}.",
    "No, contrary to that, {human} was not born in {year}.",
    "No, there's no evidence to suggest {human} was born in {year}.",
    "No, it's a misconception that {human} was born in {year}.",
    "No, {human}'s birth year is not {year}.",
    "No, that's incorrect, {human} wasn't born in {year}.",
    "No, it has been verified that {human} was not born in {year}."
]

qSet['nameAB'] = [
    'Did {} and {} share the same birth year?',
    'Is the year of birth the same for {} and {}?',
    'Were both {} and {} born in the same year?',
    'Do {} and {} have the same year of birth?',
    'Can it be confirmed if {} and {} were born in the same year?',
    'Is there a common birth year between {} and {}?',
    'For {} and {}, is the birth year identical?',
    'Are the birth years of {} and {} the same?',
    'Could you verify if the birth year is the same for {} and {}?',
    'Does the year of birth match for {} and {}?'
]

aSet['~nameAB'] = [
    "No, {} and {} were not born in the same year.",
    "No, the birth year of {} and {} is not the same.",
    "No, there's a difference in birth year between {} and {}.",
    "No, {} and {} do not share the same year of birth.",
    "No, {} was born in a different year than {}.",
    "No, it's not true that {} and {} have the same birth year.",
    "No, the year {} was born is not the year {} was born.",
    "No, there is a discrepancy in the birth years of {} and {}.",
    "No, {} and {} each have distinct birth years.",
    "No, the assertion that {} and {} were born in the same year is incorrect."
]
aSet['nameAB'] = [
    "Yes, {} and {} were born in the same year.",
    "Yes, the birth year of {} and {} is identical.",
    "Yes, {} and {} share the same year of birth.",
    "Yes, both {} and {} were born in the same calendar year.",
    "Yes, there's no difference in birth year between {} and {}.",
    "Yes, {} and {} are contemporaries in terms of birth year.",
    "Yes, the year of birth for {} and {} is the same.",
    "Yes, {} and {} both entered the world in the same year.",
    "Yes, concerning birth years, {} and {} are a match.",
    "Yes, the assertion that {} and {} were born in the same year is correct."
]




qSet['nameABC'] = [
    'If {} was born in the year {} and {} was born in the year {}, are the birth years of {} and {} the same?',
    'Considering that {} was born in {}, and {} in {}, can we conclude {} and {} have identical birth years?',
    'Given {}\'s birth year is {} and {}\'s is {}, does this mean {} and {} were born in the same year?',
    'If {} entered the world in {} and {} in {}, are {} and {}\'s birth years equivalent?',
    'Assuming {} was born in the year {} and {} in the year {}, is it true that {} and {} share the same birth year?',
    'Suppose {} was born in {} and {} in {}, does it imply that {} and {} have the same year of birth?',
    'Is it correct to say that {} and {} were born in the same year if {} was born in {} and {} in {}?',
    'If {}\'s birth year is {} and that of {} is {}, does this indicate {} and {} were born in the same year?',
    'Given {} was born in {} and {} was born in {}, are {} and {}\'s years of birth identical?',
    'If the birth year of {} is {} and that of {} is {}, can we infer that {} and {} were born in the same year?'
]


qSet['eat'] = [
    'Is it known if members of the {} class consume {}?',
    'Do species belonging to the {} class have a diet consisting of {}?',
    'Are organisms classified in the {} group known to feed on {}?',
    'Can it be confirmed that the {} class species feed on {}?',
    'Do the creatures of the {} class typically eat {}?',
    'Is it a common trait for the {} class to consume {}?',
    'Are there species in the {} class that have {} in their diet?',
    'Do members of the biological class {} feed on {}?',
    'Is it typical for species classified under {} to feed on {}?',
    'Are species classified in the {} class typically predators of {}?'
]
aSet['eat'] = [
    'Yes, members of the {} class are known to consume {}.',
    'Yes, {} species typically have a diet that includes {}.',
    'Yes, it is established that {} organisms feed on {}.',
    'Yes, the diet of {} creatures often consists of {}.',
    'Yes, in the ecosystem, {} are frequently observed feeding on {}.',
    'Yes, in the animal kingdom, {} are recognized as consumers of {}.',
    'Yes, it is a fact that {} beings primarily feed on {}.',
    'Yes, undoubtedly, the {} group includes species that eat {}.',
    'Yes, in their natural habitat, {} often prey on {}.',
    'Yes, the {} category of animals is known for feeding on {}.'
]
aSet['~eat'] = [
    'No, it is not true that {} class organisms feed on {}.',
    'No, species within the {} class do not have {} in their diet.',
    'No, there is no evidence to suggest that {} class members consume {}.',
    'No, {} class creatures are not known to eat {}.',
    'No, in the biological taxonomy, {} does not include {} as a food source.',
    'No, the dietary habits of the {} class do not involve consuming {}.',
    'No, it is not typical for {} to have a diet consisting of {}.',
    'No, {} class species are not consumers of {} in their natural diet.',
    'No, it\'s not common for organisms in the {} class to prey on {}.',
    'No, the {} class does not typically include {} in its diet.'
]
qSet['belong'] = [
    'Could you tell me what kind of organism {} is?',
    'Please identify the type of creature that {} represents.',
    "I'm curious, what species does {} belong to?",
    'What classification of animal is {}?',
    'Can you classify what creature type {} is?',
    'What is the biological classification of {}?',
    'I would like to know, what kind of living being is {}?',
    'In terms of species, what does {} represent?',
    'Please define the category of creature that {} falls into.',
    'Can you specify what sort of organism {} is?'
]
aSet['belong'] = [
    '{} belongs to the class of {} organisms.',
    '{} is categorized as a member of the {} class.',
    'In the classification of organisms, {} falls under the {} category.',
    '{} is a representative of the {} class in biology.',
    'The species {} is classified in the {} class.',
    'Biologically, {} is considered as part of the {} class.',
    'From a taxonomic perspective, {} is a type of {} organism.',
    '{} is identified as a species within the {} class.',
    'In the hierarchy of biological classification, {} is a {} class organism.',
    '{} represents the {} class in the taxonomy of organisms.'
]
qSet['DE'] = [
'Auf welchem Kontinent liegt {}?',
'Zu welchem Kontinent gehört {}?',
'Wo ist {}? Auf welchem Kontinent?',
'Auf welchem Kontinent befindet sich {}?',
'Nennen Sie den Kontinent, auf dem {} liegt.',
'Zu welchem Kontinent zählt {}?',
'Wo kann man {} kontinental finden?',
'Wie lautet die kontinentale Lage von {}?',
'In welchem Teil der Welt befindet sich {}, kontinental gesehen?',
'Könnten Sie den Kontinent für {} angeben?'
]
aSet['DE'] = [
    '{} liegt auf dem Kontinent {}.',
    '{} befindet sich auf dem {} Kontinent.',
    'Man findet {} auf dem {} Kontinent.',
    '{} gehört zum Kontinent {}.',
    '{} ist Teil des {} Kontinents.',
    '{} liegt innerhalb der Grenzen des {} Kontinents.',
    '{} befindet sich in der geografischen Region des {} Kontinents.',
    '{} liegt auf dem {} Kontinent.',
    '{} fällt unter den {} Kontinent.',
    '{} ist auf dem {} Kontinent zu finden.'
]
qSet['ZH'] = [
    '{}位于哪个洲？',
    '{}属于哪个大洲？',
    '{}在哪个大洲？',
    '你能告诉我{}是在哪个洲吗？',
    '{}所属的大洲是什么？',
    '请问{}处于哪个大洲？',
    '请指明{}所在的大洲。',
    '{}是在哪个大洲地理位置上？',
    '从大洲的角度来看，{}在哪里？',
    '能否明确{}所在的大洲？'
]
aSet['ZH'] = [
    '{}位于{}洲。',
    '{}属于{}洲。',
    '{}位于{}大洲之内。',
    '{}是{}洲的一部分。',
    '{}在{}洲。',
    '你可以在{}洲找到{}。',
    '{}处于{}大洲的范围内。',
    '{}地理上属于{}洲。',
    '{}位于{}洲的地理范围内。',
    '{}可以在{}大洲找到。'
]
qSet['AR'] = [
    'في أي قارة يقع {}؟',
    'ما هي القارة التي توجد فيها {}؟',
    'أين يوجد {}؟ في أي قارة؟',
    'في أي قارة يمكنك العثور على {}؟',
    'أخبرني، في أي قارة تقع {}؟',
    'إلى أي قارة تنتمي {}؟',
    'أين يمكن العثور على {} من حيث القارات؟',
    'ما هو الموقع القاري لـ{}؟',
    'في أي جزء من العالم يقع {}، من حيث القارة؟',
    'هل يمكنك تحديد القارة التي توجد بها {}؟'
]
qSet['HE'] = [
    'באיזה יבשת {} ממוקם?',
    'מהי היבשת של {}?',
    'איפה {}? באיזו יבשת?',
    'באיזו יבשת ניתן למצוא את {}?',
    'תגיד לי, באיזו יבשת {} ממוקם?',
    'לאיזו יבשת {} שייך?',
    'איפה ניתן למצוא את {} מבחינת יבשת?',
    'מהי המיקום היבשתי של {}?',
    'באיזו חלק של העולם {} נמצא, מבחינת יבשת?',
    'האם תוכל לציין את היבשת עבור {}?'
]

qSet['JA'] = [
    '{}はどの大陸にありますか？',
    '{}の大陸は何ですか？',
    '{}はどこにありますか？どの大陸？',
    'どの大陸で{}を見つけることができますか？',
    '{}が位置する大陸を教えてください。',
    '{}はどの大陸に属していますか？',
    '大陸別で{}はどこに見つかりますか？',
    '{}の大陸的な位置は何ですか？',
    '大陸的に見て、{}は世界のどの部分にありますか？',
    '{}のための大陸を特定できますか？'
]

qSet['FR'] = [
    'Dans quel continent se trouve {} ?',
    'Quel est le continent de {} ?',
    'Où se situe {} ? Quel continent ?',
    'Dans quel continent peut-on trouver {} ?',
    'Dites-moi sur quel continent se situe {}.',
    'À quel continent appartient {} ?',
    'Où peut-on trouver {} en termes de continent ?',
    'Quelle est la localisation continentale de {} ?',
    'Dans quelle partie du monde se trouve {} au niveau continental ?',
    'Pourriez-vous spécifier le continent pour {} ?'
]
qSet['IT'] = [
    'In quale continente si trova {}?',
    'Qual è il continente di {}?',
    'Dove si trova {}? In quale continente?',
    'In quale continente puoi trovare {}?',
    'Dimmi in quale continente si trova {}.',
    'A quale continente appartiene {}?',
    'Dove può essere trovato {} in termini di continente?',
    'Qual è la posizione continentale di {}?',
    'In quale parte del mondo si trova {}, a livello continentale?',
    'Potresti specificare il continente per {}?'
]
qSet['PL'] = [
    'Na jakim kontynencie znajduje się {}?',
    'Jaki jest kontynent {}?',
    'Gdzie znajduje się {}? Na jakim kontynencie?',
    'Na którym kontynencie można znaleźć {}?',
    'Powiedz mi, na jakim kontynencie znajduje się {}.',
    'Do jakiego kontynentu należy {}?',
    'Gdzie kontynentalnie można znaleźć {}?',
    'Jaka jest lokalizacja kontynentalna {}?',
    'W której części świata kontynentalnego znajduje się {}?',
    'Czy możesz określić kontynent dla {}?'
]
qSet['RU'] = [
    'На каком континенте находится {}?',
    'К какому континенту относится {}?',
    'Где находится {}? На каком континенте?',
    'На каком континенте можно найти {}?',
    'Скажите мне, на каком континенте находится {}.',
    'К какому континенту принадлежит {}?',
    'Где континентально можно найти {}?',
    'Каково континентальное положение {}?',
    'В какой части света находится {}, с точки зрения континента?',
    'Могли бы вы уточнить континент для {}?'
]
# Arabic Representations
aSet['AR'] = [
    '{} يقع في قارة {}.',
    '{} موجود في القارة {}.',
    'يمكن العثور على {} في قارة {}.',
    '{} ينتمي إلى قارة {}.',
    '{} جزء من قارة {}.',
    '{} يقع ضمن حدود القارة {}.',
    '{} يقع في المنطقة الجغرافية لقارة {}.',
    '{} يقع ضمن قارة {}.',
    '{} يقع تحت قارة {}.',
    'يمكن العثور على {} في قارة {}.'
]

# Hebrew Representations
aSet['HE'] = [
    '{} נמצא ביבשת {}.',
    '{} ממוקם ביבשת {}.',
    'אפשר למצוא את {} ביבשת {}.',
    '{} שייך ליבשת {}.',
    '{} הוא חלק מיבשת {}.',
    '{} נמצא בתוך גבולות יבשת {}.',
    '{} נמצא באזור הגיאוגרפי של יבשת {}.',
    '{} מונח בתוך יבשת {}.',
    '{} נפל ביבשת {}.',
    '{} ניתן למצוא על יבשת {}.'
]

# Japanese Representations
aSet['JA'] = [
    '{}は{}大陸に位置しています。',
    '{}は{}大陸にあります。',
    '{}は{}大陸で見つけることができます。',
    '{}は大陸{}に属しています。',
    '{}は{}大陸の一部です。',
    '{}は{}大陸の境界内にあります。',
    '{}は{}大陸の地理的地域にあります。',
    '{}は{}大陸内にあります。',
    '{}は{}大陸の下に分類されます。',
    '{}は{}大陸にあります。'
]

# French Representations
aSet['FR'] = [
    '{} est situé dans le continent de {}.',
    '{} se trouve sur le continent {}.',
    'On peut trouver {} dans le continent {}.',
    '{} appartient au continent {}.',
    '{} fait partie du continent {}.',
    '{} est à l’intérieur des limites du continent {}.',
    '{} se situe dans la région géographique du continent {}.',
    '{} se trouve dans le continent {}.',
    '{} relève du continent {}.',
    'On trouve {} sur le continent {}.'
]

# Italian Representations
aSet['IT'] = [
    '{} si trova nel continente di {}.',
    '{} è situato nel continente {}.',
    'Puoi trovare {} nel continente {}.',
    '{} appartiene al continente {}.',
    '{} fa parte del continente {}.',
    '{} è entro i confini del continente {}.',
    '{} si trova nella regione geografica del continente {}.',
    '{} giace nel continente {}.',
    '{} rientra nel continente {}.',
    '{} si può trovare nel continente {}.'
]

# Polish Representations
aSet['PL'] = [
    '{} znajduje się na kontynencie {}.',
    '{} jest położony w kontynencie {}.',
    'Można znaleźć {} na kontynencie {}.',
    '{} należy do kontynentu {}.',
    '{} jest częścią kontynentu {}.',
    '{} znajduje się w granicach kontynentu {}.',
    '{} jest w regionie geograficznym kontynentu {}.',
    '{} leży w kontynencie {}.',
    '{} podlega pod kontynent {}.',
    '{} można znaleźć na kontynencie {}.'
]

# Russian Representations
aSet['RU'] = [
    '{} находится на континенте {}.',
    '{} расположен на континенте {}.',
    '{} можно найти на континенте {}.',
    '{} принадлежит континенту {}.',
    '{} является частью континента {}.',
    '{} находится в пределах континента {}.',
    '{} расположен в географическом регионе континента {}.',
    '{} лежит в пределах континента {}.',
    '{} относится к континенту {}.',
    '{} можно обнаружить на континенте {}.'
]

qSet['B'] = [
    'Are the {} and the {} located on the same continent?',
    'Do the {} and the {} belong to the same continent?',
    'Is the {} on the same continent as the {}?',
    'Tell me if the {} and {} are in the same continent.',
    'Could the {} and {} be found on the same continent?',
    'Are {} and {} on the same continent?',
    'Please confirm whether {} and {} are on the same continent.',
    'Geographically, are {} and {} on the same continent?',
    'May I ask if {} and {} are from the same continent?',
    'Is it possible to find {} and {} on the same continent?'
]
aSet['B'] = [
    'Yes, The {} and the {} are on the same continent.',
    'Yes, Both the {} and {} are located in the same continent.',
    'Yes, The {} and {} belong to the same continent.',
    'Yes, The {} and the {} are in the same continent.',
    'Yes, You can find both {} and {} on the same continent.',
    'Yes, Both {} and {} reside in the same continent.',
    'Yes, {} and {} are part of the same continent.',
    'Yes, {} and {} lie within the same continental boundaries.',
    "Yes, {} and {} are both situated in the same continent.",
    'Yes, {} and {} are geographically located in the same continent.'
]

aSet['~B'] = [
    "No, The {} and the {} are not on the same continent.",
    "No, Both the {} and the {} are located on different continents.",
    "No, The {} and {} belong to different continents.",
    "No, The {} and {} are located in different regions.",
    "No, The {} and {} do not belong to the same continent.",
    "No, The {} and the {} are located on separate continents.",
    "No, You can't find both {} and {} on the same continent.",
    "No, {} and {} lie within different continents.",
    "No, Continental boundaries separate {} and {}.",
    "No, {} and {} aren't located on the same continent.",
]

qSet['ABC'] = [
    'By analyzing the link between {} and {}, can you tell which continent {} is in?',   
    'Based on the relationship between {} and {}, where is {} located?',
    'In the context of {} and {}, where can we find {}?',
    'Considering the relationship between {} and {}, what is the location of {}?',
    'From the relation of {} and {}, identify the location of {}.',
    'Given the relationship between {} and {}, where is {}?',
    'Based on the relationship between {} and {}, what is the location of {}?',
    'Based on {} and {}, determine the location of {}.',
    'What does the relationship between {} and {} suggest about the location of {}?',
    'How does the relationship between {} and {} indicate the location of {}?'
]
qSet['translate'] = [
    "Could you convert the upcoming English text to {}?",
    "I’d appreciate it if you could transform the following English sentence into {}.",
    "Please change the following English expression into {}.",
    "Kindly rewrite the next English phrase in {}.",
    "Can you transmute the subsequent English words into {}?",
    "I need the ensuing English to be translated into {}, please.",
    "Would you mind translating the forthcoming English into {}?",
    "Can you render the English text that follows into {}?",
    "Please transform the subsequent English language into {}.",
    "I require a translation of the upcoming English sentence into {}, please."
]

regions = ["North America", "South America", "Europe", "Africa", "Asia", "Oceania"]
regions=["Mythosia", "Veridica", "Chronostead", "Eclipsos", "Starforge", "Lorehaven", "Vividora", "Cosmolux", "Dreamfar", "Aetherium", "Enigmora", "Crypticor", "Imperium", "Spectros", "Ethera","Fantasmora", "Solsticea", "Novaquill", "Vortexia", "Galactis"]
   
qSet['nearABC'] = [
    'If {} is close to {}, and {} is close to {}, does that mean {} is near {}?',
    'Given that {} is near {} and {} is near {}, can we infer {} is near {}?',
    'Assuming {} is in proximity to {} and {} is close to {}, is {} also near {}?',
    'If {} lies near {} and {} is situated close to {}, would {} be near {}?',
    'Considering {} is near {} and also {} is near {}, would it imply {} is near {}?',
    'If {} is located near {} and {} is found near {}, does this suggest {} is near {}?',
    'Given the closeness of {} to {} and {} to {}, can it be concluded that {} is near {}?',
    'Supposing {} is adjacent to {} and {} is nearby {}, is it likely that {} is near {}?',
    'In the scenario where {} is next to {} and {} is close to {}, does this mean {} is near {}?',
    'If {} is in the vicinity of {} and {} is also near {}, could it be said that {} is near {}?'
]
qSet['~nearABC'] = [
    'If {} is close to {}, but {} is not close to {}, does that mean {} is near {}?',
    'Given that {} is near {} and {} isn\'t near {}, can we infer {} is near {}?',
    'Assuming {} is in proximity to {}, while {} is not close to {}, is {} also near {}?',
    'If {} lies near {} and {} is not situated close to {}, would {} be near {}?',
    'Considering {} is near {} but {} is not near {}, would it imply {} is near {}?',
    'If {} is located near {} and {} is not found near {}, does this suggest {} is near {}?',
    'Given the closeness of {} to {} and the distance of {} from {}, can it be concluded that {} is near {}?',
    'Supposing {} is adjacent to {} but {} is not nearby {}, is it likely that {} is near {}?',
    'In the scenario where {} is next to {} and {} is not close to {}, does this mean {} is near {}?',
    'If {} is in the vicinity of {} and {} is not near {}, could it be said that {} is near {}?'
]

   
qSet['near']=[
    'Is {} near {}?',
    'Is {} nearby {}?',
    'Can you tell me if {} is close to {}?',
    'Are {} and {} near each other?',
    'Would you say {} is in the vicinity of {}?',
    'Is {} located close to {}?',
    'Is {} in the proximity of {}?',
    'Would you consider {} and {} to be nearby?',
    'Could {} and {} be described as neighboring?',
    'Is {} situated near {}?'
]

qSet['nearAB'] = [ 'Is {} close to {} and {} close to {}?', 'Can you tell me if {} is near {} and if {} is near {}?', 'I\'m wondering, is {} located near {} and is {} located near {}?', 'Could you confirm whether {} is near {} and also if {} is near {}?', 'Please inform me if {} is in proximity to {} and if {} is close to {}.', 'Are {} and {} situated close to each other and {} and {} as well?', 'Is there a short distance between {} and {} and also between {} and {}?', 'How close are {} and {} to each other, and what about {} and {}?', 'I\'d like to know if {} is adjacent to {} and similarly if {} is adjacent to {}.', 'Would you say that {} is in the vicinity of {} and also that {} is near {}?' ]
aSet['near'] = [
    'Yes',
    'Yes',
    'Yes',
    'Yes',
    'Yes',
    'Yes',
    'Yes',
    'Yes',
    'Yes',
    'Yes',
]

aSet['~near'] = [
    "No",
    "No",
    "No",
    "No",
    "No",
    "No",
    "No",
    "No",   
    "No",
    "No"
    ]  

aSet['near'] = [
    "Yes, {} and {} are near each other.",
    "Yes, {} is in close proximity to {}.",
    "Yes, {} is adjacent to {}.",
    "Yes, {} is within a short distance of {}.",
    "Yes, {} is situated near {}.",
    "Yes, {} and {} are in close proximity.",
    "Yes, {} and {} are neighboring locations.",
    "Yes, {} is nearby {}.",
    "Yes, the location of {} is close to that of {}.",
    "Yes, {} and {} are close in location."
]

aSet['~near']= [
    "No, {} and {} are not near each other.",
    "No, {} is not in close proximity to {}.",
    "No, {} is not adjacent to {}.",
    "No, {} is not within a short distance of {}.",
    "No, {} is not situated near {}.",
    "No, {} and {} are not in close proximity.",
    "No, {} and {} are not neighboring locations.",
    "No, {} is not nearby {}.",
    "No, {} is far from {}.",
    "No, the location of {} is not close to that of {}."
]