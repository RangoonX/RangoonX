# src/config/localization.py

import json
import os
from config import logger

EMBEDDED_TRANSLATIONS = {
    "en": {
        "app_title": "Rangoon X | Software House",
        "brand_name": "RangoonX",
        "nav_home": "Home",
        "nav_services": "Services",
        "nav_projects": "Projects",
        "nav_contact": "Contact",
        "hero_tag": "PRECISION ENGINEERING",
        "hero_title": "Myanmar's Premier Software Engineering Firm",
        "hero_subtitle": "We build robust, high-performance digital solutions designed to scale. From complex cloud architectures to elegant mobile applications.",
        "explore_services": "Explore Services",
        "contact_sales": "Contact Sales",
        "our_capabilities": "Our Capabilities",
        "capabilities_subtitle": "Engineered for reliability. We leverage modern stacks to deliver uncompromising performance.",
        "cloud_title": "Cloud Native Architecture",
        "cloud_desc": "Scalable, distributed systems built on AWS and Google Cloud. Microservices design for ultimate resilience.",
        "custom_software_title": "Custom Software",
        "custom_software_desc": "Tailored enterprise applications designed to streamline complex business workflows.",
        "mobile_eng_title": "Mobile Engineering",
        "mobile_eng_desc": "Native and cross-platform mobile experiences with uncompromising UI/UX.",
        "ai_ml_title": "AI & Machine Learning",
        "ai_ml_desc": "Integrating predictive models and generative AI into existing enterprise workflows to drive automation.",
        "footer_slogan": "Precision Engineering for the Digital Era.",
        "solutions": "Solutions",
        "connect": "Connect",
        "copyright": "© 2026 RangoonX Software House. Precision Engineering.",
        "services_page_title": "Our Services",
        "services_page_subtitle": "We deliver precision-engineered software solutions designed to scale. Our expertise spans custom application development, seamless cloud integrations, and advanced AI implementations.",
        "service_1_title": "Custom Software Engineering",
        "service_1_desc": "Bespoke web and mobile applications engineered from the ground up to meet your specific operational requirements. We utilize modern frameworks and rigorous testing methodologies to ensure high performance and reliability.",
        "service_2_title": "Cloud Migration & Architecture",
        "service_2_desc": "Seamlessly transition your legacy systems to scalable cloud environments. We design robust cloud architectures on AWS and Azure, focusing on security, cost-optimization, and continuous deployment pipelines.",
        "service_3_title": "AI & Data Integrations",
        "service_3_desc": "Leverage the power of machine learning and data analytics to drive business intelligence. We integrate LLMs, predictive models, and data pipelines to automate processes and unlock actionable insights.",
        "service_4_title": "Enterprise System Support",
        "service_4_desc": "Ongoing maintenance, security auditing, and performance optimization for your critical business systems. We provide dedicated SLAs to ensure your software remains operational and secure.",
        "services_cta_title": "Ready to start a project?",
        "services_cta_desc": "Contact our engineering team to discuss your technical requirements.",
        "get_in_touch": "Get in Touch",
        "contact_page_title": "Let's build together.",
        "contact_page_subtitle": "Reach out to discuss custom software solutions, cloud migrations, or how we can integrate AI into your workflow.",
        "contact_hq_title": "HQ",
        "contact_hq_address": "Level 8, Tower B, HAGL Myanmar Centre, Yangon, Myanmar",
        "contact_email_title": "Email",
        "contact_phone_title": "Phone",
        "form_first_name": "First Name",
        "form_last_name": "Last Name",
        "form_email": "Work Email",
        "form_interest": "Area of Interest",
        "form_interest_opt1": "Custom Software Development",
        "form_interest_opt2": "Cloud Infrastructure & Migration",
        "form_interest_opt3": "AI & Machine Learning Integration",
        "form_interest_opt4": "Other Inquiry",
        "form_message": "Project Details",
        "form_submit": "Send Inquiry",
        "form_success": "Thank you for reaching out! We will contact you shortly."
    },
    "mm": {
        "app_title": "ရန်ကုန် X | ဆော့ဖ်ဝဲလ် အိမ်တော်",
        "brand_name": "RangoonX",
        "nav_home": "ပင်မစာမျက်နှာ",
        "nav_services": "ဝန်ဆောင်မှုများ",
        "nav_projects": "စီမံကိန်းများ",
        "nav_contact": "ဆက်သွယ်ရန်",
        "hero_tag": "တိကျသေချာသော ဆော့ဖ်ဝဲလ် အင်ဂျင်နီယာအတတ်ပညာ",
        "hero_title": "မြန်မာနိုင်ငံ၏ ထိပ်တန်း ဆော့ဖ်ဝဲလ် နည်းပညာ ကုမ္ပဏီ",
        "hero_subtitle": "ယုံကြည်စိတ်ချရမှုနှင့် အရည်အသွေးမြင့်မားမှုကို အဓိကထား၍ ခေတ်မီ ဆော့ဖ်ဝဲလ်စနစ်များ၊ Cloud စနစ်များနှင့် Mobile App များကို ရေးဆွဲပေးပါသည်။",
        "explore_services": "ဝန်ဆောင်မှုများ ကြည့်ရှုရန်",
        "contact_sales": "ဆက်သွယ်မေးမြန်းရန်",
        "our_capabilities": "ကျွမ်းကျင်မှုနှင့် ဝန်ဆောင်မှုများ",
        "capabilities_subtitle": "ခေတ်မီဆန်းသစ်သော နည်းပညာများကို အသုံးပြု၍ စိတ်ချယုံကြည်ရသော စနစ်များကို ဖန်တီးပေးပါသည်။",
        "cloud_title": "Cloud Native Architecture",
        "cloud_desc": "AWS နှင့် Google Cloud ပေါ်တွင် တည်ဆောက်ထားသော အရွယ်အစား တိုးချဲ့နိုင်သည့် စနစ်များ။",
        "custom_software_title": "Custom Enterprise Software",
        "custom_software_desc": "လုပ်ငန်းခွင် လုပ်ငန်းစဉ်များကို ပိုမိုမြန်ဆန် ချောမွေ့စေမည့် စိတ်ကြိုက် ဆော့ဖ်ဝဲလ်များ။",
        "mobile_eng_title": "Mobile Application Engineering",
        "mobile_eng_desc": "အရည်အသွေးမြင့်မားပြီး အသုံးပြုရလွယ်ကူသော iOS နှင့် Android မိုဘိုင်းအပလီကေးရှင်းများ။",
        "ai_ml_title": "AI & Machine Learning Integration",
        "ai_ml_desc": "လုပ်ငန်းစဉ်များ အလိုအလျောက် ဆောင်ရွက်နိုင်ရန် AI နှင့် Predictive Models များ ထည့်သွင်းခြင်း။",
        "footer_slogan": "ဒီဂျစ်တယ်ခေတ်အတွက် တိကျသေချာသော နည်းပညာ support",
        "solutions": "ဝန်ဆောင်မှုများ",
        "connect": "ဆက်သွယ်ရန်",
        "copyright": "© 2026 RangoonX Software House. Precision Engineering.",
        "services_page_title": "ကျွန်ုပ်တို့၏ ဝန်ဆောင်မှုများ",
        "services_page_subtitle": "အရည်အသွေးမြင့်မားပြီး ယုံကြည်စိတ်ချရသော ဆော့ဖ်ဝဲလ်စနစ်များ၊ Cloud နည်းပညာများနှင့် AI စနစ်များကို အစအဆုံး တည်ဆောက်ပေးပါသည်။",
        "service_1_title": "အထူးပြု ဆော့ဖ်ဝဲလ်ရေးဆွဲခြင်း",
        "service_1_desc": "လုပ်ငန်းသုံး သီးသန့် Web နှင့် Mobile Application များကို ခေတ်မီ နည်းပညာများဖြင့် စနစ်တကျ ရေးဆွဲပေးပါသည်။",
        "service_2_title": "ကလောက်ဒ် နည်းပညာဝန်ဆောင်မှု",
        "service_2_desc": "လုပ်ငန်းစနစ်များကို AWS နှင့် Azure Cloud ပေါ်သို့ လုံခြုံစိတ်ချစွာ ရွှေ့ပြောင်းခြင်းနှင့် စနစ်တည်ဆောက်ခြင်း။",
        "service_3_title": "ဉာဏ်ရည်တုနှင့် ဒေတာပေါင်းစပ်ခြင်း",
        "service_3_desc": "Machine Learning နှင့် Data Analytics များကို အသုံးပြု၍ လုပ်ငန်းစဉ်များကို အလိုအလျောက် ဆောင်ရွက်ပေးခြင်း။",
        "service_4_title": "လုပ်ငန်းသုံး စနစ်ထိန်းသိမ်းမှု",
        "service_4_desc": "လုပ်ငန်းသုံး ဆော့ဖ်ဝဲလ်စနစ်များ စေတီမပြတ် လုံခြုံချောမွေ့စေရန် ၂၄ နာရီ ထိန်းသိမ်းစောင့်ရှောက်ပေးခြင်း။",
        "services_cta_title": "ပရောဂျက်တစ်ခု စတင်ရန် အဆင်သင့်ဖြစ်ပြီလား။",
        "services_cta_desc": "သင်၏ နည်းပညာ လိုအပ်ချက်များကို ဆွေးနွေးရန် ကျွန်ုပ်တို့၏ အင်ဂျင်နီယာ အဖွဲ့ထံ ဆက်သွယ်ပါ။",
        "get_in_touch": "ဆက်သွယ်ရန်",
        "contact_page_title": "အတူတကွ တည်ဆောက်ကြစို့။",
        "contact_page_subtitle": "စိတ်ကြိုက် ဆော့ဖ်ဝဲလ်စနစ်များ၊ Cloud စနစ်များနှင့် AI ပေါင်းစပ်မှုများကို ဆွေးနွေးရန် ဆက်သွယ်နိုင်ပါသည်။",
        "contact_hq_title": "ရုံးချုပ်",
        "contact_hq_address": "အဆောက်အအုံ B၊ အဆင့် ၈၊ HAGL မြန်မာ စင်တာ၊ ရန်ကုန်မြို့။",
        "contact_email_title": "အီးမေးလ်",
        "contact_phone_title": "ဖုန်း",
        "form_first_name": "အမည်",
        "form_last_name": "မျိုးရိုးနာမည်",
        "form_email": "အီးမေးလ်",
        "form_interest": "စိတ်ပါဝင်စားသည့် ဝန်ဆောင်မှု",
        "form_interest_opt1": "စိတ်ကြိုက် ဆော့ဖ်ဝဲလ် ရေးဆွဲခြင်း",
        "form_interest_opt2": "Cloud စနစ် တည်ဆောက်ခြင်းနှင့် ရွှေ့ပြောင်းခြင်း",
        "form_interest_opt3": "AI နှင့် Machine Learning ပေါင်းစပ်ခြင်း",
        "form_interest_opt4": "အခြား မေးမြန်းချက်များ",
        "form_message": "ပရောဂျက် အသေးစိတ်",
        "form_submit": "မေးမြန်းချက် ပေးပို့မည်",
        "form_success": "ကျေးဇူးတင်ရှိပါသည်။ ကျွန်ုပ်တို့၏ အဖွဲ့မှ သင့်ထံ မကြာမီ ဆက်သွယ်ပါမည်။"
    }
}


