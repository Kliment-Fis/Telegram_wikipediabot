import wikipedia as wiki

wiki.set_lang('ru')
query = wiki.summary('Wikipedia')
print(query)
