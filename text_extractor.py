#!/usr/bin/env python

#################################################################
# text_extractor.py
# The TextExtractor class can extract the text from a given file
# and store the result to a sqlite database.
# Copyright 2015 Vasilakis Georgios
# MIT License
#################################################################

import magic
import re
from db import DB

class TextExtractor:
    __supported_filetypes = ('text/plain')

    def extract_text(self, filename):
        """
        Handles the extraction of the text for the given file.
        This function will verify that the file is supported and will call the appropriate extract function.

        Parameters:
            filename - the filename of the file to be extracted

        Returns:
            Nothing
        """
        filetype = magic.from_file(filename, mime=True)

        if filetype not in TextExtractor.__supported_filetypes:
            raise Exception("File type is not supported yet!")

        # Here we will place an if statement handling more file types later
        self.text_file_extract(filename)

    def text_file_extract(self,filename):
        """
        Extracts the words from a text file and stores the result in a sqlite database.
        It makes all the words lowercase and deletes all the dublicates.

        Parameters:
            filename - the filename of the file to be extracted

        Returns:
            Nothing
        """

        sqlitedb = DB()

        sqlitedb.init_db()

        with open(filename) as textFile:
            for line in textFile:
                wordlist =  re.compile('[a-zA-Z]+').findall(line)
                for word in wordlist:
                    word = word.lower()
                    if len(word)>2:
                        sqlitedb.insert_word_no_commit(word)

        sqlitedb.delete_dublicate_words()
        sqlitedb.commit()
        sqlitedb.close_connection()




