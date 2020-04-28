import os
os.mkdir('C:\\Users\\Admin\\Desktop\\Projects\wound\\ChronicWoundSeg\\training_history\\training_history')
try:
    open('C:\\Users\\Admin\\Desktop\\Projects\wound\\ChronicWoundSeg\\training_history\\training_history', 'x')
except OSError as err:
    print(err)
finally:
    os.rmdir('C:\\Users\\Admin\\Desktop\\Projects\wound\\ChronicWoundSeg\\training_history\\training_history')