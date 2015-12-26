#!/usr/bin/env python

#################################################################
# translator.py
# The Translator class can translate a sqlite database column to
# the given language and store the result to another collumn.
# Copyright 2015 Vasilakis Georgios
# MIT License
#################################################################

from textblob import TextBlob
from db import DB

class Translator():

    def translate_db(self, language):
        """
        Translates all the words in the sqlite database to the given language.
        It stores the result in another collumn of the same database.

        Parameters:
            language - the language to translate the words

        Returns:
            Nothing
        """
        sqlitedb = DB()

        for word in sqlitedb.get_words():
            try:
                blob = TextBlob(word[0])
                translation = blob.translate(to=language)
                sqlitedb.insert_translation_no_commit(word[0], translation)
            except Exception as ex:
                print ex.message

        sqlitedb.commit()
