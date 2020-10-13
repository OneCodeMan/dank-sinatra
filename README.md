# dank-sinatra
Language learning tool. \
Makes a CSV file out of English/German sentence pairs, so that they are easily importable into Anki. 

## Context:
- When I read books in my L2 (German), I write down sentences I find interesting and would like to remember.
- I enter those sentences into https://www.deepl.com/translator (the left-hand side), and they get translated (on the right-hand side) like so:
![DeepL](https://imgur.com/1pxtNbH.png)
- I manually have to copy and paste all these German sentences along with their translation in my Anki deck. 
With a lot of sentences, this can get time-consuming.
![DeepL Example](https://imgur.com/xV20CKF.png) 
![Anki](https://imgur.com/RJzEKET.png)
- **FEAR NOT. THERE IS A BETTER WAY! Anki supports importing CSV data.**
- This program lets you input a text file, and generates a CSV file of German/English sentence pairs.
- The format of the text file THAT YOU WOULD INPUT (i.e. place text file on same directory as program) should look like this: \
![Text file format](https://imgur.com/Rc7fSL5.png) \
_Copy and paste the English lines (left-hand side of DeepL) and place above divider._ \
_Copy and paste the German lines (right-hand side of DeepL) and place below divider._ \
_NOTE: FOR NOW, THE DIVIDER MUST BE EXACTLY THIS: --------_
- The generated CSV file looks something like: \
![CSV file format](https://imgur.com/ALWnUlc.png) \
_English sentences on first column._ \
_German translated sentences on second column._ \
_EACH PAIR SEPARATED BY A COMMA._
- Then on Anki, import the generated CSV file: \
![Import button](https://imgur.com/ldFOSGJ.png) \
![Look for generated file](https://imgur.com/VxH1e6P.png) \
![Proper settings](https://imgur.com/zm6GND5.png) \
_Make sure that the field separator is set to a comma!_
- After clicking 'import', you would have successfully made these cards and added them into your Anki deck.

## Notes:
- This doesn't necessarily have to be in German, DeepL doesn't necessarily need to be used. **It just has to follow the text file format.**
- German doesn't necessarily have to be at the back, English doesn't necessarily have to be at the front. 
Simply change the order of the text file input. (i.e. English sentences above divider, German sentences below.. or manipulate Anki fields when importing).
- This only supports the very basic front/back plain text-only format. No additional fields, styling texts, audio files, images, etc. If
you're interested in having that functionality for this, feel free to submit a PR.
