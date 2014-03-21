class Translator(object):
    def convert(self, s):
        return self.translator.convert(s)


class LangconvTranslator(Translator):
    def __init__(self, language):
        import langconv
        self.translator = langconv.Converter(language)


class OpenCCTranslator(Translator):
    def __init__(self, config_name):
        try:
            import pyopencc as opencc  # pyopencc on PyPi
        except ImportError as e:
            try:
                import opencc  # opencc-python on PyPi
            except ImportError:
                raise e
        self.translator = opencc.OpenCC(config_name)
 