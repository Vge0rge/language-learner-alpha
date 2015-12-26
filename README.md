# language-learner-alpha

[![GitHub license](https://img.shields.io/github/license/mashape/apistatus.svg)](http://opensource.org/licenses/MIT)

Language-learner-alpha is a tool that extracts the vocabulary from a file and translates the vocabulary to a given language. 

Currently supports only text files but support for more files will be added in the future.

### Requirements
--python-magic library
https://github.com/ahupp/python-magic

-- TextBlob library 
https://textblob.readthedocs.org/en/dev/

---


## Basic Usage

```python
>>> from text_extractor import TextExtractor
>>> from translator import Translator
>>> text_extractor = TextExtractor()
>>> translator = Translator()
>>> text_extractor.extract_text(text_file)
>>> translator.translate_db(language)
```
---

