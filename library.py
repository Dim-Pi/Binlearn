



def convertpe (text):
    
    con_dic = {
    
        'ا' : 'a0a',  'آ' : 'A0a',  'ب' : 'b0b',  'پ' : 'p0p',  'ت' : 't0t',  'ث' : 's0c',
        'ج' : 'j0j',  'چ' : 'c0h',  'ح' : 'H0H',  'خ' : 'k0h',  'د' : 'd0d',  'ذ' : 'z0Z',
        'ر' : 'r0r',  'ز' : 'z0z',  'ژ' : 'z0h',  'س' : 's0s',  'ش' : 's0h',  'ص' : 'S0S',
        'ض' : 'Z0Z',  'ط' : 'T0T',  'ظ' : 'Z0z',  'ع' : 'A0A',  'غ' : 'g0H',  'ف' : 'f0f',
        'ق' : 'g0h',  'ک' : 'c0k',  'گ' : 'g0g',  'ل' : 'l0l',  'م' : 'm0m',  'ن' : 'n0n',
        'و' : 'v0w',  'ه' : 'h0h',  'ی' : 'y0y',  ' ' :  ' '


    }

    
    newtext = ''
    
    

    for q in text:
        if q in con_dic :
            newtext += con_dic [q]
        else:

            newtext = text
            break
            
            
    


    if text != '' and newtext == '':
        newtext = text


    return newtext














def convertep (text):

    from re import sub

    con_dic = {



        'a0a': 'ا',  'A0a': 'آ',  'b0b': 'ب',  'p0p': 'پ',  't0t': 'ت',  's0c': 'ث',
        'j0j': 'ج',  'c0h': 'چ',  'H0H': 'ح',  'k0h': 'خ',  'd0d': 'د',  'z0Z': 'ذ',
        'r0r': 'ر',  'z0z': 'ز',  'z0h': 'ژ',  's0s': 'س',  's0h': 'ش',  'S0S': 'ص',
        'Z0Z': 'ض',  'T0T': 'ط',  'Z0z': 'ظ',  'A0A': 'ع',  'g0H': 'غ',  'f0f': 'ف',
        'g0h': 'ق',  'c0k': 'ک',  'g0g': 'گ',  'l0l': 'ل',  'm0m': 'م',  'n0n': 'ن',  
        'v0w': 'و',  'h0h': 'ه',  'y0y': 'ی',   



    }

    rtext = text
    for q in con_dic:

        rtext = sub ('(%s)'%q , con_dic[q] ,rtext)

    return rtext
























def b_per (text) :



    con_dic = {
    
        'ا' : 'a0a',  'آ' : 'A0a',  'ب' : 'b0b',  'پ' : 'p0p',  'ت' : 't0t',  'ث' : 's0c',
        'ج' : 'j0j',  'چ' : 'c0h',  'ح' : 'H0H',  'خ' : 'k0h',  'د' : 'd0d',  'ذ' : 'z0Z',
        'ر' : 'r0r',  'ز' : 'z0z',  'ژ' : 'z0h',  'س' : 's0s',  'ش' : 's0h',  'ص' : 'S0S',
        'ض' : 'Z0Z',  'ط' : 'T0T',  'ظ' : 'Z0z',  'ع' : 'A0A',  'غ' : 'g0H',  'ف' : 'f0f',
        'ق' : 'g0h',  'ک' : 'c0k',  'گ' : 'g0g',  'ل' : 'l0l',  'م' : 'm0m',  'ن' : 'n0n',
        'و' : 'v0w',  'ه' : 'h0h',  'ی' : 'y0y',  ' ' : ' '


    }

    
    
    u = True

    for q in str(text).strip() :
        if not (q in con_dic) :
            u = False
    

    return u 
            















def give_data ():
    from mysql.connector import connect
























def get_data () :

    from mysql.connector import connect
    from re import findall as find
    from bs4 import BeautifulSoup as bs
    from requests import get 
    from time import sleep

    urls = [ "https://lang.b-amooz.com/en/vocabulary/subcategories/643/lesson-1",
             "https://lang.b-amooz.com/en/vocabulary/subcategories/1690/lesson-2",
             "https://lang.b-amooz.com/en/vocabulary/subcategories/1389/lesson-3",
             "https://lang.b-amooz.com/en/vocabulary/subcategories/201/lesson-4"
            ]


    bd = lambda x : True if find ('\d+',x) != [] and len (find ('\d+',x) ) == 1 and find ('\d+',x) [0] == str(x) else False

    for url in urls :
    #page = webdriver.Chrome()

        page = get(url)

        #sleep (3)

        qq = page.text

        z = bs(qq,'html.parser')

        x = z.findAll ('li')

        r = []

        b = 0

        for q in x :

            ok = find(r'\w+\s{0,1}\w*',q.text)
            if  len(ok) != 0 and bd (ok[0]):
                r.append(ok)

        yo = r[3:]


        y = []



        for s0 in yo :
            if b < 6 or not( s0[0] in ['1','2','3','4','5'] ) :
                po = ""
                for j in s0 :
                    if b_per (j) :
                        po += ' %s ' % j.strip()
                y.append (( s0[1].strip() , convertpe (po.strip())  ))

            b += 1


        sql = connect (
            password = '1122'
            , user = 'pyth'
            , database = 'bot'
        )

        mydb = sql.cursor()

        for en , fa in y :


            mydb.execute ('INSERT INTO words (en  ,fa) VALUES  ("%s"  ,"%s") '  % (en  ,fa))

            sql.commit()

    



















