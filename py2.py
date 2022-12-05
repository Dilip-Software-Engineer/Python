letter = ('Dear <|NAME|>,\n'
          'you are selected!\n'
          '\n'
          'Date:<|DATE|>\n')
name = input("Enter your Name\n")
date = input("Enter Date\n")
letter = letter.replace("<|Name|>", name)
letter = letter.replace("<|Date|>", date)
print(letter)
