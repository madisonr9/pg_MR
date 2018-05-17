import pyautogui as pg
import time
import webbrowser

#Ask a question
shops = pg.prompt(
    """
What are you shopping for today?
a)clothes for boys
b)clothes for girls
c)cool things on amazon
d)shoes

""")
if answer == "a":
    cost = pg.prompt(
        """

Are you looking for expensive or cheap stuff?
a)cheap
b)expensive
c)I don't care


""")
    if cost == "a":
        webbrowser.open("http://www.hm.com/us/department/MEN?gclid=EAIaIQobChMIgcqdque02gIVEUwNCh32UA1YEAAYAiAAEgI1NvD_BwE&s_kwcid=AL!860!3!59009570037!e!!g!!mens%20clothing&ef_id=WbRB7QAAAPONa3E@:20180412130900:s/")
        webbrowser.open("https://www.forever21.com/us/shop/Catalog/Category/21men/mens-main")
    if cost == "b":
        webbrowser.open("https://www.vineyardvines.com/mens-clothing/")
        webbrowser.open("https://www.supremenewyork.com/")
        webbrowser.open("https://www.farfetch.com/shopping/men/off-white/items.aspx?utm_source=google&utm_medium=cpc&pid=googleadwords_int&af_channel=Search&c=653349257&af_c_id=653349257&af_siteid=&af_keywords=kwd-179549940&af_adset_id=33904166315&af_ad_id=262927736119&is_retargeting=true&gclid=EAIaIQobChMIh_Wki4PY2gIVWODICh0YJAebEAAYAiAAEgJEAfD_BwE")
        webbrowser.open("https://www.gucci.com/us/en/ca/men/mens-ready-to-wear-c-men-readytowear")
    if cost == "c":
        webbrowser.open("http://www.hm.com/us/department/MEN?gclid=EAIaIQobChMIgcqdque02gIVEUwNCh32UA1YEAAYAiAAEgI1NvD_BwE&s_kwcid=AL!860!3!59009570037!e!!g!!mens%20clothing&ef_id=WbRB7QAAAPONa3E@:20180412130900:s/")
        webbrowser.open("https://www.forever21.com/us/shop/Catalog/Category/21men/mens-main")
        webbrowser.open("https://www.vineyardvines.com/mens-clothing/")
        webbrowser.open("https://www.gucci.com/us/en/ca/men/mens-ready-to-wear-c-men-readytowear")


elif answer == "b":
    cost = pg.prompt(
        """

Are you looking for expensive or cheap stuff?
a)cheap
b)expensive
c)I don't care


""") 

    if cost == "a":
        webbrowser.open("http://us.romwe.com/?url_from=usgooglebrandromwe_romwe02_20170720&gclid=EAIaIQobChMIh7Gtz-m02gIVT0sNCh3SDAPDEAAYASAAEgJRX_D_BwE")
        webbrowser.open("http://us.shein.com/US-WomenClothing-20180401-vc-63576.html?url_from=usadgs03WomensOnline&gclid=EAIaIQobChMI5dux2-m02gIVTYezCh0TBg95EAAYASAAEgJgMvD_BwE")
        webbrowser.open("https://www.zaful.com/")
    if cost == "b":
        webbrowser.open("https://shop.nordstrom.com/?&cm_mmc=googlesearch_nord-_-brand_us-_-362587189-_-9657961278_dc314ba1-5744-48c2-b1f5-8f76fcb4611e&cm_mmca1=kwd-303545116050_e")
        webbrowser.open("https://www.vineyardvines.com/womens-clothing/")
        webbrowser.open("https://www.freepeople.com/dresses/")
    if cost == "c":
        webbrowser.open("https://shop.lululemon.com/?&CID=GOOGLE_Fetch_BRAND_A165_A822_C035098&gclid=EAIaIQobChMIyvXBvoLY2gIV2YKzCh3a4gZyEAAYASAAEgLTlfD_BwE&gclsrc=aw.ds")
        webbrowser.open("https://www.brandymelvilleusa.com/")
        webbrowser.open("http://us.topshop.com/?geoip=home")
        webbrowser.open("http://www.tobi.com/new/new-all?utm_source=google&utm_medium=cpc&utm_campaign=1330953041&utm_term=tobi-e&utm_content=53148651557-c-9003435-264270679116--1t1&gclid=EAIaIQobChMIq_j3tIPY2gIV2oKzCh314AqNEAAYASAAEgISy_D_BwE")


elif answer == "c":
    cost = pg.prompt(
        """

What are you looking for?
a)gaming
b)outdoors
c)books

""")

    if cost == "a":
        webbrowser.open("https://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=gaming+consoles&rh=i%3Aaps%2Ck%3Agaming+consoles")
    if cost == "b":
        webbrowser.open("https://www.amazon.com/man-cave/b/ref=nav_shopall_sa_sp_gamerm?ie=UTF8&node=706808011")
    if cost == "c":
        webbrowser.open("https://www.amazon.com/books-used-books-textbooks/b/ref=nav_shopall_bo_t3?ie=UTF8&node=283155")
    
elif answer == "d":
    cost = pg.prompt(
        """

What are you looking for?
a)Mens shoes
b)Womens shoes

""")

    if costsss == "a":
        webbrowser.open("https://www.flightclub.com/adidas/adidas-yeezy")
        webbrowser.open("http://m.adidas.com/us/men-shoes")
        webbrowser.open("https://store.nike.com/us/en_us/pw/mens-shoes/7puZoi3?redirect=true")
        webbrowser.open("https://www.sperry.com/en/mens/")
    if costsss == "b":
        webbrowser.open("https://www.lordandtaylor.com/search/EndecaSearch.jsp?bmForm=endeca_search_form_one&bmFormID=mb_1dwj&bmUID=mb_1dwk&bmIsForm=true&bmPrevTemplate=%2FEntry.jsp&bmText=SearchString&SearchString=womens+shoes&submit-search=&bmSingle=N_Dim&N_Dim=0&bmHidden=Ntk&Ntk=Entire+Site&bmHidden=Ntx&Ntx=mode%2Bmatchpartialmax&bmHidden=prp8&prp8=t15&bmHidden=prp13&prp13=&bmHidden=sid&sid=163020EE4730&bmHidden=FOLDER%3C%3Efolder_id&FOLDER%3C%3Efolder_id=")
        webbrowser.open("https://www.vans.com/webapp/wcs/stores/servlet/VFSearchDisplay?storeId=10153&catalogId=10703&langId=-1&beginIndex=0&searchSource=Q&sType=SimpleSearch&searchTerm=womens+")
        webbrowser.open("https://www.samedelman.com/shoes?originalsearchterm=shoes")
        webbrowser.open("https://store.nike.com/us/en_us/pw/womens-shoes/7ptZoi3?redirect=true")
        webbrowser.open("https://www.adidas.com/us/women-shoes")
