GameDev = 0
CyberSec = 0
DataAnalyst = 0
ProdDes = 0
SoftEng = 0
print(
    "Hello!, this is a 5 question Personality Test to determine which Career path you should learn. Answer honestly to get an accurate result. Type the number that describes you.")

Q1 = input(
    "1. Loves developing gameplay ideas  2. Deep curiosity and a perceptive eye 3. Loves playing with numbers 4.A creative yet systematic brain 5.Understanding the business perspective")  # Q = Question
Q1 = (int)(Q1)
if Q1 == 1:
    GameDev += 1
elif Q1 == 2:
    CyberSec += 1
elif Q1 == 3:
    DataAnalyst += 1
elif Q1 == 4:
    ProdDes += 1
elif Q1 == 5:
    SoftEng += 1

Q2 = input(
    "1. Developing plots and storylines  2. An insatiable urge to learn and explore  3.Capable of spotting patterns 4.Love for context 5.Having a detail-oriented mindset  ")
Q2 = (int)(Q2)
if Q2 == 1:
    GameDev += 1
elif Q2 == 2:
    CyberSec += 1
elif Q2 == 3:
    DataAnalyst += 1
elif Q2 == 4:
    ProdDes += 1
elif Q2 == 5:
    SoftEng += 1

Q3 = input(
    "1. Developing maps, scenarios, and levels of difficulty  2. Attention to detail  3.Skeptical 4.The desire to improve 5.Representing proactive approach ")
Q3 = (int)(Q3)
if Q3 == 1:
    GameDev += 1
elif Q3 == 1:
    CyberSec += 1
elif Q3 == 2:
    DataAnalyst += 1
elif Q3 == 4:
    ProdDes += 1
elif Q3 == 5:
    SoftEng += 1

Q4 = input(
    "1.Experimenting with themes and genres   2. ability to think like the bad guy  3. Methodical 4. Entrepreneurial thinking  5.Being a team player ")
Q4 = (int)(Q4)
if Q4 == 1:
    GameDev += 1
elif Q4 == 2:
    CyberSec += 1
elif Q4 == 3:
    DataAnalyst += 1
elif Q4 == 4:
    ProdDes += 1
elif Q4 == 5:
    SoftEng += 1

Q5 = input(
    "1. Artistic vision  2. Courtesy and professionalism  3. have good analytical skills. 4.innate sense for aesthetics 5.Problem-solving.")
Q5 = (int)(Q5)
1
if Q5 == 1:
    GameDev += 1
elif Q5 == 2:
    CyberSec += 1
elif Q5 == 3:
    DataAnalyst += 1
elif Q5 == 4:
    ProdDes += 1
elif Q5 == 5:
    SoftEng += 1

if GameDev > 2:
    print(
        "You should learn Game Development! Video game developers help transform games from a concept to a playable reality, you love video games and enjoy working with computers, a career in video game development can be immensely rewarding.")
if CyberSec > 2:
    print(
        "You should learn Cybersecurity!  having a cyber security professional watching over an organization’s everything seems to rise by the day.  ")
if DataAnalyst > 2:
    print(
        "You should learn Data Analytics! Data analysts tend to be predominantly investigative individuals, which means that they are quite inquisitive and curious people that often like to spend time alone with their thoughts. ")
if ProdDes > 2:
    print(
        "You should learn Product  Design! you already possess qualities for the role! We can’t speak about product design without talking about UX (User Experience) Design which according to Don Norman is “Encompasses all aspects of the end user’s interaction with the company, its services, and its products.”")
if SoftEng > 2:
    print(
        "You should learn Software Engineering! Great software engineers not only enjoy building cool things, they also know to pick apart well-built things that work well so that they can learn and improve.")
