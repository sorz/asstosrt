class Translator(object):
    def convert(self, s):
        return self.translator.convert(s)


class LangconvTranslator(Translator):
    def __init__(self, language):
        import langconv
        self.translator = langconv.Converter(language)


class OpenCCTranslator(Translator):
    def __init__(self, config_name):
        import pyopencc
        self.translator = pyopencc.OpenCC(config_name)
 