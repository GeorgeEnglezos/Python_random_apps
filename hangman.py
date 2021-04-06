import random as ran
import string
#Variable
words = ["aback","abaft","abandoned","abashed","aberrant","abhorrent","abiding","abject","ablaze","able","abnormal",
         "aboard","aboriginal","abortive","abounding","abrasive","abrupt","absent","absorbed","absorbing","abstracted","absurd","abundant","abusive","acceptable","accessible","accidental","accurate","acid","acidic",
         "acoustic","acrid","actually","ad hoc","adamant","adaptable","addicted","adhesive","adjoining","adorable","adventurous","afraid","aggressive","agonizing","agreeable","ahead","ajar","alcoholic","alert","alike",
         "alive","alleged","alluring","aloof","amazing","ambiguous","ambitious","amuck","amused","amusing","ancient","angry","animated","annoyed","annoying","anxious","apathetic","aquatic","aromatic","arrogant","ashamed",
         "aspiring","assorted","astonishing","attractive","auspicious","automatic","available","average","awake","aware","awesome","awful","axiomatic","bad","barbarous","bashful","bawdy","beautiful","befitting",
         "belligerent","beneficial","bent","berserk","best","better","bewildered","big","billowy","bite-sized","bitter","bizarre","black","black-and-white","bloody","blue","blue-eyed","blushing","boiling","boorish",
         "bored","boring","bouncy","boundless","brainy","brash","brave","brawny","breakable","breezy","brief","bright","bright","broad","broken","brown","bumpy","burly","bustling","busy","cagey","calculating","callous",
         "calm","capable","capricious","careful","careless","caring","cautious","ceaseless","certain","changeable","charming","cheap","cheerful","chemical","chief","childlike","chilly","chivalrous","chubby","chunky",
         "clammy","classy","clean","clear","clever","cloistered","cloudy","closed","clumsy","cluttered","coherent","cold","colorful","colossal","combative","comfortable","common","complete","complex","concerned",
         "condemned","confused","conscious","cooing","cool","cooperative","coordinated","courageous","cowardly","crabby","craven","crazy","creepy","crooked","crowded","cruel","cuddly","cultured","cumbersome","curious",
         "curly","curved","curvy","cut","cute","cute","cynical","daffy","daily","damaged","damaging","damp","dangerous","dapper","dark","dashing","dazzling","dead","deadpan","deafening","dear","debonair","decisive",
         "decorous","deep","deeply","defeated","defective","defiant","delicate","delicious","delightful","demonic","delirious","dependent","depressed","deranged","descriptive","deserted","detailed","determined","devilish",
         "want","warm","warn","wash","waste","watch","water","wave","weigh","welcome","whine","whip","whirl","whisper","whistle","wink","wipe","wish","wobble","wonder","work","worry","wrap","wreck","wrestle","wriggle",
         "x-ray","yawn","yell","zip","zoom"]

def get_valid_word():
    word=ran.choice(words)
    if " " in word or "-" in word or "_" in word:
        get_valid_word()

    print("For the Test(line 11), the word=",word,"\n")
    return word.upper()

def breakToLetters(word):
    lettersInWord=set(word)
    return lettersInWord

def hangman():
    newProgress= [letter if letter in correctLetters else '_' for letter in wordToGuess]
    print("Word: ",newProgress)
    return newProgress

def checkUserInput():
    while(True):
        print("Wrong Letters Till Now:",wrongLetters,"\nCorrect Letters Till Now:",correctLetters,"\n")
        char=input("Choose a Letter:").upper()
        alphabet = set(string.ascii_uppercase)
        if char in alphabet and not (char in wrongLetters or char in correctLetters):

            if char in lettersInWord:
                correctLetters.append(char)
                return True
            else:
                wrongLetters.append(char)
                return False
        else:
            print("Wrong input, or letter is already in used!")



if __name__ == '__main__':
    # Variables
    wrongLetters = []
    correctLetters = []
    progress = ""  # The word H___o
    hp = 5  # How many letters i have to use
    foundWord = False  # if i find the word

    wordToGuess=get_valid_word()
    lettersInWord=breakToLetters(wordToGuess)
    hangman()


    while hp>0 and not foundWord:
        print(f"_______hp={hp}_________")
        if checkUserInput()==True:
            progress=hangman()
            if not "_" in progress:
                foundWord=True
        else:
            hp-=1
    if hp==0:
        print("Better Luck Next Time")
    elif foundWord:
        print(f"You won the word is: {wordToGuess} and you had {hp} tries left!!")

