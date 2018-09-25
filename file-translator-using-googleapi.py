'''
by: Prathmesh Pure
This program is written to translate small text or srt files from
original language to target language.
Source language is detected automatically.
This program is just passing a string and language code to google translate api
and takes response from api and displays only translated text.
Language codes are mentioned at the end of file.
'''

from urllib.request import Request, urlopen


def translate(to_translate, to_langage="auto"):
    # agents are required to request, else google gives 403 error
    agents = {'User-Agent': "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)"}

    link = "http://translate.google.com/m?hl=en&sl=auto&tl=%s&q=%s" % (to_langage, to_translate.replace(" ", "+"))
    # https://translate.google.com/m?hl=en&sl=auto&tl=hi&q=ti+amo       <- sample url

    request = Request(link, headers=agents)
    page = urlopen(request).read()

    ''' Translated text on html page is written between following tag
        <div dir="ltr" class="t0"></div>
    '''
    before_trans = b'class="t0">'
    n = len(before_trans)
    frm = page.find(before_trans) + n
    result = page[frm:]
    result = result.split(b"<")[0]
    # decode() is required to write text in utf-8 again
    return result.decode()


def main(src, dest, ln):
    srcfile = open(src, "r", encoding="utf-8-sig")
    destfile = open(dest, "w", encoding="utf-8-sig")
    for line in srcfile:
        trans = translate(line, "hi")+"\n"
        destfile.writelines(trans)

    destfile.close()
    srcfile.close()

if __name__ == '__main__':
    srcfile = "NFO.txt"
    destfile = "File2.txt"
    lang = "hi"             # hi = hindi, en = english likewise other also
    print(main(srcfile, destfile, lang))

'''
LANGUAGES = {
    'af': 'afrikaans',
    'sq': 'albanian',
    'am': 'amharic',
    'ar': 'arabic',
    'hy': 'armenian',
    'az': 'azerbaijani',
    'eu': 'basque',
    'be': 'belarusian',
    'bn': 'bengali',
    'bs': 'bosnian',
    'bg': 'bulgarian',
    'ca': 'catalan',
    'ceb': 'cebuano',
    'ny': 'chichewa',
    'zh-cn': 'chinese (simplified)',
    'zh-tw': 'chinese (traditional)',
    'co': 'corsican',
    'hr': 'croatian',
    'cs': 'czech',
    'da': 'danish',
    'nl': 'dutch',
    'en': 'english',
    'eo': 'esperanto',
    'et': 'estonian',
    'tl': 'filipino',
    'fi': 'finnish',
    'fr': 'french',
    'fy': 'frisian',
    'gl': 'galician',
    'ka': 'georgian',
    'de': 'german',
    'el': 'greek',
    'gu': 'gujarati',
    'ht': 'haitian creole',
    'ha': 'hausa',
    'haw': 'hawaiian',
    'iw': 'hebrew',
    'hi': 'hindi',
    'hmn': 'hmong',
    'hu': 'hungarian',
    'is': 'icelandic',
    'ig': 'igbo',
    'id': 'indonesian',
    'ga': 'irish',
    'it': 'italian',
    'ja': 'japanese',
    'jw': 'javanese',
    'kn': 'kannada',
    'kk': 'kazakh',
    'km': 'khmer',
    'ko': 'korean',
    'ku': 'kurdish (kurmanji)',
    'ky': 'kyrgyz',
    'lo': 'lao',
    'la': 'latin',
    'lv': 'latvian',
    'lt': 'lithuanian',
    'lb': 'luxembourgish',
    'mk': 'macedonian',
    'mg': 'malagasy',
    'ms': 'malay',
    'ml': 'malayalam',
    'mt': 'maltese',
    'mi': 'maori',
    'mr': 'marathi',
    'mn': 'mongolian',
    'my': 'myanmar (burmese)',
    'ne': 'nepali',
    'no': 'norwegian',
    'ps': 'pashto',
    'fa': 'persian',
    'pl': 'polish',
    'pt': 'portuguese',
    'pa': 'punjabi',
    'ro': 'romanian',
    'ru': 'russian',
    'sm': 'samoan',
    'gd': 'scots gaelic',
    'sr': 'serbian',
    'st': 'sesotho',
    'sn': 'shona',
    'sd': 'sindhi',
    'si': 'sinhala',
    'sk': 'slovak',
    'sl': 'slovenian',
    'so': 'somali',
    'es': 'spanish',
    'su': 'sundanese',
    'sw': 'swahili',
    'sv': 'swedish',
    'tg': 'tajik',
    'ta': 'tamil',
    'te': 'telugu',
    'th': 'thai',
    'tr': 'turkish',
    'uk': 'ukrainian',
    'ur': 'urdu',
    'uz': 'uzbek',
    'vi': 'vietnamese',
    'cy': 'welsh',
    'xh': 'xhosa',
    'yi': 'yiddish',
    'yo': 'yoruba',
    'zu': 'zulu',
    'fil': 'Filipino',
    'he': 'Hebrew'
}
'''