class LocalizationManager:
    _translations = {}

    @classmethod
    def _get_lang_folder_path(cls):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        src_dir = os.path.dirname(current_dir)
        
        candidates = [
            os.path.join(src_dir, "assets", "langs"),
            os.path.join(src_dir, "assets", "lang"),
            os.path.join("assets", "langs"),
            os.path.join("assets", "lang"),
            os.path.join("src", "assets", "langs"),
            os.path.join("src", "assets", "lang"),
        ]
        
        for candidate in candidates:
            if os.path.exists(candidate):
                return candidate

        return None

    @classmethod
    def load_translations(cls, lang_code: str):
        if lang_code in cls._translations and cls._translations[lang_code]:
            return cls._translations[lang_code]
        
        lang_folder = cls._get_lang_folder_path()
        if lang_folder:
            file_path = os.path.join(lang_folder, f"{lang_code}.json")
            if os.path.exists(file_path):
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        cls._translations[lang_code] = json.load(f)
                        logger.info(f"Successfully loaded '{lang_code}' translation from disk.")
                        return cls._translations[lang_code]
                except Exception as e:
                    logger.error(f"Error parsing JSON translation for {lang_code}: {e}")

        # Fallback to embedded translation dictionary (Guarantees Pyodide WASM compatibility)
        logger.info(f"Using embedded translation fallback for '{lang_code}'.")
        fallback = EMBEDDED_TRANSLATIONS.get(lang_code, EMBEDDED_TRANSLATIONS.get("en", {}))
        cls._translations[lang_code] = fallback
        return fallback

    @classmethod
    def get_string(cls, lang_code: str, key: str) -> str:
        translations = cls.load_translations(lang_code)
        return translations.get(key, key)