from translate import Translator

#translating to spanish(es)
translator = Translator(to_lang="es" )

text = "Hello  How are you"

#translating
translation = translator.translate(text)

print("Translation text: " , translation)