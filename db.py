#!/usr/bin/env python

#################################################################
# db.py
# The DB class can execute all the needed sqlite queries.
# Copyright 2015 Vasilakis Georgios
# MIT License
#################################################################

import _sqlite3
import os

class DB():
    __db_files_dir = "/tmp/"
    __db_filename = "dictionary.db"

    def __init__(self):
        """
        Starts the connection with the database.

        Parameters:
            Nothing

        Returns:
            Nothing
        """
        self.__conn =  _sqlite3.connect(DB.__db_files_dir + DB.__db_filename )

    def init_db(self):
        """
        Initializes the database file.
        Checks if the database and the table exists and if not, it creates them.

        Parameters:
            Nothing

        Returns:
            Nothing
        """

        if(not os.path.isdir(DB.__db_files_dir) and not os.path.exists(DB.__db_files_dir)):
            os.makedirs(DB.__db_files_dir)
            self.__conn =  _sqlite3.connect(DB.__db_files_dir + DB.__db_filename )

        self.__conn.execute("CREATE TABLE IF NOT EXISTS words (word text, translation text)")

        self.__conn.commit()

    def insert_word(self,word):
        """
        It inserts a given word at the column with name 'word' of table 'words'.
        It performs a commit to the database after the insertion.

        Parameters:
            word - the word to insert to the table

        Returns:
            Nothing
        """
        self.__conn.execute("INSERT INTO words (WORD) VALUES ( '{}' )".format(word))
        self.__conn.commit()

    def insert_word_no_commit(self,word):
        """
        It inserts a given word at the column with name 'word' of table 'words'.
        It doesn't perform a commit to the database after the insertion.

        Parameters:
            word - the word to insert to the table

        Returns:
            Nothing
        """
        self.__conn.execute("INSERT INTO words (WORD) VALUES ( '{}')".format(word))

    def commit(self):
        """
        It performs a commit to the database.

        Parameters:
            Nothing

        Returns:
            Nothing
        """
        self.__conn.commit()

    def delete_dublicate_words(self):
        """
        It deletes all the dublicate values at the column with name 'word' of table 'words'.
        Commits the database.

        Parameters:
            Nothing

        Returns:
            Nothing
        """
        self.__conn.execute("DELETE FROM words WHERE rowid not in(SELECT MAX(rowid) FROM WORDS GROUP BY word)")
        self.__conn.commit()

    def insert_translation_no_commit(self, word, translation):
        """
        Updates the column with name 'translation' of table 'words' with the value of translation variable
        where the column with name 'word' has the value of word variable.


        Parameters:
            word - the word of which the translation is given
            translation - the translation of the word variable

        Returns:
            Nothing
        """
        self.__conn.execute("UPDATE words SET translation = '{}' WHERE word = '{}' ".format(translation, word))

    def close_connection(self):
        """
        Closes the connection with the database.

        Parameters:
            Nothing

        Returns:
            Nothing
        """
        self.__conn.close()

    def get_words(self):
        """
        Returns all the values of column with name 'word' of table 'words'.

        Parameters:
            Nothing

        Returns:
            Nothing
        """
        return self.__conn.execute("SELECT word FROM words")

