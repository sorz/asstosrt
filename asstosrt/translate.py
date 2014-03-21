class Translator(object):
    def convert(self, s):
        return self.translator.convert(s)


class LangconvTranslator(Translator):
    def __init__(self, language):
        import langconv
        self.translator = langconv.Converter(language)


class OpenCCTranslator(Translator):
    def __init__(self, config_name):
        import opencc
        self.translator = opencc.OpenCC(config_name)
 