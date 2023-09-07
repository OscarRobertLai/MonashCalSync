import requests

url = "https://my-timetable.monash.edu/odd/student"
params = {
    'ss': '591180863b524eba9712274c8d98ab6a',
    'state': '13cef47a-15c4-4c43-a6cc-213b27e2ed70',
    'session_state': 'ada04164-4cf4-41ec-b11e-46a27e7146f2',
    'code': '99ed04c6-4de4-4476-a0b1-e8cc770e5831.ada04164-4cf4-41ec-b11e-46a27e7146f2.e2b26c8f-05da-4e27-88cf-cee7eb8971df'
}

headers = {
    'authority': 'my-timetable.monash.edu',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'cookie': 'JSESSIONID=41CF0741FB90634CF8C5B55B620A3C49; _gid=GA1.2.658234999.1693740692; location_country_code=AU; CONSENTMGR=c1:1%7Cc2:1%7Cc3:1%7Cc4:1%7Cc5:1%7Cc6:1%7Cc7:1%7Cc8:1%7Cc9:1%7Cc10:1%7Cc11:1%7Cc12:1%7Cc13:1%7Cc14:1%7Cc15:1%7Cts:1693741098501%7Cconsent:true; _gcl_au=1.1.1517237491.1693741099; _fbp=fb.1.1693741098965.296334547; _scid=0baa3696-dec2-49de-9adc-24770464b19e; Hm_lvt_23acb057462e288c0ce7e5930f5e95f0=1693196467,1693197465,1693739971,1693741100; _sctr=1%7C1693663200000; utag_main=v_id:018a5ad402a9002b3631a5d9074a05075003f06d019b8$_sn:4$_se:1$_ss:1$_st:1693793615165$dc_visit:4$ses_id:1693791815165%3Bexp-session$_pn:1%3Bexp-session$dc_event:1%3Bexp-session$dc_region:ap-southeast-2%3Bexp-session; _scid_r=0baa3696-dec2-49de-9adc-24770464b19e; Hm_lpvt_23acb057462e288c0ce7e5930f5e95f0=1693791817; _ga_1TCL5RJ9ME=GS1.1.1693791816.4.1.1693791867.0.0.0; _ga_CRNN5NCFGE=GS1.1.1693791815.3.1.1693791868.0.0.0; OAuth_Token_Request_State=13cef47a-15c4-4c43-a6cc-213b27e2ed70; _gat_gtag_UA_93698210_5=1; _ga_9N8TCX4J1C=GS1.1.1693798633.25.1.1693804332.0.0.0; _ga=GA1.2.1849842075.1693740692; AWSALB=LaY77Nl5kkZ3bs57rZx7+DNJh9TyBO/Y5C3nrAf7jgW8Ac97gDZ6bs0ulJiEpvGI9wkXmczxx2hNa6ScgmBcStZngwCpmidB7tLwZeC2F9s/Bbjp+kw0NK/arnGH; AWSALBCORS=LaY77Nl5kkZ3bs57rZx7+DNJh9TyBO/Y5C3nrAf7jgW8Ac97gDZ6bs0ulJiEpvGI9wkXmczxx2hNa6ScgmBcStZngwCpmidB7tLwZeC2F9s/Bbjp+kw0NK/arnGH',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}

response = requests.get(url, params=params, headers=headers)
print(response.text)
